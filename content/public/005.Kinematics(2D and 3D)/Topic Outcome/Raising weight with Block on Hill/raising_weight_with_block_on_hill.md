---
title: Raising weight with Block on Hill
topic: Kinematics(2D and 3D)
author: Peyman Yousefi
source: APSC 181, Lecture 13, Q3
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 5.9.1.0
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
- L13Q3.png
part1:
  type: number-input
  pl-customizations:
    label: $v_{A}=$
    weight: 1
    allow-blank: true
    rtol: 0.02
    suffix: $m/s$
part2:
  type: number-input
  pl-customizations:
    label: $a_{A}=$
    weight: 1
    allow-blank: true
    rtol: 0.02
    suffix: $m/s^2$
substitutions:
  params:
    vars:
      title: Raising weight with Block on Hill
      units_v: m/s
      units_a: m/s^2
    v_b: 5.0
    a_b: 3.2
---
# {{ params.vars.title }}
<img src="L13Q3.png" width=85%>

In the moment shown above, $B$ is travelling downwards at $v = {{params.v_b}}m/s$, but accelerating upwards at $a = {{params.a_b}}m/s^2$.

## Part 1

Determine the velocity of block $A$. Positive if downhill, negative if uphill.

### Answer Section

Please enter an integer value in ${{ params.vars.units_v }}$.

## Part 2

Determine the acceleration of block $A$. Positive if downhill, negative if uphill.

### Answer Section

Please enter an integer value in ${{ params.vars.units_a }}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)