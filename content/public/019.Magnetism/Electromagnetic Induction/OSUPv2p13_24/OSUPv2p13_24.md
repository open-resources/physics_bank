---
title: Coil in Uniform Magnetic Field
topic: Magnetism
author: Ava Cornell
source: 2.13.24
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
outcomes:
- 19.8.1.0
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
- problem 24
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
      title: Coil in Uniform Magnetic Field
    N: '50'
    d: '10'
    B: '0.50'
    t: '0.2'
---
# {{ params.vars.title }}

## Question Text

A {{params.N }} turn coil has a diameter of {{params.d }} $\textrm{ cm}$. The coil is placed in a spatially uniform magnetic field of magnitude {{params.B }} $\textrm{ T}$ so that the face of the coil and the magnetic field are perpendicular. Find the magnitude of the emf induced in the coil if the magnetic field is reduced to zero uniformly in {{params.t }} $\textrm{ s}$.

### Answer Section

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$\varepsilon=$ {{ correct_answers.part1_ans_str }} $\rm\ V$

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)