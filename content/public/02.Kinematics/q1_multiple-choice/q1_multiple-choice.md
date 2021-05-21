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
            name: Abbas
            vehicle: ice skates
            units: m/s
        v: 4
        t: 10
        part1: !!python/object/apply:collections.defaultdict
          args:
          - *id001
          dictitems:
            ans1: !!python/object/apply:collections.defaultdict
              args:
              - *id001
              dictitems:
                value: 42
                correct: false
            ans2: !!python/object/apply:collections.defaultdict
              args:
              - *id001
              dictitems:
                value: 40
                correct: true
            ans3: !!python/object/apply:collections.defaultdict
              args:
              - *id001
              dictitems:
                value: 14
                correct: false
            ans4: !!python/object/apply:collections.defaultdict
              args:
              - *id001
              dictitems:
                value: 0.4
                correct: false
            ans5: !!python/object/apply:collections.defaultdict
              args:
              - *id001
              dictitems:
                value: -6
                correct: false
            ans6: !!python/object/apply:collections.defaultdict
              args:
              - *id001
              dictitems:
                value: -7.800000000000001
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
