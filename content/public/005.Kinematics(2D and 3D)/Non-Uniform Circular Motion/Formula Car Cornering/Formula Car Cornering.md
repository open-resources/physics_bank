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
    params_vars_title: Formula Car Cornering
    params_vars_units: $m/s^2$
    params_x: 4
    params_y1: 1.139
    params_y2: 1.478
    params_r: 59
    params_z: 126
    params_t: 1.7085
---
# {{ params_vars_title }}
A formula car is driving on the Autodromo Nazionale Monza race track. The car takes the racing line shown in blue through the Curva Parabolica corner.
The car's tangential motion is governed by the equation $s(t) = \frac{1}{3}( {{params_x}}(t-{{params_y1}})^3 + {{params_z}}t +{{params_y2}})$, when it starts taking the corner. It hits the apex of the corner at the time $t = {{params_t}} \ \rm{s}$, where the
turning radius is $r = {{params_r}} \ \rm{m}$.

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