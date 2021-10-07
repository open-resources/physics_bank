---
title: Switched RL Series Circuit
topic: Circuits
author: Joseph Wandinger
source: 2.14.52
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
outcomes:
- 21.4.1.1
- 21.14.3.0
- 21.14.3.1
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
- chapter 14
- problem 52
- circuits
- inductance
- RL circuits
- multi-part
- JW
assets:
- fig_OSUPv2p14_52.png
part1:
  type: number-input
  pl-customizations:
    label: $\tau_L = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ s$
    weight: 1
    custom-format: .3g
part2:
  type: number-input
  pl-customizations:
    label: $I_{R, \rm\ i} = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ A$
    weight: 1
    custom-format: .3g
part3:
  type: number-input
  pl-customizations:
    label: $I_{R, \rm\ f} = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ A$
    weight: 1
    custom-format: .3g
part4:
  type: number-input
  pl-customizations:
    label: $I_R(t^{\star} = {{ params.num }} \tau_L) = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ A$
    weight: 1
    custom-format: .3g
part5:
  type: number-input
  pl-customizations:
    label: $V_L(t^{\star} = {{ params.num }} \tau_L) = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ V$
    weight: 1
    custom-format: .3g
part6:
  type: number-input
  pl-customizations:
    label: $V_R(t^{\star} = {{ params.num }} \tau_L) = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ V$
    weight: 1
    custom-format: .3g
substitutions:
  params:
    vars:
      title: Switched RL Series Circuit
    num: '2'
    emf: '13.0'
    L: '20.0'
    R: '9.00'
---
# {{ params.vars.title }}
Consider the $RL$ circuit shown below.

<img src="fig_OSUPv2p14_52.png" width=250>

Here, ${\boldsymbol \varepsilon} = {{ params.emf }}\rm\ V$, $L = {{ params.L }}\rm\ mH$, and $R = {{ params.R }}\rm\ \Omega$.

## Part 1

Determine the time constant of the circuit.

### Answer Section

Please enter in a numeric value in $\rm\ s$.

## Part 2

Immediately after switch $\rm S$ is closed, what is the initial current through the resistor?

### Answer Section

Please enter in a numeric value in $\rm\ A$.

## Part 3

What is the final current through the resistor?

### Answer Section

Please enter in a numeric value in $\rm\ A$.

## Part 4

What is the current through the resistor when $t = t^{\star} = {{ params.num }} \tau_L$?

### Answer Section

Please enter in a numeric value in $\rm\ A$.

## Part 5

What is the voltage across the inductor when $t = t^{\star} = {{ params.num }} \tau_L$?

### Answer Section

Please enter in a numeric value in $\rm\ V$.

## Part 6

What is the voltage across the resistor when $t = t^{\star} = {{ params.num }} \tau_L$?

### Answer Section

Please enter in a numeric value in $\rm\ V$.

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)