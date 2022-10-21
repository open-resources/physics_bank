---
title: Rocket
topic: Math
author: Jake Bobowski
source: 2015 Practice Midterm 1 Q6
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 1.8.1.2
- 1.7.2.1
- 4.3.1.0
- difficulty: null
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- EW
assets: null
part1:
  type: symbolic-input
  label: $x(t)=$
  pl-customizations:
    variables: t
    weight: 1
    allow-blank: true
part2:
  type: symbolic-input
  label: $a= $
  pl-customizations:
    variables: t
    weight: 1
    allow-blank: true
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a= $
    suffix: $m/s^2$
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t= $
    suffix: $s$
substitutions:
  params:
    vars:
      title: Rocket
      units1: $m/s^2$
      units2: $s$
    v_1: 6
    t_1: 2
    t_2: 5
---
# {{ params.vars.title }}
A rocket has a velocity (pointing away from the launch pad) given by $v(t)$={{ params.v_1 }}$t$-$t^2$
where $x$ is in meters, and $t$ is in seconds.

Please enter in fractions rather than decimals when applicable (e.g. use 1/2 rather than 0.5)

## Part 1

(a) If the rocket started at height $x(0)$ = 0, What is the height as a function of time in $m$?

### Answer Section

Please enter the equation.

## Part 2

(b) What is the acceleration as a function of time in $m/s^2$?

### Answer Section

Please enter the equation.

## Part 3

(c) What is the average acceleration between $t =$ {{ params.t_1 }}$s$ and $t =$ {{ params.t_2 }}$s$?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1 }}.

## Part 4

(d) At what time does the rocket stop rising upwards and begin falling down?

### Answer Section

Please enter in a numeric value in {{ params.vars.units2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)