---
title: Stretched Spring
topic: Work
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
showCorrectAnswer: false
outcomes:
- 9.2.1.0
- 6.9.1.0
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
- StretchedSpring.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\Delta x= $
    suffix: $\rm{m}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $W= $
    suffix: $\rm{J}$
myst:
  substitutions:
    params:
      vars:
        title: Stretched Spring
      m: 5
      deltaX: 0.11
      k: 3070
      nu: 0.15
---
# {{ params.vars.title }}
A ${{params.m}} \ \rm{kg}$ mass is attached to a wall by a spring of spring constant ${{params.k}} \ \rm{N/m}$.
A person pulls the mass until the spring is stretched ${{params.deltaX}} \ \rm{m}$ from its rest position.
They release the mass and it springs towards the wall.

<img src="StretchedSpring.png" height=150 alt="A mass attached to a wall by spring. The spring is stretched delta x. Coefficient of friction between mass and floor is nu." >

## Part 1

Given that the kinetic coefficient of friction is ${{params.nu}}$, how far will the spring compress from its rest state?

### Answer Section

Please enter in a numeric value in m.

## Part 2

How much energy is lost to friction?

### Answer Section

Please enter in a numeric value in J.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)