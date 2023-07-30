---
title: Spring Oscillator
topic: Force
author: Ammar Zavahir
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 4.9.1.1
- 4.9.1.2
- 6.3.1.2
- 6.5.1.1
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
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F= $
    suffix: $\rm{N}$
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a_{max}= $
    suffix: $\rm{ms^{-2}}$
    comparison: sigfig
    digits: 2
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t_{period}= $
    suffix: $\rm{s}$
    comparison: sigfig
    digits: 2
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t_{period}= $
    suffix: s
    comparison: sigfig
    digits: 2
myst:
  substitutions:
    params_m: 6
    params_k: 380
    params_x_0: 7
---
# Spring Oscillator
A wooden train is attached to two linear springs of spring constant $k$ in a closed box. The train is displaced from the center of the box by $x_0 \ \rm{m}$.

<img src="part1.png" width=600>

## Part 1

If the train is released from rest and it moves along the frictionless floor, what is the total force in the x-direction acting on the train at the point of release?<br>
$m= {{ params_m }} \ \rm{kg}$, $x\_{0}= {{ params.x_0 }} \ \rm{cm}$, $k = {{ params_k }} \ \rm{Nm^{-1}}$.

### Answer Section

Please enter in a numeric value in $N$.

## Part 2

What is the maximum acceleration of the train?

### Answer Section

Please enter in a numeric value in $ms^{-2}$.

## Part 3

By obtaining the displacement of the train as a function of time, determine the period of oscillation of the train i.e the time that it takes for the train to return back to its starting position.

### Answer Section

Please enter in a numeric value in $s$.

## Part 4

If the spring stiffness constant is quadrupled, what is the new period of oscillation?

### Answer Section

Please enter in a numeric value in $s$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)