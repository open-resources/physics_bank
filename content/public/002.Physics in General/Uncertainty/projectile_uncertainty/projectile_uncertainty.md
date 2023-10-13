---
title: Projectile Uncertainty
topic: Physics in General
author: Jake Bobowski
source: 2017 Final Q19
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 2.4.1.1
- 2.4.1.2
difficulty:
- hard
randomization:
- 0
taxonomy:
- undefined
span:
- multi-chapter
length:
- long
tags:
- MP
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_o= $
    suffix: m/s
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\Delta d= $
    suffix: m
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\Delta v_o= $
    suffix: m/s
myst:
  substitutions:
    params_vars_title: Projectile Uncertainty
    params_vars_name: Mateo
    params_vars_units1: m/s
    params_vars_units2: m
    params_d: 0.126
    params_s: 0.053
    params_theta: 30
    params_N: 30
---
# {{ params_vars_title }}
In the second PHYS 111 lab, {{ params_vars_name }} repeatedly launched a metal sphere and measured the horizontal distance $d$ it traveled.
The launch angle was $\theta$ and the sphere was fired from a height $h$ above the ground.
Using the measured value of $d$ and the known values of $g$, and $h$, {{ params_vars_name }} could determine the launch speed $v_0$ of the projectile.
However, the expression for $v_0$ in terms of $d$, $g$, $\theta$, and $h$ was complicated!
Things get quite a bit simpler if $h = 0$.
In this case:

$$v = \sqrt{\frac{gd}{2cos(\theta)sin(\theta)}}$$

Suppose that, with $h = 0$, {{ params_vars_name }} and their lab partner make 30 measurements of $d$.
{{ params_vars_name }} then determines that the average and standard deviation of their 30 measurements were $\bar{d}$ = {{params_d}} $m$
and $\sigma$= {{params_s}} $m$, respectively.

## Part 1

If g = 9.81 $\frac{m}{s^2}$ and $\theta$ = {{params_theta}}, what is the launch speed $v_0$?

### Answer Section

Please enter in a numeric value in {{ params_vars_units1}}.

## Part 2

What is the uncertainty in your measured value of $d$?

### Answer Section

Please enter in a numeric value in {{ params_vars_units2}}.

## Part 3

What is the uncertainty in the value of $v_0$ that you determined? For this problem, assume that the launch angle is known to very high accuracy, such that its uncertainty can be neglected.

### Answer Section

Please enter in a numeric value in {{ params_vars_units1}}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)