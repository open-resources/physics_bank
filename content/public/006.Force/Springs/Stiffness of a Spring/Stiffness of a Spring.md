---
title: Stiffness of a Spring
topic: Force
author: Peyman Yousefi
source: APSC 181, Lecture 18, Q1
template_version: 1.2
attribution: standard
outcomes:
- 6.11.2.1
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
- Stiffness of a Spring.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $k= $
    suffix: $N/m$
    comparison: relabs
    rtol: 0.02
substitutions:
  params:
    vars:
      title: Stiffness of a Spring
    h: 326
    F: 155
    x: 125
    d: 40
    m: 4
---
# {{ params.vars.title }}
<img src="Stiffness of a Spring.png" width=400>

The box A of mass ${{ params.m }}kg$ slides up the shaft $h = {{ params.h }}mm$ tall with negligible friction.
When the box is released from rest at the bottom of the shaft, it moves up from the constant force $F = {{ params.F }}N$ over the pully B, ${{ params.x }}mm$ away from the shaft.
Find the value of k if the spring only compresses ${{ params.d }}mm$.
$d = {{ params.d }}mm$.

## Part 1

### Answer Section

Please enter in a numeric value in $N/m$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)