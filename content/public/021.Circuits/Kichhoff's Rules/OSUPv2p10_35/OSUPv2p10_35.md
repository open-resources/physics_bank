---
title: Simple Series Circuit
topic: Circuits
author: Joseph Wandinger
source: 2.10.35
template_version: 1.3
attribution: openstax-physics-vol2
showCorrectAnswer: false
outcomes:
- 21.8.1.1
- 21.8.2.0
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
- problem 35
- circuits
- resistors
- multi-part
- JW
assets:
- fig_OSUPv2p10_35.png
part1:
  type: number-input
  pl-customizations:
    label: $R=$
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ \Omega$
    custom-format: .3g
    weight: 1
part2:
  type: number-input
  pl-customizations:
    label: $I_1=$
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ A$
    custom-format: .3g
    weight: 1
part3:
  type: number-input
  pl-customizations:
    label: $I_2=$
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ A$
    custom-format: .3g
    weight: 1
part4:
  type: number-input
  pl-customizations:
    label: $I_3=$
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ A$
    custom-format: .3g
    weight: 1
part5:
  type: number-input
  pl-customizations:
    label: $V_1=$
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ V$
    custom-format: .3g
    weight: 1
part6:
  type: number-input
  pl-customizations:
    label: $V_2=$
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ V$
    custom-format: .3g
    weight: 1
part7:
  type: number-input
  pl-customizations:
    label: $V_3=$
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ V$
    custom-format: .3g
    weight: 1
part8:
  type: number-input
  pl-customizations:
    label: $P_1=$
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ W$
    custom-format: .3g
    weight: 1
part9:
  type: number-input
  pl-customizations:
    label: $P_2=$
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ W$
    custom-format: .3g
    weight: 1
part10:
  type: number-input
  pl-customizations:
    label: $P_3=$
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ W$
    custom-format: .3g
    weight: 1
part11:
  type: number-input
  pl-customizations:
    label: $P=$
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ W$
    custom-format: .3g
    weight: 1
myst:
  substitutions:
    params_vars_title: Simple Series Circuit
    params_V: '13.0'
    params_R1: '3.50'
    params_R2: '3.00'
    params_R3: '5.00'
---
# {{ params_vars_title }}
Consider the circuit shown below.

<img src="fig_OSUPv2p10_35.png" width=250>

The terminal voltage of the battery is ${{ params_V }}\rm\ V$ and the resistances are $R_1 = {{ params_R1 }}\rm\ \Omega$, $R_2 = {{ params_R2 }}\rm\ \Omega$, and $R_3 = {{ params_R3 }}\rm\ \Omega$.

## Part 1

Find the equivalent resistance of the circuit.

### Answer Section

Please enter a numeric value.

## Part 2

Find the current through $R_1$.

### Answer Section

Please enter a numeric value.

## Part 3

Find the current through $R_2$.

### Answer Section

Please enter a numeric value.

## Part 4

Find the current through $R_3$.

### Answer Section

Please enter a numeric value.

## Part 5

Find the voltage drop across $R_1$.

### Answer Section

Please enter a numeric value.

## Part 6

Find the voltage drop across $R_2$.

### Answer Section

Please enter a numeric value.

## Part 7

Find the voltage drop across $R_3$.

### Answer Section

Please enter a numeric value.

## Part 8

Find the power dissipated by $R_1$.

### Answer Section

Please enter a numeric value.

## Part 9

Find the power dissipated by $R_2$.

### Answer Section

Please enter a numeric value.

## Part 10

Find the power dissipated by $R_3$.

### Answer Section

Please enter a numeric value.

## Part 11

Find the power supplied by the battery.

### Answer Section

Please enter a numeric value.

### pl-submission-panel

{{ feedback.part1_ans }}<br>
{{ feedback.part2_ans }}<br>
{{ feedback.part3_ans }}<br>
{{ feedback.part4_ans }}<br>
{{ feedback.part5_ans }}<br>
{{ feedback.part6_ans }}<br>
{{ feedback.part7_ans }}<br>
{{ feedback.part8_ans }}<br>
{{ feedback.part9_ans }}<br>
{{ feedback.part10_ans }}<br>
{{ feedback.part11_ans }}

### pl-answer-panel

$R =$ {{ correct_answers.part1_ans_str }} $\rm\ \Omega$<br>
$I_1 =$ {{ correct_answers.part2_ans_str }} $\rm\ A$<br>
$I_2 =$ {{ correct_answers.part3_ans_str }} $\rm\ A$<br>
$I_3 =$ {{ correct_answers.part4_ans_str }} $\rm\ A$<br>
$V_1 =$ {{ correct_answers.part5_ans_str }} $\rm\ V$<br>
$V_2 =$ {{ correct_answers.part6_ans_str }} $\rm\ V$<br>
$V_3 =$ {{ correct_answers.part7_ans_str }} $\rm\ V$<br>
$P_1 =$ {{ correct_answers.part8_ans_str }} $\rm\ W$<br>
$P_2 =$ {{ correct_answers.part9_ans_str }} $\rm\ W$<br>
$P_3 =$ {{ correct_answers.part10_ans_str }} $\rm\ W$<br>
$P =$ {{ correct_answers.part11_ans_str }} $\rm\ W$

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)