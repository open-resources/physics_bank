---
title: Wire in an external magnetic field
topic: Magnetism
author: Jake Bobowksi
source: 2.12.25
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 19.2.4.1
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
- problem 25
- Ampere's law
- line of current
- magnetic field
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
    label: $B= $
    suffix: $\rm\ \mu T$
myst:
  substitutions:
    params_vars_title: Wire in an external magnetic field
    params_I: '16.0'
    params_Bext: '32.5'
    params_d: '28.5'
---
# {{ params_vars_title }}
A long, straight, horizontal wire carries a left-to-right current of {{ params_I }}$\rm\ A$.
The wire is placed in a uniform magnetic field of magnitude {{ params_Bext }}$~\mu\mathrm{T}$ that is directed vertically downward.

## Question Text

What is the magnitude of the net magnetic field {{ params_d }}$\rm\ cm$ above the wire?

### Answer Section

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$B=$ {{ correct_answers.part1_ans_str }} $\rm\ \mu T$

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)