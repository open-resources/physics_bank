---
title: System Open or Closed
topic: Momentum and Impulse
author: Jake Bobowski
source: 2015 Practice Midterm Q3
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
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
substitutions:
  params:
    vars:
      title: System Open or Closed
      vehicle_c: Bus
      vehicle: bus
      units: kg
    i_a: 142
    i_b: 290
    part1:
      ans1:
        value: Yes, because the two carts are on a track with no friction.
      ans2:
        value: Yes, because their change in velocities are the same.
      ans3:
        value: No, because the total momentum is nonzero.
      ans4:
        value: No, because the momentum is not conserved
---
# {{ params.vars.title }}
Two {{ params.vars.vehicle }}s collide on a track. {{ params.vars.vehicle_c }}  A comes up behind {{ params.vars.vehicle }}  B and runs into it.
{{ params.vars.vehicle_c }} A has mass of {{ params.i_a }} {{ params.vars.units }}, {{ params.vars.vehicle }} B has mass of {{ params.i_b }} {{ params.vars.units }}.
The following graph shows the velocity of each {{ params.vars.vehicle }} as a function of time.

<img alt="A velocity versus time graph where {{ params.vars.vehicle }} A has an initial velocity of 8 meters per second and {{ params.vars.vehicle }} B has an initial velocity of 1 meter per second. The two {{ params.vars.vehicle }}s collide at around 4 seconds. The velocity of {{ params.vars.vehicle }} A decreases to 2 meters per second and the velocity of {{ params.vars.vehicle }} B increases to 5 meters per second." src="open_closed.png" width=400>

## Question Text

Is the system isolated? Why or why not?

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)