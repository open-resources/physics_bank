---
title: Ballistic Launcher
topic: Vectors
author: John Hopkinson
source: PHYS 112 2015W Group Problem Solving IV Q1
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 5.1.1.0
- 5.5.1.0
- 3.2.1.0
- 3.5.1.3
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
- PW
- tutorial
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a_x= $
    suffix: $m/s^2$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a_y= $
    suffix: $m/s^2$
part3:
  type: symbolic-input
  pl-customizations:
    label: $\overrightarrow{a} (t) =$
    variables: g , x_hat, y_hat
    weight: 1
    allow-blank: true
part4:
  type: symbolic-input
  pl-customizations:
    label: $v_{x,\theta^{\circ}}=$
    variables: t, v_max, g , theta
    weight: 1
    allow-blank: true
part5:
  type: symbolic-input
  pl-customizations:
    label: $v_{y,\theta^{\circ}}=$
    variables: t, v_max, g , theta
    weight: 1
    allow-blank: true
part6:
  type: symbolic-input
  pl-customizations:
    label: $\overrightarrow{v}_{\theta^{\circ}}(t) =$
    variables: v_x, v_y, x_hat, y_hat
    weight: 1
    allow-blank: true
part7:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t= $
    suffix: $s$
part8:
  type: symbolic-input
  pl-customizations:
    label: $x=$
    variables: t, x0, y0, g, v_x, v_y
    weight: 1
    allow-blank: true
part9:
  type: symbolic-input
  pl-customizations:
    label: $y=$
    variables: t, x0, y0, g, v_x, v_y
    weight: 1
    allow-blank: true
part10:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: $m$
substitutions:
  params:
    vars:
      title: Ballistic Launcher
    dist: 31.9
    vmax: 4.91
    theta_1: 32.4
    theta_2: 48.5
---
# {{ params.vars.title }}
A steel ball is fired from a ballistic launcher at different angles.  The launched ball has been found to travel from the edge of a table to land {{ params.dist }} $cm$ from the far end of the table when starting from the height of the table and launched at an angle of {{ params.theta_1 }}$^{\circ}$ above the horizontal.  When launched at {{ params.theta_2 }}$^{\circ}$, the ball easily clears the table to land on the floor.

You may assume that $t=0$ at the instant that the ball leaves the launcher.

## Part 1

Ignoring air resistance, write an expression for the $x$-component of the acceleration of the ball while it is in the air.

### Answer Section

Please enter in a numeric value in $m/s^2$.

## Part 2

Ignoring air resistance, write an expression for the $y$-component of the acceleration of the ball while it is in the air.

### Answer Section

Please enter in a numeric value in $m/s^2$.

## Part 3

Write an expression for the full acceleration vector in terms of the unit vectors $\hat{x}$ and $\hat{y}$.

You should provide a symbolic answer in terms of the following variables: $\hat{x}$, $\hat{y}$, and $g$.

Note that it may not be necessary to use every variable. Use the following table as a reference for using each variable.

| $Variable$ | Use   |
|----------|-------|
| $g$      | g     |
| $\hat{x}$ | x_hat |
| $\hat{y}$ | y_hat |

### Answer Section

Please enter in a symbolic answer.

## Part 4

On its maximum setting, the speed of the ejected steel ball is $v\_{max}$.

Write an expression for the $x$-component of the velocity of the ball as a function of time when the angle of launch is $\theta^{\circ}$.

You should provide a symbolic answer in terms of the following variables: $t$, $v\_{max}$, $\theta$, $\hat{x}$, $\hat{y}$, and $g$.

Note that it may not be necessary to use every variable. Use the following table as a reference for using each variable.

| $Variable$ | Use   |
|----------|-------|
| $t$ | t |
| $v\_{max}$ | v_max |
| $\theta$ | theta |
| $g$      | g     |

### Answer Section

Please enter in a symbolic answer.

## Part 5

On its maximum setting, the speed of the ejected steel ball is $v\_{max}$.

Write an expression for the $y$-component of the velocity of the ball as a function of time when the angle of launch is $\theta^{\circ}$.

You should provide a symbolic answer in terms of the following variables: $t$, $v\_{max}$, $\theta$, $\hat{x}$, $\hat{y}$, and $g$.

Note that it may not be necessary to use every variable. Use the following table as a reference for using each variable.

| $Variable$ | Use   |
|----------|-------|
| $t$ | t |
| $v\_{max}$ | v_max |
| $\theta$ | theta |
| $g$      | g     |

### Answer Section

Please enter in a symbolic answer.

## Part 6

Write an expression for the full velocity vector as a function of time.

You should provide a symbolic answer in terms of the following variables: $v_x$ and $v_y$.

Note that it may not be necessary to use every variable. Use the following table as a reference for using each variable.

| $Variable$ | Use   |
|----------|-------|
| $v\_{x}$ | v_x |
| $v\_{y}$ | v_y |
| $\hat{x}$ | x_hat |
| $\hat{y}$ | y_hat |

### Answer Section

Please enter in a symbolic answer.

## Part 7

On its maximum setting, the speed of the ejected steel ball is $v\_{max} = $ {{ params.vmax }} $m/s$.

From your expression for $v\_{y,\theta^{\circ}}$, solve for the time that the ball was in the air, when the ball was launched at a {{ params.theta_1 }}$^{\circ}$ angle.

*Hint: what would be the vertical component of the velocity of the ball just before it hit the table when it returns to the same height from which it left?*

### Answer Section

Please enter in a numeric value in $s$.

## Part 8

Letting the edge of the table from which the ball was launched have coordinates $(x_0, y_0) = (0, 0)$, write an expression for the $x$-component of the object's position vector.

You should provide a symbolic answer in terms of the following variables: $t$, $x_0$, $y_0$, $v\_{0_x}$, $v\_{0_y}$, and $g$.

Note that it may not be necessary to use every variable. If a value is zero, do not include it. Use the following table as a reference for using each variable.

| $Variable$ | Use  |
|----------|-------|
| $t$ | t |
| $x_0$ | x0|
| $y_0$ | y0|
| $v\_{0_x}$ | v_x |
| $v\_{0_y}$ | v_y |
| $g$ | g |

### Answer Section

Please enter in a symbolic answer.

## Part 9

Letting the edge of the table from which the ball was launched have coordinates $(x_0, y_0) = (0, 0)$, write an expression for the $y$-component of the object's position vector.

You should provide a symbolic answer in terms of the following variables: $t$, $x_0$, $y_0$, $v\_{0_x}$, $v\_{0_y}$, and $g$.

Note that it may not be necessary to use every variable. If a value is zero, do not include it. Use the following table as a reference for using each variable.

| $Variable$ | Use  |
|----------|-------|
| $t$ | t |
| $x_0$ | x0|
| $y_0$ | y0|
| $v\_{0_x}$ | v_x |
| $v\_{0_y}$ | v_y |
| $g$ | g |

### Answer Section

Please enter in a symbolic answer.

## Part 10

Using your results from Part 8 and/or Part 9, estimate the total length of the table.  Note that the steel ball landed about {{ params.dist }} $cm$ from the end of the table when fired at a {{ params.theta_1 }}$^{\circ}$ angle.

### Answer Section

Please enter in a numeric value in $m$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)