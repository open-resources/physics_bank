---
title: Ball in the wind
topic: Kinematics(2D and 3D)
author: Peyman Yousefi
source: original
template_version: 1.1
attribution: standard
outcomes:
- 5.5.1.0
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
- AP
- APSC 181 - LA
assets:
- L5Q4.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\theta= $
    suffix: ${\circ}$
substitutions:
  params:
    vars:
      title: Ball in the wind
      units: ${\circ}$
    v0: 5
    wind_speed: 1.0
---
# {{ params.vars.title }}
A child throws a ball upward with a speed of $v\_{0} = {{params.v0}} m/s$.
A gust of wind imparts a horizontal acceleration of ${{params.wind_speed}} m/s^2$ to the left.

<img src="L5Q4.png" width=400>

## Question Text

At what angle must the ball be thrown so that it returns to the child's hand?
Assume that the wind does not affect vertical motion.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)