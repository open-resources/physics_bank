---
title: Kinetic Energy and Momentum
topic: Energy
author: Jake Bobowski
source: 2016 Final Q3
template_version: 1.0
attribution: standard
outcomes:
- 7.2.1.1
- 6.5.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- unknown
assets: null
server:
  imports: |
    import random
    import pandas as pd
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: |
    # Start problem code

    data2 = nested_dict()

    # define or load names/items/objects from server files

    # store phrases etc
    data2["params"]["vars"]["title"] = "Kinetic Energy and Momentum"

    # Randomize Variables

    # store the variables in the dictionary "params"

    # define possible answers

    data2["params"]["part1"]["ans1"]["value"] = "If I throw an object straight up (vertically) in the air, its kinetic energy at the highest point will be zero."
    data2["params"]["part1"]["ans1"]["correct"] = True

    data2["params"]["part1"]["ans2"]["value"] = "If I throw an object diagonally up in the air, its kinetic energy at the highest point will be zero."
    data2["params"]["part1"]["ans2"]["correct"] = False

    data2["params"]["part1"]["ans3"]["value"] = "If I throw an object diagonally up in the air, its momentum at the highest point will be zero."
    data2["params"]["part1"]["ans3"]["correct"] = False

    data2["params"]["part1"]["ans4"]["value"] = "If I throw an object into the AIR, the system composed of the object and the earth is a CLOSED system."
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
      title: Kinetic Energy and Momentum
    part1:
      ans1:
        value: If I throw an object straight up (vertically) in the air, its kinetic
          energy at the highest point will be zero.
        correct: true
      ans2:
        value: If I throw an object diagonally up in the air, its kinetic energy at
          the highest point will be zero.
        correct: false
      ans3:
        value: If I throw an object diagonally up in the air, its momentum at the
          highest point will be zero.
        correct: false
      ans4:
        value: If I throw an object into the AIR, the system composed of the object
          and the earth is a CLOSED system.
        correct: false
---
# {{ params.vars.title }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)