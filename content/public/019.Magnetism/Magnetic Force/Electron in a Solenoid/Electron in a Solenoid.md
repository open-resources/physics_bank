---
title: Electron in a Solenoid
topic: Magnetism
author: Jake Bobowksi
source: 2.12.55
template_version: 1.0
attribution: openstax-physics-vol2
outcomes:
- 19.2.3.0
- 19.2.3.1
- 19.3.2.0
- 19.3.2.1
- 19.6.1.0
- 19.6.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- OSUP
- volume 2
- chapter 12
- problem 55
- magnetic force
- solenoid
- centripetal acceleration
- circular motion
- numeric
- JB
assets: null
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $I= $
    suffix: $\rm\ A$
    comparison: relabs
    rtol: 0.03
    atol: 0
substitutions:
  params:
    n: '25'
    r: '2.90'
    v: '1.60'
    p: '6'
---
# {{ params.vars.title }}
A solenoid with ${{ params.n }}$ turns per centimter carries a current $I$.
An electron moves within the solenoid in a circle of radius ${{ params.r}}\textrm{ cm}$.
The plane of the circular motion is perpendicular to the axis of the solenoid.The speed of the electron is ${{ params.v }}\times 10^{ {{ params.p }} }\textrm{ m/s}$.
## Question Text

What is the current $I$ in the solenoid?

### Answer Section

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)