---
title: Distance travelled
topic: Kinematics
author: Firas Moosvi
source: original
template_version: 0.2
outcomes:
- LO.kinematics.2305
- LO.kinematics.2304
tags:
- quiz
- homework
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      name: Santiago
      vehicle: a bicycle
      units: m/s
      title: Distance travelled
    v: 6
    t: 9
    part1:
      ans1:
        value: 42
        correct: false
      ans2:
        value: 54
        correct: true
      ans3:
        value: 15
        correct: false
      ans4:
        value: 0.6666666666666666
        correct: false
      ans5:
        value: -3
        correct: false
      ans6:
        value: -3.9000000000000004
        correct: false
---
# {{ params.vars.title }}
## Part 1

{{ params.vars.name }} is traveling on {{ params.vars.vehicle }} at {{ params.v }} {{ params.vars.units }}.
How far does {{ params.vars.name }} travel in {{ params.t }} seconds, assuming they continue at the same velocity?

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}
- {{ params.part1.ans5.value }} {{ params.vars.units}}
- {{ params.part1.ans6.value }} {{ params.vars.units}}
