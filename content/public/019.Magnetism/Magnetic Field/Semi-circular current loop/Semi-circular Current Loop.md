---
title: Semi-circular Current Loop
topic: Magnetism
author: Jake Bobowksi
source: 2.12.18
template_version: 1.1
attribution: openstax-physics-vol2
outcomes:
- 19.2.1.0
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
- problem 18
- magnetic field
- current source
- Biot-Savart law
- symbolic
- JB
assets:
- OSUPv2p12_18.png
part1:
  type: symbolic-input
  pl-customizations:
    label: $B = $
    variables: a, b, I, μ0
    weight: 1
    allow-blank: false
part2:
  type: dropdown
  pl-customizations:
    weight: 1
    blank: true
substitutions:
  params:
    vars:
      title: Semi-circular Current Loop
    part2:
      ans1:
        value: points out of the screen
      ans2:
        value: points into the screen
      ans3:
        value: points parallel to the screen
---
# {{ params.vars.title }}
What is the magnetic field at point P due to the current $I$ in the loop of wire shown?

<img src="OSUPv2p12_18.png" width=300 alt="Semi-circular loop of current">

## Part 1

You may copy the Greek symbol Î¼0 into your symbolic expression.

Magnitude:

### Answer Section

## Part 2

Direction:

### Answer Section

- {{ params.part2.ans1.value }}
- {{ params.part2.ans2.value }}
- {{ params.part2.ans3.value }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)