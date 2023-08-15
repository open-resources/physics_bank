---
title: Crate A & B pushed up a hill
topic: Kinematics(2D and 3D)
author: Ranya Ghosh
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 4.7.3.0
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
- RG
assets:
- crate.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a = $
    suffix: $\rm{m/s^2}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x$
    suffix: $\rm{m}$
myst:
  substitutions:
    params_vars_title: Crate A & B pushed up a hill
    params_vars_units: m, m/$s^2$
    params_m1: 5.71
    params_m2: 15.12
    params_v0: 18
    params_theta: 61.18
---
# {{ params_vars_title }}
A person is pushing crate $\rm{A}$ and $\rm{B}$ up a hill to have it slide down into an area for pickup and loading.
Crate A has a mass of $m_1 = {{ params_m1 }} \ \rm{kg}$ and Crate B has a mass of $m_2 = {{params_m2}} \ \rm{kg}$.
The hill makes an angle of $\theta =  {{ params_theta }}^{\circ}$ with the horizontal.

<img src="crate.png" width=800>

## Part 1

What is the acceleration on those crates as they move up the hill?

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 2

How far will the boxes go until coming to a stop if the speed is $v_0 = {{params_m1}}\ \rm{m/s}$?

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)