# Rounding and Significant Figures in problems

Rounding correctly and having your problems set to the appropriate number of significant figures is not an easy problem to solve algorthmically. 
We will do our best using some wrapper functions I wrote that rely on the [custom sigfig package](https://sigfig.readthedocs.io/en/latest/).

## When to round

This is important in questions with measured quantities, i.e. everytime you're doing a calculation.

Here's how to do it:

First,

> `import problem_bank_helpers as pbh`

## Round a number to a specific number of sig figs

This will be the most common use-case.

To round a number `original_number` to a specific number of significant figures (`sigfigs`):

> `pbh.roundp(original_number, sigfigs = number of sigfigs, format = *)`

Useful when dealing with numbers with unnecessary length but unlike decimal function, will not round to zero.
> `pbh.roundup(0.0285720, sigfigs = 3)`

The output will then be (a number):
> 0.0206

## To format numbers as text (as a string)

Generally you will not be using this, but if you ever need it, to produce a number of a particular format (for e.g., with a thousands separator) use:

`pbh.roundp(741535, sigfigs = 5, format = 'English')`

> '742,000'

## To format numbers as Scientific Notation (as a string)

Generally you will not be using this, but if you ever need it, here's how to format a number as scientific notation:

`pbh.roundp(0.014159,sigfigs=3, format = 'sci')`
> '1.42E-2'

`pbh.roundp(original number, decimals = number of digits after the decimal place)`

Useful when dealing with calculated values that are unnecessarily long.

For example:

`math.sin(theta)`

> 0.9129452507276277

`pbh.roundp(math.sin(theta), decimals=3)`
> 0.912

pbh.roundp(original number, uncertainty = measured uncertainty, format = changes format of returned value)
To use when dealing with a measurment and its uncertainty.

Will return the number rounded to the number of decimal places needed to give the uncertainty one sig fig.
pbh.roundp(3.02893103, uncertainty = 0.0029014839, format = 'std')

- If you set `format =  'std'`, here's how it will display (as a string):
> '3.029 +/- 0.003'

-  If you set `format = 'sci'`, here's how it will display (as a string)
> '3.029 +/- 3E-3'
