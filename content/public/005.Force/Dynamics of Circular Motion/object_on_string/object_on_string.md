---
title: Object Swung in Circular Path
topic: Force
author: Jake Bobowski
source: 2017 Final Q8
template_version: 1.0
attribution: standard
outcomes:
- 6.12.2.0
- 6.2.1.2
- 6.12.1.1
- 6.12.2.0
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
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: |
    # Start problem code

    data2 = nested_dict()

    # store phrases etc
    data2["params"]["vars"]["title"] = "Object Swung in Circular Path"
    data2["params"]["vars"]["units"] = "N"

    # Randomize Variables
    m = random.randint(1,20)*0.1
    r = random.randint(1,20)*0.5
    w = random.randint(1,9)
    g = 9.8

    # store the variables in the dictionary "params"
    data2["params"]["m"] = m
    data2["params"]["r"] = r
    data2["params"]["w"] = w

    # define possible answers
    data2["params"]["part1"]["ans1"]["value"] = pbh.roundp(m*((r*(w**2))-g), decimals=2)
    data2["params"]["part1"]["ans1"]["correct"] = True

    data2["params"]["part1"]["ans2"]["value"] = pbh.roundp(m*(r*((w**2)-g)), decimals=2)
    data2["params"]["part1"]["ans2"]["correct"] = False

    data2["params"]["part1"]["ans3"]["value"] = pbh.roundp(m*((r*(w**2))), decimals=2)
    data2["params"]["part1"]["ans3"]["correct"] = False

    data2["params"]["part1"]["ans4"]["value"] = 2*g
    data2["params"]["part1"]["ans4"]["correct"] = False

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
      title: Object Swung in Circular Path
      units: N
    m: 1.6
    r: 7.0
    w: 5
    part1:
      ans1:
        value: 264.32
        correct: true
      ans2:
        value: 170.24
        correct: false
      ans3:
        value: 280.0
        correct: false
      ans4:
        value: 19.6
        correct: false
---
# {{ params.vars.title }}
A {{params.m}} kg object attached to the end of a string of length {{params.r}} m is swung in a circular path
and in a vertical plane.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)