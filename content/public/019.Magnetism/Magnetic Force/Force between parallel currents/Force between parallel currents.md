---
title: Force between parallel currents
topic: Magnetism
author: Jake Bobowski
source: 2.12.30
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
- problem 30
- magnetic fields
- parallel currents
- force
- numeric
- JB
assets: null
part1:
  type: number-input
  pl-customizations:
    label: $F/\ell=$
    allow-blank: false
    show-correct-answer: true
    comparison: relabs
    rtol: 0.03
    atol: 0
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
    params_vars_title: Force between parallel currents
    params_d: '28.0'
    params_I: '74.0'
    params_txt: the same direction
    params_part2_ans1_value: Attract
    params_part2_ans2_value: Repel
---
# {{ params_vars_title }}
Two long, straight wires are parallel and ${{ params_d }}\rm\ cm$ apart.

## Part 1

If each wire carries a current of ${{ params_I }}\rm\ A$ in {{ params_txt }}, what is the magnetic force per meter exerted on each wire?

### Answer Section

## Part 2

Do the wire attract or repel eachother?

### Answer Section

- {{ params_part2_ans1_value }}
- {{ params_part2_ans2_value }}

### pl-submission-panel

{{ feedback.part1_ans }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)