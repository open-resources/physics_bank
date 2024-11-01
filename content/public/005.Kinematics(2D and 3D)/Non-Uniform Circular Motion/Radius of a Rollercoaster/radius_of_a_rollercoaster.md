---
title: Radius of a Rollercoaster
topic: Rotational Motion
author: Peyman Yousefi
source: APSC 181, Lecture 6, Q2
template_version: 1.1
attribution: standard
singleVariant: false
showCorrectAnswer: true
outcomes:
- 5.7.1.1
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
- APSC181
- Lecture Activities
assets:
- L6Q2.gif
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\rho= $
    suffix: $m$
myst:
  substitutions:
    params:
      vars:
        title: Radius of a Rollercoaster
        units: $m$
      speed_of_car: 227
      rate_of_decrease: 8
      a: 5
---
# {{ params.vars.title }}
As a rollercoaster passes the bottommost point in a loop, an accelerometer records an acceleration of ${{params.a}}g$.
The speed of the car is ${{params.speed_of_car}}km/h$ and is decreasing at a rate of ${{params.rate_of_decrease}}km/h$ every second.

<img src="L6Q2.gif" width=85%>

## Question Text

Determine the radius of curvature at the position shown.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)