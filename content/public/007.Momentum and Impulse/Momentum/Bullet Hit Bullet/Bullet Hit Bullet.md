---
title: Bullet Hit Bullet
topic: Momentum and Impulse
author: Tarek Alkabbani
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 7.2.2.0
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
    label: $v_x= $
    suffix: m/s
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_y= $
    suffix: m/s
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_y= $
    suffix: m/s
myst:
  substitutions:
    params_vars_title: Bullet Hit Bullet
    params_vars_units: m/s
    params_v: 659
    params_theta: 80
    params_phi: 61
    params_vx: 66.81
    params_vy: 165.35
    params_vz: 621.94
    params_t1: 0.07
    params_t2: 0.06
    params_mass: 8.0
---
# {{ params_vars_title }}
We are conducting an experiment with bullets where we shoot two bullets and they collide in midair. We shoot the first bullet such that it has a velocity of $v = {{params_v}}$ m/s at an angle $\phi = {{params_phi}}^\circ$ and angle of $\theta = {{ params_theta}}^\circ$. It travels for ${{params_t1}}$ seconds and then collides with the second bullet that is travelling with the following velocity, $\vec{v} ={{params_vx}}.\widehat{\mathbf{i}}+{{params_vy}}.\widehat{\mathbf{j}}+{{params_vz}}.\widehat{\mathbf{k}}$. They are embedded together and travel a further ${{params_t2}}$ seconds. The mass of each bullet is ${{params_mass}}$ g.

Find the velocity of the bullets at that point in time. Consider that gravity acts on the z-axis and that $\phi$ is the angle between the vector and the $xy$ plane.

## Part 1

What is $v_x$?

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 2

What is $v_y$?

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 3

What is $v_z$?

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)