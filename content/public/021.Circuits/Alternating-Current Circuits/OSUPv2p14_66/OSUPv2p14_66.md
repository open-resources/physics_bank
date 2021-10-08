---
title: Frequency and Voltage of an LC Circuit
topic: Circuits
author: Joseph Wandinger
source: 2.14.66
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
outcomes:
- 21.14.4.0
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
- problem 66
- circuits
- voltage
- RL circuits
- multi-part
- JW
part1:
  type: number-input
  pl-customizations:
    label: $f = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ Hz$
    weight: 1
    custom-format: .3g
part2:
  type: number-input
  pl-customizations:
    label: $I_{\rm max} = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ A$
    weight: 1
    custom-format: .3g
substitutions:
  params:
    vars:
      title: Frequency and Voltage of an LC Circuit
    L: '22.0'
    C: '3.0'
    V: '55.0'
---
# {{ params.vars.title }}
The self-inductance and capacitance of an oscillating $LC$ circuit are $L = {{ params.L }}\rm\ mH$ and $C = {{ params.C }}\rm\ \mu F$, respectively.

## Part 1

What is the frequency of the oscillations?

### Answer Section

Please enter in a numeric value in $\rm\ Hz$.

## Part 2

If the maximum potential difference between the plates of the capacitor is ${{ params.V }}\rm\ V$, what is the maximum current in the circuit?

### Answer Section

Please enter in a numeric value in $\rm\ A$.

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)