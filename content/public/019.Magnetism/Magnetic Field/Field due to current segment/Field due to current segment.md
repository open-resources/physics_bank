---
title: Field due to current segment
topic: Magnetism
author: Jake Bobowksi
source: 2.12.16
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 18.11.2.3
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
- problem 16
- Biot-Savart law
- current segment
- magnetic field
- numeric
- JB
assets:
- OSUPv2p12_16.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $B= $
    suffix: $\rm\ T$
myst:
  substitutions:
    params_vars_title: Field due to current segment
    params_I: '3.0'
    params_x: '4.80'
    params_y: '5.20'
    params_dl: '0.20'
---
# {{ params_vars_title }}
A ${{ params_I }}\rm\ A$ current flows through the wire shown in the figure.
Take $x = {{ params_x }}\rm\ cm$ and $y = {{ params_y }}\rm\ cm$.

<img src="OSUPv2p12_16.png" width=400 alt="A wire segment carrying a current">
<p></p>

## Question Text

What is the magnitude of the magnetic field due to a ${{ params_dl }}\rm\ mm$ segment of wire as measured at point P?

### Answer Section

### pl-submission-panel

{{ submitted_answers.part1_ans_str }}

{{ feedback.part1_ans }}

### pl-answer-panel

$B=$ {{ correct_answers.part1_ans_str }} $\rm\ T$

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)