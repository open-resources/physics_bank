---
title: Dinner Plate
topic: Momentum and Impulse
author: Jake Bobowski
source: 2016 Final Q1 P2
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 10.1.1.1
- 10.5.2.2
- 11.4.1.1
- 7.2.3.2
- 7.2.3.2
- 7.5.3.2
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- multi-chapter
length:
- long
tags:
- AK
- final_exam
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    allow-blank: true
    weight: 1
    label: $\omega_i = $
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    allow-blank: true
    weight: 1
    label: $I_p = $
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    allow-blank: true
    weight: 1
    label: $L_i = $
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    allow-blank: true
    weight: 1
    label: $w_f = $
part5:
  type: number-input
  pl-customizations:
    rtol: 0.05
    allow-blank: true
    weight: 1
    label: $\Delta E = $
myst:
  substitutions:
    params_vars_title: Dinner Plate
    params_vars_part1_units: rad/s
    params_vars_part2_units: $kg m^2$
    params_vars_part3_units: $kg m^2$/s
    params_vars_part4_units: rad/s
    params_vars_part5_units: J
    params_m_p: 1.24
    params_r_p: 0.14
    params_m: 2.17
    params_r: 0.23
    params_x: 6
---
# {{ params_vars_title }}
A cylindrical dinner plate is spinning out in space. It has mass $m_p =$ {{params_m_p}} $kg$, radius $r =$ {{ params_r_p }} $m$ and it rotates clockwise (as seen from above) {{ params_x }} times every second.
A (non-rotating) cylindrical cake is shot at it and the cake sticks to the surface of the plate.
The cake has a mass $m =$ {{ params_m }} $kg$ and radius $r =$ {{ params_r }} $m$.
In the end, both the cake and the plate rotate together.

## Part 1

Calculate the initial angular velocity of the plate.

### Answer Section

Please enter in a numeric value in {{ params_vars_part1_units }}.

## Part 2

Calculate the moment of interia of the plate.

### Answer Section

Please enter in a numeric value in {{ params_vars_part2_units }}.

## Part 3

Calculate the initial angular momentum of the system.

### Answer Section

Please enter in a numeric value in {{ params_vars_part3_units }}.

## Part 4

Calculate the final angular velocity of the system.

### Answer Section

Please enter in a numeric value in {{ params_vars_part4_units }}.

## Part 5

How much energy is dissipated in the collision?

### Answer Section

Please enter in a numeric value in {{ params_vars_part5_units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)