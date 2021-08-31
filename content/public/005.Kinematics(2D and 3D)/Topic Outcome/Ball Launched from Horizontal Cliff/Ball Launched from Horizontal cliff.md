---
title: Ball Launched from a Horizontal Cliff
topic: Kinematics(2D and 3D)
author: Jake Bobowski
source: 2012 Midterm 1 Q5 Section 002
template_version: 1.1
attribution: standard
outcomes:
- 5.1.1.0
- 5.5.1.0
- 5.5.1.2
- 4.1.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- PW
assets:
- q5_2012Mid1_002.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $t= $
    suffix: $s$
    comparison: sigfig
    digits: 3
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\theta= $
    suffix: rad
    comparison: sigfig
    digits: 3
part3:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    suffix: $\hat{\imath} \; (m/s)$
    comparison: sigfig
    digits: 3
part4:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    suffix: $\hat{\jmath} \; (m/s)$
    comparison: sigfig
    digits: 3
substitutions:
  params:
    vars:
      title: Ball Launched from a Horizontal Cliff
      unit1: $s$
      unit2: rad
      unit3: $m/s$
    v0: 2.37
    h: 67.6
---
# {{ params.vars.title }}
A small ball is launched from a horizontal cliff with initial speed {{ params.v0 }} $m/s$. The side of the cliff is sloped. The ball makes contact with the cliff side after falling a vertical distance of {{ params.h }} cm.

![Figure of a ball launched from a horizontal cliff with a sloped side. Theta is the angle between the sloped side and the vertical line going through the point where the slope starts.](q5_2012Mid1_002.png)

## Part 1

How long was the ball in the air before hitting the side of the cliff?

### Answer Section

Please enter in a numeric value in {{ params.vars.unit1 }}.

## Part 2

What is the value of the angle $\theta$ shown in the figure?

### Answer Section

Please enter in a numeric value in {{ params.vars.unit2 }}.

## Part 3

What is the velocity of the ball just before hitting the side of the cliff? Give your final answer in terms of the $x$- and $y$-components of the velocity and the unit vectors $\hat{\imath}$ and $\hat{\jmath}$.

Please enter the coefficient of $\hat{\imath}$ (in $m/s$).

### Answer Section

Please enter in a numeric value in {{ params.vars.unit3 }}.

## Part 4

What is the velocity of the ball just before hitting the side of the cliff? Give your final answer in terms of the $x$- and $y$-components of the velocity and the unit vectors $\hat{\imath}$ and $\hat{\jmath}$.

Please enter the coefficient of $\hat{\jmath}$ (in $m/s$).

### Answer Section

Please enter in a numeric value in {{ params.vars.unit3 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)