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
myst:
  substitutions:
    params_vars_title: The Magnitude of a Particle's Vector
    params_vars_units: $m/s$
    params_r_i: $-t^3 - 5t^2 + 7t$
    params_r_j: $8t^2 + 4t$
    params_t: $12$
    params_choice: acceleration
---
# {{ params_vars_title }}

## Question Text

A particle has a trajectory given as $\vec{r} = ($ {{ params.r_i }} $) \hat{\imath} + ($ {{ params.r_j }} $) \hat{\jmath}$ $m$ for $t$ given in seconds. What is the magnitude of the {{ params_choice }} vector for this particle at $t = $ {{ params_t }} $s$?

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)