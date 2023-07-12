---
title: Box on a Slant with a Pulley
topic: Force
author: Jake Bobowski
source: 2013 Midterm 2 002 Q4
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.1.1.4
- 6.3.1.2
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
- MP
- JR
assets:
- Q4.png
part1:
  type: symbolic-input
  pl-customizations:
    label: $f = $
    variables: ms, mh, g, mu, theta
    weight: 1
    allow-blank: false
part2:
  type: symbolic-input
  pl-customizations:
    label: $T = $
    variables: ms, mh, g, mu, theta
    weight: 1
    allow-blank: false
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $m_s = $
    suffix: $\rm{kg}$
myst:
  substitutions:
    params_vars_title: Box on a Slant with a Pulley
    params_angl: 31
    params_coef: 0.6
    params_mass: 6
---
# {{ params_vars_title }}
The figure shows a block of mass $m_s$ resting on a $\theta = {{params_angl}}^\circ$ slope.
The coefficient of static friction between the block and the sloped surface is $\mu_s = {{params_coef}}$.
The block on the slope is connected to a hanging block of mass $m_h = {{params_mass}} \rm{kg}$ via a massless string that passes over a massless, frictionless pulley. Assume $g = 9.81 \rm{m/s^2}$.

<img src="Q4.png" width=400 alt = "A box sits on a ramp that is at an angle theta from the horizontal. The box is connected by a string to another mass that hangs freely from a pulley.">

## Part 1

What is the force of friction acting on the block on the slope $f$? Express your answer in terms of the variables in the question.

Note that it may not be necessary to use every variable. Use the following table as a reference for each variable:

| For      | Use   |
|----------|-------|
| $m_s$    | ms    |
| $m_h$    | mh    |
| $g$      | g     |
| $\mu_s$   | mu    |
| $\theta$ | theta |

### Answer Section

## Part 2

What is the tension in the string $T$? Express your answer in terms of the variables in the question.

Note that it may not be necessary to use every variable. Use the following table as a reference for each variable:

| For      | Use   |
|----------|-------|
| $m_s$    | ms    |
| $m_h$    | mh    |
| $g$      | g     |
| $\mu_s$   | mus   |
| $\theta$ | theta |

### Answer Section

## Part 3

Use Newton's second law and your answers to Part 1 and 2 to determine the minimum value of the mass of the block on the slope $m_s$ such that the system remains at rest.

### Answer Section

Please enter in a numeric value in $\rm{kg}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)