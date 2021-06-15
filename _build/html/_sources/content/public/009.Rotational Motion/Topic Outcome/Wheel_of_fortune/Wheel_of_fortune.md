---
title: Wheel of Fortune
topic: Kinematics
author: Jake Bobowski
source: 2016 Final Q2
template_version: 1.0
attribution: standard
outcomes:
- 9.1.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- unknown
assets:
- wheel_of_fortune.png
server:
  imports: |
    import random
    import pandas as pd
    import math
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: |
    # Start problem code

    data2 = nested_dict()

    # define or load names/items/objects from server files

    # store phrases etc
    data2["params"]["vars"]["units"] = "rad/s"
    data2["params"]["vars"]["title"] = "Wheel of Fortune"

    # Randomize Variables
    w_i = math.pi/random.randint(2, 4)
    t = random.randint(4, 6)

    # store the variables in the dictionary "params"
    data2["params"]["w_i"] = w_i
    data2["params"]["t"] = t

    # define possible answers
    data2["params"]["part1"]["ans1"]["value"] = pbh.roundp(2*(-w_i/t)*((math.pow(-w_i,2))/2*-(w_i/t)),decimals=2)
    data2["params"]["part1"]["ans1"]["correct"] = False

    data2["params"]["part1"]["ans2"]["value"] = pbh.roundp(math.sqrt(2*(-w_i/t)*((math.pow(-w_i,2))/2*-(w_i/t))),decimals=2)
    data2["params"]["part1"]["ans2"]["correct"] = True

    data2["params"]["part1"]["ans3"]["value"] = pbh.roundp(2*(math.sqrt(2*(-w_i/t)*((math.pow(-w_i,2))/2*-(w_i/t)))),decimals=2)
    data2["params"]["part1"]["ans3"]["correct"] = False

    data2["params"]["part1"]["ans4"]["value"] = pbh.roundp(w_i,decimals=2)
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
      units: rad/s
      title: Wheel of Fortune
    w_i: 1.5707963267948966
    t: 5
    part1:
      ans1:
        value: 0.24
        correct: false
      ans2:
        value: 0.49
        correct: true
      ans3:
        value: 0.99
        correct: false
      ans4:
        value: 1.57
        correct: false
---
# {{ params.vars.title }}

## Attribution

![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png) Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).