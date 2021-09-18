---
title: Log up a Hill
topic: Energy
author: Peyman Yousefi
source: APSC 181, Lecture 19, Q2
template_version: 1.2
attribution: standard
outcomes:
- 8.5.1.0
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
- Log up a Hill.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $u_k= $
    comparison: relabs
    rtol: 0.02
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $a= $
    suffix: $ft/s^2$
    comparison: relabs
    rtol: 0.02
substitutions:
  params:
    vars:
      title: Log up a Hill
    W: 754
    t: 40
    v: 10
    P: 6
    P2: 8
---
# {{ params.vars.title }}
<img src="Log up a Hill.png" width=400>

A powered pulley moves a ${{params.W}} lb$ log up a hill ($\theta=${{params.t}} $^\circ$) at a constant speed of ${{params.v}}ft/s$.

## Part 1

If the power output is ${{params.P}}hp$, compute the coefficient of kinetic friction between the log and hill.

### Answer Section

Please enter in a numeric value.

## Part 2

If the power is increased to ${{params.P2}}hp$, what is the new acceleration?

### Answer Section

Please enter in a numeric value in $m/s^2$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)