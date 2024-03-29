---
title: Relative Soccer Ball
topic: Kinematics(2D and 3D)
author: Tarek Alkabbani
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.8.1.3
- 7.3.1.3
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
- TA
- APSC181
assets:
- Relative Soccer Ball.jpg
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_x= $
    suffix: $\rm{N}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_y= $
    suffix: $\rm{N}$
myst:
  substitutions:
    params_vars_title: Relative Soccer Ball
    params_vars_units: N
    params_m: 0.33
    params_vp: 2.7
    params_theta: 54
    params_t: 0.048
    params_vbp: 11.33
    params_vy: 17.93
    params_vx: 19.73
---
# {{ params_vars_title }}
<img src="Relative Soccer Ball.jpg" width=700>

A football player is running up the soccer field at a velocity ${{params_vp}}\ \rm{m/s}$. A ball that has mass $m = {{params_m}}\ \rm{kg}$ is passed their way, and just before the player shoots the ball they observe that the ball is moving at a speed of ${{params_vbp}} \ \rm{m/s}$ and angle $\theta = {{params_theta}}^\circ$ relative to their motion.

Their foot is in contact with the ball for ${{params_t}}$ seconds and it imparted a change of velocity such that the absolute velocity now is $v_x = {{params_vx}} \ \rm{m/s}$ and  $v_y = {{params_vy}}\ \rm{m/s}$.

Find the average force components needed for this kick.

## Part 1

What is the x-component of the average force?

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 2

What is the y-component of the average force?

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)