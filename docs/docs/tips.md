# Tips for authoring questions

Below is a list of suggestions and recommendataions when authoring questions.

## Shuffling choices

Let's imagine an MCQ that has 3 distractors and 1 correct choice (total of 4).

1. PL will automatically shuffle Multiple Choice / Dropdown / checkbox choices so each variant produces a uniquely ordered list. 
2. The reason we used `random.shuffle()`, is because we had a "bank" of choices (say 10 distractors) and 3 correct choices, and we wanted to construct a series of questions where each variant would get DIFFERENT distractors and DIFFERENT correct answers

So, in short, here's the guideline: 

- If your question is one where the distractors are always the same (whether they are calculated or fixed), you don't need to shuffle and draw from the list. PL will randomize the order. 
- If your question has a bank of correct and a bank of incorrect choices, then you should shuffle the list so that each variant has different choices.

## Preventing randomization

We would want to prevent answer choices from being randomized in the following cases:

- When the answer options are simple letters. E.g. 'A', 'B', 'C', ...
- When the answer options are figure labels such as 'Figure A', 'Figure 1', ...

In these cases, randomizing the choices could lead to confusion.

The solution is to add the Prairie Learn customization ```fixed-order: true``` under ```pl-customizations:```.

Here is an example.

```
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
    fixed-order: true
```

## Answer choices containing $\pm$ 

Assume that we have answer choices in the following format: 0.5 $\pm$ 0.1 $J$ where 0.5 is stored in ```params.part1.constant``` and 0.1 is stored in ```params.part1.ans1.value```. 

```{{ params.part1.constant }} $\pm$ {{ params.part1.ans1.value }} {{ params.vars.units}} ``` will not work.  The solution is to store the whole expression in ```{{ params.part1.ans1.value }}``` as a string in the following manner: ```str(constant) + " $\pm$ " + str(randomized value)```



## Dealing with vectors and polynomials

### Using pbh.sign_str()

When randomly generating vector components, for example, $0.50 \hat\imath - 16 \hat\jmath$ or $0.50 \hat\imath + 16 \hat\jmath$, we would want to determine the sign of the $\jmath$ vector algorithmically. This can be done using the ```pbh.sign_str()``` function.  It returns the sign of the input number as a string.

The function can be used in the following ways.

- ```pbh.sign_str(-50500)```
- ```pbh.sign_str( {{ params.part1.varx }})```

**Example**. 

Assume that we would like to randomise the coefficients of a vector and display it in the format $\vec{v_1} = a \hat\imath +b \hat\jmath$ where $a$ and $b$ are real numbers.

```pbh.sign_str()``` will be used to determine the sign of the coefficient of the $\jmath$ component.  This sign will be stored in the ```data2``` dictionary as ```data2["params"]["v1_j_sign"] ```. 

Steps:

1. Break up the vector into components.  Let us call them $v1_i$ and $v1_j$. 

2. Create another dictionary element $v1_j_abs$. The absolute value is needed for the $\jmath$ component since we would not want the sign two appear twice if we have a negative coefficient. Assuming that $v1_i$ and $v1_j$ have been initialised, we would have the following code.

```
data2["params"]["v1_i"] = v1_i
data2["params"]["v1_j_abs"] = numpy.abs(v1_j)
data2["params"]["v1_j_sign"] = pbh.sign_str(v1_j)
```

3. Using this code in the question text section,

```
$\vec{v_1} = $ {{ params.v1_i}} $\hat{\imath}$ {{params.v1_j_sign}} {{ params.v1_j_abs}} $\hat{\jmath}$
```
the correct output will be obtained.

4. If the answer choices also need to be in the same format, the following template can be used.

```
data2["params"]["part1"]["ans1"]["value"] = str(v1_i) + "$\hat{\imath}$" + pbh.sign_str(v1_j) + str(numpy.abs(v1_j)) + "$\hat{\jmath}$"
```

Notice that the coefficients have to be converted to string and the final answer is obtained by concatenating each part.

## Creating and using your own functions

In some cases, writing a function might be needed to improve code readability (and for reusability!).

Functions can be defined inside the ```generate()``` section of the server code.


*Note*: If you feel the function could be generalized and used in other questions, please request for it to be added to the ```pbh``` package.

## Sympy
### Calling a sympy object in your html file
Sometimes it is nice to have sympy expressions in the question.html file. If you simply call a sympy object in, it will not render properly.
Say we have some sympy expression 'expr': 
First, convert it to a string: srt_expr = string(expr)
For nicer printing, you can also convert double * ' s to ^ with str_expr.replace(' ** ',' ^ ') - (without the spaces)
And single * ' s with str_expr.replace('* ','') - (again, without the spaces)

### Sympy object doesn't convert nicely to json for answer.
Sympy to json conversion in prairielearn doesn't like floats. It also doesn't like fractions in brackets. 
So, it's best to do something like:
Y = X/2
As opposed to:
Y = 0.5 * X or Y = 1/2 * X
At this time, there isn't a clear way for using floats in PL via sympy. 

