---
title: Springs on a Disk
topic: Force
author: Peyman Yousefi
source: APSC 181, Lecture 16, Q1
template_version: 1.2
attribution: standard
outcomes:
- 6.1.1.8
difficulty:
- hard
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- APSC 181 - LA
- JR
assets:
- Springs On a Disk.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: m
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $N= $
    suffix: $N$
substitutions:
  params:
    vars:
      title: Springs on a Disk
    w: 167
    d: 59
    k: 398
    m: 0.2
    x: 21
---
# {{ params.vars.title }}
<img src="Springs On a Disk.png" width=400>

A flat disk rotates around a tube in its vertical axis, with a rotational speed of $\omega= {{ params.w }}rev/min$. Prior to rotation, each of the ${{ params.m }}kg$ sliding blocks has the position $x = {{ params.x }}mm$ with no force in the spring. The springs both have stiffness of ${{ params.k }}N/m$. Answer the following questions with the given information. Neglect friction and the mass of the springs. $d = {{ params.d }}mm$

## Part 1

Determine the value of $x$ for the springs once rotation has begun.

### Answer Section

Please enter in a numeric value in metres.

## Part 2

Find the normal force $N$ exerted by the side of the slot on the block.

### Answer Section

Please enter in a numeric value in Newtons.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)