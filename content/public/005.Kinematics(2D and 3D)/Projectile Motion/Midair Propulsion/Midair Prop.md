---
title: Midair Propulsion
topic: Kinematics(2D and 3D)
author: Tarek Alkabbani
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.5.1.1
- 5.5.1.3
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
- Midair Propulsion.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $y= $
    suffix: $\rm{m}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t= $
    suffix: $\rm{s}$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 4
    allow-blank: true
    label: $x= $
    suffix: $\rm{m}$
myst:
  substitutions:
    params_vars_title: Midair Propulsion
    params_vars_time_units: s
    params_vars_dist_units: m
    params_vars_velo_units: m/s
    params_vars_acc_units: m/s^2
    params_v: 30
    params_theta: 38
    params_N: 4
    params_C: 1.4
---
# Midair Propulsion
We launch a projectile at an angle ${{ params_theta }}$ in degrees and speed ${{ params_v }}$ in $\rm{m/s}$ in a flat plane. At the peak of the projectile motion, a rocket turns on and starts accelerating the projectile in the x-axis according to the function $ a(t) = {{ params_C }} \times t^{ {{ params_N }} } $ in $\rm{m/s^2}$. Find the range it travels over the flight duration.

<img src="Midair Propulsion.png" width=600>

## Part 1

What is the maximum height the projectile will reach in {{ params_vars.dist_units }}?

### Answer Section

Please enter in a numeric value in {{ params_vars.dist_units }}.

## Part 2

How long will it take the projectile to reach this height in {{ params_vars.time_units }}?

### Answer Section

Please enter in a numeric value in {{ params_vars.time_units }}.

## Part 3

What is the range of travel for the projectile in {{ params_vars.dist_units }}?

### Answer Section

Please enter in a numeric value in {{ params_vars.dist_units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)