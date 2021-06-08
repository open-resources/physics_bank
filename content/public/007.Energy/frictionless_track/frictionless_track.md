---
title: Horizontal frictionless track
topic: Energy
author: Jake Bobowski
source: 2013 Final Q12
template_version: 0.4
outcomes:
- 8.2.1.0
- 8.3.1.0
- 8.5.1.1
- 9.1.1.1
- 9.2.1.1
tags:
- quiz
- homework
assets:
- q12image.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $F= $
    suffix: N
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\mu = $
    suffix: null
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Horizontal frictionless track
      units: N
    m: 0.25
    v: 5
    R: 1.5
    L: 3
---
# {{ params.vars.title }}
## Part 1

A small block of mass m = {{params.m}} kg is fired with an initial speed v0 = {{params.v}} m/s along a horizontal section of frictionless track, as shown in the top portion of the figure.
The block then moves along the frictionless semicircular vertical track of radius R = {{params.R}} m.
(a) Determine the force exerted by the track on the block at point A.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.
## Part 2

(b) The bottom of the track consists of a horizontal section (L = {{params.L}} m) with friction.
Determine the coefficient of kinetic friction between the block and the bottom portion of the track if the block just makes it to point B before coming to rest.

### Answer Section

Please enter in a numeric value.

## Attribution

![Image representing the Creative Commons 4.0 BY-NC-SA license.](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png) Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).