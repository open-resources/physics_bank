---
title: Charged particle near the Earth
topic: Electrostatics
author: Jake Bobowski
source: 2.7.69
template_version: 1.1
attribution: openstax-physics-vol2
outcomes:
- 18.6.1.3
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- OSUP
- volume 2
- chapter 7
- problem 69
- charge
- gravity
- numeric
- JB
assets: null
part1:
  type: number-input
  pl-customizations:
    label: $E=$
    allow-blank: false
    show-correct-answer: true
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ N/C$
    weight: 1
    custom-format: .3g
part2:
  type: dropdown
  pl-customizations:
    blank: true
    weight: 1
substitutions:
  params:
    vars:
      title: Charged particle near the Earth
    charge: electron
    part2:
      ans1:
        value: Away from the surface of the Earth.
      ans2:
        value: Towards the surface of the Earth.
---
# {{ params.vars.title }}

## Part 1

What is the magnitude of the electric field that supports the weight of a free {{ params.charge }} near the surface of the Earth?

### Answer Section

Please enter a numeric value.

## Part 2

What is the direction of the electric field?

### Answer Section

- {{ params.part2.ans1.value }}
- {{ params.part2.ans2.value }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)