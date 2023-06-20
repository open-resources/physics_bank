---
title: Rotating Coil
topic: Magnetism
author: Ava Cornell
source: 2.13.40
template_version: 1.1
attribution: openstax-physics-vol2
showCorrectAnswer: false
outcomes:
- 19.8.6.0
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
- problem 40
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
    label: $\varepsilon= $
    suffix: $\rm\ V$
myst:
  substitutions:
    params_vars_title: Rotating Coil
    params_N: '1400'
    params_a: '35'
    params_t: '0.005'
    params_B: '7.0'
---
# {{ params_vars_title }}

## Question Text

A coil of ${{params_N }}$ turns encloses an area of ${{params_a }}\rm\ {cm^2}$. It is rotated in ${{params_t }}\textrm{ s}$ from a position where its plane is perpendicular to Earth's magnetic field to one where its plane is parallel to the field. If the strength of the field is ${{params_B }} \times 10^{-5} \textrm{ T}$ what is the average emf induced in the coil?

### Answer Section

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$\varepsilon=$ {{ correct_answers.part1_ans_str }} $\rm\ V$

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)