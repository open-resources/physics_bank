---
title: Vehicle Crash
topic: Kinematics(1D)
author: John Hopkinson
source: PHYS 112 2016 W1 002 Mock Test Q4
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
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
      name: Santiago
      vehicle_1: van
      vehicle_2: van
    dist: 5.19
    v: 37.6
    acc: 10.4
    s_1: 0.1
    s_2: 1.492
    part1:
      ans1:
        value: 23.12 $m/s$
      ans2:
        value: 22.08 $m/s$
      ans3:
        value: 36.56 $m/s$
      ans4:
        value: 21.04 $m/s$
      ans5:
        value: 37.6 $m/s$
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