---
title: Rocket in the wind
topic: Kinematics(2D and 3D)
author: Peyman Yousefi
source: original
template_version: 1.1
attribution: standard
singleVariant: false
showCorrectAnswer: false
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
- APSC181
- Lecture Activities
assets:
- L5Q4.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\theta= $
    suffix: ${\circ}$ E of N
myst:
  substitutions:
    params_vars_title: Rocket in the wind
    params_vars_units: ${\circ}$
    params_v0: 10
    params_wind_acc: 0.8
---
# {{ params_vars_title }}
A model rocket looks to launch with a speed $v\_{0} = {{params_v0}} m/s$.
A the windy day imparts a horizontal acceleration of ${{params.wind_acc}} m/s^2$ to the left.

<img src="L5Q4.png" width=400>

## Question Text

At what angle must the rocket launch so that it returns to its liftoff point?
Assume that the wind does not affect vertical motion.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)