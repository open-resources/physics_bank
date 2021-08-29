---
title: Rotating Buckets
topic: Momentum and Impulse
author: Jake Bobowski
source: 2015 Final Q18
template_version: 1.1
attribution: standard
outcomes:
- 7.2.3.1
- 7.5.3.1
- 11.4.1.1
- 10.5.2.3
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- PW
assets:
- 2015FinalQ18.png
part1:
  type: symbolic-input
  label: $I = $
  pl-customizations:
    variables: m, l
    weight: 1
    allow-blank: false
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $m_{rain}= $
    suffix: kg
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Rotating Buckets
      units: kg
    m1: 2.85
    c: 4
---
# {{ params.vars.title }}
A pair of buckets are connected by a *massless* rod. As shown in the figure, the buckets rotate about an axis through the centre of mass of the two-bucket system.

![Two buckets connected by a rod rotating anti-clockwise.](2015FinalQ18.png)

## Part 1

If each bucket has a mass $m$ and the rod has length $l$, what is the rotational inertia of the system? Give your answer in terms of $m$ and $l$. Treat the buckets as point masses and recall that $I = \sum\limits_i m_ir_i^2$.

Note that it may not be necessary to use every variable. Use the following table as a reference for each variable:

| $Variable$ | Use   |
|----------|-------|
| $m$  | m  |
| $l$  | l  |

### Answer Section

{{ substitutions.part1.label }}

## Part 2

Assume that initially the buckets rotate with angular speed $\omega_0$. Then it rains for a short time. After the rain has stopped, the buckets are observed to be rotating with angular speed $\omega_f = \omega/${{ params.c}}. How much rain (in kg) has been collected by the two buckets? When empty, the buckets each have a mass of {{ params.m1 }} kg.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)