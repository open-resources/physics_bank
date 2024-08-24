---
title: Formula Car Cornering
topic: Kinematics(2D and 3D)
author: Tarek Alkabbani
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.7.1.1
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
- TA
assets:
- formula.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a = $
    suffix: $\rm{m/s^2}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\theta = $
    suffix: $^{\circ}$
myst:
  substitutions:
    params:
      vars:
        title: Formula Car Cornering
        units: $m/s^2$
      x: 3
      y1: 1.602
      y2: 4.111
      r: 55
      z: 147
      t: 2.403
---
# {{ params.vars.title }}
A formula car is driving on the Autodromo Nazionale Monza race track. The car takes the racing line shown in blue through the Curva Parabolica corner.
The car's tangential motion is governed by the equation $s(t) = \frac{1}{3}( {{params.x}}(t-{{params.y1}})^3 + {{params.z}}t +{{params.y2}})$, when it starts taking the corner. It hits the apex of the corner at the time $t = {{params.t}} \ \rm{s}$, where the
turning radius is $r = {{params.r}} \ \rm{m}$.

## Part 1

What is the net acceleration at $t = {{parmas.t}} \ \rm{s}$?

### Answer Section

Please enter in a numeric value in $\rm{m/s^2}$.

## Part 2

What angle does the car's acceleration make with the tangential path?

### Answer Section

Please enter in a numeric value in degrees.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)