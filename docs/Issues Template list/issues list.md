# List of Issues 

## Template 
- Verify the template version
- Verify that the title is stored in the dictionary
- Make sure the heading level of each section is correct.
- For symbolic input questions, verify that the label and variables are correct.
- For number input questions, verify that the label and suffix are correct.
- Verify that the answer section follows the correct template format.

## Style
- Verify that the question displays nicely. (e.g. extra space required, etc)
- If a value is not a number, double quotes should be used.
- Concise and short variable names. They should generally follow physics conventions.
- Indentation errors
- Good comment practices
## Topic and Outcomes

- Verify that the topic and Learning Outcomes are correct.
## Images

- Verify if there is any missing image.
- Verify that the image has been inserted in the markup section using either markup or HTML
    ```<img src = "image.png" width = 300>``` or ```![alt text](image.png)```
    * Verify that an alt-text has been added. 

## Mathematical elements and LaTeX 

- Verify LaTeX syntax. Avoid using HTML.
- Rounding Errors.
    * Make sure the rounded value of the variable is used in the calculations.
    * Correct use of ```pbh.roundp()```. Avoid using the python built-in function ```round()``` as it uses banker's rounding. 
- Significant Figures
- For uncertainty questions using $\pm$, the answer value should be a string for it to display correctly. See PR #77
- For questions involving trig functions, make sure the radian value is being used. ```math.sin(math.radians(theta))```

### Vectors and Polynomials

- Verify that the sign of each component of the vector is displayed correctly. (use ```pbh.sign_str()```)

## Randomisation 

- Make sure the question is randomised as much as possible.
- Verify that names and vehicles are randomised.
- Verify the bounds
    * Verify that randomisation (especially when coupled with trigonometric functions) does not lead to positive variables becoming negative and vice-versa. See PR #55 - ```# need [cos(theta_0) - cos (theta_c)] < 0 for v_cut to be positive```
    * Verify that the upper and lower bounds are within reason.
    * For questions dealing with coefficients of friction, we need $\mu_s > \mu_k$. See PR #56
- For textual questions, verify that the answers are being shuffled. ```random.shuffle()```

### Tables

- Make sure that the values are randomised and are sensible.

## Python

- Verify the conditions of if-statements and loops
