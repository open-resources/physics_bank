---
title: Ball Bouncing Down Ramp
topic: Momentum and Impulse
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
outcomes:
- 5.5.1.0
- 5.5.1.1
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
- BallBouncingDownRamp.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t= $
    suffix: $\rm{s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $d= $
    suffix: $\rm{m}$
myst:
  substitutions:
    params_vars_title: Ball Bouncing Down Ramp
    params_h: 3.69
    params_theta: 25
    params_e: 0.75
---
# {{ params_vars_title }}
A ball is dropped from a height ${{params_h}} \ \rm{m}$ above a ${{params_theta}}^{\circ}$ sloped ramp. The coefficient of restitution between the ball and the ramp is $e={{params_e}}$.

<img src="BallBouncingDownRamp.png" width=500 alt="A basketball dropped vertically onto a ramp." >

## Part 1

What is the flight time between the initial collision and the second time it hits the ramp?

### Answer Section

Please enter in a numeric value in s.

## Part 2

How far along the ramp did the ball travel in that bounce?

### Answer Section

Please enter in a numeric value in m.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)