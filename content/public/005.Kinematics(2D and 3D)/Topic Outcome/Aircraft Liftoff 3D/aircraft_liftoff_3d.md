---
title: Aircraft Liftoff 3D
topic: Kinematics(2D and 3D)
author: Peyman Yousefi
source: APSC 181, Lecture 10, Q1
template_version: 1.1
attribution: standard
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.7.1.2
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
- AP
- APSC181
- Lecture Activities
assets:
- L10Q1.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\dot{R}= $
    suffix: $km/h$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\dot{\theta}= $
    suffix: $rad/s$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\dot{\phi}= $
    suffix: $rad/s$
myst:
  substitutions:
    params:
      vars:
        title: Aircraft Liftoff 3D
      v: 11
      z: 275
      x: 467
      angle: 28
---
# {{ params.vars.title }}
<img src="L10Q1.png" width=85%>

A hot air balloon takes off at $A$ and climbs at a steady angle, $\theta\_{1} = {{params.angle}}^{\circ}$ in the y-z plane at a speed of {{params.v}} $km/h$. The hot air balloon is watched by two observers $O$.
Calculate the following values as the balloon passes point $B$, $x =$ {{params.x}} $m$ and $z =$ {{params.z}} $m$.

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