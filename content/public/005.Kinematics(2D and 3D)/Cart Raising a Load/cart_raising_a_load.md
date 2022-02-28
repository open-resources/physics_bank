---
title: Cart raising a load
topic: Kinematics(2D and 3D)
author: Peyman Yousefi
source: APSC 181, Lecture 13, Q2
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 5.9.1.0
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
- APSC 181 - LA
assets:
- L13Q2.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $v_{b}=$
    suffix: $m/s$
    weight: 1
    allow-blank: true
substitutions:
  params:
    vars:
      title: Cart raising a load
      units: m/s
    v_a: 3
    x: 8
    h: 3
---
# {{ params.vars.title }}

## Question Text

<img src="L13Q2.png" width=85%>

Determine the magnitude of the total velocity of $B$ as cart $A$ moves to the right with $v = {{params.v_a}}m/s$.
Assume the cable for $B$ remains vertical, and the diameter of the pully is negligible.
Assume $x = {{params.x}}m$, and $h = {{params.h}}m$.

### Answer Section

Please enter an integer value in ${{ params.vars.units }}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)