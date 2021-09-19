---
title: Potential Difference of Rod
topic: Magnetism
author: Ava Cornell
source: 2.13.42
template_version: 1.1
attribution: openstax-physics-vol2
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
    weight: 1
    allow-blank: false
    label: ${\Delta}V= $
    suffix: $\rm\ V$
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
part2:
  type: dropdown
  pl-customizations:
    weight: 1
    blank: true
substitutions:
  params:
    vars:
      title: Potential Difference of Rod
    B: '1.00'
    v: '11'
    part2:
      ans1:
        value: Bottom
      ans2:
        value: Top
---
# {{ params.vars.title }}
The rod shown in the accompanying figure is moving through a uniform magnetic field of strength ${{params.B }} \textrm{ T}$ with a constant velocity of magnitude ${{params.v }} \textrm{ m/s}$.

<img src="Fig13_42.png">

## Part 1

What is the potential difference between the ends of the rod?

### Answer Section

Please enter a numeric value.

## Part 2

Which end of the rod is at a higher potential?

### Answer Section

- {{ params.part2.ans1.value }}
- {{ params.part2.ans2.value }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)