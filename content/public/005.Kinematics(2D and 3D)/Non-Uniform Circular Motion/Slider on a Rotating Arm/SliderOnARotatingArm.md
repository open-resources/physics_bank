---
title: Slider on a Rotating Arm
topic: Kinematics(2D and 3D)
author: Patrick Jilek-Rodriguez
source: WebWork
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.3.1.0
- 5.7.1.1
- 5.9.1.0
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
- PJ
assets:
- SliderOnARotatingArm.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a= $
    suffix: $\rm{m/s^2}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $\rm{m/s}$
myst:
  substitutions:
    params_vars_title: Slider on a Rotating Arm
    params_n1: 0.1
    params_n2: 0.91
    params_n3: 0.16
    params_theta: 50
---
# {{ params_vars_title }}
The rotation of the arm $OA$ rotates about $O$ such that $\theta={{params_n1}}t^2$, where $\theta$ is in radians and $t$ in seconds.
Collar $B$ slides along the arm such that its distance to $O$ is $r={{params_n2}} - {{params_n3}}t^2$, where $r$ is in meters, and $t$ in seconds.

<img src="SliderOnARotatingArm.png" width=400 alt="An arm OA rotates about point O, and a collar slides along the arm. Its distance to O is r." >

## Part 1

After the arm $OA$ has rotated through ${{params_theta}}^\circ$, what is the magnitude of the relative acceleration of the collar $B$ with respect to the arm?

### Answer Section

Please enter in a numeric value in $m/s^2$.

## Part 2

What is the total relative speed of collar $B$ with respect to the arm?

### Answer Section

Please enter in a numeric value in $m/s$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)