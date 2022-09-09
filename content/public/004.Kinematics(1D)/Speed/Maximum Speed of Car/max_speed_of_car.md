---
title: Maximum Speed of Car
topic: Kinematics(1D)
author: Peyman Yousefi
source: APSC 181, Lecture 5, Q1
template_version: 1.1
attribution: standard
singleVariant: false
showCorrectAnswer: false
outcomes:
- 4.6.2.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- AP
- APSC 181 - LA
assets:
- L5Q1.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{max}= $
    suffix: $ft/s$
substitutions:
  params:
    vars:
      title: Maximum Speed of Car
      units: $ft/s$
    yards: 100
    max_speed_t: 8
    overall_t: 11
---
# {{ params.vars.title }}
<img src="L5Q1.png" width=85%>

A car reaches its maximum speed in {{params.max_speed_t}} $seconds$ from rest with constant acceleration.
It then maintains that speed and travels {{params.yards}} miles with an overall time of {{params.overall_t}} $hours$.

## Question Text

Determine the maximum speed $v\_{max}$ of the car.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)