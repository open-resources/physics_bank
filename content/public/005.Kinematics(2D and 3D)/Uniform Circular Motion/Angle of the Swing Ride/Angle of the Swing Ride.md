---
title: Angle of the Swing Ride
topic: Kinematics(2D and 3D)
author: Tarek Alkabbani
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 5.6.3.0
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
- TA
- APSC181
assets:
- part1.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\theta= $
    suffix: $^{\circ} $
myst:
  substitutions:
    params:
      vars:
        name: Maya
        title: Angle of the Swing Ride
        units: degrees
      omega: 2.71
      d: 7.6
      m: 87
---
# {{ params.vars.title }}
<img src = "part1.png" width=600>

A person is on a swing ride, rotating at a $\omega = {{ params.omega}}\ \rm{rad/s}$. The combined mass of the person and the seat is $m = {{ params.m }}\ \rm{kg}$. The length of the cable connecting the seat to the ride is $ d =$ ${{ params.d}}\ \rm{m}$.

## Part 1

What is the angle $\theta$ in degrees?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)