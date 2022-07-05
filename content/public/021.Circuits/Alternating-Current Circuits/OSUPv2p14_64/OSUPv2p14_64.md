---
title: Frequency and Capacitance of an LC Circuit
topic: Circuits
author: Joseph Wandinger
source: 2.14.64
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 21.14.4.0
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
- problem 64
- circuits
- frequency
- LC circuits
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
substitutions:
  params:
    vars:
      title: Frequency and Capacitance of an LC Circuit
    f: '73.0'
    C: '14.5'
---
# {{ params.vars.title }}

## Question Text

What is the self-inductance of an $LC$ circuit that oscillates at ${{ params.f }}\rm\ Hz$ when the capacitance is ${{ params.C }}\rm\ \mu F$?

### Answer Section

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$L =$ {{ correct_answers.part1_ans_str }} $\rm\ H$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)