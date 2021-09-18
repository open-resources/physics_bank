---
title: Ball Bouncing off a Wall
topic: Momentum and Impulse
author: Jake Bobowski
source: 2012 Midterm 2 Q6
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 7.4.1.2
- 7.3.1.2
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
- MP
assets:
- q6.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $J_x= $
    suffix: $\frac{kg*m}{s}$
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $F_{avg}= $
    suffix: $N$
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Ball Bouncing off a Wall
      units1: $\frac{kg*m}{s}$
      units2: $N$
    m: 6
    v: 8
    theta: 25
    t: 0.888
---
# {{ params.vars.title }}
A {{params.m}} kg steel bass strikes a massive wall at {{params.v}} m/s at an angle of {{params.theta}} with the plane of the wall. It bounces off of the wall with the same speed and angle (see the figure).

<img src="q6.png" width=400 alt="Ball bouncing on then off a wall at angle theta">

## Part 1

What is the x-component of the impulse that the wall exerts on the ball during the collision?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1 }}.

## Part 2

If the ball is in contact with the wall for 0.200 s, what is the average force that the wall exerts on the ball during the collision?

### Answer Section

Please enter in a numeric value in {{ params.vars.units2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)