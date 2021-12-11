---
title: Velocity and Acceleration of Particle in Curvilinear motion
topic: Kinematics(2D and 3D)
author: Peyman Yousefi
source: APSC181, Lecture 4, Q2
template_version: 1.1
attribution: standard
outcomes:
- 5.3.1.0
- 5.4.1.0
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
- APSC 181 - LA
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $m/s$
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $a= $
    suffix: $m/s^2$
substitutions:
  params:
    vars:
      title: Velocity and Acceleration of Particle in Curvilinear motion
    x_position: 2
    t: 0
    y_position: 0
    vxcon: 21
    vxcof: 15
---
# {{ params.vars.title }}
The curvilinear motion of a particle is defined by the x velocity, $v\_{x} = {{params.vxcon}} - {{params.vxcof}}t$ and the y position, $y = 50 - 2t^2$,
where $v\_{x}$ is in meters per second, $y$ is in $m$, and $t$ is in $seconds$.
If the x position is {{params.x_position}} at $t = {{params.t}}$:

## Part 1

Determine its velocity when $y={{params.y_position}}$.

### Answer Section

## Part 2

Determine its acceleration when $y={{params.y_position}}$.

### Answer Section

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)