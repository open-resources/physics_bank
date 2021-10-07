---
title: Acceleration of a Particle
topic: Kinematics(1D)
author: Jake Bobowski
source: 2012 Midterm 1 Q6 Section 002
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 4.7.3.0
- 1.7.2.4
- 1.7.2.2
difficulty:
- hard
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- PW
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t_1= $
    suffix: $s$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t_2= $
    suffix: $s$
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
    label: $a= $
    suffix: $m/s^2$
substitutions:
  params:
    vars:
      title: Acceleration of a Particle
      unit1: $s$
      unit2: $m/s^2$
    c1: 4
    c2: 7
    c3_abs: 8
    c3_sign: ' + '
---
# {{ params.vars.title }}
The position of a particle is given by the function $x = (${{ params.c1 }}$t^3 -${{ params.c2 }}$t^2$ {{ params.c3_sign }} {{ params.c3_abs }}) $m$ where $t$ is in seconds.

As you solve the questions below, you will be asked to find several times ($t_1$, $t_2$, $t_3$, etc...) based on certain conditions.
In all cases, order your $t_1$, $t_2$, $t_3$ values such that $t_1$ is the lowest one, and subsequent values increase in time.

## Part 1

At what time is $v_x = 0$ $m/s$? Enter $t_1$, the smallest of the values (if there is more than one).

### Answer Section

Please enter in a numeric value in {{ params.vars.unit1 }}.

## Part 2

At what time after $t_1$, is $v_x = 0$ $m/s$ again? Enter $t_2$, the next value.
*Hint: If there is no such time, enter the special value `-1000` and NOT 0!*

### Answer Section

Please enter in a numeric value in {{ params.vars.unit1 }}.

## Part 3

What is the particle's accelerations at the time $t_1$? Enter $a_1$, the acceleration corresponding to $t_1$.

### Answer Section

Please enter in a numeric value in {{ params.vars.unit2 }}.

## Part 4

What is the particle's accelerations at the time $t_2$? Enter $a_2$, the acceleration corresponding to $t_2$.

*Hint: If $t_2$ does not exist, enter the special value `-1000` for the acceleration and NOT 0!*

### Answer Section

Please enter in a numeric value in {{ params.vars.unit2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)