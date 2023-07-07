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
myst:
  substitutions:
    params_vars_title: Vehicle Crash
    params_vars_name: Maya
    params_vars_vehicle_1: bus
    params_vars_vehicle_2: van
    params_dist: 3.95
    params_v: 39.6
    params_acc: 11.8
    params_s_1: 0.3
    params_s_2: 1.36
    params_part1_ans1_value: 27.09 $m/s$
    params_part1_ans2_value: 23.55 $m/s$
    params_part1_ans3_value: 36.06 $m/s$
    params_part1_ans4_value: 20.01 $m/s$
    params_part1_ans5_value: 39.6 $m/s$
---
# {{ params_vars_title }}
{{params_vars_name}} is following {{params_dist}} $m$ behind a {{params_vars.vehicle_1}} when it suddenly brakes with an acceleration of -{{params_acc}} $m/s^2$.
Both {{params_vars_name}}'s {{params_vars.vehicle_2}} and the {{params_vars.vehicle_1}} in front of {{params_vars_name}} were initially travelling at {{params_v}} $m/s$.
{{params_vars_name}} begins to brake ( with the same acceleration as the {{params_vars.vehicle_1}} in front) {{params.s_1}} $s$ after the {{params_vars.vehicle_1}} in front of {{params_vars_name}}.
{{params.s_2}} $s$ after the {{params_vars.vehicle_1}} in front of {{params_vars_name}} starts to brake, {{params_vars_name}} hits their {{params_vars.vehicle_1}}.

## Part 1

At what speed is {{params_vars_name}}'s {{params_vars.vehicle_2}} travelling when {{params_vars_name}} hit the {{params_vars.vehicle_1}} in front of them?

### Answer Section

- {{ params_part1_ans1_value }}
- {{ params_part1_ans2_value }}
- {{ params_part1_ans3_value }}
- {{ params_part1_ans4_value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)