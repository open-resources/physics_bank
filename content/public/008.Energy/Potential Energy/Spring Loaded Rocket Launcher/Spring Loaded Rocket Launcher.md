---
title: Spring Loaded Rocket Launcher
topic: Energy
author: Ammar Zahavir
source: Original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes: null
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
- TA
- APSC181
assets:
- Spring Loaded Rocket Launcher.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $u_p = $
    suffix: $\rm{m/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_p = $
    suffix: $\rm{m/s}$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_r = $
    suffix: $\rm{m/s}$
myst:
  substitutions:
    params_vars_title: Spring Loaded Rocket Launcher
    params_mp: 70
    params_mr: 161
    params_k: 124
    params_x0: 11
    params_x1: 4.9
    params_e: 0.84
---
# {{ params_vars_title }}
<img src="Spring Loaded Rocket Launcher.png" width=800>

A foam rocket launcher consists of a compressed spring attached to a platform of mass $m_p$, which when released collides with a stationary rocket setting it into motion.

<br>

A simplified cross-sectional view of the launch module is shown above.

<br>

$x_0 = {{params_x0}} \ \rm{m}$, $x_1 = {{params_x1}} \ \rm{m}$, $m_p = {{params_mp}} \ \rm{kg}$, $m_r = {{params_mr}} \ \rm{kg}$, $k = {{params_k}}$.

## Part 1

If the spring is un-deformed at the point of impact $x_0$, determine the speed $u_p$ of the platform just before it hits the rocket.
<br>
Neglect the mass of the spring and any resistive forces. Assume the launcher is fixed to the ground.

### Answer Section

Please enter in a numeric value in $\rm{m/s}$.

## Part 2

If the coefficient of restitution between the two colliding surfaces is $e = {{params_e}}$, calculate the final speeds of both the rocket and the platform.
<br>
Neglect the effects of gravity and force in the spring during the duration of impact.
<br>
What is $v_p$?

### Answer Section

Please enter in a numeric value in $\rm{m/s}$.

## Part 3

What is $v_r$?

### Answer Section

Please enter in a numeric value in $\rm{m/s}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)