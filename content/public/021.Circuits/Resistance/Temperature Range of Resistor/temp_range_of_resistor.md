---
title: Temperature Range of Resistor
topic: Circuits
author: Vanshika Sharma
source: 2.9.44
template_version: 1.1
attribution: openstax-physics-vol2
outcomes:
- 21.3.1.0
- 21.3.3.0
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
- problem 44
- resistance
- temperature
- VS
assets: null
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: false
    show-correct-answer: true
    label: $\Delta T = \pm $
    suffix: $^{\circ}\textrm{C}$
    comparison: relabs
    rtol: 0.03
    atol: 0
substitutions:
  params:
    vars:
      title: Temperature Range of Resistor
    p: 8
    metal: Platinum
    T_0: 54
---
# {{ params.vars.title }}

## Part 1

A resistor made of {{params.metal}} wire is used in an application where its resistance cannot change more than {{params.p}} percent from its value at {{params.T_0}}$^{\circ}\textrm{C}$.
Over what temperature range can it be used?

### Answer Section

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)