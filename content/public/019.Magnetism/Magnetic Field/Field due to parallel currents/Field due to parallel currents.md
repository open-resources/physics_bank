---
title: Field due to parallel currents
topic: Magnetism
author: Jake Bobowski
source: 2.12.26
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
outcomes:
- 19.2.4.1
- 19.2.4.5
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
- chapter 12
- problem 26
- magnetic fields
- parallel currents
- numeric
- JB
assets:
- OSUPv2p12_26.png
part1:
  type: number-input
  pl-customizations:
    label: $B=$
    allow-blank: false
    show-correct-answer: true
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ T$
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
      title: Field due to parallel currents
    I1: '17.5'
    I2: '22.5'
    r1: '8.0'
    r2: '12.0'
    part2:
      ans1:
        value: Out of the screen.
      ans2:
        value: Into the screen.
      ans3:
        value: Towards the top of the screen.
      ans4:
        value: Towards the bottom of the screen.
      ans5:
        value: To the right.
      ans6:
        value: To the left.
      ans7:
        value: The magnetic field is zero.
---
# {{ params.vars.title }}
The two long, parallel wires shown in the figure carry currents in the same direction (towards the bottom of the screen).
Note that the figure is not drawn to scale.

<img src="OSUPv2p12_26.png" width=400 alt="Parallel currents.">

## Part 1

If $I_1 = {{params.I1}}\rm\ A$, $r_1 = {{params.r1}}\rm\ cm$, $I_2 = {{params.I2}}\rm\ A$, and $r_2 = {{params.r2}}\rm\ cm$, what is the magnitude of the magnetic field at point P?

### Answer Section

## Part 2

What is the direction of the magnetic field at point P?

### Answer Section

- {{ params.part2.ans1.value }}
- {{ params.part2.ans2.value }}
- {{ params.part2.ans3.value }}
- {{ params.part2.ans4.value }}
- {{ params.part2.ans5.value }}
- {{ params.part2.ans6.value }}
- {{ params.part2.ans7.value }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)