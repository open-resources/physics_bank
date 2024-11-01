---
title: Pendulum
topic: Rotational Dynamics
author: Firas Moosvi
source: OPUS V1 Problem 10.6.79
template_version: 1.4
attribution: openstax-physics-vol1
partialCredit: true
singleVariant: true
showCorrectAnswer: false
outcomes:
- 11.3.1.2
- 11.3.1.4
difficulty:
- hard
randomization:
- 5
taxonomy:
- undefined
span:
- undefined
length:
- short
tags:
- JR
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.03
    weight: 1
    allow-blank: true
    label: $\tau = $
    suffix: $\rm{N \cdot m}$
    comparison: sigfig
    digits: 3
myst:
  substitutions:
    params:
      vars:
        title: Pendulum
      mr: 0.9
      lr: 13
      ms: 0.8
      rs: 32
      theta: 35
---
# {{ params.vars.title }}
A pendulum consists of a rod of mass ${{ params.mr }}$ $\rm{kg}$ and length ${{ params.lr }}$ $\rm{m}$ connected to a pivot with a solid sphere attached at the other end with mass ${{ params.ms }}$ $\rm{kg}$ and radius ${{ params.rs }}$ $\rm{cm}$.

## Part 1

What is the torque $\tau$ about the pivot when the pendulum makes an angle of ${{ params.theta }}^\circ$ with respect to the vertical?

### Answer Section

Please enter a numeric value in $\rm{N \cdot m}$.

## Attribution

Problem is from the [OpenStax University Physics Volume 1](https://openstax.org/details/books/university-physics-volume-1) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)