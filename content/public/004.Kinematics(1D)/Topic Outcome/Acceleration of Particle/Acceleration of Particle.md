---
title: Acceleration of a Particle
topic: Kinematics(1D)
author: Jake Bobowski
source: 2012 Midterm 1 Q6 Section 002
template_version: 1.1
attribution: standard
outcomes:
- 4.7.3.0
- 1.7.2.4
- 1.7.2.2
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- PW
assets: null
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $t_1= $
    suffix: $s$
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $t_2= $
    suffix: $s$
    comparison: sigfig
    digits: 2
part3:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $a= $
    suffix: $m/s^2$
    comparison: sigfig
    digits: 2
part4:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $a= $
    suffix: $m/s^2$
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Acceleration of a Particle
      unit1: $s$
      unit2: $m/s^2$
    c1: 2
    c2: 7
    c3_abs: 21
    c3_sign: ' - '
---
# {{ params.vars.title }}
The position of a particle is given by the function $x = ({{ params.c1 }}t^3 -{{ params.c2 }}t^2 {{ params.c3_sign }} {{ params.c3_abs }})$ m where $t$ is in seconds.
## Part 1

At what time or times is $v_x = 0$ $m/s$? Enter $t_1$, the smallest of the values (if there is more than one).

### Answer Section

Please enter in a numeric value in {{ params.vars.unit1 }}.
## Part 2

At what time or times is $v_x = 0$ $m/s$? Enter $t_2$, the next value. If there is none, enter -1000.

### Answer Section

Please enter in a numeric value in {{ params.vars.unit1 }}.
## Part 3

What are the particle's accelerations at this/these time(s)? Enter $a_1$, the acceleration corresponding to $t_1$.

### Answer Section

Please enter in a numeric value in {{ params.vars.unit2 }}.
## Part 4

What are the particle's accelerations at this/these time(s)? Enter $a_2$, the acceleration corresponding to $t_2$. If there is none, enter -1000.

### Answer Section

Please enter in a numeric value in {{ params.vars.unit2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)