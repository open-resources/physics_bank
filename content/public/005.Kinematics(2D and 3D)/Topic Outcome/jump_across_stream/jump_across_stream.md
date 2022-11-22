---
title: Jump Across Stream
topic: Kinematics(2D and 3D)
author: Jake Bobowski
source: Final 2016 Q4 P2
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
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
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: $\rm{m}$
part7:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $y= $
    suffix: $\rm{m}$
part8:
  type: symbolic-input
  pl-customizations:
    label: $\vec{V} = $
    variables: i_hat, j_hat
    weight: 1
    allow-blank: false
part9:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Jump Across Stream
      units: m
    m: 208
    w_s: 3.6
    h_s: 1.7
    v_i: 2
    v_j: 4
    h_b: 3.3
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
The stream is {{params.w_s}} $m$ wide and the east bank of the stream is {{params.h_s}} $\rm{m}$ higher than the west bank (where the bear starts).
The bear can jump with an initial velocity $\overrightarrow{V_i} = $ {{params.v_i}}$\rm{m\over s}\hat{\imath}+$ {{params.v_j}} $\rm{m\over s}\hat{\jmath}$, and decides to start from {{params.h_b}} $\rm{m}$ in the air, halfway up a sturdy tree.

## Part 1

If the origin is at the bear's foot (up in the tree), write an equation describing the $x$ coordinate of the bear while it is in the air.

Use the following table as a reference. Note that it may not be necessary to use every variable.

| For  | Use   |
|----------|-------|
| $\Delta t$  | t  |
| $g$ | g |

### Answer Section

## Part 2

If the origin is at the bear's foot (up in the tree), write an equation describing the $y$ coordinate of the bear while it is in the air.

Use the following table as a reference. Note that it may not be necessary to use every variable.

| For  | Use   |
|----------|-------|
| $\Delta t$  | t  |
| $g$ | g |

### Answer Section

## Part 3

If the origin is at the bear's foot (up in the tree), write an equation describing the $V_x$ component of the velocity of the bear while it is in the air.

Use the following table as a reference. Note that it may not be necessary to use every variable.

| For  | Use   |
|----------|-------|
| $\Delta t$  | t  |
| $g$ | g |

### Answer Section

## Part 4

If the origin is at the foot of the bear's jumping tree, write an equation describing the $V_y$ component of the velocity of the bear while it is in the air.

Use the following table as a reference. Note that it may not be necessary to use every variable.

| For  | Use   |
|----------|-------|
| $\Delta t$  | t  |
| $g$ | g |

### Answer Section

## Part 5

Does the bear make it to the other side of the stream?

### Answer Section

- {{ params.part5.ans1.value}}
- {{ params.part5.ans2.value}}

## Part 6

When the bear is at its highest ($y$ or vertical) position above the stream, what is the $x$-coordinate of the bear?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 7

Where is the $y$-coordinate of the bear's highest position above the stream?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 8

What is the bear's velocity when it reaches its maximum height?

Use the following table as a reference.

| For  | Use   |
|----------|-------|
| $\hat{\imath}$  | i_hat  |
| $\hat{\jmath}$  | j_hat |

### Answer Section

{{ substitutions.part8.label }}

## Part 9

This question is much easier to do in the frame of an observer moving with velocity $\vec{u}  = $ {{params.v_i}} $\rm{m\over s}\hat{\imath} + $ 0 $\rm{m\over s}\hat{\jmath}$. Describe why?

### Answer Section

- {{ params.part9.ans1.value}}
- {{ params.part9.ans2.value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)