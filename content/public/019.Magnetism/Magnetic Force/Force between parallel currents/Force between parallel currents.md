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
substitutions:
  params:
    vars:
      title: Force between parallel currents
    d: '46.0'
    I: '76.0'
    txt: opposite directions
    part2:
      ans1:
        value: Attract
      ans2:
        value: Repel
---
# {{ params.vars.title }}
Two long, straight wires are parallel and ${{ params.d }}\rm\ cm$ apart.

## Part 1

If each wire carries a current of ${{ params.I }}\rm\ A$ in {{ params.txt }}, what is the magnetic force per meter exerted on each wire?

### Answer Section

## Part 2

Do the wire attract or repel eachother?

### Answer Section

- {{ params.part2.ans1.value }}
- {{ params.part2.ans2.value }}

### pl-submission-panel

{{ feedback.part1_ans }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)