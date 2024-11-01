---
title: Shooting a Pendulum
topic: Energy
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
showCorrectAnswer: false
outcomes:
- 7.5.14
- 8.2.1.0
- 8.3.2.4
- 8.5.1.1
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
- APSC181
- PJ
assets:
- ShootingAPendulum.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\theta= $
    suffix: $^\circ$
myst:
  substitutions:
    params:
      vars:
        title: Shooting a Pendulum
      L: 1.67
      m1: 0.05
      m2: 17.72
      v: 543
---
# {{ params.vars.title }}
A bullet of mass $m_1={{params.m1}} \ \rm{kg}$ is traveling at velocity $v={{params.v}} \ \rm{m/s}$.
It collides with a mass $m_2={{params.m2}} \ \rm{kg}$ hanging at rest on a rope of length $L={{params.L}} \ \rm{m}$.
Both masses combine and swing to an angle $\theta$.

<img src="ShootingAPendulum.png" width=600 alt="A bullet of mass m1 moving towards a ball of mass m2 hanging on a rope of length L. It swings to an angle theta." >

## Part 1

What is this angle?

### Answer Section

Please enter in a numeric value in $^\circ$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)