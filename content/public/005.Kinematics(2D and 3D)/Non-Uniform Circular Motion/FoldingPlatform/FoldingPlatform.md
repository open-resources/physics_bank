---
title: Folding Platform
topic: Kinematics(2D and 3D)
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
outcomes:
- 5.6.1.0
- 5.7.1.2
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
- FoldingPlatform.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\dot{\theta}= $
    suffix: $\rm{rad/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\ddot{\theta}= $
    suffix: $\rm{rad/s^2}$
myst:
  substitutions:
    params_vars_title: Folding Platform
    params_h: 6
    params_x: 6
    params_l_dot: 0.46
    params_theta: 54
---
# {{ params_vars_title }}
A platform of length $x = {{params_x}}\ \rm{m}$ is being folded up against a wall by a rope pulling on its end.
The rope is retracting at a constant rate of $\dot{\ell} = {{params.l_dot}}\ \rm{m/s}$.
The distance between the pivot and where the rope is pulling from is $h = {{params_h}}\ \rm{m}$.

<img src="FoldingPlatform.png" width=500 alt="A platform sticking out of a wall." >

## Part 1

When $\theta = {{params_theta}}^{\circ}$, what is $\dot{\theta}$?

### Answer Section

Please enter in a numeric value in $/s$.

## Part 2

What is $\ddot{\theta}$?

### Answer Section

Please enter in a numeric value in $/s^2$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)