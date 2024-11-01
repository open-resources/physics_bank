---
title: Crate Down Ramp
topic: Force
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.9.1.3
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
- CrateDownRamp.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a= $
    suffix: $\rm{m/s^2}$
myst:
  substitutions:
    params:
      vars:
        title: Crate Down Ramp
      nu: 0.25
      theta: 37
      m: 15
      T: 41
---
# {{ params.vars.title }}
A ${{params.m}} \ \rm{kg}$ crate is sliding down a ${{params.theta}}^{\circ}$ slope. A man attempts to stop it by pulling uphill on a rope parallel to the slope.
<img src="CrateDownRamp.png" width=800 alt="A man pulling a crate up a slope using a rope." >

## Part 1

If the coefficient of kinetic friction is ${{params.nu}}$ and the tension of the rope is ${{params.T}} \ \rm{N}$, what is the acceleration of the block?
Enter a negative number if the crate accelerates downwards.

### Answer Section

Please enter in a numeric value in m/s^2.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)