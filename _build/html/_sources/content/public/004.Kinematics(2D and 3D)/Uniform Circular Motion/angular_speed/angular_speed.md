---
title: Angular Speed
topic: Kinematics(2D and 3D)
author: Jake Bobowski
source: 2012 Practice Final Q2
template_version: 1.0
attribution: standard
outcomes:
- 5.6.2.0
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
    data2["params"]["vars"]["title"] = 'Angular Speed'
    data2["params"]["vars"]["units"] = "rad/s"

    # Randomize Variables
    rev = random.randint(2,15)

    # store the variables in the dictionary "params"
    data2["params"]["rev"] = rev

    # define possible answers
    data2["params"]["part1"]["ans1"]["value"] = pbh.roundp((2*math.pi)/rev, sigfigs = 2)
    data2["params"]["part1"]["ans1"]["correct"] = False

    data2["params"]["part1"]["ans2"]["value"] = pbh.roundp(rev*(math.pi), sigfigs = 2)
    data2["params"]["part1"]["ans2"]["correct"] = False

    data2["params"]["part1"]["ans3"]["value"] = pbh.roundp(rev*(2*math.pi), sigfigs = 2)
    data2["params"]["part1"]["ans3"]["correct"] = True

    data2["params"]["part1"]["ans4"]["value"] = pbh.roundp(rev/(2*math.pi), sigfigs = 2)
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
      title: Angular Speed
      units: rad/s
    rev: 9
    part1:
      ans1:
        value: 0.7
        correct: false
      ans2:
        value: 28.0
        correct: false
      ans3:
        value: 57.0
        correct: true
      ans4:
        value: 1.4
        correct: false
---
# {{ params.vars.title }}

## Attribution

![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png) Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).