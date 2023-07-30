---
title: Motor Lifting a Mass
topic: Work
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
outcomes:
- 9.3.1.1
- 9.5.1.0
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
- MotorLiftingAMass.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $P= $
    suffix: $\rm{W}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\dot \theta= $
    suffix: $\rm{RPM}$
myst:
  substitutions:
    params_vars_title: Motor Lifting a Mass
    params_e: 0.66
    params_r: 0.29
    params_m1: 18
    params_m2: 4
    params_RPM: 22
---
# {{ params_vars_title }}
A motor with an efficiency of ${{params_e}}$ is rotating a ${{params_r}} \ \rm{m}$ radius wheel at $\dot \theta = {{params_RPM}} \ \rm{RPM}$ to lift a ${{params_m1}} \ \rm{kg}$ mass.

<img src="MotorLiftingAMass.png" height=400 alt="A motor with a wheel of radius r pulling a rope that is lifting a mass m1." >

## Part 1

How much power does the motor consume?

### Answer Section

Please enter in a numeric value in W.

## Part 2

After adding an ${{params_m2}} \ \rm{kg}$ load, you notice the wheel spins slower.
The power consumption does not change.
What is the new RPM?

### Answer Section

Please enter in a numeric value in RPM.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)