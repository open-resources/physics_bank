---
title: Olympian Dive
topic: Force
author: Ranya Ghosh
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- null
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
- RG
- JR
- APSC181
assets:
- OlympianDive.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\omega = $
    suffix: $\rm{rad/s}$
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\theta = $
    suffix: $^\circ$
    comparison: sigfig
    digits: 2
myst:
  substitutions:
    params_vars_title: Olympic Diving
    params_vars_units: m
    params_W: 153
    params_d: 1.2
    params_k: 1.5
    params_theta: 25
    params_h: 15
---
# {{ params_vars_title }}
<img src="OlympianDive.png" width=100%>

A diver is practicing their dives for the Olympics! They have a weight of $W = {{ params_W }} \ \rm{lb}$. In figure (**a**), their center of gravity is $d = {{ params_d }} \ \rm{ft}$ from the board, and the rotation radius about their center of gravity is $k_G = {{ params_k }} \ \rm{ft}$. When they jump off the board, an angle of ${{ params_theta }}^\circ$ is made from the board. The height of the board is $h = {{ params_h }} \ \rm{ft}$ from the water.

## Part 1

What is the angular velocity of the diver as they jump off the board?
(Hint: Consider the energy from their centre of gravity, and how it realates to their rotational movement)

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 2

How many revolutions do they complete before they land in the water?

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)