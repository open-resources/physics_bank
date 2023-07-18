---
title: Decelerating Mass
topic: Momentum and Impulse
author: Patrick Jilek-Rodriguez
source: WebWork
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
outcomes:
- 7.5.1.4
- 7.5.1.9
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
- DeceleratingMass.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $m= $
    suffix: $\rm{kg}$
myst:
  substitutions:
    params_vars_title: Decelerating Mass
    params_k: 5
    params_t: 7
    params_v: 18
---
# {{ params_vars_title }}
An object is traveling with a speed of ${{params_v}}\ \rm{m/s}$.
At $t = 0$, a force whose magnitude follows the relation $F = {{params_k}}t \ \rm{N}$ is applied in the direction opposite to motion.

<img src="DeceleratingMass.png" width=500 alt="A box moving to the right at speed v. A force F is stopping it." >

## Part 1

If the object decelerates to a complete stop in ${{params_t}} \ \rm{s}$, what is its mass?

### Answer Section

Please enter in a numeric value in kg.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)