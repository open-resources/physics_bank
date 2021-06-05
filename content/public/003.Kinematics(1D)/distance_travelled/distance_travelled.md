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
      name: Ximena
      vehicle: a tricycle
      units: m/s
      title: Distance travelled
    v: 6
    t: 10
    part1:
      ans1:
        value: 42
      ans2:
        value: 60
      ans3:
        value: 16
      ans4:
        value: 0.6
      ans5:
        value: -4
      ans6:
        value: -5.2
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
