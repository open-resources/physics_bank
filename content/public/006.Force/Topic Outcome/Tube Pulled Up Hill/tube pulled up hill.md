---
title: Tube pulled Uphill
topic: Force
author: Peyman Yousefi
source: APSC 181, Lecture 14, Q2
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.1.1.4
- 6.1.1.5
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- section
length:
- average
tags:
- AP
- APSC181
- Lecture Activities
assets:
- L14Q2.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a_{x}= $
    suffix: $m/s^2$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a_{x}= $
    suffix: $m/s^2$
myst:
  substitutions:
    params:
      vars:
        title: Tube pulled Uphill
      m: 36
      theta_s: 16
      theta_2: 9
      T_2: 246
      T_1: 119
---
# {{ params.vars.title }}
<img src="L14Q2.png" width=80%>

At a waterpark, a motor pulls a $m = {{params.m}}kg$ tube and person up a ${{params.theta_s}}^{\circ}$ frictionless incline, creating a tension $T$ in the cable.
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