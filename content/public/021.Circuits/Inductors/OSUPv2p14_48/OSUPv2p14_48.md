---
title: Energy Stored in Different Coils
topic: Circuits
author: Joseph Wandinger
source: 2.14.48
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 21.14.2.3
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
- problem 48
- circuits
- inductance
- solenoids
- energy
- numeric
- JW
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $E_B/E_A =$
    comparison: relabs
    rtol: 0.03
    atol: 0
myst:
  substitutions:
    params_vars_title: Energy Stored in Different Coils
    params_num: '3'
---
# {{ params_vars_title }}
Solenoid $A$ is tightly wound while solenoid $B$ has windings that are evenly spaced with a gap equal to ${\rm {{ params_num }}} d$, where $d$ is the diameter of the wire.
The solenoids are otherwise identical.

## Question Text

Determine the ratio of the energies stored per unit length of these solenoids when the same current flows through each.

### Answer Section

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$E_B/E_A =$ {{ correct_answers.part1_ans_str }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)