---
title: Ball Bouncing Across Gap
topic: Momentum and Impulse
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.5.1.0
- 5.5.1.1
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
- PJ
assets:
- BallBouncingAcrossGap.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $n= $
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $d= $
    suffix: $\rm{m}$
myst:
  substitutions:
    params:
      vars:
        title: Ball Bouncing Across Gap
      h1: 2.67
      h2: 0.83
      v: 9
      theta: 35
      e: 0.76
---
# {{ params.vars.title }}
A rubber ball is launched off a platform $h_1={{params.h1}} \ \rm{m}$ high with an initial velocity $v={{params.v}} \ \rm{m/s}$ at an angle ${{params.theta}}^\circ$.
The ball bounces its way onto another platform $h_2={{params.h2}} \ \rm{m}$ high.
The coefficient of restitution between the ball and the ground is ${{params.e}}$.
The ball just barely makes it onto the platform.
In other words, if the platform was any farther, the ball wouldn't have made it.

<img src="BallBouncingAcrossGap.png" width=800 alt="A ball is launched from a platform, bounces multiple times, and lands on another platform." >

## Part 1

How many times did the ball bounce?

### Answer Section

Please enter in a numeric value.

## Part 2

At what horizontal distance $d$ was the platform from the launch surface?

### Answer Section

Please enter in a numeric value in m.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)