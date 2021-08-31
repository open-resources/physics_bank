---
title: Electrical Appliances Plugged into an Outlet
topic: Circuits
author: Joseph Wandinger
source: 2.10.28
template_version: 1.1
attribution: openstax-physics-vol2
outcomes:
- 21.1.1.6
- 21.12.1.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- OSUP
- volume 2
- chapter 10
- problem 28
- circuits
- current
- fuses
- JW
assets: null
part1:
  type: number-input
  pl-customizations:
    label: $P=$
    allow-blank: false
    show-correct-answer: true
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ W$
    custom-format: .3g
    weight: 1
part2:
  type: number-input
  pl-customizations:
    label: $P=$
    allow-blank: false
    show-correct-answer: true
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ W$
    custom-format: .3g
    weight: 1
part3:
  type: number-input
  pl-customizations:
    label: $P=$
    allow-blank: false
    show-correct-answer: true
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ W$
    custom-format: .3g
    weight: 1
part4:
  type: dropdown
  pl-customizations:
    blank: true
    weight: 1
substitutions:
  params:
    P_T: '1890'
    P_S: '1360'
    P_L: '85.0'
    I_F: '27.0'
    V: '125.0'
    prep: an
    part4:
      ans1:
        value: 'Yes'
      ans2:
        value: 'No'
---
# {{ params.vars.title }}
A ${{ params.P_T }}\rm\ W$ toaster, a ${{ params.P_S }}\rm\ W$ speaker, and {{ params.prep }} ${{ params.P_L }}\rm\ W$ lamp are plugged into the same outlet in a ${{ params.I_F }}\rm\ A$ fuse and ${{ params.V }}\rm\ V$ circuit.
(The three devices are in parallel when plugged into the same socket.)

## Part 1

What is the current drawn by the toaster?

### Answer Section

Please enter a numeric value.

## Part 2

What is the current drawn by the speaker?

### Answer Section

Please enter a numeric value.

## Part 3

What is the current drawn by the lamp?

### Answer Section

Please enter a numeric value.

## Part 4

Will this combination blow the ${{ params.I_F }}\rm\ A$ fuse?

### Answer Section

- {{ params.part4.ans1.value }}
- {{ params.part4.ans2.value }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)