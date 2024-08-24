---
title: Helicopter Takeoff
topic: Rotational Dynamics
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
showCorrectAnswer: false
outcomes:
- 7.5.3.0
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
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t= $
    suffix: $ \rm{s}$
myst:
  substitutions:
    params:
      vars:
        title: Helicpoter Takeoff
        units:
          part1: s
      L: 12
      n: 4
      m: 108
      M: 1540
      RPM: 464
---
# {{ params.vars.title }}
A helicopter with ${{params.n}}$ blades needs to spin its rotor at ${{params.RPM}} \ \rm{RPM}$ to take off.
Each blade has a length ${{params.L}} \ \rm{m}$ and a mass of ${{params.m}}\ \rm{kg}$.
Assume the mass of the blades is uniformly distributed across its length.
The blades are initially stationary.

## Part 1

If the rotor exerts a constant moment of ${{params.M}} \ \rm{Nm}$, how much time is needed for the blades to spin fast enough for takeoff?

### Answer Section

Please enter in a numeric value in {{ params.vars.units.part1 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)