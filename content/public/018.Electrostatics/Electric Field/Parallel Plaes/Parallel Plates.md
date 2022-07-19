---
title: Parallel Plates
topic: Electrostatics
author: Jake Bobowski
source: 2.6.67
template_version: 1.0
attribution: openstax-physics-vol2
showCorrectAnswer: false
outcomes:
- 18.9.1.2
- 18.9.1.5
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- OSUP
- volume 2
- chapter 6
- problem 67
- electric field
- parallel plates
- Gauss's law
- numeric
- JB
assets: null
part1:
  type: number-input
  pl-customizations:
    label: $E=$
    allow-blank: false
    show-correct-answer: true
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ N/C$
    weight: 1
    custom-format: .3g
part2:
  type: dropdown
  pl-customizations:
    blank: true
    weight: 1
substitutions:
  params:
    L: '15'
    q: '3.8'
    p: '-9'
    d: '0.9'
    part2:
      ans1:
        value: points towards the negative plate
      ans2:
        value: points towards the positive plate
      ans3:
        value: points parallel to the plates
---
# {{ params.vars.title }}
Two parallel conducting plates ${{params.L}} \textrm{ cm}$ on a side are given equal and opposite charges of magnitude ${{params.q}}\times 10^{ {{params.p}} } \textrm{ C}$.

The plates are ${{params.d}}\rm\ mm$ apart.

## Part 1

What is the magnitude of the electric field at the centre of the region between the plates?

### Answer Section

## Part 2

What is the direction of the electric field at the centre of the region between the plates?

### Answer Section

- {{ params.part2.ans1.value }}
- {{ params.part2.ans2.value }}
- {{ params.part2.ans3.value }}

### pl-submission-panel

{{ feedback.part1_ans }}

### pl-answer-panel

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)