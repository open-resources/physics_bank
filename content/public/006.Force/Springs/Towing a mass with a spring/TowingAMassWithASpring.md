---
title: Towing a Mass With a Spring
topic: Force
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
outcomes:
- 6.11.2.1
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
- TowingAMassWithASpring.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $k= $
    suffix: $\rm{N/m}$
myst:
  substitutions:
    params:
      vars:
        title: Towing a Mass With a Spring
      m: 34
      x: 0.49
      L: 0.56
      nu: 0.4
      a: 2.97
---
# {{ params.vars.title }}
A person accelerates a ${{params.m}} \ \rm{kg}$ mass at ${{params.a}} \ \rm{m/s^2}$ by pulling on a spring that is ${{params.x}} \ \rm{m}$ long at rest.
The coefficient of friction between the two surfaces is ${{params.nu}}$.

<img src="TowingAMassWithASpring.png" height=150 alt="A rectangular mass m being dragged by a string of length L with a force F." >

## Part 1

If the spring extends to ${{params.L}} \ \rm{m}$, what is the spring constant $k$?

### Answer Section

Please enter in a numeric value in N/m.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)