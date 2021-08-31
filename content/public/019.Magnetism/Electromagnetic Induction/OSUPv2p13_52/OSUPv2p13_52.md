---
title: Uniformly Decreasing Magnetic Field
topic: Magnetism
author: Ava Cornell
source: 2.13.52
template_version: 1.1
attribution: openstax-physics-vol2
outcomes:
- 19.8.6.0
- 19.8.6.1
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
    weight: 1
    allow-blank: false
    label: $E= $
    suffix: $\rm\ {N/C}$
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
      title: Uniformly Decreasing Magnetic Field
    r: '5'
    B: '1.5'
    t: '30'
    part2:
      ans1:
        value: Clockwise
      ans2:
        value: Counterclockwise
---
# {{ params.vars.title }}
The magnetic field at all points within the cylindrical region whose cross-section is indicated in the accompanying figure starts at magnetic field of ${{params.B }} \textrm{ T}$ and decreases uniformly to zero in ${{params.t }} \textrm{ s}$.

<img src="Fig13_52.png">

## Part 1

What is the magnitude of the electric field when $r$, the distance from the geometric center of the region, is ${{params.r }} \textrm{ cm}$?

### Answer Section

Please enter a numeric value.

## Part 2

What is the direction of this electric field?

### Answer Section

- {{ params.part2.ans1.value }}
- {{ params.part2.ans2.value }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)