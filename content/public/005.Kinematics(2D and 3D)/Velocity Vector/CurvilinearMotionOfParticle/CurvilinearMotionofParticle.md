---
title: Curvilinear Motion Of A Particle Path
topic: Kinematics(2D and 3D)
author: Ranya Ghosh
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 1.7.2.4
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
span:
- undefined
length:
- undefined
tags:
- RG
- JR
- APSC181
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v = $
    suffix: $\rm{m/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a = $
    suffix: $\rm{m/s^2}$
myst:
  substitutions:
    params_vars_title: Particle Curvilinear Motion
    params_vars_units: m/s
    params_m: 7
    params_n: 2
    params_r: 6
    params_p: 4
    params_t: 1
---
# {{ params_vars_title }}
A particle moves in a curvilinear motion according to the following equations:

$x = {{ params_m }}t^2 - {{ params_n }}t$

$y = {{ params_r }}t^2 - \frac{t^3}{ {{ params_p }} }$

Find the following at $t = {{ params_t }} \ \rm{s}$

## Part 1

The velocity $v$

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 2

The acceleration $a$

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)