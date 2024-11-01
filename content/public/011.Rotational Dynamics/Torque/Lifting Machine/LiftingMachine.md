---
title: Lifting Machine
topic: Rotational Dynamics
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
outcomes:
- 5.9.1.0
- 6.6.1.2
- 11.3.1.0
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
- LiftingMachine.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $\rm{m/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F= $
    suffix: $\rm{N}$
myst:
  substitutions:
    params:
      vars:
        title: Lifting Machine
      r1: 0.3
      r2: 0.06
      r3: 0.19
      r4: 0.09
      thetaDot: 5
      m: 56
---
# {{ params.vars.title }}
The machine illustrated below lifts a mass m by turning a pedal with radius $r_1 = {{params.r1}} \ \rm{m}$.
The pedal rotates a gear system, which pulls a rope along a pulley system that is lifting a mass of ${{params.m}} \ \rm{kg}$.
$r_2 = {{params.r2}} \ \rm{m}$  $r_3 = {{params.r3}} \ \rm{m}$  $r_4 = {{params.r4}} \ \rm{m}$.

<img src="LiftingMachine.png" width=600 alt="A mass is suspended on a double pulley system. The rope is pulled by a large gear with r3, which is spun by a smaller gear with r2. The smaller gear is spun with a pedal of r1. The rope makes contact with the larger gear at r4." >

## Part 1

If the pedal is rotated at ${{params.thetaDot}} \ \rm{rad/s}$, how fast is the mass rising?

### Answer Section

Please enter in a numeric value in m/s.

## Part 2

Find the minimum force required to lift the mass at a constant velocity.

### Answer Section

Please enter in a numeric value in N.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)