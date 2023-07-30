---
title: Pendulum
topic: Energy
author: Ranya Ghosh
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.12.1.1
- 8.2.1.1
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
- PJ
assets:
- Pendulum.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_A= $
    suffix: $ \rm{m/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_T= $
    suffix: $ \rm{N}$
myst:
  substitutions:
    params_vars_title: Pendulum
    params_vars_units_part1: "$\rm{m/s}$"
    params_vars_units_part2: "$\rm{N}$"
    params_m: 0.4
    params_l: 1.2
    params_theta: 45
    params_mainText: A $0.4 \ \rm{kg}$ yoyo attached to a string of length $1.2 \
      \rm{m}$ is held horizontal before being released. After some time it reaches
      point $A$ with angle $45^\circ$.
    params_part1Text: Find the speed of the yoyo at point $A$
    params_part2Text: Find the tension in the string at point $A$
---
# {{ params_vars_title }}
{{params_mainText}}

<img src="Pendulum.png" width=500 alt="A pendulum made of a ball of mass m on a string of length L. The pendulum starts at horizontal and goes to angle theta." >

## Part 1

{{params_part1Text}}

### Answer Section

Please enter in a numeric value in {{ params_vars_units_part1 }}.

## Part 2

{{params_part2Text}}

### Answer Section

Please enter in a numeric value in {{ params_vars_units_part2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)