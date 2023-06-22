---
title: Camera Flash
topic: Circuits
author: Joseph Wandinger
source: 2.14.38
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 21.14.5.0
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
- problem 38
- circuits
- inductance
- capacitance
- LC circuits
- numeric
- JW
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $t =$
    suffix: $\rm\ s$
    comparison: relabs
    rtol: 0.03
    atol: 0
myst:
  substitutions:
    params_vars_title: Camera Flash
    params_I: '0.150'
    params_L: '2.25'
    params_V: '550'
---
# {{ params_vars_title }}
When a camera uses a flash, a fully-charged capacitor discharges through an inductor.

## Question Text

In what time must the ${{ params_I }}\rm\ A$ current through a ${{ params_L }}\rm\ mH$ inductor be switched on or off to induce a ${{ params_V }}\rm\ V$ emf?

### Answer Section

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$t =$ {{ correct_answers.part1_ans_str }} $\rm\ s$.

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)