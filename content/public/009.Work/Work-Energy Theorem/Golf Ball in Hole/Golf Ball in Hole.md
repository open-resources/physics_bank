---
title: Golf Ball in Hole
topic: Work
author: Ammar Zavahir
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.3.1.2
- 6.5.1.3
- 6.12.1.1
- 9.2.1.1
- 8.5.2.2
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
- APSC181
- A.Z
assets:
- part1.png
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{max}= $
    suffix: $\rm{ms^{-1}}$
    comparison: sigfig
    digits: 2
part3:
  type: multiple-choice
  pl-customizations:
    weight: 1
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $r_{stable}= $
    suffix: $\rm{m}$
    comparison: sigfig
    digits: 2
part5:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{stable}= $
    suffix: $\rm{ms^{-1}}$
    comparison: sigfig
    digits: 2
myst:
  substitutions:
    params_h: 0.26
    params_a: 54
    params_r_h: 0.1324766168685515
    params_r: 0.091
    params_u: 1.4
    params_part1_ans1_value: true
    params_part1_ans2_value: false
    params_part3_ans1_value: 'No'
    params_part3_ans2_value: 'Yes'
---
# Golf Ball in Hole
A golf ball lands with a speed of $u = {{ params_u }}\ \rm{ms^{-1}}$ in a tapered frictionless hole as shown below.

<img src="part1.png" width=600>

## Part 1

Does the golf ball remain in stable orbit at the circle of radius $r$, if the ball begins to rotate about the vertical axis of the hole at point A?<br>
$r = {{ params_r }}\ \rm{m}$, $\alpha = {{ params_a }}^{\circ}$

### Answer Section

- {{ params_part1_ans1_value}}
- {{ params_part1_ans2_value}}

## Part 2

Determine the maximum speed of the ball for it to remain in stable orbit about the circle of radius $r$.

### Answer Section

Please enter a value in $m/s$.

## Part 3

Using principles of conservation of energy, does the ball spin out of the hole?<br>
$H\_{hole} = {{ params_h }}\ \rm{m}$, $R\_{hole}= {{ params_r_h }}\ \rm{m}$.

### Answer Section

- {{ params_part3_ans1_value}}
- {{ params_part3_ans2_value}}

## Part 4

Determine the radius of the stable orbit gained by the golf ball(i.e stable implies that the centripetal force is sufficiently provided by the forces acting on the ball and the ball rotates in a circle of constant height).

### Answer Section

Please enter a value in $m$.

## Part 5

What is the speed of the golf ball in this stable orbit?

### Answer Section

Please enter a value in $m/s$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)