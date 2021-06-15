---
title: Rotational Inertia
topic: Rotational Dynamics
author: Jake Bobowski
source: 2013 Final Q6
template_version: 1.0
attribution: standard
outcomes:
- 10.4.1.0
- 10.3.1.4
- 10.4.1.1
- 9.5.2.2
- 10.2.1.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- MP
assets:
- q6image.png
server:
  imports: |
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: |
    # Start problem code
    data2 = nested_dict()

    # store phrases etc
    data2["params"]["vars"]["title"] = 'Rotational Inertia'
    data2["params"]["vars"]["units"] = 'm/s^2'

    # define possible answers
    data2["params"]["part1"]["ans1"]["value"] =  'g'
    data2["params"]["part1"]["ans1"]["correct"] = False

    data2["params"]["part1"]["ans2"]["value"] = '3g/4'
    data2["params"]["part1"]["ans2"]["correct"] = False

    data2["params"]["part1"]["ans3"]["value"] = '2g'
    data2["params"]["part1"]["ans3"]["correct"] = False

    data2["params"]["part1"]["ans4"]["value"] = '2g/3'
    data2["params"]["part1"]["ans4"]["correct"] = True

    data2["params"]["part1"]["ans5"]["value"] = 'g/2'
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
      title: Rotational Inertia
      units: m/s^2
    part1:
      ans1:
        value: g
        correct: false
      ans2:
        value: 3g/4
        correct: false
      ans3:
        value: 2g
        correct: false
      ans4:
        value: 2g/3
        correct: true
      ans5:
        value: g/2
        correct: false
---
# {{ params.vars.title }}

## Attribution

![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png) Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).