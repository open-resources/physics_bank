---
title: Work on Sliding Object
topic: Work
author: Jake Bobowski
source: 2017 Final Q6
template_version: 1.0
attribution: openstax-physics-vol2
outcomes:
- 9.2.1.1
- 9.1.1.1
- 8.3.1.0
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
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: |
    # Start problem code

    data2 = nested_dict()

    # store phrases etc
    data2["params"]["vars"]["title"] = 'Work on Sliding Object'

    # define possible answers
    data2["params"]["part1"]["ans1"]["value"] = 'equal to the work required to accelerate the object from v = 0 to v'
    data2["params"]["part1"]["ans1"]["correct"] = False

    data2["params"]["part1"]["ans2"]["value"] = 'twice the work required to accelerate the object from v = 0 to v'
    data2["params"]["part1"]["ans2"]["correct"] = False

    data2["params"]["part1"]["ans3"]["value"] = 'three times the work required to accelerate the object from v = 0 to v'
    data2["params"]["part1"]["ans3"]["correct"] = True

    data2["params"]["part1"]["ans4"]["value"] = 'four times the work required to accelerate the object from 2v to 3v'
    data2["params"]["part1"]["ans4"]["correct"] = False

    data2["params"]["part1"]["ans5"]["value"] = 'not known without knowledge of the acceleration'
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
      title: Work on Sliding Object
    part1:
      ans1:
        value: equal to the work required to accelerate the object from v = 0 to v
        correct: false
      ans2:
        value: twice the work required to accelerate the object from v = 0 to v
        correct: false
      ans3:
        value: three times the work required to accelerate the object from v = 0 to
          v
        correct: true
      ans4:
        value: four times the work required to accelerate the object from 2v to 3v
        correct: false
      ans5:
        value: not known without knowledge of the acceleration
        correct: false
---
# {{ params.vars.title }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)