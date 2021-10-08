---
title: Barge Pulled by Tugboats
topic: Vectors
author: OpenStax University Physics Volume 1
source: 1.2.60
template_version: 1.3
attribution: openstax-physics-vol1
partialCredit: true
singleVariant: false
outcomes:
- 3.1.1.2
- 3.4.1.0
- 3.4.1.2
- 3.5.1.0
- 3.5.1.1
- 3.5.1.3
- 3.5.1.5
- 3.5.1.6
- 3.6.1.1
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
- OSUP
- volume 1
assets:
- osup2.60.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_{2_x}= $
    suffix: units of force
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_{2_y}= $
    suffix: units of force
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_{1_x}= $
    suffix: units of force
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_{1_y}= $
    suffix: units of force
part5:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $mag(F_{R})= $
    suffix: units of force
part6:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Barge Pulled by Tugboats
    F1: 5116
    F2: 3912
    theta_1: 25
    theta_2: 8
    part6:
      ans1:
        value: 10.8$^{\circ}$ to the left of AB.
      ans2:
        value: 10.8$^{\circ}$ to the right of AB.
      ans3:
        value: 79.2$^{\circ}$ to the left of AB.
      ans4:
        value: 79.2$^{\circ}$ to the right of AB.
      ans5:
        value: 108.0$^{\circ}$ to the left of AB.
      ans6:
        value: 108.0$^{\circ}$ to the right of AB.
---
# {{ params.vars.title }}
A barge is pulled by the two tugboats shown in the following figure.
One tugboat pulls on the barge with a force of magnitude $F_2 = $ {{ params.F2 }} units of force at $\theta_2 = $ {{ params.theta_2 }}$^{\circ}$ above the line AB and the other tugboat pulls on the barge with a force of magnitude $F_1 = $ {{ params.F1 }} units of force at $\theta_1 = $ {{ params.theta_1 }}$^{\circ}$ below the line AB.

Assume $+y$ is straight ahead, and $+x$ is to the right.

<img longdesc="Barge Pulled by Tugboats.md#desc" alt="Figure of a barge pulled by two tugboats." src="osup2.60.png">

<div id="desc">
<h5>Figure of a barge pulled by two tugboats.</h5>
A straight line AB is drawn through the center of the barge. One tugboat pulls the barge to the left with a force of magnitude F one at an angle theta one relative to AB. The other tugboat pulls to the right with a force F two at angle theta two relative to AB.
</div>

## Part 1

Resolve the pulling forces to theircomponents.
What is the $x$-component of the force above the line AB i.e. the right force?
Remember to consider the sign convention.

### Answer Section

Please enter in a numeric value in 'units of force'.

## Part 2

Resolve the pulling forces to theircomponents.
What is the $y$-component of the force above the line AB i.e. the right force?
Remember to consider the sign convention.

### Answer Section

Please enter in a numeric value in 'units of force'.

## Part 3

Resolve the pulling forces to theircomponents.
What is the $x$-component of the force below the line AB i.e. the left force?
Remember to consider the sign convention.

### Answer Section

Please enter in a numeric value in 'units of force'.

## Part 4

Resolve the pulling forces to theircomponents.
What is the $y$-component of the force below the line AB i.e. the left force?
Remember to consider the sign convention.

### Answer Section

Please enter in a numeric value in 'units of force'.

## Part 5

What is the magnitude of the resultant pull?

### Answer Section

Please enter in a numeric value in 'units of force'.

## Part 6

What is the direction of the resultant vector relative to the line AB?

### Answer Section

- {{ params.part6.ans1.value }}
- {{ params.part6.ans2.value }}
- {{ params.part6.ans3.value }}
- {{ params.part6.ans4.value }}
- {{ params.part6.ans5.value }}
- {{ params.part6.ans6.value }}

## Attribution

Problem is from the [OpenStax University Physics Volume 1](https://openstax.org/details/books/university-physics-volume-1) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)