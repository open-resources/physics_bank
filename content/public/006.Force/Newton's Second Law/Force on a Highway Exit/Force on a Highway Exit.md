---
title: Force on a Highway Exit
topic: Force
author: Peyman Yousefi
source: APSC 181, Lecture 15, Q1
template_version: 1.2
attribution: standard
outcomes:
- 6.5.1.3
difficulty:
- hard
randomization:
- 2
taxonomy:
- undefined
span:
- multi-chapter
length:
- long
tags:
- APSC 181 - LA
- JR
assets:
- Force on a Highway Exit.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_b= $
    suffix: $m/s$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F= $
    suffix: $N$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F= $
    suffix: $N$
substitutions:
  params:
    vars:
      title: Force on a Highway Exit
    va: 43
    vc: 29
    W: 6326
    d: 184
    r: 150
---
# {{ params.vars.title }}
<img src="Force on a Highway Exit.png" width=400>

A {{ params.W }}$kg$ truck travels with a speed of ${{ params.va }}m/s$ as it approaches point A. At A, it decelerates uniformly to a speed of ${{ params.vc }}m/s$ as it passes point C on the horizontal unbanked ramp highway ramp.
$R = {{ params.r }}m$, $d = {{ params.d }}m$.

## Part 1

What is the velocity as the truck passes point B?

### Answer Section

Please enter in a numeric value in $m/s$.

## Part 2

What is the force at point B?

### Answer Section

Please enter in a numeric value in $N$.

## Part 3

What is the force at point C? Assume the car does not slip.

### Answer Section

Please enter a numeric value in $N$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)