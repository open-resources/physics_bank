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
- APSC 181 - LA
assets: null
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
      title: Velocity of a ball from acceleration
      units: m/s
    v0: 24
    s0: 8
    k: 0.03
    s: 10
---
# {{ params.vars.title }}
The acceleration of a ball is given by $a(x) = -5kx^2$, where $a$ is acceleration of the ball in $m/s^2$, $k$ is a constant with unspecified units, and $x$ is the position of the ball in $m$.

## Question Text

Consider the following initial conditions for position $x_0$ and velocity $v_0$ at $t = 0 s$:
$x_0 = {{params.s0}} m$
$v_0 = {{params.v0}} m/s$
Use these conditions to detemine the velocity of the ball at $x = {{params.s}} m$.
You may use $k = {{params.k}} $.

### Answer Section

Please enter in a numeric value in ${{ params.vars.units }}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)