---
title: Power and Currents in a Three-Loop Circuit
topic: Circuits
author: Joseph Wandinger
source: 2.10.41
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 21.8.1.1
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
- problem 41
- circuits
- Kirchhoff's rules
- multi-part
- JW
assets:
- fig_OSUPv2p10_41.png
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
    custom-format: .3g
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
    custom-format: .3g
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
    custom-format: .3g
part4:
  type: number-input
  pl-customizations:
    label: $I_4 = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ A$
    weight: 1
    custom-format: .3g
part5:
  type: number-input
  pl-customizations:
    label: $I_5 = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ A$
    weight: 1
    custom-format: .3g
part6:
  type: number-input
  pl-customizations:
    label: $P_{\rm\ in} = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ W$
    weight: 1
    custom-format: .3g
part7:
  type: number-input
  pl-customizations:
    label: $P_{\rm\ out} = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ W$
    weight: 1
    custom-format: .3g
myst:
  substitutions:
    params_vars_title: Power and Currents in a Three-Loop Circuit
    params_R1: '5.00'
    params_R2: '2.00'
    params_R3: '4.00'
    params_R4: '8.00'
    params_V1: '13.0'
    params_V2: '10.00'
---
# {{ params_vars_title }}
Consider the circuit shown below.

<img src="fig_OSUPv2p10_41.png" width=400>

It is known that $V_1 = {{ params_V1 }}\rm\ V$, $V_2 = {{ params_V2 }}\rm\ V$, $R_1 = {{ params_R1 }}\rm\ \Omega$, $R_2 = {{ params_R2 }}\rm\ \Omega$, $R_3 = {{ params_R3 }}\rm\ \Omega$, and $R_4 = {{ params_R4 }}\rm\ \Omega$.

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

## Part 4

Find $I_4$.

### Answer Section

Please enter in a numeric value in $\rm\ A$.

## Part 5

Find $I_5$.

### Answer Section

Please enter in a numeric value in $\rm\ A$.

## Part 6

Find the total power supplied by the voltage sources.

### Answer Section

Please enter in a numeric value in $\rm\ W$.

## Part 7

Find the total power dissipated by the circuit.

### Answer Section

Please enter in a numeric value in $\rm\ W$.

### pl-submission-panel

{{ feedback.part1_ans }}<br>
{{ feedback.part2_ans }}<br>
{{ feedback.part3_ans }}<br>
{{ feedback.part4_ans }}<br>
{{ feedback.part5_ans }}<br>
{{ feedback.part6_ans }}<br>
{{ feedback.part7_ans }}

### pl-answer-panel

$I_1=$ {{ correct_answers.part1_ans_str }} $\rm\ A$<br>
$I_2=$ {{ correct_answers.part2_ans_str }} $\rm\ A$<br>
$I_3=$ {{ correct_answers.part3_ans_str }} $\rm\ A$<br>
$I_4=$ {{ correct_answers.part4_ans_str }} $\rm\ A$<br>
$I_5=$ {{ correct_answers.part5_ans_str }} $\rm\ A$<br>
$P\_{\rm in}=$ {{ correct_answers.part6_ans_str }} $\rm\ W$<br>
$P\_{\rm out}=$ {{ correct_answers.part7_ans_str }} $\rm\ W$

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)