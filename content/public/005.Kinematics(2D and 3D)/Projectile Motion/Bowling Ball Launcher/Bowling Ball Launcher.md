---
title: Bowling Ball Launcher
topic: Kinematics(2D and 3D)
author: Tarek Alkabbani
source: WebWork
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.5.1.1
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
- TA
assets:
- Bowling Ball Launcher.jpg
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: $\rm{m}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $y= $
    suffix: $\rm{m}$
myst:
  substitutions:
    params_L: 2.9
    params_theta: 304
    params_omega: 287
    params_t: 4.2
---
# Projectile Motion on an Incline
A robot holds a bowling ball that is spun at a rate of ${{ params_omega }} \ \rm{rpm}$ CCW in a plane perpendicular to the ground. The robot arm is ${{params_L}} \ \rm{m}$ long.
At $t=0 \ \rm{s}$, the bowling ball is released such that the arm makes an angle $\theta = {{params_theta}}^{\circ}$ with the positive x-axis.

<img src="Bowling Ball Launcher.jpg" width=600>

## Part 1

Determine the position of the bowling ball after $t={{params_t}} \ \rm{s}$
Treat the ball as a particle and neglect any resistive forces.

### Answer Section

Please enter the poistion in $\rm{m}$.

## Part 2

### Answer Section

Please enter the poistion in $\rm{m}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)