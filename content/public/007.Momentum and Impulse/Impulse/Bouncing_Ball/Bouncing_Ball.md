---
title: Bouncing Ball
topic: Momentum and Impulse
author: Jake Bobowski
source: 2012 Practice Final Q3
template_version: 1.0
attribution: standard
outcomes:
- 7.3.1.3
- 7.4.1.2
- 8.5.1.1
difficulty:
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
    import math
    import pandas as pd
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: |
    # Start problem code

    data2 = nested_dict()

    # store phrases etc
    data2["params"]["vars"]["title"] = 'Bouncing Ball'
    data2["params"]["vars"]["units_m"] = "kg"
    data2["params"]["vars"]["units_h"] = "m"
    data2["params"]["vars"]["units"] = "kgm/s"

    # Randomize Variables
    m = pbh.roundp(random.uniform(0.15,0.50), sigfigs = 3)
    h = pbh.roundp(random.uniform(0.5,2.5), sigfigs = 2)


    # store the variables in the dictionary "params"
    data2["params"]["m"] = m
    data2["params"]["h"] = h

    #define g
    g = 9.81

    # define possible answers
    data2["params"]["part1"]["ans1"]["value"] = pbh.roundp(m*math.sqrt(g*h), sigfigs = 2)
    data2["params"]["part1"]["ans1"]["correct"] = False

    data2["params"]["part1"]["ans2"]["value"] = pbh.roundp(m*math.sqrt(2*g*h), sigfigs = 2)
    data2["params"]["part1"]["ans2"]["correct"] = False

    data2["params"]["part1"]["ans3"]["value"] = pbh.roundp(2*m*math.sqrt(g*h), sigfigs = 2)
    data2["params"]["part1"]["ans3"]["correct"] = False

    data2["params"]["part1"]["ans4"]["value"] = pbh.roundp(2*m*math.sqrt(2*g*h), sigfigs = 2)
    data2["params"]["part1"]["ans4"]["correct"] = True

    data2["params"]["part1"]["ans5"]["value"] = pbh.roundp(g*m*h, sigfigs = 2)
    data2["params"]["part1"]["ans5"]["correct"] = False


    # Update the data object with a new dict
    data.update(data2)
  prepare: 'pass

    '
  parse: 'pass

    '
  grade: 'pass

    '
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Bouncing Ball
      units_m: kg
      units_h: m
      units: kgm/s
    m: 0.406
    h: 2.1
    part1:
      ans1:
        value: 1.8
        correct: false
      ans2:
        value: 2.6
        correct: false
      ans3:
        value: 3.7
        correct: false
      ans4:
        value: 5.2
        correct: true
      ans5:
        value: 8.4
        correct: false
---
# {{ params.vars.title }}
A ball of mass {{ params.m }} {{ params.vars.units_m}} is dropped vertically from a height of {{ params.h }} {{ params.vars.units_h}} and bounces back to the original height.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)