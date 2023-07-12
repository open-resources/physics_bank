---
title: Uniformly Decreasing Magnetic Field
topic: Magnetism
author: Ava Cornell
source: 2.13.52
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 19.8.6.0
- 19.8.6.1
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
- chapter 13
- problem 52
- electromagnetic induction
- multi-part
- numeric
- AC
assets:
- Fig13_52.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    label: $E= $
    suffix: $\rm\ {N/C}$
    show-help-text: true
part2:
  type: dropdown
  pl-customizations:
    weight: 1
    blank: true
myst:
  substitutions:
    params_vars_title: Uniformly Decreasing Magnetic Field
    params_r: '10'
    params_B: '0.5'
    params_t: '30'
    params_part2_ans1_value: Clockwise
    params_part2_ans2_value: Counterclockwise
---
# {{ params_vars_title }}
The magnetic field at all points within the cylindrical region whose cross-section is indicated in the accompanying figure starts at magnetic field of {{params_B }} $\textrm{ T}$ and decreases uniformly to zero in {{params_t }}  $\textrm{ s}$.

<img src="Fig13_52.png">

## Part 1

What is the magnitude of the electric field when $r$, the distance from the geometric center of the region, is ${{params_r }} \textrm{ cm}$?

### Answer Section

Please enter a numeric value.

## Part 2

What is the direction of this electric field?

### Answer Section

- {{ params_part2_ans1_value }}
- {{ params_part2_ans2_value }}

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}
{{ feedback.part1_ans }}

### pl-answer-panel

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)