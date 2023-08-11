---
title: Circular Motion of a Swinging Ball
topic: Kinematics(2D and 3D)
author: Ranya Ghosh
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.6.1.0
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
- APSC181
- RG
assets:
- ball.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t= $
    suffix: $\rm{s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $d= $
    suffix: $\rm{m}$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $T= $
    suffix: $\rm{N}$
myst:
  substitutions:
    params_vars_title: Circular Motion of a Swinging Ball
    params_vars_units: m, s, N
    params_m: 34
    params_r: 22.87
    params_h: 11
    params_v0: 9.63
---
# {{ params_vars_title }}
A ball with a mass of $m = {{ params_m }} \ \rm{kg}$ is being swung above in a horizontal circle.
If the radius is $r = {{params_r}} \ \rm{m}$, the height is $h = {{params_h}} \ \rm{m}$, and the speed is $v_0 = {{params_v0}} \ \rm{m/s}$ once the string breaks:

<img src="ball.png" width=400>

## Part 1

Find the time required for the ball to hit the ground.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 2

Find the distance the ball travels till it hits the ground.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}

## Part 3

Fine the tension in the string before the string broke

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)