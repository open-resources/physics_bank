---
title: Trapped Hiker
topic: Energy
author: Peyman Yousefi
source: APSC 181, Lecture 19, Q3
template_version: 1.2
attribution: standard
singleVariant: false
showCorrectAnswer: false
outcomes:
- 8.5.1.0
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
- Spring Restraining Cart.png
part1:
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
      title: Trapped Hiker
    m: 78
    F: 1485
    x1: 8.0
    d: 17.0
    h: 9.0
    k: 30
    thetad: 6
---
# {{ params.vars.title }}
<img src="Spring Restraining Cart.png" width=400>

A hiker is trapped in a tunnel after a minor rockslide.
A rescue helicopter arrived and lowered a pulley to help them escape.
The ${{params.m}}kg$ hiker is pulled up through an opening, without touching the walls (No friction).
A bungee cord from their pack sticks to them, acting as a spring with a stiffness of ${{params.k}}N/m$ and is stretched ${{params.x1}}m$ at A, where the hiker is initially pulled from rest.
The $F = {{params.F}}N$ force over a pulley is constantly pulling the hiker free. Calculate the velocity as they passes point C.
$\theta=${{params.thetad}}$^\circ$,$d = {{params.d}}m$,and $h = {{params.h}}m$.

## Part 1

### Answer Section

Please enter in a numeric value in $m/s$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)