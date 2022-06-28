# Tips for authoring questions

Below is a list of suggestions and recommendations when authoring questions.

## Legend
- Shuffling Choices
- Preventing Randomization
- LaTeX Issues
- Dealing with vectors and polynomials
- Creating and using your own functions
- Sympy
- Adding Images to a Question
- Using numpy
- Randomizing Tables
- Choosing two or more names/animals/objects without repetition

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

## LaTeX Issues

See the [latex](./latex.md) section for common issues using LaTeX.

## Dealing with vectors and polynomials

### Using pbh.sign_str()

When randomly generating vector components, for example, $0.50 \hat\imath - 16 \hat\jmath$ or $0.50 \hat\imath + 16 \hat\jmath$, we would want to determine the sign of the $\hat\jmath$ vector algorithmically. This can be done using the ```pbh.sign_str()``` function.  It returns the sign of the input number as a string.

Note: The signs are stored as ```' + '``` and ```' - '``` instead of ```'+'``` and ```'-'``` (note the spaces).

The function can be used in the following ways.

- ```pbh.sign_str(-50500)```
- ```pbh.sign_str( {{ params.part1.varx }})```

**Example**. 

Assume that we would like to randomize the coefficients of a vector and display it in the format $\vec{v_1} = a \hat\imath +b \hat\jmath$ where $a$ and $b$ are real numbers.

```pbh.sign_str()``` will be used to determine the sign of the coefficient of the $\jmath$ component.  This sign will be stored in the ```data2``` dictionary as ```data2["params"]["v1_j_sign"] ```. 

Steps:

1. Break up the vector into components.  Let us call them ```v1_i``` and ```v1_j```. 

2. Create another dictionary element ```v1_j_abs```. The absolute value is needed for the $\jmath$ component since we would not want the sign two appear twice if we have a negative coefficient. Assuming that ```v1_i``` and ```v1_j``` have been initialised, we would have the following code.

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

## Using the `sympy` package

### Calling a `sympy` object in your html file

Sometimes it is nice to have `sympy` expressions in the question.html file. If you simply call a `sympy` object in, it will not render properly.
Say we have some `sympy` expression 'expr': 
First, convert it to a string: `srt_expr = string(expr)`
For nicer printing, you can also convert double * ' s to ^ with str_expr.replace(' ** ',' ^ ') - (without the spaces)
And single * ' s with str_expr.replace('* ','') - (again, without the spaces)

### `sympy` object doesn't convert nicely to json for answer.

Sympy to json conversion in PrairieLearn doesn't like floats.
It also doesn't like fractions in brackets. 
So, it's best to do something like:
Y = X/2
As opposed to:
Y = 0.5 * X or Y = 1/2 * X
At this time, there isn't a clear way for using floats in PL via `sympy`. 

### You get the error: "Object of type Null is not JSON serializable"

The code here: 
    
```
# Declare math symbols to be used by sympy
t, v_o, g = sp.symbols('t, v_o, g')

# define bounds of the variables
theta = random.randint(2,5)*10
l = random.randint(1,9)*100
l2 = 0.5*l
a1 = g*math.sin(math.radians(theta))

# store the variables in the dictionary "params"
data2["params"]["theta"] = theta
data2["params"]["l"] = l
data2["params"]["l2"] = l2

# Describe the solution equation
x1 = a1*t**2/2
x2 = l + v_o*t + a1*t**2/2
```
    
Will result in that error.
The code below will not:

```  
# Declare math symbols to be used by sympy
t, v_o, g = sp.symbols('t, v_o, g')

# define bounds of the variables
theta = random.randint(2,5)*10
l = random.randint(1,9)*100
l2 = (1/2)*l
a1 = 9.8*math.sin(math.pi*theta/180)

# store the variables in the dictionary "params"
data2["params"]["theta"] = theta
data2["params"]["l"] = l
data2["params"]["l2"] = l2

# Describe the solution equation   
x1 = t**2 / 2 * g * sp.sin(sp.pi*theta/180)
x2 = 1 + v_o*t + t**2 / 2 * g * sp.sin(sp.pi*theta/180)
```
 
 Be sure to use `sp.sin` rather than `math.sin` for symbolic questions, and remember that `pl.to_json` conversion or `pl.sympy_to_json()` doesn't like floats.

### You get the error: "argument of type 'int' is not iterable"

