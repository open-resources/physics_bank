---
title: A Coyote and a Rat
topic: Kinematics(1D)
author: John Hopkinson
source: PHYS 112 2017W1 002 Final Q15
template_version: 1.1
attribution: standard
outcomes:
- 4.1.1.1
- 4.9.1.0
- 7.2.1.1
- 7.5.1.3
- 7.5.1.4
- 7.5.1.9
- 6.1.1.4
- 6.3.1.2
- 6.7.1.0
- 6.9.1.3
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
  type: symbolic-input
  pl-customizations:
    label: $x = $
    variables: t, vf, vi, a
    weight: 1
    allow-blank: false
part2:
  type: symbolic-input
  pl-customizations:
    label: $v = $
    variables: t, vf, vi, a
    weight: 1
    allow-blank: false
part3:
  type: symbolic-input
  pl-customizations:
    label: $x = $
    variables: t, vf, vi, a
    weight: 1
    allow-blank: false
part4:
  type: symbolic-input
  pl-customizations:
    label: $v = $
    variables: t, vf, vi, a
    weight: 1
    allow-blank: false
part5:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $t= $
    suffix: $s$
    comparison: sigfig
    digits: 2
part6:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $m/s$
    comparison: sigfig
    digits: 2
part7:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $m/s$
    comparison: sigfig
    digits: 2
part8:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: $m$
    comparison: sigfig
    digits: 2
part9:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $m/s$
    comparison: sigfig
    digits: 2
part10:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: A Coyote and a Rat
    m_c: 15
    m_r: 3
    d_b: 40
    d_c: 23
    v_r: 4
    a_c: 8
    mu_k: 2.6
    part10:
      ans1:
        value: Yes, the coyote will be able to stop before hitting the thorny bush.
      ans2:
        value: No, the coyote hits the thorny bush.
---
# {{ params.vars.title }}
A {{ params.m_c }} $kg$ coyote notices a {{ params.m_r }} $kg$ rat running past it, but the rat has a possible route to safety. At the end of the field ({{ params.d_b }} $m$ to the right from where the rat starts) there is a thorny bush. If the rat can reach the bush before the coyote catches it, the coyote will not be able to pursue it any farther. At $t=0$ $s$, the rat is running towards the bush at a constant velocity of {{ params.v_r }} $m/s$, and the coyote is at rest, {{ params.d_c }} $m$ to the left of the rat. However, the coyote begins running to the right with an acceleration of $a = $ {{ params.a_c }} $m/s^2$.

## Part 1

Set your reference frame to be located with the origin at the original location of the coyote, and the rightward direction corresponding to $x$-increasing. Write the position of the coyote as a function of time. Do not plug in values for velocity and acceleration.

Use the following table as a reference for each variable. Note that it may not be necessary to use every variable.

| $Variable$ | Use   |
|----------|-------|
| $\Delta t$  | t  |
| $v_f$  | vf  |
| $v_i$  | vi  |
| $a$  | a  |

### Answer Section

## Part 2

Set your reference frame to be located with the origin at the original location of the coyote, and the rightward direction corresponding to $x$-increasing. Write the velocity of the coyote as a function of time. Do not plug in values for velocity and acceleration.

Use the following table as a reference for each variable. Note that it may not be necessary to use every variable.

| $Variable$ | Use   |
|----------|-------|
| $\Delta t$  | t  |
| $v_f$  | vf  |
| $v_i$  | vi  |
| $a$  | a  |

### Answer Section

## Part 3

Set your reference frame to be located with the origin at the original location of the coyote, and the rightward direction corresponding to $x$-increasing. Write the position of the rat as a function of time. Do not plug in values for velocity and acceleration.

Use the following table as a reference for each variable. Note that it may not be necessary to use every variable.

| $Variable$ | Use   |
|----------|-------|
| $\Delta t$  | t  |
| $v_f$  | vf  |
| $v_i$  | vi  |
| $a$  | a  |

### Answer Section

## Part 4

Set your reference frame to be located with the origin at the original location of the coyote, and the rightward direction corresponding to $x$-increasing. Write the velocity of the rat as a function of time. Do not plug in values for velocity and acceleration.

Use the following table as a reference for each variable. Note that it may not be necessary to use every variable.

| $Variable$ | Use   |
|----------|-------|
| $\Delta t$  | t  |
| $v_f$  | vf  |
| $v_i$  | vi  |
| $a$  | a  |

### Answer Section

## Part 5

At what time does the coyote catch the rat?

### Answer Section

Please enter in a numeric value in seconds.

## Part 6

At this time, what is the velocity of the coyote?

### Answer Section

Please enter in a numeric value in $m/s$.

## Part 7

At this time, what is the velocity of the rat?

### Answer Section

Please enter in a numeric value in $m/s$.

## Part 8

What is the location at which the coyote will catch the rat?

### Answer Section

Please enter in a numeric value in $m$.

## Part 9

In the process where the coyote grabs the rat in its teeth, momentum is conserved. Imagine it takes only an instant. What is the velocity of the coyote after it grabs the rat?

### Answer Section

Please enter in a numeric value in $m/s$.

## Part 10

Although it has caught its prey, momentum still might carry the coyote into the thorny bush. It puts its feet down hard, in an attempt to slow down. If the coefficient of friction between its feet and the ground is $\mu\_{kin}=$ {{ params.mu_k }}, will the coyote be able to stop before it hits the thorny bush?

### Answer Section

- {{ params.part10.ans1.value}}
- {{ params.part10.ans2.value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)