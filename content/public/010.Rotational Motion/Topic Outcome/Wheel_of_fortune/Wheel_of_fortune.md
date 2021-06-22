---
title: Wheel of Fortune
topic: Rotational Motion
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
- AK
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
    w_int = random.randint(2,4)
    w_i = pbh.roundp(math.pi/w_int, decimals=2)
    t = random.randint(4, 6)
    a = w_i/t
    theta = (3/2)*math.pi

    # store the variables in the dictionary "params"
    data2["params"]["w_i"] = w_i
    data2["params"]["t"] = t
    data2["params"]["w_int"] = w_int


    # define possible answers
    data2["params"]["part1"]["ans1"]["value"] = pbh.roundp(2*a*(theta),decimals=2)
    data2["params"]["part1"]["ans1"]["correct"] = False

    data2["params"]["part1"]["ans2"]["value"] = pbh.roundp(math.sqrt(2*a*(theta)),decimals=2)
    data2["params"]["part1"]["ans2"]["correct"] = True

    data2["params"]["part1"]["ans3"]["value"] = pbh.roundp(2*(math.sqrt(2*a*theta)),decimals=2)
    data2["params"]["part1"]["ans3"]["correct"] = False

    data2["params"]["part1"]["ans4"]["value"] = f'$\pi$/{w_int}'
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
    w_i: 1.05
    t: 4
    w_int: 3
    part1:
      ans1:
        value: 2.47
        correct: false
      ans2:
        value: 1.57
        correct: true
      ans3:
        value: 3.15
        correct: false
      ans4:
        value: $\pi$/3
        correct: false
---
# {{ params.vars.title }}
I want to win a game of Wheel-of-Fortune.
The grand prize is initially located at a position at the top of the wheel (shown) and I only win if the wheel stops when the prize is at the position to the right ($\theta$ = 0).I note that when another contestant set the wheel spinning at $w_i = {\pi \over {{params.w_int}}} {rad\over s}$, it takes {{params.t}} seconds to stop.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)