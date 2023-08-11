---
title: Marble Course
topic: Rotational Motion
author: Peyman Yousefi
source: APSC 181, Lecture 8, Q1
template_version: 1.1
attribution: standard
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.6.1.0
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
- AP
- APSC181
- Lecture Activities
assets:
- L8Q1.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\gamma= $
    suffix: $in$
myst:
  substitutions:
    params_vars_title: Marble Course
    params_vars_units: $in$
    params_max_acc_A: 0.7
    params_max_acc_B: 1.0
    params_ra: 355
    params_rb: 372
    params_angle: 56
---
# {{ params_vars_title }}
Two marbles travel in track as part of a Rube Goldberg machine.
Both marbles cross line $C$ at the same time, and flow at a their maximum speed.
The maximum horizontal acceleration for marble A is ${{params.max_acc_A}}g$ with $R\_{A} = {{params_ra}} in$ and for marble B is ${{params.max_acc_B}}g$ with $R\_{B} = {{params_rb}} in$.
The angle $\theta = {{params_angle}}^{\circ}$.

<img src="L8Q1.png" width=400>

## Question Text

Determine the distance $\gamma$ which the second marble has yet to go along its path to reach line $D$ when the first marble reaches it.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)