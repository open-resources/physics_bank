---
title: Rotational Displacement of Tires
topic: Rotational Motion
author: Jake Bobowski
source: 2015 Final Q9
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 10.1.1.1
difficulty:
- easy
randomization:
- 2
taxonomy:
- undefined
span:
- section
length:
- short
tags:
- PW
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\Delta \theta $
    suffix: rad
substitutions:
  params:
    vars:
      vehicle: truck
      title: Rotational Displacement of Tires
      units: rad
    a: 4.48
    t: 26.6
---
# {{ params.vars.title }}
A {{ params.vars.vehicle }} accelerates from rest at $t = 0$ such that its tires undergo a constant rotational acceleration of $\alpha = $ {{ params.a }} $s^{-2}$.

## Question Text

Compute the rotational displacement of each tire at $t = $ {{ params.t }} $s$.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)