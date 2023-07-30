---
title: Pool Ball Collision
topic: Momentum and Impulse
author: Ammar Zavahir
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 7.4.1.2
- 7.5.1.7
- 7.5.1.5
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- APSC181
- A.Z
assets:
- part1.png
- part2.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\theta= $
    suffix: $\rm{^{\circ}}$
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{black}= $
    suffix: $\rm{m/s}$
    comparison: sigfig
    digits: 2
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{white}= $
    suffix: $\rm{m/s}$
    comparison: sigfig
    digits: 2
part4:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params_u: 9
    params_a: 31
    params_part4_ans1_value: false
    params_part4_ans2_value: true
---
# Pool ball collision
In a game of pool, the white cue ball is shot in a straight line towards a stationary black ball with speed $u_1$.
<br>

<img src="part1.png" width=600>

## Part 1

If the oblique collision is deemed perfectly elastic, what is the angle $\theta$ with which each ball is deflected relative to each other?<br>
Treat the two balls as particles having the same mass and neglect any resistive forces.

### Answer Section

Please enter the angle in $\circ$.

## Part 2

If the **black** ball leaves the collision at an angle $\alpha$ measured from below the horizontal, what is the speed of the **black** ball after the collision?
<br>
$u_1 = {{ params_u }}\ \rm{ms^{-1}}$ , $\alpha = {{ params_a }}^{\circ}$

<img src="part2.png" width=600>

### Answer Section

Please enter the speed of the black ball in $ms^{-1}$.

## Part 3

What is the speed of the **white** cue ball after the collision?

### Answer Section

Please enter the speed of the white cue ball in $ms^{-1}$.

## Part 4

If the final direction of one of the balls was undetermined, using the principles of conservation of momentum and energy, can the speeds of the two balls leaving the collision be determined?

### Answer Section

- {{ params_part4_ans1_value}}
- {{ params_part4_ans2_value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)