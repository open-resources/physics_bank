---
title: Jump across stream
topic: Kinematics(2D and 3D)
author: Jake Bobowski
source: Final 2016 Q4 P2
template_version: 1.1
attribution: standard
outcomes:
- 5.1.1.0
- 5.2.1.0
- 5.2.1.1
- 5.5.1.0
- 5.5.1.1
- 5.5.1.2
- 5.8.1.1
- 4.1.1.1
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
- AK
- PW
assets: null
part1:
  type: symbolic-input
  pl-customizations:
    label: $x = $
    variables: t, g
    weight: 1
    allow-blank: false
part2:
  type: symbolic-input
  pl-customizations:
    label: $y = $
    variables: t, g
    weight: 1
    allow-blank: false
part3:
  type: symbolic-input
  pl-customizations:
    label: $V_x = $
    variables: t, g
    weight: 1
    allow-blank: false
part4:
  type: symbolic-input
  pl-customizations:
    label: $V_y = $
    variables: t, g
    weight: 1
    allow-blank: false
part5:
  type: multiple-choice
  pl-customizations:
    weight: 1
part6:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: $m$
    comparison: sigfig
    digits: 2
part7:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $y= $
    suffix: $m$
    comparison: sigfig
    digits: 2
part8:
  type: symbolic-input
  pl-customizations:
    label: $\vec{V} = $
    variables: ihat, jhat
    weight: 1
    allow-blank: false
part9:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Jump across stream V2
      units: $m$
    m: 410
    w_s: 4.8
    h_s: 1.1
    v_i: 6
    v_j: 2
    h_b: 3.9
    part5:
      ans1:
        value: Yes, the bear makes it to the other side of the stream.
      ans2:
        value: No, the bear does not make it to the other side of the stream.
    part9:
      ans1:
        value: The problem would become a 1-D problem with motion only in the $y$-direction.
      ans2:
        value: The problem would become a 1-D problem with motion only in the $x$-direction.
---
# {{ params.vars.title }}
A very bored {{params.m}} $kg$ bear decided to jump across a stream.
The stream is {{params.w_s}} $m$ wide and the east bank of the stream is {{params.h_s}} $m$ higher than the west bank (where the bear starts).
The bear can jump with an initial velocity $\overrightarrow{V_i} = {{params.v_i}}{m\over s}\hat{\imath}+{{params.v_j}} {m\over s}\hat{\jmath}$, and decides to start from {{params.h_b}} $m$ in the air, halfway up a sturdy tree.

## Part 1

If the origin is at the foot of the bear's jumping tree, write an equation describing the $x$ coordinate of the bear while it is in the air.

Use the following table as a reference. Note that it may not be necessary to use every variable.

| $Variable$ | Use   |
|----------|-------|
| $\Delta t$  | t  |
| $g$ | g |

### Answer Section

{{ substitutions.part1.label }}

## Part 2

If the origin is at the foot of the bear's jumping tree, write an equation describing the $y$ coordinate of the bear while it is in the air.

Use the following table as a reference. Note that it may not be necessary to use every variable.

| $Variable$ | Use   |
|----------|-------|
| $\Delta t$  | t  |
| $g$ | g |

### Answer Section

{{ substitutions.part2.label }}

## Part 3

If the origin is at the foot of the bear's jumping tree, write an equation describing the $V_x$ component of the velocity of the bear while it is in the air.

Use the following table as a reference. Note that it may not be necessary to use every variable.

| $Variable$ | Use   |
|----------|-------|
| $\Delta t$  | t  |
| $g$ | g |

### Answer Section

{{ substitutions.part3.label }}

## Part 4

If the origin is at the foot of the bear's jumping tree, write an equation describing the $V_y$ component of the velocity of the bear while it is in the air.

Use the following table as a reference. Note that it may not be necessary to use every variable.

| $Variable$ | Use   |
|----------|-------|
| $\Delta t$  | t  |
| $g$ | g |

### Answer Section

{{ substitutions.part4.label }}

## Part 5

Does the bear make it to the other side of the stream?

### Answer Section

- {{ params.part5.ans1.value}}
- {{ params.part5.ans2.value}}

## Part 6

Where is the $x$-coordinate of the bear's highest position above the stream?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 7

Where is the $y$-coordinate of the bear's highest position above the stream?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 8

What is the bear's velocity when it reaches its maximum height?

Use the following table as a reference.

| $Variable$ | Use   |
|----------|-------|
| $\hat{\imath}$  | ihat  |
| $\hat{\jmath}$  | jhat |

### Answer Section

{{ substitutions.part8.label }}

## Part 9

This question is much easier to do in the frame of an observer moving with velocity $\vec{u}  ={{params.v_i}}{m\over s}\hat{\imath}+0 {m\over s}\hat{\jmath}$. Describe why?

### Answer Section

- {{ params.part9.ans1.value}}
- {{ params.part9.ans2.value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)