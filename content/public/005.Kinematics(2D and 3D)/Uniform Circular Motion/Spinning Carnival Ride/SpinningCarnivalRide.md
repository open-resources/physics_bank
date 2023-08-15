---
title: Spinning Carnival Ride
topic: Kinematics(2D and 3D)
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
outcomes:
- 5.6.1.0
- 5.8.1.3
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
- SpinningCarnivalRide.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{max}= $
    suffix: $\rm{m/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{min}= $
    suffix: $\rm{m/s}$
myst:
  substitutions:
    params_vars_title: Spinning Carnival Ride
    params_alpha_dot: 0.23
    params_beta_dot: 0.66
    params_r1: 3
    params_r2: 1.28
---
# {{ params_vars_title }}
The carnival ride illustrated below is spinning at $\dot \alpha = {{params.alpha_dot}} \ \rm{rev/s}$.
Each compartment's center is $r_1 = {{params_r1}} \ \rm{m}$ away from the center of the mechanism.
Passengers sit along the inner edge of the compartments, which have a radius $r_2 = {{params_r2}} \ \rm{m}$.
The compartments and the mechanism are spinning counterclockwise.

<img src="SpinningCarnivalRide.png" width=500 alt="A cross shape with circles at each end. Each circle is r1 away from the center, and each circle has radius r2. The whole mechanism spins at alpha dot, and a compartment is spinning at beta dot.">

## Part 1

If a compartment is spinning at $\dot \beta = {{params.beta_dot}} \ \rm{rev/s}$ relative to the arm holding it, what is the maximum speed felt by a passenger during the ride?

### Answer Section

Please enter in a numeric value in m/s.

## Part 2

What is the lowest speed?

### Answer Section

Please enter in a numeric value in m/s.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)