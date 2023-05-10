---
title: Supply plane
topic: Kinematics(2D and 3D)
author: Jake Bobowski
source: 2017 Midterm 1 (002) Q5
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 4.10.1.2
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
- AK
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.03
    weight: 1
    allow-blank: true
    label: $R= $
    suffix: $m$
    digits: 3
part2:
  type: number-input
  pl-customizations:
    rtol: 0.03
    weight: 1
    allow-blank: true
    label: $\overrightarrow{a}= $
    suffix: $m/s^2 \ \ \hat\jmath$
    digits: 3
part3:
  type: number-input
  pl-customizations:
    rtol: 0.03
    weight: 1
    allow-blank: true
    label: $V_x= $
    suffix: $m/s \ \ \hat\imath$
    digits: 3
part4:
  type: number-input
  pl-customizations:
    rtol: 0.03
    weight: 1
    allow-blank: true
    label: $V_y= $
    suffix: $m/s \ \ \hat\jmath$
    digits: 3
myst:
  substitutions:
    params_vars_title: Supply plane
    params_vars_units1: m
    params_vars_units2: $m/s^2 \ \ \hat\jmath$
    params_vars_units3: $m/s \ \ \hat\imath$
    params_vars_units4: $m/s \ \ \hat\jmath$
    params_h: 60
    params_s: 180
    params_vert: 60
---
# {{ params_vars_title }}
A supply plane needs to drop a package of food to scientists working on a glacier in Greenland.
The plane flies {{params_h}}$m$ above the glacier at a velocity of {{params_s}} $\hat\imath$ $m/s$.
The horizontal distance between the plane and the drop site is $R$ at the time the package is released from the plane.
For this question, assume that $-\hat\jmath$ (negative y) is downward and $-\hat\imath$ (negative x) is to the left, round your answers to 2 decimal places.

## Part 1

What value of $R$ is required to ensure that the package arrives on target? Neglect air resistance.

### Answer Section

Please enter in a numeric value in {{ params_vars_units1 }}.

## Part 2

What is the acceleration vector of the package after it has fallen a vertical distance of {{params_vert}}$m$? Remember to consider the sign of your answer.

### Answer Section

Please enter in a numeric value in {{ params_vars_units2 }}.

## Part 3

What is the $\hat\imath$-component of the velocity vector ($V_x$) of the package after it has fallen a vertical distance of {{params_vert}}$m$? Remember to consider the sign of your answer.

### Answer Section

Please enter in a numeric value in {{ params_vars_units3 }}.

## Part 4

What is the $\hat\jmath$-component of the velocity vector ($V_y$) of the package after it has fallen a vertical distance of {{params_vert}}$m$? Remember to consider the sign of your answer.

### Answer Section

Please enter in a numeric value in {{ params_vars_units4 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)