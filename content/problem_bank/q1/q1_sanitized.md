---
title: Distance travelled
type: mcq
tags:
- kinematics
- test
outcomes:
- LO.kinematics.2305
- LO.kinematics.2304
assets:
- chunk.md
- ball.gif
substitutions:
  params:
    v: 2
    t: 10
    ans1: 20
    ans2: 12
    ans3: 0.2
    ans4: -8
    ans5: -10.4
    correct_answer: nan
  vars:
    name: Savannah
    vehicle: a tricycle
    title: Distance travelled
    units: m/s
---
# {{ vars.title }}

## Question Text

{{ vars.name }} is traveling on {{ vars.vehicle }} at {{ params.v }} {{ vars.units }}.
How far does {{ vars.name }} travel in {{ params.t }} seconds, assuming they continue at the same velocity?

<img src="ball.gif" width=300>

## Answer Choices

- {{ params.ans1}} {{ vars.units}} 
- {{ params.ans2}} {{ vars.units}} 
- {{ params.ans3}} {{ vars.units}} 
- {{ params.ans4}} {{ vars.units}} 
- {{ params.ans5}} {{ vars.units}} 