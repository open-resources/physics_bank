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
    params:
      vars:
        title: Drag Through Jello
        units: m/s
      v: 10
      t: 2.56
      theta: 38
      k: 0.4
---
# {{ params.vars.title }}
A projectile is shot into cherry Jello with velocity $v = {{ params.v }} \ \rm{m/s}$ at an angle $\theta = {{ params.theta }} ^{\circ}$ in the xy plane.
While in the Jello, the acceleration is subject to drag based on the tangential path the projectile travels.
The acceleration along the tangential path is given by $a = -kv$, where $k = {{ params.k }}$ is a constant and $v$ is the velocity of the projectile.

## Part 1

What is the x-velocity at $t = {{ params.t }} \ \rm{s}$

### Answer Section

## Part 2

What is the y-velocity at $t = {{ params.t }} \ \rm{s}$

### Answer Section

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)