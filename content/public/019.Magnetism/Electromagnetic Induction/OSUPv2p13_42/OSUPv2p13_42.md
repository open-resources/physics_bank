---
title: Potential Difference of Rod
topic: Magnetism
author: Ava Cornell
source: 2.13.42
template_version: 1.1
attribution: openstax-physics-vol2
showCorrectAnswer: false
outcomes:
- 19.8.4.0
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
- problem 42
- electromagnetic induction
- multi-part
- numeric
- AC
assets:
- Fig13_42.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    label: ${\Delta}V= $
    suffix: $\rm\ V$
    show-help-text: true
part2:
  type: dropdown
  pl-customizations:
    weight: 1
    blank: true
myst:
  substitutions:
    params_vars_title: Potential Difference of Rod
    params_B: '1.00'
    params_v: '11'
    params_part2_ans1_value: Bottom
    params_part2_ans2_value: Top
---
# {{ params_vars_title }}
The rod shown in the accompanying figure is moving through a uniform magnetic field of strength ${{params_B }} \textrm{ T}$ with a constant velocity of magnitude ${{params_v }} \textrm{ m/s}$.

<img src="Fig13_42.png">

## Part 1

What is the potential difference between the ends of the rod?

### Answer Section

Please enter a numeric value.

## Part 2

Which end of the rod is at a higher potential?

### Answer Section

- {{ params_part2_ans1_value }}
- {{ params_part2_ans2_value }}

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}
{{ feedback.part1_ans }}

### pl-answer-panel

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)