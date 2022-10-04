---
title: Switched LC Circuit
topic: Circuits
author: Joseph Wandinger
source: 2.14.68
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 21.13.3.0
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
- problem 68
- circuits
- voltage
- LC circuits
- multi-part
- JW
assets:
- fig_OSUPv2p14_68.png
part1:
  type: number-input
  pl-customizations:
    label: $f = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ Hz$
    weight: 1
    custom-format: .3g
part2:
  type: number-input
  pl-customizations:
    label: $Q_{C, \rm\ max} = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ C$
    weight: 1
    custom-format: .3g
part3:
  type: number-input
  pl-customizations:
    label: $I_{L, \rm\ max} = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ A$
    weight: 1
    custom-format: .3g
substitutions:
  params:
    vars:
      title: Switched LC Circuit
    L: '109.0'
    C: '4.75'
    V: '12.0'
---
# {{ params.vars.title }}
Consider the switched $LC$ circuit shown below.

<img src="fig_OSUPv2p14_68.png" width=325>

Consider the case that $\rm S_1$ is opened and $\rm S_2$ is closed simultaneously.
Here, $V = {{ params.V }}\rm\ V$, $L = {{ params.L }}\rm\ mH$, and $C = {{ params.C }}\rm\ \mu F$.

## Part 1

What is the frequency of the resulting oscillations?

### Answer Section

Please enter in a numeric value in $\rm\ Hz$.

## Part 2

What is the maximum charge on the capacitor?

### Answer Section

Please enter in a numeric value in $\rm\ C$.

## Part 3

What is the maximum current through the inductor?

### Answer Section

Please enter in a numeric value in $\rm\ A$.

### pl-submission-panel

{{ feedback.part1_ans }}<br>
{{ feedback.part2_ans }}<br>
{{ feedback.part3_ans }}

### pl-answer-panel

$f=$ {{ correct_answers.part1_ans_str }} $\rm\ Hz$<br>
$Q\_{C, \rm\ max}=$ {{ correct_answers.part2_ans_str }} $\rm\ C$<br>
$I\_{L, \rm\ max}=$ {{ correct_answers.part3_ans_str }} $\rm\ A$

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)