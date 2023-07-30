---
title: Flywheels
topic: Rotational Dynamics
author: Firas Moosvi
source: OPUS V1 Problem 10.6.71
template_version: 1.4
attribution: openstax-physics-vol1
partialCredit: true
singleVariant: true
showCorrectAnswer: false
outcomes:
- 11.3.1.2
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
- JR
assets:
- flywheels.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_l = $
    suffix: $\rm{N}$
    comparison: sigfig
    digits: 2
myst:
  substitutions:
    params_vars_title: Flywheels
    params_Rs: 21
    params_Rl: 42
    params_Fs: 48
---
# {{ params_vars_title }}
Two flywheels of negligible mass and different radii are bonded together and rotate about a common axis (see below).

<img src="flywheels.png" width=400 alt="An image showing two concentric disks connected to each other and to a fixed axis through their centres. The smaller disk is pulled to the right by a rope connected to the top part of the disk. The larger disk is pulled to the left by a rope connected to the top part of the disk.">

## Part 1

The smaller flywheel of radius $R_s = {{ params_Rs }} \rm{cm}$ has a cord that has a pulling force of $F_s = {{ params_Fs }} \rm{N}$ on it. What pulling force $F_l$ needs to be applied to the cord connecting the larger flywheel of radius $R_l = {{ params_Rl }} \rm{cm}$ such that the combination does not rotate?

### Answer Section

Please enter a numeric value in $\rm{N}$.

## Attribution

Problem is from the [OpenStax University Physics Volume 1](https://openstax.org/details/books/university-physics-volume-1) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)