---
title: Force Vectors
topic: Force
author: Jake Bobowski
source: Original
template_version: 1.0
attribution: standard
outcomes:
- 6.6.1.1
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
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: |
    # Start problem code

    data2 = nested_dict()

    # define or load names/items/objects
    names = pd.read_csv("data/names.csv")["Names"].tolist()

    # store phrases etc
    data2["params"]["vars"]["title"] = 'Force Vectors'

    # define useful variables/lists

    # create list of anwers and shuffle
    answers = ["If two objects push on each other, they will accelerate in opposite directions.", "If two objects push on each other, their velocities will change by the same amount (though opposite directions).", "If two objects push on each other, their momenta will change by the same amount (though opposite directions).", "If you have a complicated system made of many objects (all interacting among themselves) only external forces can cause the center of mass of the system to accelerate.", "If you have a complicated system made of many objects (all interacting among themselves) only external forces can add or remove energy from the system." ]
    random.shuffle(answers)


    # Create ans_choices
    total_choices = len(answers)
    ans_choices = ["ans{0}".format(i+1) for i in range(total_choices)]


    # define possible answers
    for i in range(total_choices):
        choice = ans_choices.pop(0)
        this_answer = answers.pop()
        data2["params"]["part1"][choice]["value"] = this_answer

        if(this_answer == "If two objects push on each other, their velocities will change by the same amount (though opposite directions)." or this_answer == "If you have a complicated system made of many objects (all interacting among themselves) only external forces can add or remove energy from the system."):
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
      title: Force Vectors
    part1:
      ans1:
        value: If two objects push on each other, they will accelerate in opposite
          directions.
        correct: true
      ans2:
        value: If two objects push on each other, their momenta will change by the
          same amount (though opposite directions).
        correct: true
      ans3:
        value: If you have a complicated system made of many objects (all interacting
          among themselves) only external forces can add or remove energy from the
          system.
        correct: false
      ans4:
        value: If two objects push on each other, their velocities will change by
          the same amount (though opposite directions).
        correct: false
      ans5:
        value: If you have a complicated system made of many objects (all interacting
          among themselves) only external forces can cause the center of mass of the
          system to accelerate.
        correct: true
---
# {{ params.vars.title }}

## Attribution

![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png) Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).