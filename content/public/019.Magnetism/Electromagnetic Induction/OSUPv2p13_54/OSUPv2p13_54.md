---
title: Electric Field Outside Solenoid
topic: Magnetism
author: Ava Cornell
source: 2.13.54
template_version: 1.1
attribution: openstax-physics-vol2
showCorrectAnswer: false
outcomes:
- 19.8.6.0
- 19.8.6.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- OSUP
- volume 2
- chapter 13
- problem 54
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
    label: $E= $
    suffix: $\rm\ {N/C}$
myst:
  substitutions:
    params_vars_title: Electric Field Outside Solenoid
    params_R: '3'
    params_r: '7'
    params_n: '25'
    params_DI: '5'
---
# {{ params_vars_title }}

## Question Text

The current in a long solenoid of radius ${{params_R }}\rm\ {cm}$ and ${{params_n }}\rm\ {turns/cm}$ is varied with time at a rate of ${{params_DI }}\rm\ {A/s}$. Find the magnitude of the electric field at a distance of ${{params_r }}\rm\ {cm}$ from the center of the solenoid.

### Answer Section

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$E=$ {{ correct_answers.part1_ans_str }} $\rm\ {N/C}$

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)