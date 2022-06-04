---
title: Force vs Position Graph
topic: Work
author: Jake Bobowski
source: 2017 Final Q15
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 8.2.1.0
- 9.2.1.0
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- average
tags:
- MP
assets:
- q15image.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $W= $
    suffix: $J$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_x= $
    suffix: $m/s$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: $m$
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $K= $
    suffix: $J$
substitutions:
  params:
    vars:
      title: Force vs Position Graph
      units1: J
      units2: m/s
      units3: m
    m: 2.5
    v: 3.0
    x: 2.5
---
# {{ params.vars.title }}
The graph below shows the net force on a particle as a function of its position. The mass of
the particle is $m =$ {{params.m}} $kg$.

<img src="q15image.png" width=400 alt="Force vs position graph">

## Part 1

What is the total work done on the particle?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1 }}.

## Part 2

If the particle has a velocity of $v_x =$ {{params.v}} $m/s$ when $x =$ 0 $m$, what is the particle's velocity
when $x =$ {{params.x}} $m$?

### Answer Section

Please enter in a numeric value in {{ params.vars.units2 }}.

## Part 3

At what value of x (in meters) does the particle have the maximum kinetic energy?

### Answer Section

Please enter in a numeric value in {{ params.vars.units3 }}.

## Part 4

What is the particle's maximum kinetic energy?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)