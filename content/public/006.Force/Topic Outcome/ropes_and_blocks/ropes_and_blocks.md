---
title: Ropes and Blocks
topic: Force
author: Jake Bobowski
source: 2017 Final Q13
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.1.1.4
- 6.1.1.5
- 6.2.1.2
- 6.3.1.2
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- MP
assets:
- q13image.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a= $
    suffix: $\frac{m}{s^2}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $T= $
    suffix: N
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F= $
    suffix: N
myst:
  substitutions:
    params_vars_title: Ropes and Blocks
    params_vars_units1: $\frac{m}{s^2}$
    params_vars_units2: N
    params_m_a: 8
    params_m_b: 1
    params_m_c: 16
    params_f_a: 94
---
# {{ params_vars_title }}
Assume the three blocks portrayed in the figure move on a frictionless surface and a {{params.f_a}} N force
acts as shown on block C. The masses of the blocks are as follows: $m_a$ = {{params.m_a}} kg, $m_b$ = {{params.m_b}} kg, $m_c$ = {{params.m_c}} kg.

**Note: The blocks are _NOT_ drawn to scale, pay close attention to $m_a$, $m_b$, and $m_c$!**

<img src="q13image.png" alt="Blocks A, B and C, with force F_a pulling on them." >

## Part 1

Determine the acceleration of block C.

### Answer Section

Please enter in a numeric value in {{ params_vars_units1 }}.

## Part 2

Determine the magnitude of the tension in the cord connecting block C and block A.

### Answer Section

Please enter in a numeric value in {{ params_vars_units2 }}.

## Part 3

Determine the magnitude of the force exerted by block B on block A.

### Answer Section

Please enter in a numeric value in {{ params_vars_units2}}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)