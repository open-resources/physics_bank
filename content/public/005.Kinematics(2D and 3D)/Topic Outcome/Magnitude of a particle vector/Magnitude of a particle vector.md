---
title: The Magnitude of a Particle Vector
topic: Kinematics(2D and 3D)
author: Jake Bobowski
source: 2012 Final Q1
template_version: 1.4
attribution: standard
partialCredit: false
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
- NR
- SS
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: 'Magnitude = '
    suffix: '{{params.vars.units}}'
    comparison: sigfig
    digits: 3
myst:
  substitutions:
    params:
      vars:
        title: The Magnitude of a Particle's Vector
        units: "$\r{m/s}^2$"
      r_i: $3t^2 - 8t$
      r_j: $2t^2 + 6t$
      t: $14$
      choice: acceleration
---
# {{ params.vars.title }}

## Part 1

A particle has a trajectory given as $\vec{r} = ($ {{ params.r_i }} $) \hat{\imath} + ($ {{ params.r_j }} $) \hat{\jmath}$ $m$ for $t$ given in seconds. What is the magnitude of the {{ params.choice }} vector for this particle at $t = $ {{ params.t }} $s$?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)