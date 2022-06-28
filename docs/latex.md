# Using LaTeX in problems

## What is LaTeX?

LaTeX is a markup language that allows you to format the appearance of a document using specific syntax.
In our project you will mostly be using it to typset mathematical formulas. Markdown supports LaTeX, you just need to surround it with `$___$`.

## Table of Math Symbols

Here is a table of the main mathematical symbols you will be using.

![LaTeX Math Symbols: Common mathematical symbols in LaTeX.](images/latex_math.png)
Image credit for the above table is from [Winston Chang](https://github.com/wch/latexsheet/blob/ef6d3f438c0e2e5499ffbe79a4be21960c9b3b07/latexsheet.pdf).

## Examples

To capitalize a greek letter, you just need to capitalize the first letter of it in LaTeX.

Ex:

> \alpha and \Alpha

To create a fraction of LaTeX symbols, you can simply insert the symbols you need into the fraction function

Ex:

> \frac{\alpha}{\theta\pi}

You can add LaTeX anywhere into your markdown code, as long as you surround it with $...$

> The block travels on an incline of 30$^{\circ}$.

For superscripts:

> $3^4$ should be \$3^4\$

> $3^{-4}$ should be \$3^{-4}\$ since more than one character is being used in the superscript

## Additional Resources

For a more thorough collection of LaTeX syntax, [click here.](https://github.com/wch/latexsheet/blob/ef6d3f438c0e2e5499ffbe79a4be21960c9b3b07/latexsheet.pdf)

## Issues with LaTeX

LaTeX code might sometimes not render properly on PL.
Most of the time, using two back slashes instead of one will solve the issue.

Some examples:

| Issue | Fix |
| -- | -- |
| ```\frac{}{}``` | Use ```\dfrac{}{}``` or ```\\frac{}{}```|
| ```\theta``` | ```\\theta``` |
| ```\vec{}``` | ```\\vec{}``` |

Furthermore, if adding the extra back slash does not work, separating the LaTeX elements into different strings and then applying concatenation might fix the problem.

For instance, ```"$\Delta\vec{p}_A$"``` will not display correctly while ```"$\Delta$" + "$\\vec{p}_A$"``` will.

### Storing and displaying answers with LaTeX elements

Assume that we have answer choices in the following format: 0.5 $\pm$ 0.1 $J$ where 0.5 is stored in ```params.part1.constant``` and 0.1 is stored in ```params.part1.ans1.value```. 

```"{{ params.part1.constant }} $\pm$ {{ params.part1.ans1.value }} {{ params.vars.units}}"``` will not work.  

The solution is to use a raw string (prepend an ```r```).

So, ```r"{{ params.part1.constant }} $\pm$ {{ params.part1.ans1.value }} {{ params.vars.units}}"``` will produce the correct output.