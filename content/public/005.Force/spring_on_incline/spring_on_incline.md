---
title: Spring on an Incline
topic: Energy
author: Jake Bobowski
source: 2013 Final Q10
template_version: 0.3
outcomes:
- 5.9.1.0
- 5.11
- 7.2.1.0
- 8.1.1.0
- 8.3.1.0
tags:
- quiz
- homework
assets:
- q10image.png
part1:
  type: number-input
  pl-customizations:
    label: $x=$
    allow-blank: true
    weight: 1
    suffix: m
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    label: $K_{max}=$
    allow-blank: true
    weight: 1
    suffix: J
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Spring on an Incline
      units1: m
      units2: J
    m: 4
    k: 653
    theta: 28
    mu: 0.25
    d: 5
    g: 9.8
---
# {{ params.vars.title }}
## Part 1

A small {{params.m}} kg block is accelerated from rest on a flat surface by a compressed spring (k = {{params.k}} N/m) along a frictionless, horizontal surface.
The block leaves the spring at the spring’s equilibrium position (x = 0) and travels on an incline (θ = {{params.theta}}◦) with a coefficient of kinetic friction μk = {{params.mu}}.
The block moves a horizontal distance D = {{params.d}} m before coming to a stop.

(a) What is the initial compression of the spring?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1 }}.
## Part 2

(b) What is the maximum kinetic energy of the block?

### Answer Section

Please enter in a numeric value in {{ params.vars.units2 }}.

## Attribution

![Image representing the Creative Commons 4.0 BY-NC-SA license.](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png) Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).