---
title: Velocity and Net Force
topic: Force
author: Jake Bobowski
source: 2013 Final Q1
template_version: 1.0
attribution: standard
outcomes:
- 5.1.1.1
- 5.11.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- MP
assets:
- q1image.png
server:
  imports: |
    import random
    import pandas as pd
    import math
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: |
    # Start problem code

    data2 = nested_dict()

    # store phrases etc
    data2["params"]["vars"]["title"] = 'Velocity and Net Force'

    # set bounds of variables
    t = random.randint(0,4)
    v = math.cos(math.pi*t) #this value only represents the sign of v, not the actual value
    a = -math.sin(math.pi*t) #this value only represents the sign of a, not the actual value

    # define possible answers
    data2["params"]["part1"]["ans1"]["value"] = "Velocity is negative, net force is to the left"
    if v < 0 and a<0:
      data2["params"]["part1"]["ans1"]["correct"] = True
    else:
      data2["params"]["part1"]["ans1"]["correct"] = False

    data2["params"]["part1"]["ans2"]["value"] = "Velocity is negative, net force is to the right"
    if v < 0 and a > 0:
      data2["params"]["part1"]["ans2"]["correct"] = True
    else:
      data2["params"]["part1"]["ans2"]["correct"] = False

    data2["params"]["part1"]["ans3"]["value"] = "Velocity is negative, net force is zero"
    if v < 0 and a == 0:
      data2["params"]["part1"]["ans3"]["correct"] = True
    else:
      data2["params"]["part1"]["ans3"]["correct"] = False

    data2["params"]["part1"]["ans4"]["value"] = "Velocity is positive, net force is to the left"
    if v > 0 and a < 0:
      data2["params"]["part1"]["ans4"]["correct"] = True
    else:
      data2["params"]["part1"]["ans4"]["correct"] = False

    data2["params"]["part1"]["ans5"]["value"] = "Velocity is positive, net force is to the right"
    if v > 0 and a > 0:
      data2["params"]["part1"]["ans5"]["correct"] = True
    else:
      data2["params"]["part1"]["ans5"]["correct"] = False

    data2["params"]["part1"]["ans6"]["value"] = "Velocity is positive, net force is zero"
    if v > 0 and a == 0:
      data2["params"]["part1"]["ans6"]["correct"] = True
    else:
      data2["params"]["part1"]["ans6"]["correct"] = False

    data2["params"]["part1"]["ans7"]["value"] = "Velocity is zero, net force is to the left"
    if v == 0 and a < 0:
      data2["params"]["part1"]["ans7"]["correct"] = True
    else:
      data2["params"]["part1"]["ans7"]["correct"] = False

    data2["params"]["part1"]["ans8"]["value"] = "Velocity is zero, net force is to the right"
    if v == 0 and a > 0:
      data2["params"]["part1"]["ans8"]["correct"] = True
    else:
      data2["params"]["part1"]["ans8"]["correct"] = False

    data2["params"]["part1"]["ans9"]["value"] = "Velocity is zero, net force is zero"
    if v == 0 and a == 0:
      data2["params"]["part1"]["ans9"]["correct"] = True
    else:
      data2["params"]["part1"]["ans9"]["correct"] = False

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
      title: Velocity and Net Force
    part1:
      ans1:
        value: Velocity is negative, net force is to the left
        correct: true
      ans2:
        value: Velocity is negative, net force is to the right
        correct: false
      ans3:
        value: Velocity is negative, net force is zero
        correct: false
      ans4:
        value: Velocity is positive, net force is to the left
        correct: false
      ans5:
        value: Velocity is positive, net force is to the right
        correct: false
      ans6:
        value: Velocity is positive, net force is zero
        correct: false
      ans7:
        value: Velocity is zero, net force is to the left
        correct: false
      ans8:
        value: Velocity is zero, net force is to the right
        correct: false
      ans9:
        value: Velocity is zero, net force is zero
        correct: false
---
# {{ params.vars.title }}
The position versus time graph of a mass on a spring is shown in the image.

<img src="q1image.png" alt="Position vs. Time of Mass on Spring" width=300>

## Attribution

![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png) Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).