---
title: Characteristics of a Moving Rocket
topic: Kinematics(1D)
author: John Hopkinson
source: PHYS 112 2020W Midterm 1 Q1
template_version: 1.2
attribution: standard
outcomes:
- 4.3.1.0
- 4.6.3.0
- 4.7.3.0
- 1.7.2.2
- 1.8.1.2
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
span:
- undefined
length:
- undefined
tags:
- PW
assets: null
part1:
  type: checkbox
  pl-customizations:
    weight: 1
    partial-credit: true
    partial-credit-method: EDC
myst:
  substitutions:
    params:
      v_y: $-2t^3 - t^2 - 3t$
      vars:
        title: Characteristics of a Moving Rocket
      part1:
        ans1:
          value: $a_y(t) = -6t^2 - 2t - 3$
        ans2:
          value: $a_y(t = $ 6.8$s) = $ -294.04 $m/s^2$
        ans3:
          value: $y(t) = -t^4/2 - t^3/3 - 3t^2/2 + 7.7$
        ans4:
          value: $v_y(t=$ 3.3$s) = $ -92.664 $m/s$
        ans5:
          value: $v_y(t=$ 3.3$s) = $ -49.444 $m/s$
        ans6:
          value: $a_y(t = $ 6.8$s) = $ -13.485 $m/s^2$
---
# {{ params.vars.title }}

## Question Text

The velocity as a function of time for a rocket is $v_y(t) =$ {{ params.v_y }}, where $t$ is in seconds and $v_y$ is in $m/s$.

Sort the following statements about the position $y(t)$, velocity, and acceleration $a_y(t)$ of the rocket at general or specific times into those that are possibly consistent and those that are not possible given this velocity's time dependence.

Select the statements which are possibly consistent.

### Answer Section

Select all the choices that apply.

Note: You will be awarded full marks only if you select all the correct choices, and none of the incorrect choices. Choosing incorrect choices as well as not choosing correct choices will result in deductions.

- {{ params.part1.ans1.value}}
- {{ params.part1.ans2.value}}
- {{ params.part1.ans3.value}}
- {{ params.part1.ans4.value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)