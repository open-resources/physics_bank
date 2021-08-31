---
title: Electrocution Safety
topic: Circuits
author: Joseph Wandinger
source: 2.10.24
template_version: 1.1
attribution: openstax-physics-vol2
outcomes:
- 21.6.1.1
- 21.8.2.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- OSUP
- volume 2
- chapter 10
- problem 24
- circuits
- current
- multi-part
- JW
assets: null
part1:
  type: number-input
  pl-customizations:
    label: $I=$
    allow-blank: false
    show-correct-answer: true
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ A$
    custom-format: .3g
    weight: 1
part2:
  type: number-input
  pl-customizations:
    label: $P=$
    allow-blank: false
    show-correct-answer: true
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ W$
    custom-format: .3g
    weight: 1
part3:
  type: number-input
  pl-customizations:
    label: $R=$
    allow-blank: false
    show-correct-answer: true
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ \Omega$
    custom-format: .3g
    weight: 1
substitutions:
  params:
    R_b: '11.75'
    R_s: '2450'
    V_s: '20.5'
    I_max: '0.8'
---
# {{ params.vars.title }}
A person with body resistance between their hands of ${{ params.R_b }}\rm\ k \Omega$ accidentally grasps the terminals of a ${{ params.V_s }}\rm\ kV$ power supply.

(Do NOT do this!)

## Part 1

If the internal resistance of the power supply is ${{ params.R_s }}\rm\ \Omega$, what is the current through their body?

### Answer Section

Please enter a numeric value.

## Part 2

What is the power dissipated in their body?

### Answer Section

Please enter a numeric value.

## Part 3

If the power supply is to be made safe by increasing its internal resistance, what should the internal resistance be for the maximum current in this situation to be ${{ params.I_max }}\rm\ mA$ or less?

### Answer Section

Please enter a numeric value.

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)