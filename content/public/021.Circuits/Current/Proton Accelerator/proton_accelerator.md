---
title: Proton Accelerator
topic: Current
author: Vanshika Sharma
source: 2.9.30
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
outcomes:
- undefined
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
    rtol: 0.05
    label: $J=$
    allow-blank: false
    show-help-text: true
    suffix: $\rm\ A/m^2$
    weight: 1
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $\rm {v_{d}} = $
    allow-blank: false
    show-correct-answer: false
    show-help-text: true
    suffix: $\rm\ m/s$
    weight: 1
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $t=$
    allow-blank: false
    show-correct-answer: false
    show-help-text: true
    suffix: $\rm\ s$
    weight: 1
substitutions:
  params:
    vars:
      title: Proton Accelerator
    r: 0.7
    I: 34
    n: 2.58
    p: 24
---
# {{ params.vars.title }}
A high-energy proton accelerator produces a proton beam with a radius of {{params.r}} $\textrm{mm}$.
The beam current is {{params.I}} $\rm\mu \rm{A}$ and is constant.
The charge density of the beam is $n = $ {{params.n}} $ \times 10^{11}$ protons per cubic meter.

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