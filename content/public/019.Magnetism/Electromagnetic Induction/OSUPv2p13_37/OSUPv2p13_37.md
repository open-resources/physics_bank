---
title: Radio Antenna
topic: Magnetism
author: Ava Cornell
source: 2.13.37
template_version: 1.1
attribution: openstax-physics-vol2
showCorrectAnswer: false
outcomes:
- 19.8.4.0
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
- problem 37
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
substitutions:
  params:
    vars:
      title: Radio Antenna
    l: '1.5'
    v: '50'
    B: '5.5'
---
# {{ params.vars.title }}

## Question Text

An automobile with a radio antenna ${{params.l }}\textrm{ m}$ long travels at ${{params.v }}\textrm{ km/hr}$ in a location where the Earth's horizontal magnetic field is ${{params.B }} \times 10^{-5} \textrm{ T}$. What is the maximum possible emf induced in the antenna due to this motion?

### Answer Section

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$\varepsilon=$ {{ correct_answers.part1_ans_str }} $\rm\ V$

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)