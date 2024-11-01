---
title: Power and Energy Through Resistor
topic: Circuits
author: Vanshika
source: 2.9.55
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 21.8.1.1
- 21.8.1.0
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
- Chapter 9
- Problem 55
- Vanshika Sharma
- multi-part
- resistor
- power
- energy
- current
- VS
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $I=$
    allow-blank: false
    show-help-text: true
    suffix: $\rm\ {mA}$
    weight: 1
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $P=$
    allow-blank: false
    show-help-text: true
    suffix: $\rm\ W$
    weight: 1
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $P=$
    allow-blank: false
    show-help-text: true
    suffix: $\rm\ W$
    weight: 1
part4:
  type: dropdown
  pl-customizations:
    blank: true
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Power And Energy Through Resistor
      V: 23
      R: 5
      part4:
        ans1:
          value: It is converted into light energy.
        ans2:
          value: It is converted into heat.
        ans3:
          value: It is converted into chemical energy.
---
# {{ params.vars.title }}
A {{params.V}} $\textrm{ V}$ battery is used to supply current to a {{params.R} $\rm\ k\Omega$ resistor.
Assume the voltage drop across any wires used for connections is negligible.

## Part 1

What is the current through the resistor?

### Answer Section

Please enter a numeric value.

## Part 2

What is the power dissipated by the resistor?

### Answer Section

Please enter a numeric value.

## Part 3

What is the power input from the battery, assuming all the electrical power is dissipated by the resistor?

### Answer Section

Please enter a numeric value.

## Part 4

What happens to the energy dissipated by the resistor?

### Answer Section

- {{ params.part4.ans1.value }}
- {{ params.part4.ans2.value }}
- {{ params.part4.ans3.value }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)