---
title: Crane and Construction Worker
topic: Force
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
outcomes:
- 6.1.1.4
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
- CraneAndConstructionWorker.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a= $
    suffix: $\rm{m/s^2}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\alpha= $
    suffix: $^{\circ}$
myst:
  substitutions:
    params_vars_title: Crane and Construction Worker
    params_m: 132
    params_F_crane: 1758
    params_F_worker: 173
    params_theta: 28
---
# {{ params_vars_title }}
A crane is lifting a ${{params_m}} \ \rm{kg}$ block.
The tension on the crane's rope is ${{params.F_crane}} \ \rm{N}$.
A construction worker guides the object using a rope angled $\theta={{params_theta}}^{\circ}$ from the vertical.
The worker pulls the rope with a force of ${{params.F_worker}} \ \rm{N}$.

<img src="CraneAndConstructionWorker.png" width=251 alt="A block is pulled upwards with a rope. A man pulls diagonally downwards on a rope attached to the block." >

## Part 1

What is the magnitude of the acceleration of the block?

### Answer Section

Please enter in a numeric value in $m/s^2$.

## Part 2

What angle $\alpha$ from the horizontal is the acceleration?

### Answer Section

Please enter in a numeric value in $^{\circ}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)