---
title: T-bone Collision
topic: Momentum and Impulse
author: Peyman Yousefi
source: APSC 181, Lecture 21, Q2
template_version: 1.2
attribution: standard
outcomes:
- 7.6.1.2
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
- T-bone Collision.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $v_B= $
    suffix: $m/s$
    comparison: relabs
    rtol: 0.02
substitutions:
  params:
    vars:
      title: T-bone Collision
    ma: 1462
    mb: 1746
    vak: 44
    thetad: 16
---
# {{ params.vars.title }}
<img src="T-bone Collision.png" width=400>

Two cars experience a "T-bone" collision at an intersection.
Car A has a mass of ${{params.ma}}kg$, and Car B has a mass of ${{params.mb}}kg$.
The cars become entangled and move with a common velocity in the direction shown.
If Car A was travelling at ${{params.vak}}km/h$ when impacted, calculate the corresponding velocity of Car B at impact.
$\theta= {{params.thetad}}^\circ$

## Part 1

### Answer Section

Please enter in a numeric value in $m/s$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)