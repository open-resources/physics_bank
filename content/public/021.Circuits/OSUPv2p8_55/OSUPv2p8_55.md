---
title: Partially Filled Capacitor
topic: Circuits
author: Ava Cornell
source: 2.8.55
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 21.7.1.0
- 21.7.6.0
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
- chapter 8
- problem 55
- capacitors
- multi-part
- numeric
- AC
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $\kappa=$
    allow-blank: false
    show-help-text: true
    weight: 1
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $V=$
    allow-blank: false
    show-help-text: true
    suffix: $\textrm{V}$
    weight: 1
myst:
  substitutions:
    params_vars_title: Partially Filled Capacitor
    params_a: '50.0'
    params_b: '20.0'
    params_f: '6'
---
# {{ params_vars_title }}
A parallel-plate capacitor with only air between its plates is charged by connecting the capacitor to a battery. The capacitor is then disconnected from the battery, without any of the charge leaving the plates.

## Part 1

A voltmeter reads {{params_a }} $\textrm{ V}$ when placed across the capacitor. When a dielectric is inserted between the plates, completely filling the space, the voltmeter {{params_b }} $\textrm{ V}$. What is the dielectric constant of the material?

### Answer Section

Please enter a numeric value.

## Part 2

What will the voltmeter read if the dielectric is now pulled away out so it fills only $1/${{params_f }} of the space between the plates?

### Answer Section

Please enter a numeric value.

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}
{{ feedback.part1_ans }}

### pl-answer-panel

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)