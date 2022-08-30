---
title: Electron in a Solenoid
topic: Magnetism
author: Jake Bobowksi
source: 2.12.55
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 19.2.3.0
- 19.2.3.1
- 19.3.2.0
- 19.3.2.1
- 19.6.1.0
- 19.6.1.1
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
- chapter 12
- problem 55
- magnetic force
- solenoid
- centripetal acceleration
- circular motion
- numeric
- JB
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $I= $
    suffix: $\rm\ A$
substitutions:
  params:
    vars:
      title: Electron in a Solenoid
    n: '35'
    r: '2.10'
    v: "$1.80\\times 10^{4 }\textrm{ m/s}$"
---
# {{ params.vars.title }}
A solenoid with {{ params.n }} turns per centimter carries a current $I$.
An electron moves within the solenoid in a circle of radius {{ params.r}}$\textrm{ cm}$.
The plane of the circular motion is perpendicular to the axis of the solenoid.The speed of the electron is {{ params.v }} $\textrm{ m/s}$.

## Question Text

What is the current $I$ in the solenoid?

### Answer Section

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$I=$ {{ correct_answers.part1_ans_str }} $\textrm{ A}$

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)