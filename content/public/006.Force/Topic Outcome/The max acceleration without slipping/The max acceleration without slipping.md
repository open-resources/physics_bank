---
title: A Crate's Maximum Acceleration without Slipping
topic: Force
author: Jake Bobowski
source: 2012 Final Q12
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.1.1.4
- 6.3.1.2
- 6.3.1.3
- 6.7.1.0
- 6.9.1.3
difficulty:
- medium
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
    label: $a_{max} = $
    suffix: $m/s^2$
substitutions:
  params:
    vars:
      vehicle: bus
      title: A Crate's Maximum Acceleration without Slipping
      units: $m/s^2$
    mu_s: 0.52
    mu_k: 0.37
    theta: 17
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