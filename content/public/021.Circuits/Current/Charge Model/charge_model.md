---
title: Charge Model
topic: Current
author: Vanshika Sharma
source: 2.9.25
template_version: 1.1
attribution: openstax-physics-vol2
outcomes:
- 21.2.1.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- OSUP
- volume 2
- chapter 9
- problem 25
- derivative
- model
- charge
- current
- VS
assets: null
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: false
    label: $I= $
    suffix: $\rm\ A$
    comparison: relabs
    rtol: 0.03
    atol: 0
substitutions:
  params:
    vars:
      title: Charge Model
      units: A
    c1: 31
    c2: 31
    c3: 50
    t: 27
---
# {{ params.vars.title }}
The quantity of charge through a conductor is modeled as $ \textrm{Q}=$ {{params.c1}}$\rm{t^4}$ $\rm{mC \over s^4}$ - {{params.c2}}$\rm{t}$ $\rm{mC \over s}$ + {{params.c1}} $\rm{mC}$.
What is the current at time $\textrm{t} =$ {{params.t}} $\textrm{s}$?

## Question Text

### Answer Section

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)