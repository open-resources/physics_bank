---
title: Rate of Change of Current in a Coil
topic: Circuits
author: Joseph Wandinger
source: 2.14.37
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
outcomes:
- 21.14.2.2
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
- problem 37
- circuits
- inductance
- numeric
- JW
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: false
    show-correct-answer: false
    show-help-text: true
    label: $dI/dt =$
    suffix: $\rm\ A/s$
    comparison: relabs
    rtol: 0.03
    atol: 0
    custom-format: .3g
substitutions:
  params:
    vars:
      title: Rate of Change of Current in a Coil
    L: '0.300'
    V: '0.300'
---
# {{ params.vars.title }}

## Question Text

What is the rate at which the current through a ${{ params.L }}\rm\ H$ coil is changing if an emf of ${{ params.V }}\rm\ V$ is induced across the coil?

### Answer Section

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$dI/dt =$ {{ correct_answers.part1_ans_str }} $\rm\ A/s$.

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)