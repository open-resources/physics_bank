---
title: pdf-image-test
topic: Template
author: Firas Moosvi
source: 5.45
template_version: 1.1
attribution: standard
outcomes:
- null
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- unknown
assets:
- elevator.pdf
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: pdf-image-test
      name: Lorenzo
      vehicle: a skateboard
      units: m/s
    v: 6
    t: 6
    part1:
      ans1:
        value: 42
      ans2:
        value: 36
      ans3:
        value: 12
      ans4:
        value: 1.0
      ans5:
        value: 0
      ans6:
        value: 0.0
---
# {{ params.vars.title }}
{{ params.vars.name }} is traveling on {{ params.vars.vehicle }} at {{ params.v }} {{ params.vars.units }}.
## Part 1

![elevator](elevator.pdf)

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}
- {{ params.part1.ans5.value }} {{ params.vars.units}}
- {{ params.part1.ans6.value }} {{ params.vars.units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)