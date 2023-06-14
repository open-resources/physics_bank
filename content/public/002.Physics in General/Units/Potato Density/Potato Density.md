---
title: Potato Density
topic: Physics in General
author: John Hopkinson
source: PHYS 112 2020W Group Problem Solving I Q1
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 2.2.1.3
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
- PW
- tutorial
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $m_p= $
    suffix: $kg$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $m_{cp}= $
    suffix: $kg$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $V_{cp}= $
    suffix: $m^3$
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $V_p= $
    suffix: $m^3$
myst:
  substitutions:
    params_vars_title: Potato Density
    params_vars_name: Emilia
    params_vars_unit1: $kg$
    params_vars_unit2: $m^3$
    params_m_p: 156
    params_m_cp: 64
    params_l: 3
---
# {{ params_vars_title }}
For their first lab, {{ params_vars_name }} decides to measure the density of a potato.
They notice that it's an unusual shape and floats, so it's hard to calculate its volume.
The potato's mass is measured to be {{ params.m_p }} $g$.
They then cut the potato into a cube and measure that the sides of the cube have length {{ params_l}} inches, and the potato's mass is {{ params.m_cp }} $g$.
For a uniform density potato, the mass and volume are proportional.

(Useful conversions: 1 $\textrm{inch}$ = 2.54 $cm$, 1 $cm$ = $10^{-2}$ $m$, 1 $g$ = $10^{-3}$ $kg$).

## Part 1

In SI units what is the potato's mass ($m_p$)?

### Answer Section

Please enter in a numeric value in {{ params_vars_unit1 }}.

## Part 2

In SI units what is the cube of potato's mass ($m\_{cp}$)?

### Answer Section

Please enter in a numeric value in {{ params_vars_unit1 }}.

## Part 3

In SI units, what is the volume of the cube of potato after it has been cut?

### Answer Section

Please enter in a numeric value in {{ params_vars_unit2 }}.

## Part 4

In SI units, what is the volume of the original potato?

(Hint: use proportional reasoning!)

### Answer Section

Please enter in a numeric value in {{ params_vars_unit2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)