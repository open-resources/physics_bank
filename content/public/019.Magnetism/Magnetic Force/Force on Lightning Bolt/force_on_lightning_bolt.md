---
title: Force on Lightning Bolt
topic: Magnetism
author: Vanshika Sharma
source: 2.11.36
template_version: 1.1
attribution: openstax-physics-vol2
outcomes:
- undefined
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
- VS
- OSUP
- chapter 11
- problem 36
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $F=$
    allow-blank: false
    show-help-text: true
    suffix: $\rm\ N/m$
    weight: 1
    custom-format: .3g
part2:
  type: dropdown
  pl-customizations:
    blank: true
    weight: 1
substitutions:
  params:
    vars:
      title: Force on Lightning Bolt
    I: 19344
    part2:
      ans1:
        value: North
      ans2:
        value: South
      ans3:
        value: East
      ans4:
        value: West
---
# {{ params.vars.title }}

## Part 1

What is the force per meter on a lightning bolt at the equator that carries ${{params.I}}\textrm{ A}$ perpendicular to the $3 \times 10^{-5}\textrm{ T}$ magnetic field of the Earth?

### Answer Section

Please enter a numeric value.

## Part 2

What is the direction of the force if the current is straight up and the Earth's field direction is due north, parallel to the ground?

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)