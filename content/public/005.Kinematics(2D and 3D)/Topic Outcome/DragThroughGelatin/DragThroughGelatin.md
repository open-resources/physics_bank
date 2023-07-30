---
title: Drag Through Jello
topic: Kinematics(2D and 3D)
author: Firas Moosvi
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.5.1.3
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
- JR
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_x= $
    suffix: $\rm{m/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_y= $
    suffix: $\rm{m/s}$
myst:
  substitutions:
    params_vars_title: Drag Through Jello
    params_vars_units: m/s
    params_v: 13
    params_t: 3.27
    params_theta: 40
    params_k: 0.6
---
# {{ params_vars_title }}
A projectile is shot into cherry Jello with velocity $v = {{ params_v }} \ \rm{m/s}$ at an angle $\theta = {{ params_theta }} ^{\circ}$ in the xy plane.
While in the Jello, the acceleration is subject to drag based on the tangential path the projectile travels.
The acceleration along the tangential path is given by $a = -kv$, where $k = {{ params_k }}$ is a constant and $v$ is the velocity of the projectile.

## Part 1

What is the x-velocity at $t = {{ params_t }} \ \rm{s}$

### Answer Section

## Part 2

What is the y-velocity at $t = {{ params_t }} \ \rm{s}$

### Answer Section

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)