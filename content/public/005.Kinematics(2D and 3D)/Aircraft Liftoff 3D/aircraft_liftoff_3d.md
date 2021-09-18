---
title: Aircraft Liftoff 3D
topic: Kinematics(2D and 3D)
author: Peyman Yousefi
source: APSC 181, Lecture 10, Q1
template_version: 1.1
attribution: standard
outcomes:
- 5.7.1.2
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- AP
- APSC 181 - LA
assets:
- L10Q1.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\dot{R}= $
    suffix: $km/h$
    rtol: 0.02
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\dot{\theta}= $
    suffix: $rad/s$
    rtol: 0.02
part3:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\dot{\phi}= $
    suffix: $rad/s$
    rtol: 0.02
substitutions:
  params:
    vars:
      title: Aircraft Liftoff 3D
    v: 306
    z: 370
    x: 457
    angle: 0.3839724354387525
---
# {{ params.vars.title }}
<img src="L10Q1.png" width=85%>

A passenger plane takes off at $A$ and climbs at a steady angle, $\theta\_{1} = {{params.angle}}^{\circ}$ in the y-z plane at a speed of ${{params.v}}km/h$. The passenger plane is tracked by a radar dish at $O$.
Calculate the following values as the passenger plane passes point $B$, $x = {{params.x}}m$ and $z = {{params.z}}m$.

## Part 1

Calculate $\dot{R}$.

### Answer Section

## Part 2

Calculate $\dot{\theta}$.

### Answer Section

## Part 3

Calculate $\dot{\phi}$.

### Answer Section

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)