---
title: Circuit with Resistance
topic: Magnetism
author: Ava Cornell
source: 2.13.46
template_version: 1.1
attribution: openstax-physics-vol2
showCorrectAnswer: false
outcomes:
- 19.8.6.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- OSUP
- volume 2
- chapter 13
- problem 46
- electromagnetic induction
- multi-part
- numeric
- AC
assets:
- Fig13_46.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    label: $\varepsilon= $
    suffix: $\rm\ V$
    show-help-text: true
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    label: $I= $
    suffix: $\rm\ A$
    show-help-text: true
part3:
  type: dropdown
  pl-customizations:
    weight: 1
    blank: true
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    label: $F= $
    suffix: $\rm\ N$
    show-help-text: true
part5:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    label: $P= $
    suffix: $\rm\ W$
    show-help-text: true
part6:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    label: $P= $
    suffix: $\rm\ W$
    show-help-text: true
substitutions:
  params:
    vars:
      title: Circuit with Resistance
    B: '1.25'
    v: '20'
    part3:
      ans1:
        value: Clockwise
      ans2:
        value: Counterclockwise
---
# {{ params.vars.title }}
Shown below is a conducting rod that slides along metal rails. The apparatus is in a uniform magnetic field of strength ${{params.B }} \textrm{ T}$, which is directly into the page. The rod is pulled to the right at a constant speed of ${{params.v }} \textrm{ m/s}$ by a force $\overrightarrow{F}$. The only significant resistance in the circuit comes from the $2.0 \rm\ \Omega$ resistor shown.

<img src="Fig13_46.png">

## Part 1

What is the emf induced in the circuit?

### Answer Section

Please enter a numeric value.

## Part 2

What is the induced current?

### Answer Section

Please enter a numeric value.

## Part 3

Does the induced current circulate clockwise or counterclockwise?

### Answer Section

- {{ params.part3.ans1.value }}
- {{ params.part3.ans2.value }}

## Part 4

What is the magnitude of $\overrightarrow{F}$?

### Answer Section

Please enter a numeric value.

## Part 5

What is the power output of $\overrightarrow{F}$?

### Answer Section

Please enter a numeric value.

## Part 6

What is the power dissipated in the resistor?

### Answer Section

Please enter a numeric value.

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}
{{ feedback.part1_ans }}

### pl-answer-panel

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)