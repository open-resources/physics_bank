---
title: Energy Stored in a Coil
topic: Circuits
author: Joseph Wandinger
source: 2.14.46
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 21.14.2.3
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
- problem 46
- circuits
- inductance
- solenoids
- numeric
- JW
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: false
    show-correct-answer: false
    show-help-text: true
    label: $L =$
    suffix: $\rm\ H$
    comparison: relabs
    rtol: 0.03
    atol: 0
myst:
  substitutions:
    params_vars_title: Energy Stored in a Coil
    params_I: '0.20'
    params_E: '2.0'
---
# {{ params_vars_title }}
At the instant a current of ${{ params_I }}\rm\ A$ is flowing through a coil of wire, the energy stored in its magnetic field is ${{ params_E }} \times 10^{-3}\rm\ J$.

## Question Text

What is the self-inductance of the coil?

### Answer Section

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$L =$ {{ correct_answers.part1_ans_str }} $\rm\ H$.

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)