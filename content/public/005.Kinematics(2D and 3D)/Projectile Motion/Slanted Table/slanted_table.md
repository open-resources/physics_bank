---
title: Ball on a Slanted Table
topic: Kinematics(2D and 3D)
author: Jake Bobowski
source: 2014 Midterm 1 Q4
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 5.5.1.0
- 5.1.1.0
difficulty:
- hard
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
- Q4.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_0= $
    suffix: m/s
substitutions:
  params:
    vars:
      title: Ball on a Slanted Table
      units: $m/s$
    d: 3.0
    theta: 32
---
# {{ params.vars.title }}
A ball is launched with an initial velocity of $\vec{v_0}$ from one corner of a smooth, flat board.
The angle launch is $\theta$ = {{params.theta}}$^{\circ}$.
As shown, the board has a width of {{params.d}} $m$ and is tilted up at a 20.0$^{\circ}$ angle.

<img src="Q4.png" width=300 alt="A table of width d is slanted at 20 degrees. A ball is launched from the bottom left corner towards the bottom right corner at and angle theta." >

## Question Text

Determine the initial speed $v_0$ required to make the ball land at the adjacent corner labelled as "Target".

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)