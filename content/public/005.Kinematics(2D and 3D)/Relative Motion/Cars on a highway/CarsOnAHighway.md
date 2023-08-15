---
title: Cars on a Highway
topic: Kinematics(2D and 3D)
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
outcomes:
- 5.8.1.3
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
- CarsOnAHighway.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\dot \theta= $
    suffix: $ \rm{^\circ/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\ddot \theta= $
    suffix: $ \rm{^\circ/s^2}$
myst:
  substitutions:
    params_vars_title: Cars on a Highway
    params_l: 15
    params_d: 68
    params_va: 98
    params_vb: 82
---
# {{ params_vars_title }}
Two cars are driving at constant speeds on two parallel opposing lanes of a divided highway.
The lanes are $L = {{params_l}} \ \rm{m}$ apart and the cars are $d = {{params_d}} \ \rm{m}$ away from each other.
Car $A$ is traveling at ${{params_va}} \ \rm{km/h}$ and car $B$ at ${{params_vb}} \ \rm{km/h}$.

<img src="CarsOnAHighway.png" width=800 alt="Two cars are driving on opposite roads towards each other. The roads are L distance away from each other." >

## Part 1

If $\theta$ is the angle between the road and a line connecting the cars, what is $\dot \theta$?

### Answer Section

Please enter in a numeric value in $\rm{^\circ/s}$.

## Part 2

What is $\ddot \theta$?

### Answer Section

Please enter in a numeric value in $\rm{^\circ/s^2}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)