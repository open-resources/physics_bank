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
substitutions:
  params:
    vars:
      title: Single-turn Circular Loop
    r: '70'
    b: '150'
    B: '400'
    t: '0.3'
    part2:
      ans1:
        value: Clockwise
      ans2:
        value: Counterclockwise
---
# {{ params.vars.title }}
A single-turn circular loop of wire of radius {{params.r }} $\textrm{ mm}$ lies in a plane perpendicular to a spatially uniform magnetic field. During a {{params.t }} $\textrm{ s}$ time interval, the magnitude of the field increases uniformly from {{params.b }} $\textrm{ mT}$ to {{params.B }} $\textrm{ mT}$.

## Part 1

Determine the emf induced in the loop.

### Answer Section

Please enter a numeric value.

## Part 2

If the magnetic field is directed out of the screen, what is the direction of the current induced in the loop?

### Answer Section

- {{ params.part2.ans1.value }}
- {{ params.part2.ans2.value }}

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}
{{ feedback.part1_ans }}

### pl-answer-panel

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)