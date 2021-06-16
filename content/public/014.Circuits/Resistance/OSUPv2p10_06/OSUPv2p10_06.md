---
title: Resistors in a Lab
topic: Circuits
author: Joseph Wandinger
source: OSUP Volume 2, Chapter 10, Question 6
template_version: 1.0
attribution: openstax-physics-vol2
outcomes:
- 21.8.2.0
- 21.8.3.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- JW
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

    # define or load names/items/objects from server files

    # store phrases etc
    data2["params"]["vars"]["title"] = 'Resistors in a Lab'

    # Randomize Variables
    num = random.choice([0,1])
    if num == 0:
        have = 'larger'
        want = 'smaller'
    else:
        have = 'smaller'
        want = 'larger'

    # store the variables in the dictionary "params"
    data2["params"]["have"] = have
    data2["params"]["want"] = want

    # define possible answers
    data2["params"]["part1"]["ans1"]["value"] = 'Connect multiple resistors in parallel'

    data2["params"]["part1"]["ans2"]["value"] = 'Connect multiple resistors in series'

    if num == 0:
        data2["params"]["part1"]["ans1"]["correct"] = True
        data2["params"]["part1"]["ans2"]["correct"] = False
    else:
        data2["params"]["part1"]["ans1"]["correct"] = False
        data2["params"]["part1"]["ans2"]["correct"] = True

    data2["params"]["part1"]["ans3"]["value"] = 'Give up'
    data2["params"]["part1"]["ans3"]["correct"] = False

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
      title: Resistors in a Lab
    have: larger
    want: smaller
    part1:
      ans1:
        value: Connect multiple resistors in parallel
        correct: true
      ans2:
        value: Connect multiple resistors in series
        correct: false
      ans3:
        value: Give up
        correct: false
---
# {{ params.vars.title }}
Suppose you are doing a physics lab that asks you to put a resistor into a circuit, but all the resistors supplied have a {{ params.have }} resistance than the requested value.

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).
![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)