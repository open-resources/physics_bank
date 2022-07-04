---
title: Energy in a Series RL Circuit
topic: Circuits
author: Joseph Wandinger
source: 2.14.50
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
outcomes:
- 21.8.1.1
- 21.14.3.0
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
- problem 50
- circuits
- inductance
- energy
- multi-part
- JW
part1:
  type: number-input
  pl-customizations:
    label: $E = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ J$
    weight: 1
    custom-format: .3g
part2:
  type: number-input
  pl-customizations:
    label: $P = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ W$
    weight: 1
    custom-format: .3g
substitutions:
  params:
    vars:
      title: Energy in a Series RL Circuit
    L: '4.25'
    R: '500.0'
    I: '5.00'
---
# {{ params.vars.title }}
A coil with a self-inductance of ${{ params.L }}\rm\ H$ and a resistance of ${{ params.R }}\rm\ \Omega$ carries a steady current of ${{ params.I }}\rm\ A$.

## Part 1

What is the energy stored in the magnetic field of the coil?

### Answer Section

Please enter in a numeric value in $\rm\ J$.

## Part 2

What is the energy per second dissipated in the resistance of the coil?

### Answer Section

Please enter in a numeric value in $\rm\ W$.

### pl-submission-panel

{{ feedback.part1_ans }}<br>
{{ feedback.part2_ans }}

### pl-answer-panel

$E =$ {{ correct_answers.part1_ans_str }} $\rm\ J$<br>
$P =$ {{ correct_answers.part2_ans_str }} $\rm\ W$

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)