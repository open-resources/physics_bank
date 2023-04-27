---
title: 'RL Series Circuit: Energy'
topic: Circuits
author: Joseph Wandinger
source: 2.14.17
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 21.14.3.0
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
- problem 17
- circuits
- RL circuits
- numeric
- JW
assets:
- fig_OSUPv2p14_17.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $\frac{\displaystyle E_{\rm\ final}}{\displaystyle E_{\rm\ initial}} =$
    comparison: relabs
    rtol: 0.03
    atol: 0
myst:
  substitutions:
    params_vars_title: 'RL Series Circuit: Energy'
    params_factor: '3'
    params_word: reduced
    params_ans: '0.111'
---
# {{ params_vars_title }}
Consider the $RL$ circuit shown below.

<img src="fig_OSUPv2p14_17.png" width=250>

## Question Text

If the emf of the battery is {{ params_word }} by a factor of ${{ params_factor }}$, by how much does the steady-state energy stored in the magnetic field of the inductor change?

### Answer Section

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$\frac{\displaystyle E\_{\rm\ final}}{\displaystyle E\_{\rm\ initial}} =$ {{ correct_answers.part1_ans_str }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)