Assume we have a symbolic input question where the correct answer is a simple integer without any other variable.
While this could be converted to a numeric input question, we want to keep this question as a symbolic one so as not to give away the answer.
Simply setting the answer to the integer will result in an "argument of type 'int' is not iterable" error.
Converting the integer to a string before calling ```pl.to_json()``` will resolve the issue.

Here is an example taken from a multipart question.

**Question**.

A very bored bear decided to jump across a stream.
The bear can jump with an initial velocity $\overrightarrow{V_i} = 2{m\over s}\hat{\imath}+4{m\over s}\hat{\jmath}$, and decides to start from 1 $m$ in the air, halfway up a sturdy tree.

If the origin is at the foot of the bear's jumping tree, write a set of equations describing the $x$ and $y$ coordinates and the $V_x$ and $V_y$ components of the velocity of the bear while it is in the air.

Use the following table as a reference. Note that it may not be necessary to use every variable.

| $Variable$ | Use   |
|----------|-------|
| $\Delta t$  | t  |
| $g$ | g |

</br>

Let us focus on the $V_x$ component of the velocity. Here, the correct answer is simply $V_x = 2$.

Assume that we have the following code.

```
vi_x = 2                                     # i-component of the initial velocity
data2["params"]["vi_x"] = vi_x
```

Then,

```
# Describe the solution equation
Vx = vi_x

# Answer to fill in the blank input stored as JSON.
data2['correct_answers']['part3_ans'] = pl.to_json(Vx)
```

will **not** work while

```
# Describe the solution equation
Vx = str(vi_x)

# Answer to fill in the blank input stored as JSON.
data2['correct_answers']['part3_ans'] = pl.to_json(Vx)
```
will.

## Adding Images to a Question

If you want to add an image to a question: 
1. Add the image(s) to the same folder where the question file is. A PNG file is preferred.
2. Add the name of the image to the assets section in the following format: 

    ```
    assets: 
    - image1.png
    - image2.png
    server: 
    ```
    
See `q01_multiple-choice.md` template for an example.

## Using `numpy`

Some rendering issues might occur when using `numpy` for calculations, especially when using a `numpy` result in a multiple choice question answer section. The result should first be cast to an integer or a string before being used. 

In addition, if a `numpy` value is used with ```pbh.roundp()```, that value must first be cast to ```float()```.

## Randomizing Tables

For questions containing tables of data, the following approach can be used.

Assume that a table of ten measured acceleration values, as well as the mean and standard deviation of the values, needs to be generated.

1. Create a list of values and store them individually in the dictionary.

```
# generate the table
a_meas = [pbh.roundp(rd.uniform(1.3,1.8), sigfigs=3) for _ in range(10)]

# store the values in the dictionary
values = ["a{0}".format(i+1) for i in range(10)]
for x in a_meas:
    value = values.pop(0)
    data2["params"][value] = x
```

2. Calculate the mean and standard deviation using ```numpy.mean()``` and ```numpy.std()``` and store the values in the dictionary.

```
# calculate the mean measured acceleration and standard deviation
mean = pbh.roundp(float(numpy.mean(a_meas)), sigfigs = 3)
sd = pbh.roundp(float(numpy.std(a_meas)), sigfigs = 3)

# save table values in dictionary
data2["params"]["mean"] = mean
data2["params"]["sd"] = sd
```

3. Displaying the table in Markdown 

```
| Trial     | Accel. ($m/s^2$) |
| ----------- | ----------- |
| 1     |  {{ params.a1 }}     |
| 2   |   {{ params.a2 }}      |
| 3     |  {{ params.a3 }}     |
| 4   |   {{ params.a4 }}      |
| 5     |  {{ params.a5 }}     |
| 6   |   {{ params.a6 }}      |
| 7     |  {{ params.a7 }}     |
| 8   |   {{ params.a8 }}      |
| 9     |  {{ params.a9 }}     |
| 10   |   {{ params.a10 }}      |
| **Mean** | {{ params.mean }}      |
| **SD** | {{ params.sd }}      |
```

## Choosing two or more names/animals/objects without repetition

Suppose a question involves two ($n = 2$) named entities. We would not want to have the same name generated twice.

1. Assume that we have a list called `entity` of names/animals/objects (manually defined or loaded using pandas).

2. The first named `entity` is generated using ```random.choice()```.

    ```entity1 = random.choice(entity)```

3. To prevent repetition, ```entity1``` needs to be removed from the list.

    ```entity.remove(entity1)```

4. Finally, the second entity is again generated using ```random.choice()```.

    ```entity2 = random.choice(entity)```

This process can be repeated for $n > 2$.