---
title: Spring on an Incline
topic: Work
author: Jake Bobowski
source: 2013 Final Q10
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.9.1.0
- 5.11
- 7.2.1.0
- 8.1.1.0
- 8.3.1.0
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- multi-chapter
length:
- long
tags:
- MP
- final_exam
assets:
- q10image.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.02
    label: $x=$
    allow-blank: true
    weight: 1
    suffix: m
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $K_{max}=$
    allow-blank: true
    weight: 1
    suffix: J
myst:
  substitutions:
    params_vars_title: Spring on an Incline
    params_vars_units1: m
    params_vars_units2: J
    params_m: 2
    params_k: 669
    params_theta: 27
    params_mu: 0.25
    params_d: 5
    params_g: 9.8
---
# {{ params_vars_title }}
A small {{params_m}} kg block is accelerated from rest on a flat surface by a compressed spring ($k$ = {{params_k}} $N/m$) along a frictionless, horizontal surface.
The block leaves the spring at the spring's equilibrium position ($x$ = 0) and travels on an incline ($\theta$ = {{params_theta}}$^{\circ}$) with a coefficient of kinetic friction $\mu_k$ = {{params_mu}}.
The block moves a horizontal distance $D$ = {{params_d}} m before coming to a stop.

<img src="q10image.png" alt="Pictured is a block being pushed towards a ramp by a compressed string." >

## Part 1

(a) What is the initial compression of the spring?

### Answer Section

Please enter in a numeric value in {{ params_vars_units1 }}.

## Part 2

(b) What is the maximum kinetic energy of the block?

### Answer Section

Please enter in a numeric value in {{ params_vars_units2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)