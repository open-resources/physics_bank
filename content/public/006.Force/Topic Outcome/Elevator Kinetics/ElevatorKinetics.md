---
title: Elevator Kinetics
topic: Force
author: Ranya Ghosh
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.5.1.3
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
- RG
- JR
- APSC181
assets:
- ElevatorKinetics.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a= $
    suffix: $\rm{m/s^2}$
    comparison: sigfig
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $\rm{m/s}$
    comparison: sigfig
myst:
  substitutions:
    params:
      vars:
        title: Elevator Kinetics
        units: m/s$^2$
      m2: 403
      tension: 6357
      t: 4
---
# {{ params.vars.title }}
<img src="ElevatorKinetics.png" width=400>

At a construction site, a worker is on a moving elevator. The tension in the cable is $T = {{ params.tension }} \ \rm{N}$, within the first $t = {{ params.t }} \ \rm{s}$ of movement. If the total mass of the elevator with the worker is $m = {{ params.m2 }} \ \rm{kg}$, what is the velocity of the elevator after the ${{ params.t }} \ \rm{s}$ of start up movement?

## Part 1

### Answer Section

Find the acceleration for the startup movement duration of ${{ params.t }} \ \rm{s}$.
Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

Find the final velocity after ${{ params.t }} \ \rm{s}$.

Please enter in a numeric value in m/s.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)