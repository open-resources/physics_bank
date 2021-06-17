---
title: Isolated Systems
topic: Conservation of Momentum
author: Jake Bobowski
source: 2016 Final Q4
template_version: 1.0
attribution: standard
outcomes:
- 7.5.1.2
- 7.5.1.1
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

    # define or load names/items/objects

    # store phrases etc
    data2["params"]["vars"]["title"] = "Isolated Systems"

    # define useful variables/lists

    # create list of answers and shuffle
    answers = ["A system is isolated if its center of mass is moving with constant velocity", "A system is isolated if energy isn't entering or leaving the system", "A system is isolated if all of the external forces on it are balanced", "A system is isolated if its total momentum is constant"]
    random.shuffle(answers)

    # create ans_choices
    total_choices = len(answers)
    ans_choices = ["ans{0}".format(i+1) for i in range(total_choices)]

    # define possible answers

    for i in range(total_choices):
        choice = ans_choices.pop(0)
        this_answer = answers.pop()
        data2["params"]["part1"][choice]["value"] = this_answer

        if(this_answer == "A system is isolated if energy isn't entering or leaving the system"):
            data2["params"]["part1"][choice]["correct"] = False
        else:
            data2["params"]["part1"][choice]["correct"] = True

    # Update the data object with a new dict
    data.update(data2)
  prepare: 'pass

    '
  parse: 'pass

    '
  grade: 'pass

    '
part1:
  type: checkbox
  pl-customizations:
    weight: 1
    partial-credit: true
    partial-credit-method: EDC
substitutions:
  params:
    vars:
      title: Isolated Systems
    part1:
      ans1:
        value: A system is isolated if its total momentum is constant
        correct: true
      ans2:
        value: A system is isolated if energy isn't entering or leaving the system
        correct: false
      ans3:
        value: A system is isolated if all of the external forces on it are balanced
        correct: true
      ans4:
        value: A system is isolated if its center of mass is moving with constant
          velocity
        correct: true
---
# {{ params.vars.title }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)