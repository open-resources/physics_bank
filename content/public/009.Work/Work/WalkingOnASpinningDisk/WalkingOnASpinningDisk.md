---
title: Walking on a Spinning Disk
topic: Work
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.6.3.0
- 9.1.1.1
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
- WalkingOnASpinningDisk.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $W= $
    suffix: $\rm{J}$
myst:
  substitutions:
    params_vars_title: Walking on a Spinning Disk
    params_m: 65
    params_r1: 1
    params_r2: 0.23
    params_theta_dot: 1
---
# {{ params_vars_title }}
A ${{params_m}}\ \rm{kg}$ man is walking at a constant speed towards the center of a platform spinning at a constant rate of ${{params.theta_dot}} \ \rm{rad/s}$.

<img src="WalkingOnASpinningDisk.png" width=500 alt="A disk with a mass at distance r1 from the center. The mass moves closer to the center, where the radius is r2." >

## Part 1

If his initial distance from the center is $r_1={{params_r1}} \ \rm{m}$, and he moves to a new location where $r={{params_r2}}\ \rm{m}$, how much work did he do?

### Answer Section

Please enter in a numeric value in J.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)