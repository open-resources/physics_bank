---
title: Circuit with Multiple Loops
topic: Circuits
author: Joseph Wandinger
source: 2.10.38
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
outcomes:
- 21.12.1.0
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
- volume 2
- chapter 10
- problem 38
- circuits
- Kirchhoff's rules
- multi-part
- JW
assets:
- fig_OSUPv2p10_38.png
part1:
  type: number-input
  pl-customizations:
    label: $V_1 = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ V$
    weight: 1
    custom-format: .2g
part2:
  type: number-input
  pl-customizations:
    label: $I_2 = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ A$
    weight: 1
    custom-format: .2g
part3:
  type: number-input
  pl-customizations:
    label: $I_3 = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ A$
    weight: 1
    custom-format: .2g
substitutions:
  params:
    vars:
      title: Circuit with Multiple Loops
    R1: '15.0'
    R2: '9.0'
    R3: '8.0'
    I1: '2.0'
    V2: '24.0'
---
# {{ params.vars.title }}
Consider the circuit shown below.

<img src="fig_OSUPv2p10_38.png" width=350>

It is known that $R_1 = {{ params.R1 }}\rm\ \Omega$, $R_2 = {{ params.R2 }}\rm\ \Omega$, $R_3 = {{ params.R3 }}\rm\ \Omega$, $I_1 = {{ params.I1 }}\rm\ A$, and $V_2 = {{ params.V2 }}\rm\ V$.

## Part 1

Find $V_1$.

### Answer Section

Please enter in a numeric value in $\rm\ V$.

## Part 2

Find $I_2$.

### Answer Section

Please enter in a numeric value in $\rm\ A$.

## Part 3

Find $I_3$.

### Answer Section

Please enter in a numeric value in $\rm\ A$.

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)