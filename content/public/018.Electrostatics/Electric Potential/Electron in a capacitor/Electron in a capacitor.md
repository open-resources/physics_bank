---
title: Electron in a capacitor
topic: Electrostatics
author: Jake Bobowski
source: 2.7.77
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 18.11.1.4
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
- chapter 7
- problem 77
- electron
- potential
- energy
- parallel plates
- numeric
- JB
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $v=$
    allow-blank: false
    show-correct-answer: true
    show-help-text: true
    suffix: $\rm\ m/s$
    weight: 1
    custom-format: .3g
substitutions:
  params:
    vars:
      title: Electron in a capacitor
    d: '3.0'
    V: '160'
    s: $4.0\times 10^{6}$
    x: '3.0'
---
# {{ params.vars.title }}
An electron enters a region between two large parallel plates made of aluminum separated by a distance of {{ params.d }} $\rm\ cm$ and kept at a potential difference of {{ params.V }} $\rm\ V$.
The electron enters through a small hole in the negative plate and moves toward the positive plate.
At the time the electron is near the negative plate, its speed is {{ params.s }} $\rm\ m/s$.

## Question Text

Assuming the electric field between the plates is uniform, find the speed of the electron when it is {{ params.x }} $\rm\ cm$ from the negative plate.

### Answer Section

Please enter a numeric value.

### pl-submission-panel

{{ feedback.part1_ans }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)