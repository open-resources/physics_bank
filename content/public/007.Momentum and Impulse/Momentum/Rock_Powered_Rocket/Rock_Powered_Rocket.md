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
substitutions:
  params:
    vars:
      title: Rock Powered Rocket
      units1: m/s
      units2: kg
      name: Emilia
    i: 326
    m: 31
    v_1: 16
    v_2: 21
---
# {{ params.vars.title }}
{{params.vars.name}} is an astronaut, floating in space.
Their rocket is powered by throwing rocks out of a hole in the back of the spaceship.
The total inertia of {{params.vars.name}} and their rocket is {{ params.i }} kg.
{{params.vars.name}} also has two {{ params.m }} kg rocks on board.
They are initially at rest.
{{params.vars.name}} throws the first rock, and then they are moving with velocity {{ params.v_1 }} {{ params.vars.units1 }}.
Then {{params.vars.name}} throws the second rock out of the back and they are moving with velocity {{ params.v_2 }} {{ params.vars.units1 }} .

## Part 1

(a) What is the total momentum of the system?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1 }}{{ params.vars.units2 }}.

## Part 2

(b) With what velocity is the first rock {{params.vars.name}} threw moving through space?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1 }}.

## Part 3

(c) With what velocity is the second rock {{params.vars.name}} threw moving through space?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)