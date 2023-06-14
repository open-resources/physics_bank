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
myst:
  substitutions:
    params_vars_vehicle: van
    params_vars_title: A Crate's Maximum Acceleration without Slipping
    params_vars_units: $m/s^2$
    params_mu_s: 0.73
    params_mu_k: 0.46
    params_theta: 16
---
# {{ params_vars_title }}
A wood crate sits in the back of a {{ params_vars_vehicle }}.
The coefficients of friction between the crate and the {{ params_vars_vehicle }} are $\mu_s = $ {{ params.mu_s }} and $\mu_k = $ {{ params.mu_k }}.
The {{ params_vars_vehicle }} starts moving up a {{ params_theta }}$^{\circ}$ slope.

## Question Text

What is the maximum acceleration the {{ params_vars_vehicle }} can have without the crate slipping out the back?

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)