---
title: Snowboarder Impact Landing
topic: Momentum and Impulse
author: Peyman Yousefi
source: APSC 181, Lecture 23, Q3
template_version: 1.2
attribution: standard
outcomes:
- 7.6.1.1
difficulty:
- hard
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- APSC 181 - LA
- JR
assets:
- Snowboarder Impact Landing.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $N= $
    suffix: $N$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $m/s$
substitutions:
  params:
    vars:
      title: Snowboarder Impact Landing
    v: 7
    t: 0.13
    ad: 37
    m: 64
    thetad: 33
---
# {{ params.vars.title }}
<img src="Snowboarder Impact Landing.png" width=400>

A snowboarder is travelling with a velocity of ${{params.v}}m/s$, $\theta=$ {{params.thetad}} $^\circ$ below the tangent, when they land on the slope with no rebound.
The impact lasts for ${{params.t}} s$.
The weight of the boarder and board is ${{params.m}}kg$, and the hill slope is $\alpha= {{params.ad}} ^\circ$.

## Part 1

Determine their speed $v$ along the slope just after impact.

### Answer Section

Please enter in a numeric value in $N$.

## Part 2

Determine the average normal force exerted by the incline on the snowboard during the impact.

### Answer Section

Please enter in a numeric value in $m/s$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)