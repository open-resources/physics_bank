---
title: Rutland Rd
topic: Kinematics(2D and 3D)
author: John Hopkinson
source: PHYS 111 2013W1 MT2 Q1
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.8.1.3
difficulty:
- easy
randomization:
- 2
taxonomy:
- undefined
span:
- section
length:
- short
tags:
- MP
assets:
- q1.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $km/h$
part2:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params_vars_title: Rutland Rd
    params_vars_vehicle: truck
    params_vars_units: km/h
    params_v: 39
    params_part2_ans1_value: North
    params_part2_ans2_value: North-East
    params_part2_ans3_value: East
    params_part2_ans4_value: South-East
    params_part2_ans5_value: South
    params_part2_ans6_value: South-West
    params_part2_ans7_value: West
    params_part2_ans8_value: North-West
    params_part2_ans9_value: Impossible to know without knowing how far each car is
      from the intersection.
---
# {{ params_vars_title }}
A {{ params_vars_vehicle }} drives northward on Rutland Road North at {{ params_v }} {{ params_vars_units }} towards the intersection with 33rd Street.
A second {{ params_vars_vehicle }} drives eastward at {{params_v}} {{ params_vars_units }} on 33rd Street having just left the same intersection as shown in the figure below.

As a passenger in the second {{ params_vars_vehicle }}, the first {{ params_vars_vehicle }} appears to travel at a velocity $v$.

<img src="q1.png" width = 400px>

## Part 1

What is the magnitude of $v$, in {{ params_vars_units }}?

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 2

What is the (cardinal) direction of $v$ ?

### Answer Section

- {{ params_part2_ans1_value }}
- {{ params_part2_ans2_value }}
- {{ params_part2_ans3_value }}
- {{ params_part2_ans4_value }}
- {{ params_part2_ans5_value }}
- {{ params_part2_ans6_value }}
- {{ params_part2_ans7_value }}
- {{ params_part2_ans8_value }}
- {{ params_part2_ans9_value }}

### pl-submission-panel

Please enter in a numeric value in {{ params_vars_units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)