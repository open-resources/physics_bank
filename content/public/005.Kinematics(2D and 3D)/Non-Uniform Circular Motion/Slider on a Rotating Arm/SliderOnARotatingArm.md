---
title: Slider on a Rotating Arm
topic: Kinematics(2D and 3D)
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
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
    suffix: $m/s^2$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $m/s$
substitutions:
  params:
    vars:
      title: Slider on a Rotating Arm
    n1: 0.08
    n2: 0.79
    n3: 0.14
    theta: 53
---
# {{ params.vars.title }}
The rotation of the arm $OA$ rotates about $O$ such that $\theta={{params.n1}}t^2$, where $\theta$ is in radians and $t$ in seconds.
Collar $B$ slides along the arm such that its distance to $O$ is $r={{params.n2}} - {{params.n3}}t^2$, where $r$ is in meters, and $t$ in seconds.

<img src="SliderOnARotatingArm.png" width=400 alt="An arm OA rotates about point O, and a collar slides along the arm. Its distance to O is r." >

## Part 1

After the arm $OA$ has rotated through ${{params.theta}}^\circ$, what is the magnitude of the relative acceleration of the collar $B$ with respect to the arm?

### Answer Section

Please enter in a numeric value in $m/s^2$.

## Part 2

What is the total relative speed of collar $B$ with respect to the arm?

### Answer Section

Please enter in a numeric value in $m/s$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)