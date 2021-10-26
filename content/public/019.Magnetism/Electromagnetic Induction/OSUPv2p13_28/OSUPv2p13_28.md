---
title: Single-Turn Rectangular Coil
topic: Magnetism
author: Ava Cornell
source: 2.13.28
template_version: 1.0
attribution: openstax-physics-vol2
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
substitutions:
  params:
    vars:
      title: Single-Turn Rectangular Coil
    R: '3'
    B: '0.50'
    f: '100'
    t: '0.003'
---
# {{ params.vars.title }}

## Question Text

The figure below shows a single-turn rectangular coil that has a resistance of ${{params.R }}\rm \ \Omega$. The magnetic field at all points inside the coil varies according to $B=B_0e^{-{\alpha}t}$, where $B_0$ = ${{params.B }}\textrm{ T}$ and $\alpha$ = ${{params.f }}\textrm{ Hz}$. What is the current induced in the coil at ${{params.t }}\textrm{ s}$?

<img src="Fig13_28.png">

### Answer Section

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)