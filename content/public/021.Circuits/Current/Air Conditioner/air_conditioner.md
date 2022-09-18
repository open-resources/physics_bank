---
title: Air Conditioner
topic: Circuits
author: Vanshika Sharma
source: 2.9.33
template_version: 1.1
attribution: standard
showCorrectAnswer: false
outcomes:
- 21.2.1.3
- 21.2.2.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- OSUP
- VS
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $J=$
    allow-blank: false
    show-correct-answer: false
    show-help-text: true
    suffix: $\rm\ {A/m^2}$
    weight: 1
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $v_{d} =$
    allow-blank: false
    show-help-text: true
    suffix: $\rm\ {m/s}$
    weight: 1
substitutions:
  params:
    vars:
      title: Air Conditioner
    I: 30
    n: 21
---
# {{ params.vars.title }}
The current supplied to an air conditioner unit is {{params.I}} $\textrm{A}$. The air conditioner is wired using a 10-gauge (diameter 2.588 mm) wire. The charge density is $ {{{params.n}} \times 10^{28}} {electrons \over m^3} $.

## Part 1

What is the magnitude of the current density?

### Answer Section

Please enter a numeric value.

## Part 2

What is the magnitude of the drift velocity.

### Answer Section

Please enter a numeric value.

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$J=$ {{ correct_answers.part1_ans_str }}  $\rm\ {A/m^2}$

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)