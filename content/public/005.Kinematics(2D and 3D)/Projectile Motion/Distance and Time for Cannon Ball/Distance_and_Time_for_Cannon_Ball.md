---
title: Distance and Time for Cannon Ball
topic: Kinematics(2D and 3D)
author: Peyman Yousefi
source: APSC 181, Lecture 5, Q2
template_version: 1.1
attribution: standard
singleVariant: false
showCorrectAnswer: false
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
- APSC181
- Lecture Activities
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
    label: $x= $
    suffix: $m$
myst:
  substitutions:
    params_vars_title: Distance and Time for a Cannon Ball
    params_vars_distance_units: $m$
    params_vars_time_units: $seconds$
    params_distance_from_ground: 556
    params_speed_of_jett: 513
    params_angle: 57
---
# {{ params_vars_title }}
A cannon fires a projectile at a {{params_angle}}$^{\circ}$ angle at {{params.speed_of_jett}} $km/h$. The cannon is {{params.distance_from_ground}} $m$ above the ground.

<img src="L5Q3.png" width=85%>

## Part 1

Calculate the time taken $t$ from the point of fire to the point at which the projectile strikes the ground.

### Answer Section

Please enter in a numeric value in {{ params.vars.time_units }}.

## Part 2

Calculate the displacement in the $x$ direction from the point of fire to the point at which the projectile strikes the ground.

### Answer Section

- {{ params.part2.ans1.value}} {{ params.vars.distance_units}}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)