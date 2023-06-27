---
title: Position, Velocity and Acceleration
topic: Math
author: Jake Bobowski
source: 2014 Midterm 1 Q3
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 1.2.1.4
- 1.2.1.1
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
- Q3.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $m$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: $m/s$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a= $
    suffix: $m/s^2$
myst:
  substitutions:
    params_vars_title: Position, Velocity and Acceleration
    params_vars_units1: $m$
    params_vars_units2: $m/s$
    params_vars_units3: $\frac{m}{s^2}$
    params_t: 2
    params_x_i: -4
---
# {{ params_vars_title }}
The figure shows the velocity-versus-time graph for a particle moving along the x-axis. Its position at $t$ = 0 s is {{params.x_i}} $m$.

<img src="Q3.png" width=300 alt = "Graph of velocity vs time. The graph increases from 0 to 4 m/s in 1 second. It then decreases to -1m/s at 2.5s. It remains at -1m/s until 4s when it increases back to 0m/s at 5s.">

## Part 1

What is the particles velocity at $t$ = {{params_t}} $s$? If the answer is undefined, enter 100.

### Answer Section

Please enter in a numeric value in {{ params_vars_units1 }}.

## Part 2

What is the particles position at $t$ = {{params_t}} $s$? If the answer is undefined, enter 100.

### Answer Section

Please enter in a numeric value in {{ params_vars_units2 }}.

## Part 3

What is the particles acceleration at $t$ = {{params_t}} $s$? If the answer is undefined, enter 100.

### Answer Section

Please enter in a numeric value in {{ params_vars_units3 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)