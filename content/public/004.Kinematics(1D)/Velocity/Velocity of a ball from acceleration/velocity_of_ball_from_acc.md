---
title: Velocity of a ball from acceleration
topic: Kinematics(1D)
author: Peyman Yousefi
source: APSC 181, Lecture 3, Q3
template_version: 1.1
attribution: standard
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.1.1.0
- 6.1.1.1
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- short
tags:
- AP
- APSC181
- Lecture Activities
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $m/s$
myst:
  substitutions:
    params_vars_title: Velocity of a ball from acceleration
    params_vars_units: m/s
    params_v0: 23
    params_s0: 9
    params_k: 0.04
    params_s: 11
---
# {{ params_vars_title }}
The acceleration of a ball is given by $a(x) = -5kx^2$, where $a$ is acceleration of the ball in $m/s^2$, $k$ is a constant with unspecified units, and $x$ is the position of the ball in $m$.

## Question Text

Consider the following initial conditions for position $x_0$ and velocity $v_0$ at $t = 0 s$:
$x_0 = {{params_s0}} m$
$v_0 = {{params_v0}} m/s$
Use these conditions to detemine the velocity of the ball at $x = {{params_s}} m$.
You may use $k = {{params_k}} $.

### Answer Section

Please enter in a numeric value in ${{ params_vars_units }}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)