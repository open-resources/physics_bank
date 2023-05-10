---
title: Rock Powered Rocket
topic: Momentum and Impulse
author: Jake Bobowski
source: 2015 Practice Midterm 1 Q7
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.2.1.1
- 7.2.2.0
- 7.2.2.1
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- average
tags:
- EW
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    allow-blank: true
    label: $P_{total}=$
    suffix: $kg m/s$
    weight: 1
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    allow-blank: true
    label: $v_{f}=$
    suffix: $m/s$
    weight: 1
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    allow-blank: true
    label: $v_{rock f}=$
    suffix: $m/s$
    weight: 1
myst:
  substitutions:
    params_vars_title: Rock Powered Rocket
    params_vars_units1: m/s
    params_vars_units2: kg
    params_vars_name: Mateo
    params_i: 365
    params_m: 25
    params_v_1: 8
    params_v_2: 17
---
# {{ params_vars_title }}
{{params_vars_name}} is an astronaut, floating in space.
Their rocket is powered by throwing rocks out of a hole in the back of the spaceship.
The inertia of {{params_vars_name}} and their rocket together is {{ params_i }} kg.
{{params_vars_name}} also (in addition to the rocket and the person) has two {{ params_m }} kg rocks on board.
They are initially at rest.
{{params_vars_name}} throws the first rock, and then they are moving with velocity {{ params.v_1 }} {{ params_vars_units1 }}.
Then {{params_vars_name}} throws the second rock out of the back and they are moving with velocity {{ params.v_2 }} {{ params_vars_units1 }} .

## Part 1

(a) What is the total momentum of the system?

### Answer Section

Please enter in a numeric value in {{ params_vars_units1 }}{{ params_vars_units2 }}.

## Part 2

(b) With what velocity is the first rock {{params_vars_name}} threw moving through space?

### Answer Section

Please enter in a numeric value in {{ params_vars_units1 }}.

## Part 3

(c) With what velocity is the second rock {{params_vars_name}} threw moving through space?

### Answer Section

Please enter in a numeric value in {{ params_vars_units1 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)