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
substitutions:
  params:
    vars:
      animal: hamster
      title: Animal in an Elevator
      units1: $\rm{N}$
      units2: $\rm{m/s}$
    m_a: 4.09
    m_e: 29.8
    P: 1773
    a: ' + 8.6'
---
# {{ params.vars.title }}
A {{params.m_a}} $\rm{kg}$ {{params.vars.animal}} sits inside of a {{params.m_e}} $\rm{kg}$ elevator. The elevator is connected to a motor by a wire. The maximum power that can be produced by the motor is {{params.P}} $\rm{W}$.

## Part 1

Suppose that the elevator is accelerating upwards at {{params.a}} $\rm{\frac{m}{s^2}}$.

Treating the {{params.vars.animal}} and elevator as separate systems, draw a free-body diagram for the {{params.vars.animal}} and another for the elevator. Upload your diagrams as a single PDF.

### Answer Section

File upload box will be shown here.

## Part 2

Consider the acceleration in Part 1. What is the normal force from the floor on the {{params.vars.animal}}?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1}}.

## Part 3

Consider the acceleration in Part 1. What is the tension in the wire?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1}}.

## Part 4

Assume that the elevator is going upwards at a constant speed.

Now consider the system composed of the elevator and the {{params.vars.animal}} together.

Draw the free-body diagram for this system. Upload your diagram as a single PDF.

### Answer Section

File upload box will be shown here.

## Part 5

If the elevator is going upwards at a constant speed, with what speed is the elevator moving if the motor is delivering the maximum possible power?

### Answer Section

Please enter in a numeric value in {{ params.vars.units2}}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)