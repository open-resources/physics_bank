---
title: Ball Bouncing off a Wall
topic: Momentum and Impulse
author: Jake Bobowski
source: 2012 Midterm 2 Q6
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 7.4.1.2
- 7.3.1.2
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- section
length:
- average
tags:
- MP
assets:
- q6.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $J_x= $
    suffix: $\frac{kg*m}{s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_{avg}= $
    suffix: $N$
myst:
  substitutions:
    params_vars_title: Ball Bouncing off a Wall
    params_vars_units1: $\frac{kg*m}{s}$
    params_vars_units2: $N$
    params_m: 10
    params_v: 5
    params_theta: 38
    params_t: 0.769
---
# {{ params_vars_title }}
A {{params_m}} kg steel bass strikes a massive wall at {{params_v}} m/s at an angle of {{params_theta}} degrees with the plane of the wall.
It bounces off of the wall with the same speed and angle (see the figure).

<img src="q6.png" width=400 alt="Ball bouncing on then off a wall at angle theta">

## Part 1

What is the x-component of the impulse that the wall exerts on the ball during the collision?

### Answer Section

Please enter in a numeric value in {{ params_vars_units1 }}.

## Part 2

If the ball is in contact with the wall for {{ params_t }} s, what is the average force that the wall exerts on the ball during the collision?

### Answer Section

Please enter in a numeric value in {{ params_vars_units2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)