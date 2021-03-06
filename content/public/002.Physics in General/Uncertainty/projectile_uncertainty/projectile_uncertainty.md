---
title: Projectile Uncertainty
topic: Uncertainty
author: Jake Bobowski
source: 2017 Final Q19
template_version: 1.1
attribution: standard
outcomes:
- 2.4.1.1
- 2.4.1.2
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- MP
assets: null
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $v_o= $
    suffix: m/s
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\Delta d= $
    suffix: m
    comparison: sigfig
    digits: 2
part3:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\Delta v_o= $
    suffix: m/s
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Projectile Uncertainty
      units: m
    d: 0.126
    s: 0.053
    theta: 30
    N: 30
---
# {{ params.vars.title }}
In the second PHYS 111 lab, you repeatedly launched a metal sphere and measured the horizontal distance d it traveled.
The launch angle was $\theta$ and the sphere was red from a height h above the ground.
Using the measured value of d and the known values of g, and h, you could determine the launch speed v0 of the projectile.
However, the expression for v0 in terms of d, g, $\theta$, and h was complicated!
Things get quite a bit simpler if h = 0.
In this case:

$$v = \sqrt{\frac{gd}{2cos(\theta)sin(\theta)}}$$

Suppose that, with h = 0, you and your lab partner make 30 measurements of d.
You then determine that the average and standard deviation of your 30 measurements were $\bar{d}$ = {{params.d}} m
and $\sigma$= {{params.s}} m, respectively.
## Part 1

If g = 9.81 $\frac{m}{s^2}$ and $\theta$ = {{params.theta}}, what is the launch speed $v_o$?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1}}.
## Part 2

What is the uncertainty in your measured value of d?

### Answer Section

Please enter in a numeric value in {{ params.vars.units2}}.
## Part 3

What is the uncertainty in the value of $v_0$ that you determined? For this problem, assume that the launch angle is known to very high accuracy, such that its uncertainty can be neglected.

### Answer Section

Please enter in a numeric value in {{ params.vars.units1}}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)