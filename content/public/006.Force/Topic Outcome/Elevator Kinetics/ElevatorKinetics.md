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
    params_vars_title: Elevator Kinetics
    params_vars_units: m/s$^2$
    params_m2: 417
    params_tension: 5538
    params_t: 3
---
# {{ params_vars_title }}
<img src="ElevatorKinetics.png" width=400>

At a construction site, a worker is on a moving elevator. The tension in the cable is $T = {{ params_tension }} \ \rm{N}$, within the first $t = {{ params_t }} \ \rm{s}$ of movement. If the total mass of the elevator with the worker is $m_2 = {{ params_m2 }} \ \rm{kg}$, what is the velocity of the elevator after the ${{ params_t }} \ \rm{s}$ of start up movement?

## Part 1

### Answer Section

Find the acceleration for the startup movement duration of ${{ params_t }} \ \rm{s}$.
Please enter in a numeric value in {{ params_vars_units }}.

## Part 2

Find the final velocity after ${{ params_t }} \ \rm{s}$.

Please enter in a numeric value in m/s.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)