---
title: Shopping Cart Push
topic: Momentum and Impulse
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
outcomes:
- 6.1.1.4
- 6.1.1.6
- 6.4.1.1
- 7.3.1.3
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
    label: $d= $
    suffix: $\rm{m}$
myst:
  substitutions:
    params:
      vars:
        title: Shopping Cart Push
        units: m
      m1: 59
      m2: 15
      t: 2.2
      F: 444
      C: 0.1
---
# {{ params.vars.title }}
Two teenagers are playing with a shopping cart in a parking lot.
One teenager begins pushing their ${{ params.m1 }} \  \rm{kg}$ friend on the ${{ params.m2 }} \ \rm{kg}$ cart with a maximum force of $F\_{max} = {{ params.F }} \ \rm{N}$.
The magnitude of the force decreases linearly to $0 \ \rm{N}$ until the cart is released after ${{ params.t }} \ \rm{s}$.

## Question Text

If the rolling resistance coefficient of the cart is $C\_{rr} = {{ params.C }}$, how far does the cart travel from release?

Note that the rolling resistance force is analogous to the force of friction, where $F\_{rr}$ = $C\_{rr}$$F_N$ and acts in the direction opposite of motion.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)