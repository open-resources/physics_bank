---
title: RC Series Circuit
topic: Circuits
author: Joseph Wandinger
source: 2.10.53
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
outcomes:
- 21.13.2.0
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
- chapter 10
- problem 53
- circuits
- RC circuits
- multi-part
- JW
part1:
  type: number-input
  pl-customizations:
    label: $I_0 = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ A$
    weight: 1
    custom-format: .3g
part2:
  type: number-input
  pl-customizations:
    label: $\tau = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ s$
    weight: 1
    custom-format: .3g
part3:
  type: number-input
  pl-customizations:
    label: $I_1 = $
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
    label: $V = $
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
      title: RC Series Circuit
    R: '575.0'
    C: '2.00'
    V: '6.46'
---
# {{ params.vars.title }}
A ${{ params.R }}\rm\ \Omega$ resistor, an uncharged ${{ params.C }}\rm\ \mu F$ capacitor, and a ${{ params.V }}\rm\ V$ are connected in series.

## Part 1

What is the initial current?

### Answer Section

Please enter in a numeric value in $\rm\ A$.

## Part 2

What is the $RC$ time constant?

### Answer Section

Please enter in a numeric value in $\rm\ s$.

## Part 3

What is the current after one time constant?

### Answer Section

Please enter in a numeric value in $\rm\ A$.

## Part 4

What is the voltage on the capacitor after one time constant?

### Answer Section

Please enter in a numeric value in $\rm\ V$.

### pl-submission-panel

{{ feedback.part1_ans }}<br>
{{ feedback.part2_ans }}<br>
{{ feedback.part3_ans }}<br>
{{ feedback.part4_ans }}

### pl-answer-panel

$I_0 =$ {{ correct_answers.part1_ans_str }} $\rm\ A$<br>
$\tau =$ {{ correct_answers.part2_ans_str }} $\rm\ s$<br>
$I_1 =$ {{ correct_answers.part3_ans_str }} $\rm\ A$<br>
$V=$ {{ correct_answers.part4_ans_str }} $\rm\ V$

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)