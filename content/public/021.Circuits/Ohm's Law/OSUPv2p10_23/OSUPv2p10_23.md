---
title: Unknown Voltage Source
topic: Circuits
author: Joseph Wandinger
source: 2.10.23
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
- problem 23
- circuits
- Kirchhoff's rules
- multi-part
- JW
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
    weight: 1
    custom-format: .3g
part2:
  type: dropdown
  pl-customizations:
    blank: true
    weight: 1
substitutions:
  params:
    vars:
      title: Unknown Voltage Source
    dV: '2.60'
    dI: '5.70'
    part2:
      ans1:
        value: 'No'
      ans2:
        value: 'Yes'
---
# {{ params.vars.title }}

## Part 1

What is the internal resistance of a voltage source if its terminal potential drops by ${{ params.dV }}\rm\ V$ when the current supplied increases by ${{ params.dI }}\rm\ A$?

### Answer Section

Please enter a numeric value.

## Part 2

Can the emf of the voltage source be found with the information supplied?

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}
{{ feedback.part1_ans }}

### pl-answer-panel

$R=$ {{ correct_answers.part1_ans_str }} $\rm\ \Omega$

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)