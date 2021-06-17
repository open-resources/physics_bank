---
title: Rocket
topic: Math
author: Jake Bobowski
source: 2015 Practice Midterm 1 Q6
template_version: 1.0
attribution: standard
outcomes:
- 1.8.1.2
- 1.7.2.1
- 3.7.2.0
- difficulty: null
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- EW
assets: null
server:
  imports: |
    import random
    import pandas as pd
    import sympy as sp
    import prairielearn as pl
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: |
    # Start problem code

    data2 = nested_dict()

    # store phrases etc
    data2["params"]["vars"]["title"] = "Rocket"
    data2["params"]["vars"]["units1"] = "m/s^2"
    data2["params"]["vars"]["units2"] = "s"

    # define bounds of the variables
    i = random.randint(2,6)
    t_1 = random.randint(0,3)
    t_2 = random.randint(4,6)

    # store the variables in the dictionary "params"
    data2["params"]["v_1"] = i
    data2["params"]["t_1"] = t_1
    data2["params"]["t_2"] = t_2

    # Declare math symbols to be used by sympy
    t = sp.symbols('t')

    ## Part 1

    # Describe the solution equation
    height = ((i/2)*t**2)-((1/3)*t**3)

    # Answer to fill in the blank input -- must be stored as JSON.
    data2['correct_answers']['part1_ans'] = pl.to_json(height)


    ## Part 2

    # Describe the solution equation
    acc = i-(2*t)

    # Answer to fill in the blank input -- must be stored as JSON.
    data2['correct_answers']['part2_ans'] = pl.to_json(acc)

    ## Part 3

    # define correct answers
    Aavg = (((i*t_2)-((t_2)**2))-((i*t_1)-((t_1)**2)))/(t_2-t_1)
    data2['correct_answers']['part3_ans'] = Aavg

    ## Part 4

    # define correct answers
    data2["correct_answers"]['part4_ans'] = i

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
  label: $x(t)=$
  pl-customizations:
    variables: t
    weight: 1
    allow-blank: true
part2:
  type: symbolic-input
  label: $a= $
  pl-customizations:
    variables: t
    weight: 1
    allow-blank: true
part3:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $a= $
    suffix: $m/s^2$
part4:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $t= $
    suffix: s
substitutions:
  params:
    vars:
      title: Rocket
      units1: m/s^2
      units2: s
    v_1: 6
    t_1: 3
    t_2: 6
  correct_answers:
    part1_ans:
      _type: sympy
      _value: -0.333333333333333*t**3 + 3.0*t**2
      _variables:
      - t
    part2_ans:
      _type: sympy
      _value: 6 - 2*t
      _variables:
      - t
    part3_ans: -3.0
    part4_ans: 6
---
# {{ params.vars.title }}
A rocket has a velocity (pointing away from the launch pad) given by $v(t)$={{ params.i }}$t$-$t^2$
where $x$ is in meters, and $t$ is in seconds.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)