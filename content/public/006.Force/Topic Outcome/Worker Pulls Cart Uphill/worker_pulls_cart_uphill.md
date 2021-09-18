---
title: Worker Pulls Cart Uphill
topic: Force
author: Peyman Yousefi
source: APSC 181, Lecture 14, Q2
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 6.1.1.4
- 6.1.1.5
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
- AP
- APSC 181 - LA
assets:
- L14Q2.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $a_{x}= $
    suffix: $m/s^2$
    rtol: 0.02
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $a_{x}= $
    suffix: $m/s^2$
    rtol: 0.02
substitutions:
  params:
    vars:
      title: Worker Pulls Cart Uphill
    m: 50
    theta_s: 14
    theta_2: 12
    T_2: 211
    T_1: 98
---
# {{ params.vars.title }}
<img src="L14Q2.png" width=80%>

A worker pulls a $m = {{params.m}}kg$ cart up a ${{params.theta_s}}^{\circ}$ frictionless incline, creating a tension $T$ in the cable.
The cable rises ${{params.theta_2}}^{\circ}$ to travel over a frictionless pulley.
Acceleration is positive if up the slope, negative if down.
Determine the acceleration for the following cases:

## Part 1

acceleration when $T = {{params.T_1}}N$.

### Answer Section

## Part 2

acceleration when $T = {{params.T_2}}N$.

### Answer Section

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)