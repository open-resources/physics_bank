---
title: Power Transmission To Dorm
topic: Electrical Power
author: Jake Bobowski
source: 2.9.61
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
outcomes:
- 21.6.1.0
- 21.6.1.1
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
- OSUP
- chapter 9
- problem 61
- electrical power
- power transmission
- power dissipated
- VS
assets: null
part1:
  type: number-input
  pl-customizations:
    label: $\rm{P_{lost}}=$
    allow-blank: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\%$
    weight: 1
part2:
  type: number-input
  pl-customizations:
    label: $\rm{P_{lost}}=$
    allow-blank: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\%$
    weight: 1
substitutions:
  params:
    vars:
      title: Power Transmission To Dorm
    I_ref: 3
    V_ref: 135
    P_bulb: 53
    P_light: 50
    P_other: 2
    V_pp: 135
    d_pp: 8
    Al_d: 7.715
---
# {{ params.vars.title }}
A physics student has a single-occupancy dorm room.
The student has a small refrigerator that runs with a current of ${{params.I_ref}}\textrm{ A}$ and a voltage of ${{params.V_ref}}\textrm{ V}$, a lamp that contains a ${{params.P_bulb}}\textrm{ W}$ bulb, an overhead light with a ${{params.P_light}}\textrm{ W}$ bulb, and various other small devices adding up to ${{params.P_other}}\textrm{ W}$.

## Part 1

Assuming the power plant that supplies ${{params.V_pp}}\textrm{ V}$ of electricity to the dorm is ${{params.d_pp}}\textrm{ km}$ away and the two aluminum transmission cables have a diameter of ${{params.Al_d}}\textrm{ mm}$, estimate the percentage of the total power supplied by the power company that is lost in the transmission.

### Answer Section

Please enter a numeric value.

## Part 2

What would be the result if the power company delivered the electric power at ${{params.V_pp}}\textrm{ kV}$?

### Answer Section

Please enter a numeric value.

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)