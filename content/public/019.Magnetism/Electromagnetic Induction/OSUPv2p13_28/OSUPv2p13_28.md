---
title: Single-Turn Rectangular Coil
topic: Magnetism
author: Ava Cornell
source: 2.13.28
template_version: 1.0
attribution: openstax-physics-vol2
showCorrectAnswer: false
outcomes:
- 19.8.1.0
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
- problem 28
- electromagnetic induction
- numeric
- AC
assets:
- Fig13_28.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $I= $
    suffix: $\rm\ A$
myst:
  substitutions:
    params_vars_title: Single-Turn Rectangular Coil
    params_R: '1'
    params_B: '0.25'
    params_f: '200'
    params_t: '0.005'
---
# {{ params_vars_title }}

## Question Text

The figure below shows a single-turn rectangular coil that has a resistance of ${{params_R }}\rm \ \Omega$. The magnetic field at all points inside the coil varies according to $B=B_0e^{-{\alpha}t}$, where $B_0$ = ${{params_B }}\textrm{ T}$ and $\alpha$ = ${{params_f }}\textrm{ Hz}$. What is the current induced in the coil at ${{params_t }}\textrm{ s}$?

<img src="Fig13_28.png">

### Answer Section

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$I=$ {{ correct_answers.part1_ans_str }} $\rm\ A$

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)