---
title: Spring on Ramp
topic: Force
author: Jake Bobowski
source: 2017 Final Q16
template_version: 1.0
attribution: standard
outcomes:
- 6.1.1.4
- 6.1.1.5
- 6.4.1.1
- 6.9.1.3
- 6.11.2.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- MP
assets:
- q16image.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: m
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: m
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Spring on Ramp
      units: m
    m: 4
    theta: 25
    k: 200
    us: 0.7
    uk: 0.4
---
# {{ params.vars.title }}
In the figure below m = {{ params.m }} kg, $\theta$ = {{ params.theta }} $^\circ$, and k = {{ params.k }} N/m.
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