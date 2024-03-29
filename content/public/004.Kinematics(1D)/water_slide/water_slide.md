---
title: Water Slide
topic: Kinematics(1D)
author: Jake Bobowski
source: 2015 Practice Midterm 1 Q8
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 4.1.1.1
- 4.5.1.0
- 4.6.3.0
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
- MP
assets: null
part1:
  type: symbolic-input
  label: $x(t) = $
  pl-customizations:
    variables: t, v_o, g
    weight: 1
    allow-blank: false
part2:
  type: symbolic-input
  label: $x(t) = $
  pl-customizations:
    variables: t, v_o, g
    weight: 1
    allow-blank: false
part3:
  type: number-input
  label: $t=$
  pl-customizations:
    allow-blank: true
    weight: 1
part4:
  type: number-input
  label: $v=$
  pl-customizations:
    allow-blank: true
    weight: 1
myst:
  substitutions:
    params_vars_name: Savannah
    params_vars_title: Water Slide
    params_theta: 50
    params_l: 400
    params_l2: 200.0
---
# {{ params_vars_title }}
What an exciting time to be alive! A water slide has just opened up near {{ params_vars_name }}'s house! It is a ramp, L = {{params_l}} $m$ long at {{params_theta}}$^{\circ}$ to the horizontal.
At the same instant {{ params_vars_name }} begins sliding down from the top with zero initial velocity $(x=0)$, some jerk kid decides to TRY TO SLIDE UP the slide from the bottom $(x=L)$.
The kid has an unknown initial velocity $v_o$ , but they collide midway down the ramp ({{params_l2}} $m$ from the bottom).

Use the following table as a reference for each variable:

| For  | Use   |
|----------|-------|
| $t$  | t  |
| $v_o$  | v_o  |
| $g$  | g  |

## Part 1

What is the equation describing {{ params_vars_name }}'s position as a function of time?

### Answer Section

Write the position $x(t)$ in terms of time $t$.

## Part 2

What is the equation describing the position of the kid as a function of time?

### Answer Section

Write the position of the kid $x(t)$ in terms of time $t$.

## Part 3

At what time will they collide?

### Answer Section

Please enter in a numeric value in seconds.

## Part 4

What was the jerk kid's initial velocity?

### Answer Section

Please enter a numeric value in $\frac{m}{s}$

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)