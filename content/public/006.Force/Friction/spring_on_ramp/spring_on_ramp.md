---
title: Spring on Ramp
topic: Force
author: Jake Bobowski
source: 2017 Final Q16
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 6.1.1.4
- 6.1.1.5
- 6.4.1.1
- 6.9.1.3
- 6.11.2.1
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- MP
assets:
- q16image.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: m
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: m
substitutions:
  params:
    vars:
      title: Spring on Ramp
      units: m
    m: 1
    theta: 30
    k: 100
    us: 0.7
    uk: 0.35
---
# {{ params.vars.title }}
In the figure below m = {{ params.m }} kg, $\theta$ = {{ params.theta }}$^\circ$, and k = {{ params.k }} N/m.
In this problem assume that the ramp never moves and that there is friction between the block and the ramp.

<img src="q16image.png" width=400 alt="Block being pulled up a ramp by a spring">

## Part 1

If the coefficient of static friction between the block and the ramp is $\mu_s$ = {{ params.us }}, what is the maximum amount that the spring can be stretched beyond its equilibrium length before the block begins to slide up the ramp?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

Suppose now that the block is sliding up the ramp at a constant velocity.
By what length is the spring stretched?
Assume that the coefficient of kinetic friction is $\mu_k$ = {{ params.uk }}.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)