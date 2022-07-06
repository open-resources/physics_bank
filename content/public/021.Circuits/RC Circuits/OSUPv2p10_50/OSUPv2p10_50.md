---
title: Capacitor in a Heart Pacemaker
topic: Circuits
author: Joseph Wandinger
source: 2.10.50
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
outcomes:
- 21.13.1.0
- 21.13.2.0
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
- problem 50
- circuits
- RC circuits
- numeric
- JW
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $R= $
    suffix: $\rm\ \Omega$
    comparison: relabs
    rtol: 0.03
    atol: 0
substitutions:
  params:
    vars:
      title: Capacitor in a Heart Pacemaker
    rate: '77'
    C: '25.0'
    charge: '0.644'
---
# {{ params.vars.title }}
A heart pacemaker activates ${{ params.rate }}$ times per minute.
Each time, a ${{ params.C }}\rm\ nF$ capacitor is charged (by a battery in series with a resistor) to ${{ params.charge }}$ of its full voltage.

## Question Text

What is the value of the resistance?

### Answer Section

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$R=$ {{ correct_answers.part1_ans_str }} $\rm\ \Omega$

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)