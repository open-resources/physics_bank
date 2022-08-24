---
title: The Magnitude of a Particle's Vector
topic: Kinematics(2D and 3D)
author: Jake Bobowski
source: 2012 Final Q1
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 4.7.3.0
difficulty:
- easy
randomization:
- 2
taxonomy:
- undefined
span:
- section
length:
- average
tags:
- PW
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: 'Magnitude = '
    suffix: $m/s^2$
substitutions:
  params:
    vars:
      title: The Magnitude of a Particle's Vector
      units: $m/s$
    r_i: $3t^2 - 2t$
    r_j: $5t^2 - 5t$
    t: $17$
    choice: acceleration
---
# {{ params.vars.title }}

## Question Text

A particle has a trajectory given as $\vec{r} = ($ {{ params.r_i }} $) \hat{\imath} + ($ {{ params.r_j }} $) \hat{\jmath}$ $m$ for $t$ given in seconds. What is the magnitude of the {{ params.choice }} vector for this particle at $t = $ {{ params.t }} $s$?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)