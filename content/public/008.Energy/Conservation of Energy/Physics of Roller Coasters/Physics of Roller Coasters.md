---
title: Physics of Roller-Coasters
topic: Energy
author: Jake Bobowski
source: 2012 Final Q10
template_version: 1.0
attribution: standard
outcomes:
- 8.5.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- PW
assets: null
server:
  imports: "import random as rd\nimport math \nimport problem_bank_helpers as pbh\n\
    from collections import defaultdict\nnested_dict = lambda: defaultdict(nested_dict)\n"
  generate: |
    # Start problem code

    data2 = nested_dict()

    # store phrases etc
    data2["params"]["vars"]["title"] = 'Physics of Roller-Coasters'
    data2["params"]["vars"]["units"] = "m/s"

    # Randomize Variables and round
    r = pbh.roundp(rd.uniform(10.0,30.0), sigfigs = 3)

    # store the variables in the dictionary "params"
    data2["params"]["r"] = r

    # define g
    g = 9.81

    # define possible answers
    data2["params"]["part1"]["ans1"]["value"] = pbh.roundp(math.sqrt(4*g*r), sigfigs = 3)
    data2["params"]["part1"]["ans1"]["correct"] = False

    data2["params"]["part1"]["ans2"]["value"] = pbh.roundp(math.sqrt(5*g*r), sigfigs = 3)
    data2["params"]["part1"]["ans2"]["correct"] = True

    data2["params"]["part1"]["ans3"]["value"] = pbh.roundp(math.sqrt(3*g*r), sigfigs = 3)
    data2["params"]["part1"]["ans3"]["correct"] = False

    data2["params"]["part1"]["ans4"]["value"] = pbh.roundp(math.sqrt(2*g*r), sigfigs = 3)
    data2["params"]["part1"]["ans4"]["correct"] = False

    data2["params"]["part1"]["ans5"]["value"] = pbh.roundp(math.sqrt(g*r), sigfigs = 3)
    data2["params"]["part1"]["ans5"]["correct"] = False

    data2["params"]["part1"]["ans6"]["value"] = pbh.roundp(math.sqrt(6*g*r), sigfigs = 3)
    data2["params"]["part1"]["ans6"]["correct"] = False

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
      title: Physics of Roller-Coasters
      units: m/s
    r: 13.3
    part1:
      ans1:
        value: 22.8
        correct: false
      ans2:
        value: 25.5
        correct: true
      ans3:
        value: 19.8
        correct: false
      ans4:
        value: 16.2
        correct: false
      ans5:
        value: 11.4
        correct: false
      ans6:
        value: 28.0
        correct: false
---
# {{ params.vars.title }}
A roller-coaster travels over a vertical, circular loop of radius $R = $ {{ params.r }} m.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)