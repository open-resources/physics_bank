---
title: Parcel from Aircraft 3D
topic: Kinematics(2D and 3D)
author: Peyman Yousefi
source: APSC 181, Lecture 9, Q2
template_version: 1.2
attribution: standard
outcomes:
- 5.4.1.1
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- AP
- APSC 181 - LA
assets:
- L9Q2.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: $ft$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $y= $
    suffix: $ft$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $z= $
    suffix: $ft$
substitutions:
  params:
    vars:
      title: Parcel from Aircraft 3D
      units: ft
    z0: 1951
    y0: 878
    vx0: 169
    vy0: 39
---
# {{ params.vars.title }}
${{params.z0}}ft$ above the ground, a cargo plane flies in a horizontal circle with radius of ${{paramsy.y0}}ft$.
Its speed is constant at ${{params.vx0}}ft/s$.
At the moment shown, a small package is ejected from the right side of the plane with a horizontal velocity of ${{params.vx0}}ft/s$ relative to the cargo plane.
Calculate the coordinates of the point of impact, neglect air resistance.

<img src="L9Q2.png" width=400>

## Part 1

Calculate the X - coordinate of the landing point.

### Answer Section

## Part 2

Calculate the Y - coordinate of the landing point.

### Answer Section

## Part 3

Calculate the Z - coordinate of the landing point.

### Answer Section

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)