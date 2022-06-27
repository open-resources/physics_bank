---
title: Jumping Frog
topic: Kinematics(2D and 3D)
author: Reza Khanbabaie
source: PHYS 112 Projectile Motion Q3
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 5.1.1.0
- 5.5.1.0
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
- PW
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t_{jump} = $
    suffix: $s$
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\Vert v_i \Vert = $
    suffix: $m/s$
    comparison: sigfig
    digits: 2
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\theta =$
    suffix: $^\circ$
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Jumping Frog
      unit1: $s$
      unit2: $m/s$
    h: 1.2
    d: 1.3
---
# {{ params.vars.title }}
A frog, initially at rest, jumps from the surface of a body of water to catch its prey. The frog reaches a maximum height of {{ params.h }} $m$ and travels a horizontal distance of {{ params.d }} $m$ before returning to the water.

## Part 1

How long was the frog in the air before returning to the water ($t\_{jump}$)?

### Answer Section

Please enter in a numeric value in {{ params.vars.unit1 }}.

## Part 2

What was the magnitude of the frog's initial velocity, $v_i$?

### Answer Section

Please enter in a numeric value in {{ params.vars.unit2 }}.

## Part 3

What was the direction of the frog's initial velocity, $v_i$, with respect to the horizontal $\theta$?

### Answer Section

Please enter in a numeric value in degrees.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)