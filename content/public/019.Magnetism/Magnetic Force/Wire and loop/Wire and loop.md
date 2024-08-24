---
title: Wire and loop
topic: Magnetism
author: Jake Bobowksi
source: 2.12.34
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 19.3.3.0
- 19.3.3.1
- 19.3.3.4
- 19.3.4.0
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
- problem 34
- magnetic field
- current source
- parallel wires
- symbolic
- JB
assets:
- OSUPv2p12_34.png
part1:
  type: symbolic-input
  pl-customizations:
    label: $F = $
    variables: a, b, I1, I2, μ0
    weight: 1
    allow-blank: false
part2:
  type: dropdown
  pl-customizations:
    blank: true
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Wire and loop
      part2:
        ans1:
          value: to the left
        ans2:
          value: to the right
        ans3:
          value: towards to the top of the screen
        ans4:
          value: towards to the bottom of the screen
---
# {{ params.vars.title }}
The inifinite, straight wire shown in the figure carries a current $I_1$.
The rectangular loop, whose long sides are parallel to the wire, carries a current $I_2$.

<img src="OSUPv2p12_34.png" width=350 alt="An infinite wire with current I1 next to a rectangular loop of wire with current I2.">

## Part 1

Find an expression for the magnitude of the force on the rectangular loop due to the magnetic field of the wire.

You may copy and paste the Greek character μ0 into you symbolic expression.
Use `pi` to represent π.

### Answer Section

## Part 2

What is the direction of the net force on the rectangular loop due to the magnetic field of the wire?

### Answer Section

- {{ params.part2.ans1.value }}
- {{ params.part2.ans2.value }}
- {{ params.part2.ans3.value }}
- {{ params.part2.ans4.value }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)