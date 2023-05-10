---
title: Terminal Velocity of a Coffee Filter
topic: Physics in General
author: Jake Bobowski
source: 2015 Final Q19
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 2.4.1.2
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
assets: null
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\Delta v_T= $
    suffix: $m/s$
    digits: 1
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $v_T= $
    suffix: $m/s$
    digits: 2
part3:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $ \Delta b = $
    suffix: $kg/s$
    digits: 1
part4:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $ b = $
    suffix: $kg/s$
    digits: 2
myst:
  substitutions:
    params_vars_title: Terminal Velocity of a Coffee Filter
    params_vars_name: Maya
    params_vars_unit1: $m/s$
    params_vars_unit2: $kg/s$
    params_m: 5
    params_d_m: 46
    params_sd: 0.036
    params_v1: 0.74
    params_v2: 0.75
    params_v3: 0.77
    params_v4: 0.85
    params_v5: 0.78
    params_v6: 0.8
---
# {{ params_vars_title }}
In one of the PHYS 111 labs {{ params_vars_name }} measured the terminal velocity $v_T$ of a coffee filter of mass $m$ falling through the air.
In equilibrium, the drag force acting on the coffee filter exactly balances the gravitational force on the filter such that:

$bv_T = mg$

where $b$ is a "drag coefficient" determined by the shape of the filter and the density of the air.

Suppose that the following six measurements of a coffee filter's terminal velocity were made:

| Trial     | $v_T$ ($m/s$) |
| ----------- | ----------- |
| 1     |  {{ params_v1 }}     |
| 2   |   {{ params_v2 }}      |
| 3     |  {{ params_v3 }}     |
| 4   |   {{ params_v4 }}      |
| 5     |  {{ params_v5 }}     |
| 6   |   {{ params_v6 }}      |

The standard deviation of this data set is {{ params_sd }} $m/s$.

## Part 1

Use the experimental data to determine the uncertainty in the average value of the terminal velocity.  State your answer using the appropriate number of significant figures.

### Answer Section

Please enter in a numeric value in {{ params_vars_unit1 }}.

## Part 2

Use the experimental data to determine the average value of the terminal velocity.  State your answer using the appropriate number of significant figures.

### Answer Section

Please enter in a numeric value in {{ params_vars_unit1 }}.

## Part 3

If the coffee filter has a mass of $m = $ {{ params_m }} $\pm$ {{ params.d_m }} $g$, determine the value of the uncertainty in the drag coefficient $b$.  State your answer using the appropriate number of significant figures. Assume that $g= 9.81 kg/s$ and has negligible uncertainty.

### Answer Section

Please enter in a numeric value in {{ params_vars_unit2 }}.

## Part 4

If the coffee filter has a mass of $m = $ {{ params_m }} $\pm$ {{ params.d_m }} $g$, determine the value of the drag coefficient $b$.  State your answer using the appropriate number of significant figures. Assume that $g= 9.81 kg/s$ and has negligible uncertainty.

### Answer Section

Please enter in a numeric value in {{ params_vars_unit2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)