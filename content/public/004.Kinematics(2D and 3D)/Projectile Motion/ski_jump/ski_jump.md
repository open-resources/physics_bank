---
title: Ski Jump
topic: Kinematics (2D and 3D)
author: Jake Bobowski
source: 2017 Final Q3
template_version: 1.0
attribution: standard
outcomes:
- 5.5.1.0
- 5.5.1.1
- 5.2.1.1
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
    import math
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: |
    # Start problem code

    data2 = nested_dict()

    # define or load names/items/objects
    jumpers = pd.read_csv("data/jumpers.csv")["Jumpers"].tolist()

    # store phrases etc
    data2["params"]["vars"]["sport"] = random.choice(jumpers)
    data2["params"]["vars"]["title"] = 'Ski Jump'
    data2["params"]["vars"]["units"] = 'm'

    # define bounds of the variables
    v = random.randint(18,25)
    d = 3 + random.randint(1,10)*0.2
    g = 9.81

    # store the variables in the dictionary "params"
    data2["params"]["v"] = v
    data2["params"]["d"] = d

    # define possible answers
    data2["params"]["part1"]["ans1"]["value"] = g
    data2["params"]["part1"]["ans1"]["correct"] = False

    data2["params"]["part1"]["ans2"]["value"] = pbh.roundp(v*math.sqrt(d/g), decimals=2)
    data2["params"]["part1"]["ans2"]["correct"] = False

    data2["params"]["part1"]["ans3"]["value"] = pbh.roundp(v*(2*d)/g, decimals=2)
    data2["params"]["part1"]["ans3"]["correct"] = False

    data2["params"]["part1"]["ans4"]["value"] = pbh.roundp(v*math.sqrt((2*d)/g), decimals=2)
    data2["params"]["part1"]["ans4"]["correct"] = True

    data2["params"]["part1"]["ans5"]["value"] =  pbh.roundp(v*(3*d)/g, decimals=2)
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
      sport: mountain biker
      title: Ski Jump
      units: m
    v: 25
    d: 4.8
    part1:
      ans1:
        value: 9.81
        correct: false
      ans2:
        value: 17.49
        correct: false
      ans3:
        value: 24.46
        correct: false
      ans4:
        value: 24.73
        correct: true
      ans5:
        value: 36.7
        correct: false
---
# {{ params.vars.title }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)