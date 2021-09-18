---
title: Cars around a bend
topic: Kinematics(2D and 3D)
author: Peyman Yousefi
source: APSC 181, Lecture 8, Q1
template_version: 1.1
attribution: standard
outcomes:
- 5.6.1.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- AP
- APSC 181 - LA
assets:
- L8Q1.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\gamma= $
    suffix: $ft$
    rtol: 0.02
substitutions:
  params:
    vars:
      title: Cars around a bend
      units: $ft$
    max_acc_A: 0.5
    max_acc_B: 0.8
    ra: 310
    rb: 348
    angle: 57
---
# {{ params.vars.title }}
Two cars travel at constant speeds around a curve.
The front end of both cars crosses line $C$ at the same time, and each driver minimizes their time in the curve.
The maximum horizontal acceleration for car A is ${{params.max_acc_A}}g$ with $R\_{A} = {{params.ra}} ft$ and for car B is ${{params.max_acc_B}}g$ with $R\_{B} = {{params.rb}} ft$.
The angle $\theta = {{params.angle}}^{\circ}$.

<img src="L8Q1.png" width=400>

## Question Text

Determine the distance $\gamma$ which the second car has yet to go along its path to reach line $D$ when the first car reaches it.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)