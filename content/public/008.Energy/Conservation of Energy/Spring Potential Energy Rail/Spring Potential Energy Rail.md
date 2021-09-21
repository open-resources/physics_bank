---
title: Spring Potential Energy Rail
topic: Energy
author: Peyman Yousefi
source: APSC 181, Lecture 20, Q1
template_version: 1.2
attribution: standard
outcomes:
- 8.5.1.1
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
- APSC 181 - LA
- JR
assets:
- Spring Potential Energy Rail.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $m/s$
    comparison: relabs
    rtol: 0.02
substitutions:
  params:
    vars:
      title: Spring Potential Energy Rail
    m: 10
    xi: 0.39
    x: 0.67
    R: 0.8
    k: 106
---
# {{ params.vars.title }}
<img src="Spring Potential Energy Rail.png" width=400>

A spring between a collar and fixed point has an unstretched length of ${{params.xi}}m$ and a stiffness of ${{params.k}}N/m$.
The ${{params.m}}kg$ collar is released from rest at A and slides down a curve with radius $R = {{params.R}}m$.
Calculate the velocity of the slider as it reaches B, $x = {{params.x}}m$ away from the curve, if there is no friction.

## Part 1

### Answer Section

Please enter in a numeric value in $m/s$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)