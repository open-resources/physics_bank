---
title: Parallel-plate potential difference
topic: Electrostatics
author: Jake Bobowksi
source: 2.7.63
template_version: 1.0
attribution: openstax-physics-vol2
showCorrectAnswer: false
outcomes:
- 18.11.2.4
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
- problem 63
- potential difference
- parallel plates
- numeric
- JB
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    show-correct-answer: true
    label: $\Delta V= $
    suffix: $\rm\ V$
    custom-format: .3g
substitutions:
  params:
    vars:
      title: Parallel-plate potential difference
    d: '18.0'
    t: '1.0'
    q: '5.2'
    p: -10
---
# {{ params.vars.title }}
Two parallel plates ${{ params.d }}\rm\ cm$ on a side are given equal and opposite charges of magnitude ${{ params.q }}\times 10^{ {{ params.p }} }\rm\ C$.
The plates are ${{ params.t }}\rm\ mm$ apart.

## Question Text

What is the potential difference between the plates?

### Answer Section

### pl-submission-panel

{{ feedback.part1_ans }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)