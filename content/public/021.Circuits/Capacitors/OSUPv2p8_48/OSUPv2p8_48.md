---
title: Varying Separation Distance of Capacitor Plates
topic: Circuits
author: Ava Cornell
source: 2.8.48
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
outcomes:
- 21.7.1.0
- 21.7.5.0
- 21.7.5.1
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
- chapter 8
- problem 48
- capacitors
- multi-part
- AC
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $U_\textrm{i}=$
    allow-blank: false
    show-help-text: true
    suffix: $\rm\ \mu\textrm{J}$
    weight: 1
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $U_\textrm{f}=$
    allow-blank: false
    show-help-text: true
    suffix: $\rm\ \mu\textrm{J}$
    weight: 1
part3:
  type: dropdown
  pl-customizations:
    weight: 1
    blank: true
substitutions:
  params:
    vars:
      title: Varying Separation Distance of Capacitor Plates
    a: '20.0'
    b: '1.25'
    c: '2.00'
    v: '30'
    part3:
      ans1:
        value: It is lost to the surroundings in the laboratory
      ans2:
        value: Charge is transferred to the battery
      ans3:
        value: It is transferred into heat energy
---
# {{ params.vars.title }}
A parallel-plate capacitor is made of two square plates with side length {{params.a }} $\textrm{ cm}$ that are {{params.b }} $\textrm{ mm}$ apart. The capacitor is connected to a {{params.v }} $\textrm{ V}$ battery. With the battery still connected, the plates are pulled apart to a separation distance of {{params.c }} $\textrm{ mm}$.

## Part 1

What is the energy stored in the capacitor before the plates are pulled apart?

### Answer Section

Please enter a numeric value.

## Part 2

What is the energy stored in the capacitor after the plates are pulled apart?

### Answer Section

Please enter a numeric value.

## Part 3

Which best describes why the energy decreases even though work is done separating the plates?

### Answer Section

- {{ params.part3.ans1.value }}
- {{ params.part3.ans2.value }}
- {{ params.part3.ans3.value }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)