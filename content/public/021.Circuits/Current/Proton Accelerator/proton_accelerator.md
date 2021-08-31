---
title: Proton Accelerator
topic: Current
author: Vanshika Sharma
source: 2.9.30
template_version: 1.1
attribution: openstax-physics-vol2
outcomes:
- undefined
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- OSUP
- chapter 9
- problem 30
- current density
- drift velocity
- accelerator
- VS
assets: null
part1:
  type: number-input
  pl-customizations:
    label: $J=$
    allow-blank: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ A/m^2$
    weight: 1
part2:
  type: number-input
  pl-customizations:
    label: $\rm {v_{d}} = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ m/s$
    weight: 1
part3:
  type: number-input
  pl-customizations:
    label: $t=$
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ s$
    weight: 1
substitutions:
  params:
    vars:
      title: Proton Accelerator
    r: 0.76
    I: 44
    n: 3.58
    p: 27
---
# {{ params.vars.title }}
A high-energy proton accelerator produces a proton beam with a radius of {{params.r}} $\textrm{mm}$.
The beam current is {{params.I}} $\rm\mu \rm{A}$ and is constant.
The charge density of the beam is $n = {{params.n}} \times 10^{11}$ protons per cubic meter.

## Part 1

What is the current density of the beam?

### Answer Section

Please enter a numeric value.

## Part 2

What is the drift velocity of the beam?

### Answer Section

Please enter a numeric value.

## Part 3

How much time does it take for ${{params.p}} \times 10^{10}$ protons to be emitted by the accelerator?

### Answer Section

Please enter a numeric value.

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)