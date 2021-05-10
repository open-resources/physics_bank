---
title: Distance travelled
topic: Kinematics
author: Firas Moosvi
template_version: 0.2
source: original
tags:
- Firas Moosvi
- test
- 2305
- 2304
assets: null
part1:
  type: multiple-choice
  units: m/s
  pl-options:
    allow-blank: true
part2:
  type: multiple-choice
  units: m/s
  pl-options:
    allow-blank: true
substitutions:
  params:
    v: '5.00'
    t: '8.00'
    ans1: '4.00'
    ans2: '40.00'
    ans3: '13.00'
    ans4: '0.63'
    ans5: '-3.00'
    ans6: '-3.90'
    correct_answer: nan
  vars:
    name: Maya
    vehicle: a bicycle
    units: m/s
    digits_after_decimal: 2
---
# {{ vars.title }}
## Part A

{{ vars.name }} is traveling on {{ vars.vehicle }} at {{ params.v }} {{ vars.units }}.
How far does {{ vars.name }} travel in {{ params.t }} seconds, assuming they continue at the same velocity?

### Answer Section

- {{ params.ans1}} {{ vars.units}}
- {{ params.ans2}} {{ vars.units}}
- {{ params.ans3}} {{ vars.units}}
- {{ params.ans4}} {{ vars.units}}
- {{ params.ans5}} {{ vars.units}}
- {{ params.ans6}} {{ vars.units}}
## Part B

More instructions

### Answer Section

- {{ params.ans1}} {{ vars.units}}
- {{ params.ans2}} {{ vars.units}}
- {{ params.ans3}} {{ vars.units}}
- {{ params.ans4}} {{ vars.units}}
- {{ params.ans5}} {{ vars.units}}
- {{ params.ans6}} {{ vars.units}}
