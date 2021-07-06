---
title: Particle between charged plates
topic: Electrostatics
author: Jake Bobowksi
source: 2.7.61
template_version: 1.0
attribution: openstax-physics-vol2
outcomes:
- 18.11.2.4
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- OSUP
- volume 2
- chapter 6
- problem 61
- electric potential
- parallel plates
- charged particle
- numeric
- JB
assets: null
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $v= $
    suffix: $\rm\ m/s$
    comparison: relabs
    rtol: 0.03
    atol: 0
substitutions:
  params:
    sig: '26'
    d: '4.0'
    particle: An electron
    particle1: electron
    p1: negative
    p2: positive
---
# {{ params.vars.title }}
Two large plates of charge density ${{ params.sig }}\rm\ \mu C/m^2$ face each other at a separation of ${{ params.d }} \textrm{ mm}$.
{{ params.particle }} is released from rest at the {{ params.p1 }} plate.
## Question Text

With what speed does the {{ params.particle1 }} strike the {{ params.p2 }} plate?

### Answer Section

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)