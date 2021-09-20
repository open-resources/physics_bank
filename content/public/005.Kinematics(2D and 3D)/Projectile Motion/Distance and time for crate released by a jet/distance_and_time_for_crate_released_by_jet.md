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
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- AP
- APSC 181 - LA
assets:
- L5Q3.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $t= $
    suffix: $seconds$
    rtol: 0.02
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $s= $
    suffix: $m$
    rtol: 0.02
substitutions:
  params:
    vars:
      title: Distance and Time for a crate released by a Jett
      distance_units: $m$
      time_units: $seconds$
    distance_from_ground: 972
    speed_of_jett: 620
    angle: 64
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