---
title: Pair of Buckets
topic: Rotational Dynamics
author: Jake Bobowski
source: 2017 Final Q18
template_version: 1.0
attribution: standard
outcomes:
- 10.5.2.3
- 11.4.1.2
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- MP
assets: null
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
    label: $m= $
    suffix: kg
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Pair of Buckets
      units: kg
    m_b: 2.0
    w0_d: 5
---
# {{ params.vars.title }}
A pair of buckets are connected by a massless rod.
As shown in the figure, the buckets rotate about an axis through the centre of mass of the two-bucket system.

<img src="q18image.png" width=400 alt="Two buckets rotating about an axis">
## Part 1

If each bucket has a mass m and the rod has length l, what is the rotational inertia of the system? Give your answer in terms of m and l. Treat the buckets as point masses and recall that I = $$ \sum\_{i} m_ir_i^2 $$

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.
## Part 2

Assume that initially the buckets rotate with angular speed $$\omega_0$$.
Then it rains for a short time.
After the rain has stopped, the buckets are observed to be rotating with angular speed $$\omega_f = \omega_0$$/{{params.w0_d}}.
How much total rain (in kg) has been collected by the pair of buckets?
When empty, the buckets each have a mass of {{params.m_b}} kg.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)