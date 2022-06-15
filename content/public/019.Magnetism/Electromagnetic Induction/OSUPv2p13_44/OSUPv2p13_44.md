---
title: Moving Rod
topic: Magnetism
author: Ava Cornell
source: 2.13.44
template_version: 1.1
attribution: openstax-physics-vol2
outcomes:
- 19.8.6.0
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
- problem 44
- electromagnetic induction
- multi-part
- numeric
- AC
assets:
- Fig13_44.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    label: $I= $
    suffix: $\rm\ A$
    show-help-text: true
part2:
  type: dropdown
  pl-customizations:
    weight: 1
    blank: true
substitutions:
  params:
    vars:
      title: Moving Rod
    r: '4'
    v: '2'
    B: '1.75'
    a: '10'
    part2:
      ans1:
        value: Clockwise
      ans2:
        value: Counterclockwise
---
# {{ params.vars.title }}
In the accompanying figure, the rails, connecting end piece, and rod all have a resistance per unit length of ${{params.r }}$ $\rm\ \Omega$$/$$\textrm{cm}$. The rod moves to the left at a $v=$ ${{params.v }} \textrm{ m/s}$.

<img src="Fig13_44.png">

## Part 1

If $B=$ ${{params.B }} \textrm{ T}$ everywhere in the region, what is the magnitude of the induced current in the circuit when $a=$ ${{params.a }} \textrm{ cm}$?

### Answer Section

Please enter a numeric value.

## Part 2

Does the induced current circulate clockwise or counterclockwise?

### Answer Section

- {{ params.part2.ans1.value }}
- {{ params.part2.ans2.value }}

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}
{{ feedback.part1_ans }}

### pl-answer-panel

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)