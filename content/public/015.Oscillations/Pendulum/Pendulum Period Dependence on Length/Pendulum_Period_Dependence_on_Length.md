---
title: Pendulum Period Dependence on Length
topic: Oscillations
author: Jake Bobowski
source: OPUS V1 Problem 15.50
template_version: 1.4
attribution: openstax-physics-vol1
partialCredit: true
singleVariant: true
showCorrectAnswer: false
outcomes:
- 15.4.1.1
difficulty:
- easy
randomization:
- undefined
taxonomy:
- undefined
span:
- undefined
length:
- short
tags:
- JR
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\frac{T_f}{T_i} = $
    suffix: null
    comparison: relabs
substitutions:
  params:
    vars:
      title: Pendulum Period Dependence on Length
    inc: 2
    dec: 80.0
    part1:
      ans1:
        value: It increases by a factor of $\sqrt($2$)$.
      ans2:
        value: It increases by a factor of 2.
      ans3:
        value: It increases by a factor of 2$^2$.
      ans4:
        value: It decreases by a factor of $\sqrt($2$)$.
      ans5:
        value: It decreases by a factor of 2.
      ans6:
        value: It decreases by a factor of 2$^2$.
      ans7:
        value: It does not change.
---
# {{ params.vars.title }}

## Part 1

What is the effect on the period of a pendulum if you increase its length by a factor of {{ params.inc }}?

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}
- {{ params.part1.ans5.value }}
- {{ params.part1.ans6.value }}
- {{ params.part1.ans7.value }}

## Part 2

By what factor does the period of a pendulum change if you decrease its length to {{ params.dec }} % of its original length?

### Answer Section

Please enter a numeric answer.

## Attribution

Problem is from the [OpenStax University Physics Volume 1](https://openstax.org/details/books/university-physics-volume-1) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)