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
    suffix: $\rm{m/s}$
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
    suffix: $\rm{m/s}$
    comparison: sigfig
    digits: 2
myst:
  substitutions:
    params:
      h: 0.4
      a: 90
      r_h: 0.4
      r: 0.34
      u: 2.1
      part1:
        ans1:
          value: true
        ans2:
          value: false
      part3:
        ans1:
          value: 'No'
        ans2:
          value: 'Yes'
---
# Golf Ball in Hole
A golf ball lands with a speed of $u = {{ params.u }}\ \rm{m/s}$ in a tapered frictionless hole as shown below.

<img src="part1.png" width=600>

## Part 1

Does the golf ball remain in stable orbit at the circle of radius $r$, if the ball begins to rotate about the vertical axis of the hole at point A?<br>
$r = {{ params.r }}\ \rm{m}$, $\alpha = {{ params.a }}^{\circ}$

### Answer Section

- {{ params.part1.ans1.value}}
- {{ params.part1.ans2.value}}

## Part 2

Determine the maximum speed of the ball for it to remain in stable orbit about the circle of radius $r$.

### Answer Section

Please enter a value in $m/s$.

## Part 3

Using principles of conservation of energy, does the ball spin out of the hole?<br>
$H\_{hole} = {{ params.h }}\ \rm{m}$, $R\_{hole}= {{ params.r_h }}\ \rm{m}$.

### Answer Section

- {{ params.part3.ans1.value}}
- {{ params.part3.ans2.value}}

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