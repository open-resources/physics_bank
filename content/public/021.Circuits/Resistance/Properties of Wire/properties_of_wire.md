---
title: Properties of Wire
topic: Resistance
author: Vanshika Sharma
source: 2.9.47
template_version: 1.2
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
- OSUP
- VS
- chapter 9
- problem 47
- resistance
- wire
- material
part1:
  type: dropdown
  pl-customizations:
    blank: true
    weight: 1
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $R=$
    allow-blank: false
    show-help-text: true
    suffix: $\rm \Omega$
    custom-format: .3g
    weight: 1
substitutions:
  params:
    vars:
      title: Properties of Wire
    part1:
      ans1:
        value: Silver
      ans2:
        value: Gold
      ans3:
        value: Copper
      ans4:
        value: Aluminum
      ans5:
        value: Tungsten
---
# {{ params.vars.title }}
A wire is $25.0\rm\ m$ long with a diameter of $0.100\rm\ mm$. and has a resistance of $77.7 \rm\ \Omega$ at $20 ^\circ \textrm{C}$.

## Part 1

What material is the wire made of?

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}
- {{ params.part1.ans5.value }}

## Part 2

What is the resistance of the wire $150 ^\circ \textrm{C}$?

### Answer Section

Please enter a numeric value.

### pl-submission-panel

{{ submitted_answers.part2_ans_str }}
{{ feedback.part2_ans }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)