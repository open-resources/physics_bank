---
title: Frictionless Ski Jump Collision
topic: Template
author: Firas Moosvi
source: original
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes: null
difficulty:
- hard
randomization:
- undefined
taxonomy:
- undefined
span:
- undefined
length:
- undefined
tags:
- unknown
assets:
- skijump.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_B= $
    suffix: m/s
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: m
substitutions:
  params:
    vars:
      name: Mateo
      title: Frictionless Ski Jump Collision
      units1: m/s
      units2: m
    mA: 29
    mB: 22.62
    ramp_angle: 43
    ramp_h: 0.04
    jump_h: 419
---
# {{ params.vars.title }}
A frictionless ski jump is designed such that at the bottom of the hill, there is a short flat section.

After the flat section, the slope continues into a ramp of vertical height {{ params.ramp_h }} m, at an angle {{ params.ramp_angle }} degrees (relative to the horizontal).

The top of the ski jump is {{ params.jump_h }} {{ params.vars.units2 }} high off the ground.

Block A of mass {{ params.mA }}kg is released from the top of the slope so that it slides down and makes a perfectly elastic collision with Block B of mass {{ params.mB }}kg.
This causes the Block B to slide up the frictionless ramp and undergo projectile motion, before landing a horizontal distance $x$ {{ params.vars.units2 }} away from the ramp.

<img src="skijump.png" width=100%>

## Part 1

What is the speed of Block B (in {{ params.vars.units1 }}), immediately after the perfectly elastic collision?

### Answer Section

Please enter in a numeric value in m/s.

## Part 2

What is the horizontal distance (in {{ params.vars.units2 }}) that Block B travels after it goes off the ramp ($x$)?

### Answer Section

Please enter in a numeric value in m.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)