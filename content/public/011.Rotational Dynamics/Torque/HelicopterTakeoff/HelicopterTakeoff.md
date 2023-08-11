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
    params_vars_title: Helicpoter Takeoff
    params_vars_units_part1: s
    params_L: 9
    params_n: 2
    params_m: 54
    params_M: 4020
    params_RPM: 427
---
# {{ params_vars_title }}
A helicopter with ${{params_n}}$ blades needs to spin its rotor at ${{params_RPM}} \ \rm{RPM}$ to take off.
Each blade has a length ${{params_L}} \ \rm{m}$ and a mass of ${{params_m}}\ \rm{kg}$.
Assume the mass of the blades is uniformly distributed across its length.
The blades are initially stationary.

## Part 1

If the rotor exerts a constant moment of ${{params_M}} \ \rm{Nm}$, how much time is needed for the blades to spin fast enough for takeoff?

### Answer Section

Please enter in a numeric value in {{ params_vars_units_part1 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)