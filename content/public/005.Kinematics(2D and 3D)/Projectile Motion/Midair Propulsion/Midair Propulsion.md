---
title: Midair Propulsion
topic: Kinematics(2D and 3D)
author: Tarek Alkabbani
source: original
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 5.5.1.1
- 5.5.1.3
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
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $y= $
    suffix: m
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t= $
    suffix: s
    comparison: sigfig
    digits: 2
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 4
    allow-blank: true
    label: $x= $
    suffix: m
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Midair Propulsion
      time_units: s
      dist_units: m
      velo_units: m/s
      acc_units: m/s^2
    v: 28
    theta: 39
    N: 2
    C: 5.505713978682579
---
# {{ params.vars.title }}
We launch a projectile at an angle {{ params.theta }} in degrees and speed {{ params.v }} in {{ params.vars.velo_units }} in a flat plane. At the peak of the projectile motion, a rocket turns on and starts accelerating the projectile in the x-axis according to the function $a(t) = {{ params.C }} \times t^{{{ params.N }} }$ in {{ params.vars.acc_units}}. Find the range it travels over the flight duration.

## Part 1

What is the maximum height the projectile will reach in {{ params.vars.dist_units }}?

### Answer Section

Please enter in a numeric value in {{ params.vars.dist_units }}.

## Part 2

How long will it take the projectile to reach this height in {{ params.vars.time_units }}?

### Answer Section

Please enter in a numeric value in {{ params.vars.time_units }}.

## Part 3

What is the range of travel for the projectile in {{ params.vars.dist_units }}?

### Answer Section

Please enter in a numeric value in {{ params.vars.dist_units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)