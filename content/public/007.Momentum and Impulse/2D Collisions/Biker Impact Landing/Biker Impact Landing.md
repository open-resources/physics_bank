---
title: Biker Impact Landing
topic: Momentum and Impulse
author: Peyman Yousefi
source: APSC 181, Lecture 23, Q3
template_version: 1.2
attribution: standard
singleVariant: false
showCorrectAnswer: false
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
- APSC181
- Lecture Activities
- JR
assets:
- Snowboarder Impact Landing.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F= $
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
      title: Biker Impact Landing
    v: 3
    t: 0.11
    ad: 31
    m: 58
    thetad: 36
---
# {{ params.vars.title }}
<img src="Snowboarder Impact Landing.png" width=400>

A Biker is travelling with a velocity of ${{params.v}}m/s$, $\theta=$ {{params.thetad}} $^\circ$ below the tangent, when they land on the slope with no rebound.
The impact lasts for ${{params.t}} s$.
The weight of the biker and bike is ${{params.m}}kg$, and the hill slope is $\alpha= {{params.ad}} ^\circ$.

## Part 1

Determine the average normal force exerted by the incline on the snowboard during the impact.

### Answer Section

Please enter in a numeric value in $N$.

## Part 2

Determine their speed $v$ along the slope just after impact.

### Answer Section

Please enter in a numeric value in $m/s$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)