---
title: Charged particle near the Earth
topic: Electrostatics
author: Jake Bobowski
source: 2.7.69
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 18.6.1.3
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
    rtol: 0.05
    label: $E=$
    allow-blank: false
    show-correct-answer: true
    show-help-text: true
    suffix: $\rm\ N/C$
    weight: 1
    custom-format: .3g
part2:
  type: dropdown
  pl-customizations:
    blank: true
    weight: 1
myst:
  substitutions:
    params_vars_title: Charged particle near the Earth
    params_charge: proton
    params_part2_ans1_value: Away from the surface of the Earth.
    params_part2_ans2_value: Towards the surface of the Earth.
---
# {{ params_vars_title }}

## Part 1

What is the magnitude of the electric field that supports the weight of a free {{ params_charge }} near the surface of the Earth?

### Answer Section

Please enter a numeric value.

## Part 2

What is the direction of the electric field?

### Answer Section

- {{ params_part2_ans1_value }}
- {{ params_part2_ans2_value }}

### pl-submission-panel

{{ feedback.part1_ans }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)