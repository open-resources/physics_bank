---
title: Square Coil
topic: Magnetism
author: Ava Cornell
source: 2.13.56
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 19.8.6.0
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
- chapter 13
- problem 56
- electromagnetic induction
- numeric
- AC
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $\omega= $
    suffix: $\rm\ {rad/s}$
myst:
  substitutions:
    params_vars_title: Square Coil
    params_N: '10'
    params_l: '25'
    params_B: '0.060'
    params_E: '10'
---
# {{ params_vars_title }}

## Question Text

A flat, square coil of {{params_N }} turns that has sides of length {{params_l }} $\rm\ {cm}$ is rotating in a magnetic field of strength {{params_B }} $\rm\ {T}$. If the maximum emf produced in the coil is {{params_E }} $\textrm{ mV}$, what is the angular velocity of the coil?

### Answer Section

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$\omega=$ {{ correct_answers.part1_ans_str }} $\rm\ {rad/s}$

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)