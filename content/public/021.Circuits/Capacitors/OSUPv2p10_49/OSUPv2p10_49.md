---
title: Automobile Intermittent Wiper System
topic: Circuits
author: Joseph Wandinger
source: 2.10.49
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 21.13.1.0
- 21.13.2.0
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
- chapter 10
- problem 49
- circuits
- Capacitors
- multi-part
- JW
part1:
  type: number-input
  pl-customizations:
    label: $R = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ \Omega$
    weight: 1
    custom-format: .3g
part2:
  type: number-input
  pl-customizations:
    label: $R = $
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ \Omega$
    weight: 1
    custom-format: .3g
myst:
  substitutions:
    params:
      vars:
        title: Automobile Intermittent Wiper System
      C: '0.400'
      t1: '2.50'
      t2: '15.5'
---
# {{ params.vars.title }}
The timing device in an automobile's intermittent wiper system is based on an $RC$ time constant and utilizes a ${{ params.C }}\rm\ \mu F$ capacitor and a variable resistor.
Over what range must $R$ be made to vary to achieve time constants from ${{ params.t1 }}\rm\ s$ to ${{ params.t2 }}\rm\ s$?

## Part 1

What must be the value of $R$ for the time constant to be ${{ params.t1 }}\rm\ s$?

### Answer Section

Please enter in a numeric value in $\rm\ \Omega$.

## Part 2

What must be the value of $R$ for the time constant to be ${{ params.t2 }}\rm\ s$?

### Answer Section

Please enter in a numeric value in $\rm\ \Omega$.

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)