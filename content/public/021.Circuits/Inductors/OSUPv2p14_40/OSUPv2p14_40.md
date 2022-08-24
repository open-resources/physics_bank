---
title: Inductance of a Solenoid
topic: Circuits
author: Joseph Wandinger
source: 2.14.40
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
- problem 40
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
    label: $L =$
    suffix: $\rm\ H$
    comparison: relabs
    rtol: 0.03
    atol: 0
    custom-format: .3g
substitutions:
  params:
    vars:
      title: Inductance of a Solenoid
    l: '52.0'
    N: '510'
    A: '1.30'
---
# {{ params.vars.title }}
A ${{ params.l }}\rm\ cm$ long solenoid is wound with ${{ params.N }}\rm\ turns$ of wire.
The cross-sectional area of the coil is ${{ params.A }}\rm\ cm^2$.

## Question Text

What is the self-inductance of the solenoid?

### Answer Section

Please enter a numeric value in $\rm\ H$.

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$L =$ {{ correct_answers.part1_ans_str }} $\rm\ H$.

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)