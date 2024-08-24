---
title: Magnetic field of a hollow cylinder
topic: Magnetism
author: Jake Bobowski
source: 2.12.46
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 19.2.4.1
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
- problem 46
- magnetic field
- hollow cylinder
- Ampere's law
- numeric
- JB
assets:
- OSUPv2p12_46.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $B_1=$
    allow-blank: false
    show-correct-answer: true
    show-help-text: true
    suffix: $\rm\ T$
    weight: 1
    custom-format: .3g
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $B_2=$
    allow-blank: false
    show-correct-answer: true
    show-help-text: true
    suffix: $\rm\ T$
    weight: 1
    custom-format: .3g
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $B_3=$
    allow-blank: false
    show-correct-answer: true
    show-help-text: true
    suffix: $\rm\ T$
    weight: 1
    custom-format: .3g
myst:
  substitutions:
    params:
      vars:
        title: Magnetic field of a hollow cylinder
      r1: '3.0'
      r2: '5.0'
      I: '30.0'
      ra: '2.0'
      rb: '4.0'
      rc: '6.0'
---
# {{ params.vars.title }}
The figure shows a cross-section of a long, hollow, cylindrical conductor of inner radius $r_1 = {{ params.r1 }}\rm\ cm$ and outer radius $r_2 = {{ params.r2 }}\rm\ cm$.
A ${{ params.I }}\rm\ A$ current distrubted uniformly over the cross-section flows into the screen.

<img src="OSUPv2p12_46.png" width=350 alt="Cross-section of a hollow cylinder carry a uniform current.">

## Part 1

Calculate the magnitude of the magnetic field at a radius $r = {{ params.ra }}\rm\ cm$ measured from the axis of the hollow cylinder.

### Answer Section

## Part 2

Calculate the magnitude of the magnetic field at a radius $r = {{ params.rb }}\rm\ cm$ measured from the axis of the hollow cylinder.

### Answer Section

## Part 3

Calculate the magnitude of the magnetic field at a radius $r = {{ params.rc }}\rm\ cm$ measured from the axis of the hollow cylinder.

### Answer Section

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)