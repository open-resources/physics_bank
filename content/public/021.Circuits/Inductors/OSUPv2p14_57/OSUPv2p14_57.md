---
title: 'Switched RL Series Circuit: Time Constant'
topic: Circuits
author: Joseph Wandinger
source: 2.14.57
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
outcomes:
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
- problem 57
- circuits
- inductance
- RL circuits
- multi-part
- JW
assets:
- fig_OSUPv2p14_57.png
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
    label: $R = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ \Omega$
    weight: 1
    custom-format: .3g
substitutions:
  params:
    vars:
      title: 'Switched RL Series Circuit: Time Constant'
    t: '1.95'
    L: '225.0'
---
# {{ params.vars.title }}
Consider the $RL$ circuit shown below.

<img src="fig_OSUPv2p14_57.png" width=250>

The current in the circuit reaches half of its maximum value in ${{ params.t }}\rm\ ms$ after switch $\rm S$ is thrown.

## Part 1

Determine the time constant $\tau_L$ of the circuit.

### Answer Section

Please enter in a numeric value in $\rm\ s$.

## Part 2

Given $L = {{ params.L }}\rm\ mH$, determine the resistance $R$ of the circuit.

### Answer Section

Please enter in a numeric value in $\rm\ \Omega$.

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)