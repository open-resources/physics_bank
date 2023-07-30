---
title: Rocket Cart on a Track
topic: Work
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
outcomes:
- 9.2.1.0
- 6.9.1.3
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
- RocketOnATrack.png
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
    label: $W= $
    suffix: $\rm{kJ}$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{max}= $
    suffix: $\rm{m/s}$
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $W= $
    suffix: $\rm{kJ}$
myst:
  substitutions:
    params_vars_title: Rocket Cart on a Track
    params_nu: 0.24
    params_F: 2.28
    params_m: 165
    params_t: 3
---
# {{ params_vars_title }}
A ${{params_m}} \ \rm{kg}$ cart uses rocket propulsion to accelerate on a track.
The rockets are known to deliver ${{params_F}} \ \rm{kN}$ of thrust total.
The kinetic friction coefficient is ${{params_nu}}$.
The cart begins at rest, and the rockets are on for ${{params_t}} \ \rm{s}$.

<img src="RocketOnATrack.png" width=400 alt="Rockets mounted on a cart are pushing it forward on a track." >

## Part 1

What is the maximum speed of the cart?

### Answer Section

Please enter in a numeric value in m/s.

## Part 2

How much work was done by the rockets?

### Answer Section

Please enter in a numeric value in kJ.

## Part 3

If the rockets are angled upward to cancel friction, what is the new maximum speed of the cart?

### Answer Section

Please enter in a numeric value in m/s.

## Part 4

How much work was done by the rockets this time?

### Answer Section

Please enter in a numeric value in kJ.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)