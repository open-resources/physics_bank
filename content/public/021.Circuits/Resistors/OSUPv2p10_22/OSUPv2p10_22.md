---
title: Starter Motor Resistance
topic: Circuits
author: Joseph Wandinger
source: 2.10.22
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
- problem 22
- circuits
- resistors
- multi-part
- JW
assets: null
part1:
  type: number-input
  pl-customizations:
    label: $I_i=$
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
    label: $V_i=$
    allow-blank: false
    show-correct-answer: true
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ V$
    custom-format: .3g
    weight: 1
part3:
  type: number-input
  pl-customizations:
    label: $P_i=$
    allow-blank: false
    show-correct-answer: true
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ W$
    custom-format: .3g
    weight: 1
part4:
  type: number-input
  pl-customizations:
    label: $I_f=$
    allow-blank: false
    show-correct-answer: true
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ A$
    custom-format: .3g
    weight: 1
part5:
  type: number-input
  pl-customizations:
    label: $V_f=$
    allow-blank: false
    show-correct-answer: true
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ V$
    custom-format: .3g
    weight: 1
part6:
  type: number-input
  pl-customizations:
    label: $P_f=$
    allow-blank: false
    show-correct-answer: true
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ W$
    custom-format: .3g
    weight: 1
substitutions:
  params:
    vars:
      title: Starter Motor Resistance
    R_b: '0.009'
    R_m: '0.075'
    R_add: '0.099'
    V: '14.00'
---
# {{ params.vars.title }}
An automobile starter motor has an equivalent resistance of ${{ params.R_m }}\rm\ \Omega$ and is supplied by a ${{ params.V }}\rm\ V$ battery with a ${{ params.R_b }}\rm\ \Omega$ internal resistance.

## Part 1

What is the current to the motor?

### Answer Section

Please enter a numeric value.

## Part 2

What voltage is applied to the motor?

### Answer Section

Please enter a numeric value.

## Part 3

What power is supplied to the motor?

### Answer Section

Please enter a numeric value.

## Part 4

When the battery connections are corroded, its internal resistance increases by ${{ params.R_add }}\rm\ \Omega$.
Significant problems are caused by even small amounts of unwanted resistance in low-voltage, high-current applications.

What is the new current to the motor?

### Answer Section

Please enter a numeric value.

## Part 5

What is the new voltage applied to the motor?

### Answer Section

Please enter a numeric value.

## Part 6

What is the new power supplied to the motor?

### Answer Section

Please enter a numeric value.

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)