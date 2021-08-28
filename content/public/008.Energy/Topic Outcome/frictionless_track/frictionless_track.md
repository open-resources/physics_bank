---
title: Horizontal frictionless track
topic: Energy
author: Jake Bobowski
source: 2013 Final Q12
template_version: 1.0
attribution: standard
outcomes:
- 8.2.1.0
- 8.3.1.0
- 8.5.1.1
- 9.1.1.1
- 9.2.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- MP
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
    digits: 3
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
    m: 4.75
    v: 8
    R: 0.5
    L: 10
---
# {{ params.vars.title }}
A small block of mass m = {{params.m}} kg is fired with an initial speed v0 = {{params.v}} m/s along a horizontal section of frictionless track, as shown in the top portion of the figure.
The block then moves along the frictionless semicircular vertical track of radius R = {{params.R}} m.

![Mass on frictionless track.](q12image.png)

## Part 1

(a) Determine the force exerted by the track on the block at point A.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

(b) The bottom of the track consists of a horizontal section (L = {{params.L}} m) with friction.
Determine the coefficient of kinetic friction between the block and the bottom portion of the track if the block just makes it to point B before coming to rest.

### Answer Section

Please enter in a numeric value.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)