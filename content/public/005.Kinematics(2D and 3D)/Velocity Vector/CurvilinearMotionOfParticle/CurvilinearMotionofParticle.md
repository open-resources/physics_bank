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
    params:
      vars:
        title: Particle Curvilinear Motion
        units: m/s
      m: 5
      n: 3
      r: 6
      p: 4
      t: 1
---
# {{ params.vars.title }}
A particle moves in a curvilinear motion according to the following equations:

$x = {{ params.m }}t^2 - {{ params.n }}t$

$y = {{ params.r }}t^2 - \frac{t^3}{ {{ params.p }} }$

Find the following at $t = {{ params.t }} \ \rm{s}$

## Part 1

The velocity $v$

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

The acceleration $a$

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)