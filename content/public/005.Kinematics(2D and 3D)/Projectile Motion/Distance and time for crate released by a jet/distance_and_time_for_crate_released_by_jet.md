---
title: Distance and Time for a crate released by a Jett
topic: Kinematics(2D and 3D)
author: Peyman Yousefi
source: APSC 181, Lecture 5, Q2
template_version: 1.1
attribution: standard
outcomes:
- 5.5.1.2
- 5.5.1.1
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- section
length:
- average
tags:
- AP
- APSC 181 - LA
assets:
- L5Q3.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t= $
    suffix: $seconds$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $s= $
    suffix: $m$
substitutions:
  params:
    vars:
      title: Distance and Time for a crate released by a Jett
      distance_units: $m$
      time_units: $seconds$
    distance_from_ground: 512
    speed_of_jett: 345
    angle: 60
---
# {{ params.vars.title }}
The pilot of a jet pulls into a steep {{params.angle}}$^{\circ}$ climb at {{params.speed_of_jett}} $km/h$ and releases a crate at point A, {{params.distance_from_ground}} $m$ above the ground.

<img src="L5Q3.png" width=85%>

## Part 1

Calculate the time taken $t$ from the point of release to the point at which the package strikes the ground.

### Answer Section

Please enter in a numeric value in {{ params.vars.time_units }}.

## Part 2

Calculate the distance $s$ from the point of release to the point at which the package strikes the ground.

### Answer Section

- {{ params.part2.ans1.value}} {{ params.vars.distance_units}}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)