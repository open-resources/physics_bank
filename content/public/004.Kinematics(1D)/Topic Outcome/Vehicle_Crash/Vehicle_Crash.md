---
title: Vehicle Crash
topic: Kinematics(1D)
author: John Hopkinson
source: PHYS 112 2016 W1 002 Mock Test Q4
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 4.1.1.1
- 4.9.1.0
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- average
tags:
- EW
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Vehicle Crash
      name: Savannah
      vehicle_1: bus
      vehicle_2: van
    dist: 2.11
    v: 39.0
    acc: 12.7
    s_1: 0.2
    s_2: 1.543
    part1:
      ans1:
        value: 21.94 $m/s$
      ans2:
        value: 19.4 $m/s$
      ans3:
        value: 36.46 $m/s$
      ans4:
        value: 16.86 $m/s$
      ans5:
        value: 39.0 $m/s$
---
# {{ params.vars.title }}
{{params.vars.name}} is following {{params.dist}} $m$ behind a {{params.vars.vehicle_1}} when it suddenly brakes with an acceleration of -{{params.acc}} $m/s^2$.
Both {{params.vars.name}}'s {{params.vars.vehicle_2}} and the {{params.vars.vehicle_1}} in front of {{params.vars.name}} were initially travelling at {{params.v}} $m/s$.
{{params.vars.name}} begins to brake ( with the same acceleration as the {{params.vars.vehicle_1}} in front) {{params.s_1}} $s$ after the {{params.vars.vehicle_1}} in front of {{params.vars.name}}.
{{params.s_2}} $s$ after the {{params.vars.vehicle_1}} in front of {{params.vars.name}} starts to brake, {{params.vars.name}} hits their {{params.vars.vehicle_1}}.

## Part 1

At what speed is {{params.vars.name}}'s {{params.vars.vehicle_2}} travelling when {{params.vars.name}} hit the {{params.vars.vehicle_1}} in front of them?

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)