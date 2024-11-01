---
title: Spinning A Stick
topic: Rotational Dynamics
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
outcomes:
- 7.2.3.1
- 7.2.3.3
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
- SpinningAStick.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t= $
    suffix: $\rm{s}$
myst:
  substitutions:
    params:
      vars:
        title: Spinning A Stick
      L: 2.93
      F: 66
      m: 38.1
      thetaDot: 3.89
---
# {{ params.vars.title }}
A person is trying to spin a ${{params.m}}\ \rm{kg}$ stick around its center.
The stick is initially at rest and has a length $L={{params.L}}\ \rm{m}$.
He applies a force $F={{params.F}}\ \rm{N}$ at one end of the stick.

<img src="SpinningAStick.png" width=500 alt="A stick of length L rotating about its center at theta dot." >

## Part 1

How long does it take for the stick to spin at $\dot \theta={{params.thetaDot}}\ \rm{rad/s}$?

### Answer Section

Please enter in a numeric value in s.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)