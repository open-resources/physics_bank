---
title: Frequency of an LC Circuit
topic: Circuits
author: Joseph Wandinger
source: 2.14.63
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
- problem 63
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
    label: $\omega =$
    suffix: $\rm\ rad/s$
    comparison: relabs
    rtol: 0.03
    atol: 0
substitutions:
  params:
    vars:
      title: Frequency of an LC Circuit
    L: '0.11'
    C: '2.0'
---
# {{ params.vars.title }}
The self-inductance and capacitance of an $LC$ circuit are $L = {{ params.L }}\rm\ mH$ and $C = {{ params.C }}\rm\ pF$.

## Question Text

What is the angular frequency at which the circuit oscillates?

### Answer Section

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$\omega =$ {{ correct_answers.part1_ans_str }} $\rm\ rad/s$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)