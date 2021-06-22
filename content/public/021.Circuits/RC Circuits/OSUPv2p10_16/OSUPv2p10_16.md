---
title: RC Circuit with a Switch
topic: Circuits
author: Joseph Wandinger
source: 2.10.16
template_version: 1.0
attribution: openstax-physics-vol2
outcomes:
- 21.13.2.0
- 21.13.3.0
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
    data2["params"]["vars"]["title"] = 'RC Circuit with a Switch'

    # Randomize Variables

    # store the variables in the dictionary "params"

    # define possible answers
    data2["params"]["part1"]["ans1"]["value"] = 'Nothing. Current cannot flow across the capacitor, so the lamp remains dark.'
    data2["params"]["part1"]["ans1"]["correct"] = False

    data2["params"]["part1"]["ans2"]["value"] = 'When the switch is first closed, the current through the lamp is high and the lamp shines brightly. As the capacitor charges, the current decreases to zero, and the brightness of the lamp decreases until it becomes completely dark.'
    data2["params"]["part1"]["ans2"]["correct"] = True

    data2["params"]["part1"]["ans3"]["value"] = 'When the switch is first closed, the current through the lamp is low and the lamp shines dimly. As the capacitor charges, the current increases and the brightness of the lamp increases until it becomes very bright.'
    data2["params"]["part1"]["ans3"]["correct"] = False

    data2["params"]["part1"]["ans4"]["value"] = 'Current flows and the lamp turns on.'
    data2["params"]["part1"]["ans4"]["correct"] = False

    data2["params"]["part1"]["ans5"]["value"] = 'As the capacitor charges and discharges, the current flowing in the circuit fluctuates, causing the lamp to fluctuate between being bright and dark.'
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
      title: RC Circuit with a Switch
    part1:
      ans1:
        value: Nothing. Current cannot flow across the capacitor, so the lamp remains
          dark.
        correct: false
      ans2:
        value: When the switch is first closed, the current through the lamp is high
          and the lamp shines brightly. As the capacitor charges, the current decreases
          to zero, and the brightness of the lamp decreases until it becomes completely
          dark.
        correct: true
      ans3:
        value: When the switch is first closed, the current through the lamp is low
          and the lamp shines dimly. As the capacitor charges, the current increases
          and the brightness of the lamp increases until it becomes very bright.
        correct: false
      ans4:
        value: Current flows and the lamp turns on.
        correct: false
      ans5:
        value: As the capacitor charges and discharges, the current flowing in the
          circuit fluctuates, causing the lamp to fluctuate between being bright and
          dark.
        correct: false
---
# {{ params.vars.title }}
A battery, switch, capacitor, and lamp are connected in series.
The switch is initially open.

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)