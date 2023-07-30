---
title: Field due to parallel currents
topic: Magnetism
author: Jake Bobowski
source: 2.12.26
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 19.2.4.1
- 19.2.4.5
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
- chapter 12
- problem 26
- magnetic fields
- parallel currents
- numeric
- JB
assets:
- OSUPv2p12_26.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $B=$
    allow-blank: false
    show-correct-answer: true
    show-help-text: true
    suffix: $\rm\ T$
    weight: 1
    custom-format: .3g
part2:
  type: dropdown
  pl-customizations:
    weight: 1
    blank: true
    sort: fixed
myst:
  substitutions:
    params_vars_title: Field due to parallel currents
    params_I1: '12.5'
    params_I2: '17.5'
    params_r1: '12.0'
    params_r2: '8.0'
    params_part2_ans1_value: Out of the screen.
    params_part2_ans2_value: Into the screen.
    params_part2_ans3_value: Towards the top of the screen.
    params_part2_ans4_value: Towards the bottom of the screen.
    params_part2_ans5_value: To the right.
    params_part2_ans6_value: To the left.
    params_part2_ans7_value: The magnetic field is zero.
---
# {{ params_vars_title }}
The two long, parallel wires shown in the figure carry currents in the same direction (towards the bottom of the screen).
Note that the figure is not drawn to scale.

<img src="OSUPv2p12_26.png" width=400 alt="Parallel currents.">

## Part 1

If $I_1 = {{params_I1}}\rm\ A$, $r_1 = {{params_r1}}\rm\ cm$, $I_2 = {{params_I2}}\rm\ A$, and $r_2 = {{params_r2}}\rm\ cm$, what is the magnitude of the magnetic field at point P?

### Answer Section

## Part 2

What is the direction of the magnetic field at point P?

### Answer Section

- {{ params_part2_ans1_value }}
- {{ params_part2_ans2_value }}
- {{ params_part2_ans3_value }}
- {{ params_part2_ans4_value }}
- {{ params_part2_ans5_value }}
- {{ params_part2_ans6_value }}
- {{ params_part2_ans7_value }}

### pl-submission-panel

{{ feedback.part1_ans }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)