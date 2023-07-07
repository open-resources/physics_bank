---
title: Force between current-carrying wires
topic: Magnetism
author: Jake Bobowski
source: 2.12.31
template_version: 1.1
attribution: openstax-physics-vol2
showCorrectAnswer: false
outcomes:
- 19.3.3.2
- 19.3.3.4
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- OSUP
- volume 2
- chapter 12
- problem 31
- magnetic fields
- parallel currents
- force
- numeric
- JB
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $F/\ell=$
    allow-blank: false
    show-correct-answer: true
    show-help-text: true
    suffix: $\rm\ N/m$
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
    params_vars_title: Force between current-carrying wires
    params_d: '14.0'
    params_I1: '1.4'
    params_I2: '7.8'
    params_txt: the same direction
    params_part2_ans1_value: Attract
    params_part2_ans2_value: Repel
---
# {{ params_vars_title }}
Two long, straight wires are parallel and ${{ params_d }}\rm\ cm$ apart.
One carries a current of ${{ params_I1 }}\rm\ A$, the other a current of ${{ params_I2 }}\rm\ A$.

## Part 1

If the two currents flow in {{ params_txt }}, what is the magnitude of the force per unit length of one wire on the other?

### Answer Section

## Part 2

Do the wires attract or repel eachother?

### Answer Section

- {{ params_part2_ans1_value }}
- {{ params_part2_ans2_value }}

### pl-submission-panel

{{ feedback.part1_ans }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)