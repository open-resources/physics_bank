---
title: Car Testing Track
topic: Kinematics(2D and 3D)
author: Ranya Ghosh
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.6.1.0
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
- JR
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $\rm{m/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $d= $
    suffix: $\rm{m}$
myst:
  substitutions:
    params_vars_title: Distance travelled
    params_vars_units: m/s
    params_a: 0.41
    params_r: 72
---
# {{ params_vars_title }}
A car is undergoing public safety tests. It is being tested on a circular track with radius $r = {{ params_r }} \ \rm{m}$.
The car starts from rest with an instantaneous constant tangential acceleration of $a = {{ params_a }} \ \rm{m/s^2}$
Find the following at the point in time when the tangential and centripetal acceleration are the same.

## Part 1

The speed of the car.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 2

The distance the car has travelled.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)