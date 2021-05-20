---
title: Distance travelled
topic: kinematics
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
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $d= $
    suffix: m
    comparison: sigfig
    digits: 2
substitutions: !!python/object/apply:collections.defaultdict
  args:
  - &id001 !!python/name:__main__.%3Clambda%3E ''
  dictitems:
    params: !!python/object/apply:collections.defaultdict
      args:
      - *id001
      dictitems:
        vars: !!python/object/apply:collections.defaultdict
          args:
          - *id001
          dictitems:
            name: Santiago
            vehicle: a bicycle
            title: Distance travelled
            units: m/s
        v: 3
        t: 8
    correct_answers: !!python/object/apply:collections.defaultdict
      args:
      - *id001
      dictitems:
        part1_ans: 24
---
# {{ params.vars.title }}
## Question Text

{{ params.vars.name }} is traveling on {{ params.vars.vehicle }} at {{ params.v }} {{ params.vars.units }}.
How far does {{ params.vars.name }} travel in {{ params.t }} seconds, assuming they continue at the same velocity?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.
