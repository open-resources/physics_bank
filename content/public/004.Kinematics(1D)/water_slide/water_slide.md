---
title: Water Slide
topic: Kinematics(1D)
author: Jake Bobowski
source: 2015 Practice Midterm 1 Q8
template_version: 1.0
attribution: standard
outcomes:
- 4.1.1.1
- 4.6.2.0
- 4.5.1.0
- 4.6.3.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- MP
assets: null
server:
  imports: |
    import random
    import pandas as pd
    import sympy as sp
    import prairielearn as pl
    import math
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: |
    # Start problem code

    data2 = nested_dict()

    # store phrases etc
    data2["params"]["vars"]["title"] = 'Water Slide'

    # Declare math symbols to be used by sympy
    t, v_o = sp.symbols('t, v_o')

    # define bounds of the variables
    theta = random.randint(2,5)*10
    l = random.randint(1,9)*100
    l2 = 0.5*l
    a1 = 9.8*math.sin(math.radians(theta))

    # store the variables in the dictionary "params"
    data2["params"]["theta"] = theta
    data2["params"]["l"] = l
    data2["params"]["l2"] = l2

    # Describe the solution equation
    x1 = 1/2*(a1)*t**2
    x2 = l + v_o*t + 1/2*(a1)*t**2

    # Answer to fill in the blank input stored as JSON.
    data2['correct_answers']['part1_ans'] = pl.to_json(x1)
    data2['correct_answers']['part2_ans'] = pl.to_json(x2)

    # define correct answers
    data2['correct_answers']['part3_ans'] = math.sqrt(l2/a1)
    data2['correct_answers']['part4_ans'] = ((l2-l-a1*(math.sqrt(l2/a1))**2))/math.sqrt(l2/a1)

    # Update the data object with a new dict
    data.update(data2)
  prepare: 'pass

    '
  parse: 'pass

    '
  grade: 'pass

    '
part1:
  type: symbolic-input
  label: $x(t) = $
  pl-customizations:
    variables: t
    weight: 1
    allow-blank: false
part2:
  type: symbolic-input
  label: $x(t) = $
  pl-customizations:
    variables: t
    weight: 1
    allow-blank: false
part3:
  type: number-input
  label: $t=$
  pl-customizations:
    allow-blank: true
    weight: 1
part4:
  type: number-input
  label: $v=$
  pl-customizations:
    allow-blank: true
    weight: 1
substitutions:
  params:
    vars:
      title: Water Slide
    theta: 20
    l: 800
    l2: 400.0
  correct_answers:
    part1_ans:
      _type: sympy
      _value: 1.67589870229578*t**2
      _variables:
      - t
    part2_ans:
      _type: sympy
      _value: 1.67589870229578*t**2 + t*v_o + 800
      _variables:
      - t
      - v_o
    part3_ans: 10.924237049272477
    part4_ans: -73.23165877778877
---
# {{ params.vars.title }}
What an exciting time to be alive! A water slide has just opened up near my house! It is a ramp, {{params.l}} meters long at {{params.theta}}$^o$ to the horizontal. At the same instant I begin sliding down from the top (with zero initial velocity), some jerk kid decides to TRY TO SLIDE UP the slide from the bottom. The kid has an unknown initial velocity $v_o$ , but we collide midway down the ramp ({{params.l2}} m from the bottom).

Use the following table as a reference for each variable:

| $Variable$ | Use   |
|----------|-------|
| $t$  | t  |
| $v_o$  | v_o  |

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)