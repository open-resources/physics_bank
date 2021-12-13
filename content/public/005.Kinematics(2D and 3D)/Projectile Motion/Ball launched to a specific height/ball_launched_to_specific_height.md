---
title: Projectile of ball launched to a specific height
topic: Kinematics(2D and 3D)
author: Yousefi Peyman
source: APSC 181, Lecture 4, Q4
template_version: 1.1
attribution: standard
outcomes:
- 1.7.2.4
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- AP
- APSC 181 - LA
assets:
- L4Q4.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t_1= $
    suffix: $seconds$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t_2= $
    suffix: $seconds$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_1= $
    suffix: $ft/s$
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_2= $
    suffix: $ft/s$
substitutions:
  params:
    vars:
      title: Projectile of ball launched to a specific height
    v0: 393
    distance: 473
---
# {{ params.vars.title }}
A ball is launched vertically at Point A with an initial speed of $v = {{params.v0}} m/s$.
It passes through the Point C twice, once on the way up ($t_1$), and again on the way down ($t_2$).
Ignoring air resistance and drag, answer the following questions **relative to an observer standing** {{params.distance}} $m$ away, at Point B.

<img src="L4Q4.png" width=80%>

## Part 1

At what time $t_1$ will the line of sight make a $\theta$ = 45 $^{\circ}$ angle with the horizontal?

*Hint: The line of sight is the dotted line connecting Point B to Point C.*

### Answer Section

Please enter in a numeric value in $seconds$.

## Part 2

At what time $t_2 s$ will the line of sight make a $\theta$ = 45 $^{\circ}$ angle with the horizontal?

*Hint: The line of sight is the dotted line connecting Point B to Point C.*

### Answer Section

- Please enter in a numeric value in $seconds$.

## Part 3

Compute the magnitude of speed of the ball at $t_1 s$.

### Answer Section

Please enter in a numeric value in $m/s$.

## Part 4

Compute the magnitude of speed of the ball at $t_2 s$.

### Answer Section

Please enter in a numeric value in $m/s$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)