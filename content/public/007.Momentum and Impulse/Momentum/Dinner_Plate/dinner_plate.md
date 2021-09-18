---
title: Dinner Plate
topic: Momentum and Impulse
author: Jake Bobowski
source: 2016 Final Q1 P2
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 10.1.1.1
- 10.5.2.2
- 11.4.1.1
- 7.2.3.2
- 7.2.3.2
- 7.5.3.2
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
- AK
assets: null
part1:
  type: number-input
  pl-customizations:
    allow-blank: true
    weight: 1
    label: $\omega_i = $
part2:
  type: number-input
  pl-customizations:
    allow-blank: true
    weight: 1
    label: $I_p = $
part3:
  type: number-input
  pl-customizations:
    allow-blank: true
    weight: 1
    label: $L_i = $
part4:
  type: number-input
  pl-customizations:
    allow-blank: true
    weight: 1
    label: $w_f = $
part5:
  type: number-input
  pl-customizations:
    allow-blank: true
    weight: 1
    label: $\Delta E = $
substitutions:
  params:
    vars:
      title: Dinner Plate
      part1:
        units: rad/s
      part2:
        units: $kg m^2$
      part3:
        units: $kg m^2$/s
      part4:
        units: rad/s
      part5:
        units: J
    m_p: 1.03
    r_p: 0.48
    m: 2.7
    r: 0.28
    x: 3
---
# {{ params.vars.title }}
A cylindrical dinner plate is spinning out in space. It has mass $m_p =$ {{params.m_p}} $kg$, radius $r =$ {{ params.r_p }} $m$ and it rotates clockwise (as seen from above) {{ params.x }} times every second.
A (non-rotating) cylindrical cake is shot at it, in the manner shown, and it sticks to the surface of the plate.
The cake has a mass $m =$ {{ params.m }} $kg$ and radius $r =$ {{ params.r }} $m$.
In the end, both the cake and the plate rotate together.

## Part 1

Calculate the initial angular velocity of the plate.

### Answer Section

Please enter in a numeric value in {{ params.vars.part1.units }}.

## Part 2

Calculate the moment of interia of the plate.

### Answer Section

Please enter in a numeric value in {{ params.vars.part2.units }}.

## Part 3

Calculate the initial angular momentum of the system.

### Answer Section

Please enter in a numeric value in {{ params.vars.part3.units }}.

## Part 4

Calculate the final angular velocity of the system.

### Answer Section

Please enter in a numeric value in {{ params.vars.part4.units }}.

## Part 5

How much energy is dissipated in the collision?

### Answer Section

Please enter in a numeric value in {{ params.vars.part5.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)