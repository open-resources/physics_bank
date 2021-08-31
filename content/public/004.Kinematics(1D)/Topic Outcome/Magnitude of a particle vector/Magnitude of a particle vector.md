---
title: The Magnitude of a Particle's Vector
topic: Kinematics(1D)
author: Jake Bobowski
source: 2012 Final Q1
template_version: 1.1
attribution: standard
outcomes:
- 4.7.3.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- PW
assets: null
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: 'Magnitude = '
    suffix: $m/s^2$
    comparison: sigfig
    digits: 3
substitutions:
  params:
    vars:
      title: The Magnitude of a Particle's Vector
      units: $m/s^2$
    r_i: -9t^2 - 3t
    r_j: -3t^2 - 4t
    t: 14
    choice: velocity
---
# {{ params.vars.title }}

## Question Text

A particle has a trajectory given as $\vec{r} = ({{ params.r_i }}) \hat{\imath} + ({{ params.r_j }}) \hat{\jmath}$ m for $t$ given in seconds. What is the magnitude of the {{ params.choice }} vector for this particle at $t = $ {{ params.t }} s?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)