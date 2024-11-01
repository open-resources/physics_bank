---
title: Distance travelled
topic: Kinematics(1D)
author: Firas Moosvi
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 4.3.1.1
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
- HZ
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        name: Santiago
        vehicle: rollerblades
        units: m
        title: Distance travelled
      v: 2
      t: 8
      part1:
        ans1:
          value: 42.0
        ans2:
          value: 16
        ans3:
          value: 10
        ans4:
          value: 0.25
        ans5:
          value: -6
        ans6:
          value: -7.8
---
# {{ params.vars.title }}
{{ params.vars.name }} is traveling on {{ params.vars.vehicle }} at {{ params.v }} $\rm{m/s}$.

## Part 1

How far does {{ params.vars.name }} travel in {{ params.t }} $\rm{s}$, assuming they continue at the same velocity?

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}
- {{ params.part1.ans5.value }} {{ params.vars.units}}
- {{ params.part1.ans6.value }} {{ params.vars.units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)