---
title: Dissipative Process
topic: Energy
author: Jake Bobowski
source: 2016 Final q5
template_version: 1.0
attribution: standard
outcomes:
- 8.5.1.0
- 8.1.1.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- AK
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

    # store title
    data2["params"]["vars"]["title"] = "Dissipative Energy"

    # define useful variables/lists

    # create list of answers and shuffle
    answers = ["Dissipative processes are one where the total mechanical energy is not conserved.", "Irreversible processes are dissipative.", "Coherent deformations are dissipative.", "Incoherent deformations are dissipative", "If the total kinetic energy is not constant all the way through the interaction, the process is dissipative."]
    random.shuffle(answers)

    # Create ans_choices
    total_choices = len(answers)
    ans_choices = ["ans{0}".format(i+1) for i in range(total_choices)]

    # define possible answers
    for i in range(total_choices):
        choice = ans_choices.pop(0)
        this_answer = answers.pop()
        data2["params"]["part1"][choice]["value"] = this_answer

        if(this_answer == "Coherent deformations are dissipative." or this_answer == "If the total kinetic energy is not constant all the way through the interaction, the process is dissipative."):
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
      title: Dissipative Energy
    part1:
      ans1:
        value: If the total kinetic energy is not constant all the way through the
          interaction, the process is dissipative.
        correct: false
      ans2:
        value: Dissipative processes are one where the total mechanical energy is
          not conserved.
        correct: true
      ans3:
        value: Coherent deformations are dissipative.
        correct: false
      ans4:
        value: Irreversible processes are dissipative.
        correct: true
      ans5:
        value: Incoherent deformations are dissipative
        correct: true
---
# {{ params.vars.title }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)