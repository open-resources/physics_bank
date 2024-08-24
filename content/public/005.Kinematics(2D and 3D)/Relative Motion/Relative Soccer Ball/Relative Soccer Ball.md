---
title: Relative Soccer Ball
topic: Kinematics(2D and 3D)
author: Tarek Alkabbani
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.8.1.3
- 7.3.1.3
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
assets:
- Relative Soccer Ball.jpg
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_x= $
    suffix: $\rm{N}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_y= $
    suffix: $\rm{N}$
myst:
  substitutions:
    params:
      vars:
        title: Relative Soccer Ball
        units: N
      m: 0.44
      vp: 3.38
      theta: 30
      t: 0.015
      vbp: 13.46
      vy: 17.55
      vx: 19.94
---
# {{ params.vars.title }}
<img src="Relative Soccer Ball.jpg" width=700>

A football player is running up the soccer field at a velocity ${{params.vp}}\ \rm{m/s}$. A ball that has mass $m = {{params.m}}\ \rm{kg}$ is passed their way, and just before the player shoots the ball they observe that the ball is moving at a speed of ${{params.vbp}} \ \rm{m/s}$ and angle $\theta = {{params.theta}}^\circ$ relative to their motion.

Their foot is in contact with the ball for ${{params.t}}$ seconds and it imparted a change of velocity such that the absolute velocity now is $v_x = {{params.vx}} \ \rm{m/s}$ and  $v_y = {{params.vy}}\ \rm{m/s}$.

Find the average force components needed for this kick.

## Part 1

What is the x-component of the average force?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

What is the y-component of the average force?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)