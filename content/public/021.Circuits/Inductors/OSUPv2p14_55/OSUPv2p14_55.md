---
title: Current over Time in a Series RL Circuit
topic: Circuits
author: Joseph Wandinger
source: 2.14.55
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 21.14.3.0
- 21.14.3.1
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
- problem 55
- circuits
- inductance
- RL circuits
- numeric
- JW
assets:
- fig_OSUPv2p14_55.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $t =$
    suffix: $\tau_L$
    comparison: relabs
    rtol: 0.03
    atol: 0
substitutions:
  params:
    vars:
      title: Current over Time in a Series RL Circuit
    fac: '5'
---
# {{ params.vars.title }}
Consider the $RL$ circuit shown below.

<img src="fig_OSUPv2p14_55.png" width=250>

## Question Text

How long after switch $\rm S$ is thrown does it take the current in the circuit to reach $1/{{ params.fac }}$ of its maximum value?
Express your answer in terms of the time constant $\tau_L$ of the circuit.

### Answer Section

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$t =$ {{ correct_answers.part1_ans_str }} $\tau_L$.

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)