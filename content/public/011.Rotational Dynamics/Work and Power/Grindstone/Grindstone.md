---
title: Grindstone
topic: Rotational Dynamics
author: Firas Moosvi
source: OPUS V1 Problem 10.8.99
template_version: 1.4
attribution: openstax-physics-vol1
partialCredit: true
singleVariant: true
showCorrectAnswer: false
outcomes:
- 9.2.1.2
- 10.5.2.2
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
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $K_{\text{rot}} = $
    suffix: $\rm{J}
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $N = $
    suffix: $\rm{turns}$
    comparison: sigfig
    digits: 2
myst:
  substitutions:
    params:
      vars:
        title: Grindstone
      M: 11.0
      R: 12
      RPM: 1467
      F: 6.0
      mu: 0.78
---
# {{ params.vars.title }}
A uniform cylindrical grindstone has a mass of ${{ params.M }} \rm{kg}$ and a radius of ${{ params.R }} \rm{cm}$.

## Part 1

What is the rotational kinetic energy $K\_{\text{rot}}$ of the grindstone when it is rotating at ${{ params.RPM }} \rm{rev/min}$?
You may assume that the grindstone is a solid cylinder rotating about its cylinder axis.

### Answer Section

Please enter a numeric value in $\rm{J}$.

## Part 2

After the grindstone's motor is turned off, a knife blade is pressed against the outer edge of the grindstone with a perpendicular force of ${{ params.F }} \rm{N}$.
The coefficient of kinetic friction between the grindstone and the blade is ${{ params.mu }}$.
Use the work energy theorem to determine how many turns $N$ the grindstone makes before it stops.

### Answer Section

Please enter a numeric value.

## Attribution

Problem is from the [OpenStax University Physics Volume 1](https://openstax.org/details/books/university-physics-volume-1) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)