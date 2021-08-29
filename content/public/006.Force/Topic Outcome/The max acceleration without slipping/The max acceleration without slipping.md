---
title: A Crate's Maximum Acceleration without Slipping
topic: Force
author: Jake Bobowski
source: 2012 Final Q12
template_version: 1.0
attribution: standard
outcomes:
- 6.1.1.4
- 6.3.1.2
- 6.3.1.3
- 6.7.1.0
- 6.9.1.3
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
    label: $a_{max} = $
    suffix: $m/s^2$
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      vehicle: pickup truck
      title: A Crate's Maximum Acceleration without Slipping
      units: $m/s^2$
    mu_s: 0.9
    mu_k: 0.45
    theta: 11
---
# {{ params.vars.title }}
A wood crate sits in the back of a {{ params.vars.vehicle }}.
The coefficients of friction between the crate and the {{ params.vars.vehicle }} are $\mu_s = $ {{ params.mu_s }} and $\mu_k = $ {{ params.mu_k }}.
The {{ params.vars.vehicle }} starts moving up a {{ params.theta }}$^{\circ}$ slope.

## Question Text

What is the maximum acceleration the {{ params.vars.vehicle }} can have without the crate slipping out the back?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)