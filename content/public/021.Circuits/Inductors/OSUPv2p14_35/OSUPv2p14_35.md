---
title: Inductance of a Coil
topic: Circuits
author: Joseph Wandinger
source: 2.14.35
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
- problem 35
- circuits
- self-inductance
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
myst:
  substitutions:
    params_vars_title: Inductance of a Coil
    params_V: '0.25'
    params_I_i: '0.25'
    params_I_f: '0.70'
    params_t: '0.85'
---
# {{ params_vars_title }}
An emf of ${{ params_V }}\rm\ V$ is induced across a coil when the current through it changes uniformly from ${{ params.I_i }}\rm\ A$ to ${{ params.I_f }}\rm\ A$ in ${{ params_t }}\rm\ s$.

## Question Text

What is the inductance of the coil?

### Answer Section

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$L =$ {{ correct_answers.part1_ans_str }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)