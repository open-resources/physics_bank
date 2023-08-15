---
title: System Open or Closed
topic: Momentum and Impulse
author: Jake Bobowski
source: 2015 Practice Midterm Q3
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 7.5.1.1
- 7.5.1.4
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- section
length:
- short
tags:
- EW
assets:
- open_closed.png
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params_vars_title: System Open or Closed
    params_vars_vehicle_c: Car
    params_vars_vehicle: car
    params_vars_units: kg
    params_i_a: 112
    params_i_b: 318
    params_part1_ans1_value: Yes, because the two carts are on a track with no friction.
    params_part1_ans2_value: Yes, because their change in velocities are the same.
    params_part1_ans3_value: No, because the total momentum is nonzero.
    params_part1_ans4_value: No, because the momentum is not conserved
---
# {{ params_vars_title }}
Two {{ params_vars_vehicle }}s collide on a track. {{ params_vars_vehicle_c }}  A comes up behind {{ params_vars_vehicle }}  B and runs into it.
{{ params_vars_vehicle_c }} A has mass of {{ params.i_a }} {{ params_vars_units }}, {{ params_vars_vehicle }} B has mass of {{ params.i_b }} {{ params_vars_units }}.
The following graph shows the velocity of each {{ params_vars_vehicle }} as a function of time.

<img alt="A velocity versus time graph where {{ params_vars_vehicle }} A has an initial velocity of 8 meters per second and {{ params_vars_vehicle }} B has an initial velocity of 1 meter per second. The two {{ params_vars_vehicle }}s collide at around 4 seconds. The velocity of {{ params_vars_vehicle }} A decreases to 2 meters per second and the velocity of {{ params_vars_vehicle }} B increases to 5 meters per second." src="open_closed.png" width=400>

## Question Text

Is the system isolated? Why or why not?

### Answer Section

- {{ params_part1_ans1_value }}
- {{ params_part1_ans2_value }}
- {{ params_part1_ans3_value }}
- {{ params_part1_ans4_value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)