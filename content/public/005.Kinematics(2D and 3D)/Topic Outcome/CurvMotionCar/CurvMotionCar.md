---
title: Curvilinear Motion of a Car
topic: Kinematics(2D and 3D)
author: Ranya Ghosh
source: original
template_version: 1.4
attribution: standard
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.7.1.2
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- RG
- APSC181
- JR
assets:
- CurvCar.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\rho = $
    suffix: $\rm{m}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a = $
    suffix: $\rm{m/s^2}$
myst:
  substitutions:
    params:
      vars:
        title: Curvilinear Motion of a Car
      m: 0.05
      v: 13
      vdot: 9
      d: 16
      h: 12.8
---
# {{ params.vars.title }}
<img src="CurvCar.png" width=90%>

A car travels down a hill which has a parabola of $y = {{ params.m }}x^2$.
At point A, the speed is $v = {{ params.v }} \ \rm{m/s}$ and it is increasing at the rate of $\dot v = {{ params.vdot }} \ \rm{m/s^2}$.
The height relative to the ground to point A is $h = {{ params.h }} \ \rm{m}$ and the distance from the origin to point A is $d = {{ params.d }} \ \rm{m}$.
What is the magnitude of acceleration at point A?

## Part 1

Determine the radius of curveture of the hill at point A.

### Answer Section

Please enter in a numeric value in $\rm{m}$.

## Part 2

Determine the magnitude of acceleration of the car.

### Answer Section

Please enter in a numeric value in $\rm{m/s^2}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)