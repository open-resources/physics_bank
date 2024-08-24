---
title: Tetherball
topic: Kinematics(2D and 3D)
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
outcomes:
- 5.6.3.0
- 5.6.2.0
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
- Tetherball.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\theta= $
    suffix: $^\circ$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $f= $
    suffix: $\rm{rev/s}$
myst:
  substitutions:
    params:
      vars:
        title: Tetherball serve
        units:
          part1: "$\theta$"
          part2: "$\rm{/s}$"
      v: 13
      L: 10
---
# {{ params.vars.title }}
Two friends are playing tetherball. The ball is tethered to a pole by a rope of length $L = {{params.L}} \ \rm{ft}$. The first player serves with a velocity $v = {{params.v}} \ \rm{m/s}$.

<img src="Tetherball.png" width=500 alt="A ball attached to a pole via rope angled theta degrees." >

## Part 1

What angle $\theta$ does the rope make with the pole?

### Answer Section

Please enter in a numeric value in ${{ params.vars.units.part1 }}$.

## Part 2

At this speed, how many times per second would the ball go around the pole?

### Answer Section

Please enter in a numeric value in ${{ params.vars.units.part2 }}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)