---
title: Velocity of a ball from acceleration
topic: Kinematics(1D)
author: Peyman Yousefi
source: APSC 181, Lecture 3, Q3
template_version: 1.1
attribution: standard
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
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $m/s$
    rtol: 0.02
substitutions:
  params:
    vars:
      title: Velocity of a ball from acceleration
      units: m/s
    v0: 25
    s0: 7
    k: 0.03
    s: 12
---
# {{ params.vars.title }}
The acceleration of a ball is given by $a(s) = -5ks^2$,
where $a$ is in $m/s^2$,
$k$ is a constant,
and s is in $m$.

## Question Text

Determine the velocity at $s = {{params.s}}m$ if $k = {{params.k}}m^-1s^-2$ and the initial conditions for $t = 0$ are $s_0 = {{params.s0}}m$ and $v_0 = {{params.v0}}m/s$.

### Answer Section

Please enter in a numeric value in ${{ params.vars.units }}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)