---
title: Attempted Shot Block
topic: Momentum and Impulse
author: Peyman Yousefi
source: APSC 181, Lecture 22, Q1
template_version: 1.2
attribution: standard
outcomes:
- 7.6.1.2
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
- APSC 181 - LA
- JR
assets:
- Attempted Shot Block.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\theta_1= $
    suffix: $^{\circ}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\theta_2= $
    suffix: $^{\circ}$
substitutions:
  params:
    vars:
      title: Attempted Shot Block
    thetad: 16
    e: 0.9
---
# {{ params.vars.title }}
<img src="Attempted Shot Block.png" width=400>

As one basketball player throws a warmup shot, another one tries to throw a ball to block it.
The balls collide above the hoop as shown in the diagram above.
Before the collision, $v_1$ has a velocity $\theta_2= {{params.thetad}}^\circ$ above the horizontal.
The second ball has a velocity equal in magnitude at an angle $\theta_1$.
Determine the two possible values of $\theta_1$ which will cause Ball 1 to go directly into the hoop instead of blocking it.
The coefficient of restitution is ${{params.e}}$.

## Part 1

Enter the larger angle

### Answer Section

Please enter in a numeric value in $^\circ$.

## Part 2

Enter the smaller angle

### Answer Section

Please enter in a numeric value in $^\circ$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)