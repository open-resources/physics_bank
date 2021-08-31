---
title: Field due to current segment
topic: Magnetism
author: Jake Bobowksi
source: 2.12.16
template_version: 1.0
attribution: openstax-physics-vol2
outcomes:
- 18.11.2.3
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
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $B= $
    suffix: $\rm\ T$
    comparison: relabs
    rtol: 0.03
    atol: 0
substitutions:
  params:
    vars:
      title: Field due to current segment
    I: '7.5'
    x: '5.80'
    y: '5.60'
    dl: '0.50'
---
# {{ params.vars.title }}
A ${{ params.I }}\rm\ A$ current flows through the wire shown in the figure.
Take $x = {{ params.x }}\rm\ cm$ and $y = {{ params.y }}\rm\ cm$.

<img src="OSUPv2p12_16.png" width=400 alt="A wire segment carrying a current">
<p></p>

## Question Text

What is the magnitude of the magnetic field due to a ${{ params.dl }}\rm\ mm$ segment of wire as measured at point P?

### Answer Section

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)