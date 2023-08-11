---
title: Slingshot
topic: Energy
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
outcomes:
- 6.11.2.1
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
- Slingshot.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_T= $
    suffix: $\rm{N}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $\rm{m/s}$
myst:
  substitutions:
    params_vars_title: Slingshot
    params_K: 133
    params_d: 0.87
    params_x0: 0.23
    params_m: 7
---
# {{ params_vars_title }}
A slingshot made of two springs with spring constant ${{params_K}} \ \rm{N/m}$ is loaded with a mass $m={{params_m}} \ \rm{kg}$.
When relaxed, the springs have a length $x_0={{params_x0}} \ \rm{m}$.
Using a rope, someone pulls the mass $d={{params_d}} \ \rm{m}$ from its rest state.

<img src="Slingshot.png" width=600 alt="Two springs are diagonally pulled back with a horizontal force that holds the center of the slingshot a distance d from its rest state." >

## Part 1

How much tension is in the rope?

### Answer Section

Please enter in a numeric value in $N$.

## Part 2

If the rope is cut, with what speed does the mass leave the slingshot?
Assume all the energy in the springs is transferred to the mass.

### Answer Section

Please enter in a numeric value in $m/s$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)