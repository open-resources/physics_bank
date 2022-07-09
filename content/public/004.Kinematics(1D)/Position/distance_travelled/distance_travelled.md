---
title: Distance travelled
topic: Kinematics(1D)
author: Firas Moosvi
source: original
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- undefined
difficulty:
- Easy
randomization:
- 1
taxonomy:
- undefined
span:
- Section
length:
- Short
tags:
- unknown
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      name: Lorenzo
      vehicle: ice skates
      units: m
      title: Distance travelled
    v: 3
    t: 5
    part1:
      ans1:
        value: 42.0
      ans2:
        value: 15
      ans3:
        value: 8
      ans4:
        value: 0.6
      ans5:
        value: -2
      ans6:
        value: -2.6
---
# {{ params.vars.title }}
{{ params.vars.name }} is traveling on {{ params.vars.vehicle }} at {{ params.v }} {{ params.vars.units }}.

## Part 1

How far does {{ params.vars.name }} travel in {{ params.t }} seconds, assuming they continue at the same velocity?

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}
- {{ params.part1.ans5.value }} {{ params.vars.units}}
- {{ params.part1.ans6.value }} {{ params.vars.units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)