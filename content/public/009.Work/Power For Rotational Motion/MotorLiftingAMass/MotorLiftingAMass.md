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
    params:
      vars:
        title: Motor Lifting a Mass
      e: 0.7
      r: 0.17
      m1: 13
      m2: 7
      RPM: 25
---
# {{ params.vars.title }}
A motor with an efficiency of ${{params.e}}$ is rotating a ${{params.r}} \ \rm{m}$ radius wheel at $\dot \theta = {{params.RPM}} \ \rm{RPM}$ to lift a ${{params.m1}} \ \rm{kg}$ mass.

<img src="MotorLiftingAMass.png" height=400 alt="A motor with a wheel of radius r pulling a rope that is lifting a mass m1." >

## Part 1

How much power does the motor consume?

### Answer Section

Please enter in a numeric value in W.

## Part 2

After adding an ${{params.m2}} \ \rm{kg}$ load, you notice the wheel spins slower.
The power consumption does not change.
What is the new RPM?

### Answer Section

Please enter in a numeric value in RPM.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)