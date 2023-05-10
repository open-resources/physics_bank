---
title: Animal in an Elevator
topic: Work
author: Jake Bobowski
source: 2017 Final Q14
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 6.1.1.4
- 6.2.1.2
- 6.5.1.2
- 9.3.1.1
- 6.3.1.2
- 6.3.1.3
- 9.3.1.1
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
- PW
assets: null
part1:
  type: file-upload
  pl-customizations:
    file-names: FBD_p1.pdf
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\vec{N} = $
    suffix: $\rm{N}$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\vec{T} = $
    suffix: $\rm{N}$
part4:
  type: file-upload
  pl-customizations:
    file-names: FBD_p4.pdf
part5:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v = $
    suffix: $\rm{m/s}$
myst:
  substitutions:
    params_vars_animal: cat
    params_vars_title: Animal in an Elevator
    params_vars_units1: $\rm{N}$
    params_vars_units2: $\rm{m/s}$
    params_m_a: 1.99
    params_m_e: 29.2
    params_P: 1783
    params_a: ' + 5.73'
---
# {{ params_vars_title }}
A {{params.m_a}} $\rm{kg}$ {{params_vars_animal}} sits inside of a {{params.m_e}} $\rm{kg}$ elevator. The elevator is connected to a motor by a wire. The maximum power that can be produced by the motor is {{params_P}} $\rm{W}$.

## Part 1

Suppose that the elevator is accelerating upwards at {{params_a}} $\rm{\frac{m}{s^2}}$.

Treating the {{params_vars_animal}} and elevator as separate systems, draw a free-body diagram for the {{params_vars_animal}} and another for the elevator. Upload your diagrams as a single PDF.

### Answer Section

File upload box will be shown here.

## Part 2

Consider the acceleration in Part 1. What is the normal force from the floor on the {{params_vars_animal}}?

### Answer Section

Please enter in a numeric value in {{ params_vars_units1}}.

## Part 3

Consider the acceleration in Part 1. What is the tension in the wire?

### Answer Section

Please enter in a numeric value in {{ params_vars_units1}}.

## Part 4

Assume that the elevator is going upwards at a constant speed.

Now consider the system composed of the elevator and the {{params_vars_animal}} together.

Draw the free-body diagram for this system. Upload your diagram as a single PDF.

### Answer Section

File upload box will be shown here.

## Part 5

If the elevator is going upwards at a constant speed, with what speed is the elevator moving if the motor is delivering the maximum possible power?

### Answer Section

Please enter in a numeric value in {{ params_vars_units2}}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)