---
title: Long Cylindrical Solenoid
topic: Circuits
author: Joseph Wandinger
source: 2.14.43
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 21.14.2.2
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
- problem 43
- circuits
- inductance
- solenoids
- multi-part
- JW
part1:
  type: number-input
  pl-customizations:
    label: $L/\ell = $
    allow-blank: false
    show-correct-answer: true
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ H/m$
    weight: 1
    custom-format: .2g
part2:
  type: number-input
  pl-customizations:
    label: ${\boldsymbol \varepsilon}/\ell = $
    allow-blank: false
    show-correct-answer: true
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ V/m$
    weight: 1
    custom-format: .2g
myst:
  substitutions:
    params_vars_title: Long Cylindrical Solenoid
    params_n: '70'
    params_r: '2.5'
    params_dIdt: '7.0'
---
# {{ params_vars_title }}
A long, cylindrical solenoid with ${{ params_n }}\rm\ turns/cm$ has a radius of ${{ params_r }}\rm\ cm$.

## Part 1

Neglecting end effects, what is the self-inductance per unit length of the solenoid?

### Answer Section

Please enter in a numeric value in $\rm\ H/m$.

## Part 2

If the current through the solenoid changes at a rate of ${{ params_dIdt }}\rm\ A/s$, what is the emf induced per unit length?

### Answer Section

Please enter in a numeric value in $\rm\ V/m$.

### pl-submission-panel

{{ feedback.part1_ans }}<br>
{{ feedback.part2_ans }}

### pl-answer-panel

$L/\ell =$ {{ correct_answers.part1_ans_str }} $\rm\ H/m$<br>
${\boldsymbol \varepsilon}/{\ell} =$ {{ correct_answers.part2_ans_str }} $\rm\ V/m$

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)