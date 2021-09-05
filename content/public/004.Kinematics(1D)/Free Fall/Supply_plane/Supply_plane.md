---
title: Supply plane
topic: Free Fall
author: Jake Bobowski
source: 2017 Midterm 1 (002) Q5
template_version: 1.1
attribution: standard
outcomes:
- 4.10.1.2
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
- AK
assets: null
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $R= $
    suffix: $m$
    comparison: sigfig
    digits: 3
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\overrightarrow{a}= $
    suffix: $m/s^2 \ \ \hat\jmath$
    comparison: sigfig
    digits: 3
part3:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $V_x= $
    suffix: $m/s \ \ \hat\imath$
    comparison: sigfig
    digits: 3
part4:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $V_y= $
    suffix: $m/s \ \ \hat\jmath$
    comparison: sigfig
    digits: 3
substitutions:
  params:
    vars:
      title: Supply plane
      units1: m
      units2: $m/s^2 \ \ \hat\jmath$
      units3: $m/s \ \ \hat\imath$
      units4: $m/s \ \ \hat\jmath$
    h: 130
    s: 140
    vert: 70
---
# {{ params.vars.title }}
A supply plane needs to drop a package of food to scientists working on a glacier in Greenland.
The plane flies {{params.h}}$m$ above the glacier at a speed of {{params.s}}$m/s$.
The horizontal distance between the plane and the drop site is $R$ at the time the package is released from the plane.

## Part 1

What value of $R$ is required to ensure that the package arrives on target? Neglect air resistance.

### Answer Section

Please enter in a numeric value in {{ params.vars.units1 }}.

## Part 2

What is the acceleration vector of the package after it has fallen a vertical distance of {{params.vert}}$m$?

### Answer Section

Please enter in a numeric value in {{ params.vars.units2 }}.

## Part 3

What is the velocity vector $\hat\imath$ ($V_x$) of the package after it has fallen a vertical distance of {{params.vert}}$m$?

### Answer Section

Please enter in a numeric value in {{ params.vars.units3 }}.

## Part 4

What is the velocity vector $\hat\jmath$ ($V_y$) of the package after it has fallen a vertical distance of {{params.vert}}$m$?

### Answer Section

Please enter in a numeric value in {{ params.vars.units4 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)