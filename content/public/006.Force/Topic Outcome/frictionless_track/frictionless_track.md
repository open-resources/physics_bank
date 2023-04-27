---
title: Horizontal frictionless track
topic: Force
author: Jake Bobowski
source: 2013 Final Q12
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
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
span:
- undefined
length:
- undefined
tags:
- MP
assets:
- q12image.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F= $
    suffix: N
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\mu = $
    suffix: null
myst:
  substitutions:
    params_vars_title: Horizontal frictionless track
    params_vars_units: N
    params_m: 0.25
    params_v: 8
    params_R: 0.5
    params_L: 13
---
# {{ params_vars_title }}
A small block of mass m = {{params_m}} kg is fired with an initial speed $v_0$ = {{params_v}} m/s along a horizontal section of frictionless track, as shown in the top portion of the figure.
The block then moves along the frictionless semicircular vertical track of radius $R$ = {{params_R}}m.

<img src="q12image.png" alt="Mass on frictionless track." width=100%>

## Part 1

Determine the force exerted by the track on the block at point A.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 2

The bottom of the track consists of a horizontal section (L = {{params_L}} m) with friction.
Determine the coefficient of kinetic friction between the block and the bottom portion of the track if the block just makes it to point B before coming to rest.

### Answer Section

Please enter in a numeric value.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)