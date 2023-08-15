---
title: Pendulum Kinetics
topic: Energy
author: Ammar Zavahir
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 9.2.1.0
- 9.2.1.1
- 6.3.1.2
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
- APSC181
- A.Z
assets:
- part1.png
- part2.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $W= $
    suffix: $\rm{J}$
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_B= $
    suffix: $\rm{m/s}$
    comparison: sigfig
    digits: 2
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $T_{max}= $
    suffix: $\rm{N}$
    comparison: sigfig
    digits: 2
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_c= $
    suffix: $\rm{N}$
    comparison: sigfig
    digits: 2
myst:
  substitutions:
    params_m: 10
    params_l: 4.9
    params_p: 700.0
    params_v: 0.0095
    params_theta: 35
---
# Pendulum Kinetics
A pendulum submerged in a fluid with the bob initially held at an angle of $\theta^{\circ}$ degrees measured from below the horizontal, is released from rest as illustrated below.

<img src="part1.png" width=600>

## Part 1

If in addition to the tension in the string and weight of the bob, a buoyant force of constant magnitude and direction acts on the bob according to the equation; $F\_{b}=\rho g V$, where $\rho$ is the fluid density, $V$ is the volume of fluid displaced, and $g$ is the gravitational acceleration. Determine the work-done by the buoyant force on the bob when it reaches point B as shown below.<br>
$\theta = {{ params_theta }}^{\circ}$, $L = {{ params_l }} \ \rm{m}$, $V\_{bob} = {{ params_v }} \ \rm{m^3}$, $\rho = {{ params_p }}\ \rm{kg.m^{-3}}$.

<img src="part2.png" width=600>

### Answer Section

Please enter in a numeric value in $\rm{N.m}$.

## Part 2

Determine the speed of the bob at point B.<br>
$m = {{ params_m }} \ \rm{kg}$.

### Answer Section

Please enter in a numeric value in $m/s$.

## Part 3

Determine the maximum tension force in the string through the pendulum motion.

### Answer Section

Please enter in a numeric value in $N$.

## Part 4

Determine the centripetal force in the string at point B.

### Answer Section

Please enter in a numeric value in $N$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)