---
title: Frictionless Ski Jump Collision
topic: Template
author: Firas Moosvi
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes: null
difficulty:
- hard
randomization:
- 5
taxonomy:
- undefined
span:
- undefined
length:
- medium
tags:
- JR
assets:
- skijump.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_B = $
    suffix: $\rm{m/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.03
    weight: 1
    allow-blank: true
    label: $x = $
    suffix: $\rm{m}$
myst:
  substitutions:
    params:
      vars:
        name: Mateo
        title: Frictionless Ski Jump Collision
      mA: 15
      mB: 7.2
      ramp_angle: 32
      ramp_h: 0.63
      hill_h: 438
---
# {{ params.vars.title }}
A ski jump consists of a hill, a short flat section, and a ramp. The hill has height of ${{ params.hill_h }}$ $\rm{m}$ and the ramp has a height of ${{ params.ramp_h }}$ $\rm{m}$, making an angle of $\theta = {{ params.ramp_angle }}^\circ$ with the horizontal.

Block A of mass $m_A = {{ params.mA }}$ $\rm{kg}$ is released from rest at the top of the frictionless hill and slides down to the frictionless short flat section, where it undergoes a perfectly elastic collision with Block B of mass $m_B = {{params.mB }}$ $\rm{kg}$. This causes Block B to slide up the frictionless ramp and undergo projectile motion, before landing a horizontal distance $x$ away from the ramp at the same height as the short flat section.

<img src="skijump.png" width=100%>

## Part 1

What is the speed of Block B immediately after the perfectly elastic collision?

### Answer Section

Please enter in a numeric value in $\rm{m/s}$.

## Part 2

What is the horizontal distance that Block B travels after it goes off the ramp ($x$)?

### Answer Section

Please enter in a numeric value in $\rm{m}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)