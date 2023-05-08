---
title: Forming helium atoms
topic: Electrostatics
author: Jake Bobowski
source: 2.7.73
template_version: 1.1
attribution: openstax-physics-vol2
showCorrectAnswer: false
outcomes:
- 18.11.1.4
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- OSUP
- volume 2
- chapter 7
- problem 73
- charge
- gravity
- numeric
- JB
assets:
- OSUPv2p7_73.png
part1:
  type: number-input
  pl-customizations:
    label: $W=$
    allow-blank: false
    show-correct-answer: true
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ J$
    weight: 1
    custom-format: .3g
myst:
  substitutions:
    params_vars_title: Forming helium atoms
    params_d: '0.540000'
    params_p: -10
---
# {{ params_vars_title }}
To form a helium atom, an alpha particle that contains two protons and two neutrons is fixed at one location, and two electrons are brought from far away, one at a time.
The first electron is placed a distance $d = {{ params_d }}\times 10^{ {{ params_p }} }\rm\ m$ from the alpha particle and held there while the second electron is brought a distance $d = {{ params_d }}\times 10^{ {{ params_p }} }\rm\ m$ from the alpha particle on the other side from the first electron.
The final configuration of the particles is shown in the figure.

<img src="OSUPv2p7_73.png" width=400 alt="Final configuration of the alpha particle and electrons.">

## Question Text

What is the work done by the system to assemble the charges?

### Answer Section

Please enter a numeric value.

### pl-submission-panel

{{ feedback.part1_ans }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)