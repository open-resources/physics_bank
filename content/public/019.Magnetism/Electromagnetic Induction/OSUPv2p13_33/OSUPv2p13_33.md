---
title: Single-turn Circular Loop
topic: Magnetism
author: Ava Cornell
source: 2.13.33
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 19.8.6.0
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
- problem 33
- electromagnetic induction
- multi-part
- numeric
- AC
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    label: $\varepsilon= $
    suffix: $\rm\ V$
    show-help-text: true
part2:
  type: dropdown
  pl-customizations:
    weight: 1
    blank: true
myst:
  substitutions:
    params_vars_title: Single-turn Circular Loop
    params_r: '70'
    params_b: '125'
    params_B: '400'
    params_t: '0.5'
    params_part2_ans1_value: Clockwise
    params_part2_ans2_value: Counterclockwise
---
# {{ params_vars_title }}
A single-turn circular loop of wire of radius {{params_r }} $\textrm{ mm}$ lies in a plane perpendicular to a spatially uniform magnetic field. During a {{params_t }} $\textrm{ s}$ time interval, the magnitude of the field increases uniformly from {{params_b }} $\textrm{ mT}$ to {{params_B }} $\textrm{ mT}$.

## Part 1

Determine the emf induced in the loop.

### Answer Section

Please enter a numeric value.

## Part 2

If the magnetic field is directed out of the screen, what is the direction of the current induced in the loop?

### Answer Section

- {{ params_part2_ans1_value }}
- {{ params_part2_ans2_value }}

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}
{{ feedback.part1_ans }}

### pl-answer-panel

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)