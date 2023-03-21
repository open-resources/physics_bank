---
title: Artificial Gravity Simulator
topic: Plane Curvilinear Motion Kinetics
author: Ammar Zavahir
source: original
template_version: 1.0
attribution: standard
outcomes:
- 6.12.2.1
- 6.12.2.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- APSC 181
- A.Z
assets:
- spacecraft.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: m/s
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Artificial Gravity Simulator
    m: 88
    r: 594
---
# {{ params.vars.title }}
To simulate the effects of $â$weight$â$ in deep space, the spacecraft is made to rotate with the astronaut $â$standing$â$ on the outer hull of a circular chamber. The artificial gravity experienced by the astronaut is the inertial reaction to the normal force pulling them to the center of rotation.

<img src="spacecraft.png" width=400>

## Question Text

What is the rotational speed($v$) with which the rocket has to rotate to mimic earthâs gravity($g$).
M = {{ params.m }}$kg$, R = {{ params.r }}$m$

### Answer Section

Please enter in a numeric value in m/s.s

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)