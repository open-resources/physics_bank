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
    suffix: $\rm{m/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_y= $
    suffix: $\rm{m/s}$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_y= $
    suffix: $\rm{m/s}$
myst:
  substitutions:
    params:
      vars:
        title: Bullet Hit Bullet
        units: m/s
      v: 539
      theta: 74
      phi: 80
      vx: 208.22
      vy: 391.61
      vz: 528.57
      t1: 0.05
      t2: 0.05
      mass: 9.0
---
# {{ params.vars.title }}
We are conducting an experiment with bullets where we shoot two bullets and they collide in midair. We shoot the first bullet such that it has a velocity of $v = {{params.v}}\ \rm{m/s}$ at an angle $\phi = {{params.phi}}^\circ$ and angle of $\theta = {{ params.theta}}^\circ$. It travels for ${{params.t1}}$ seconds and then collides with the second bullet that is travelling with the following velocity, $\vec{v} ={{params.vx}}.\widehat{\mathbf{i}}+{{params.vy}}.\widehat{\mathbf{j}}+{{params.vz}}.\widehat{\mathbf{k}}$. They are embedded together and travel a further ${{params.t2}}$ seconds. The mass of each bullet is ${{params.mass}}\ \rm{g}$.

Find the velocity of the bullets at that point in time. Consider that gravity acts on the $z$-axis and that $\phi$ is the angle between the vector and the $xy$ plane.

## Part 1

What is $v_x$?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

What is $v_y$?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 3

What is $v_z$?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)