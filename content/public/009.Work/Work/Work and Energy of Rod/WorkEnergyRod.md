---
title: Work and Energy of a Rod
topic: Work
author: Ranya Ghosh
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- null
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
assets:
- WorkEnergyRod.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\omega = $
    suffix: $\rm{rad/s}$
    comparison: sigfig
    digits: 2
myst:
  substitutions:
    params:
      vars:
        title: Work and Energy of a Rod
        units: rad/s
      m: 4
      L: 8
      F: 190
---
# {{ params.vars.title }}
<img src="WorkEnergyRod.png" width=400>

A rod with a mass of $m = {{ params.m }} \ \rm{kg}$ and length $l = {{ params.L }} \ \rm{m}$ hangs at rest when the force $F = {{ params.F }} \ \rm{N}$ is applied.

## Part 1

Find the angular velocity of the rod when it has rotated $90^{\circ}$ clockwise.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)