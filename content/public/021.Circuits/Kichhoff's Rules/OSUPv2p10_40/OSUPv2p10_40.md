---
title: Circuit Loop within a Loop
topic: Circuits
author: Joseph Wandinger
source: 2.10.40
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 21.12.1.0
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
- problem 40
- circuits
- Kirchhoff's rules
- multi-part
- JW
assets:
- fig_OSUPv2p10_40.png
part1:
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
    custom-format: .2g
part2:
  type: number-input
  pl-customizations:
    label: $I_2 = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ A$
    weight: 1
    custom-format: .2g
part3:
  type: number-input
  pl-customizations:
    label: $I_3 = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ A$
    weight: 1
    custom-format: .2g
myst:
  substitutions:
    params_vars_title: Circuit Loop within a Loop
    params_R1: '5.0'
    params_R2: '4.0'
    params_R3: '5.0'
    params_V1: '20.0'
    params_V2: '10.0'
---
# {{ params_vars_title }}
Consider the circuit shown below.

<img src="fig_OSUPv2p10_40.png" width=350>

It is known that $V_1 = {{ params_V1 }}\rm\ V$, $V_2 = {{ params_V2 }}\rm\ V$, $R_1 = {{ params_R1 }}\rm\ \Omega$, $R_2 = {{ params_R2 }}\rm\ \Omega$, and $R_3 = {{ params_R3 }}\rm\ \Omega$.

## Part 1

Find $I_1$.

### Answer Section

Please enter in a numeric value in $\rm\ A$.

## Part 2

Find $I_2$.

### Answer Section

Please enter in a numeric value in $\rm\ A$.

## Part 3

Find $I_3$.

### Answer Section

Please enter in a numeric value in $\rm\ A$.

### pl-submission-panel

{{ feedback.part1_ans }}<br>
{{ feedback.part2_ans }}<br>
{{ feedback.part3_ans }}

### pl-answer-panel

$I_1 =$ {{ correct_answers.part1_ans_str }} $\rm\ A$<br>
$I_2 =$ {{ correct_answers.part2_ans_str }} $\rm\ A$<br>
$I_3 =$ {{ correct_answers.part3_ans_str }} $\rm\ A$

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)