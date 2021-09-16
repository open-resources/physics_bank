---
title: Terminal Velocity of a Coffee Filter
topic: Physics in General
author: Jake Bobowski
source: 2015 Final Q19
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
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
    comparison: sigfig
    digits: 1
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $v_T= $
    suffix: $m/s$
    comparison: sigfig
    digits: 2
part3:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $ \Delta b = $
    suffix: $kg/s$
    comparison: sigfig
    digits: 1
part4:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $ b = $
    suffix: $kg/s$
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Terminal Velocity of a Coffee Filter
      name: Ximena
      unit1: $m/s$
      unit2: $kg/s$
    m: 4
    d_m: 35
    sd: 0.046
    v1: 0.97
    v2: 0.87
    v3: 0.82
    v4: 0.85
    v5: 0.89
    v6: 0.87
---
# {{ params.vars.title }}
In one of the PHYS 111 labs {{ params.vars.name }} measured the terminal velocity $v_T$ of a coffee filter of mass $m$ falling through the air.
In equilibrium, the drag force acting on the coffee filter exactly balances the gravitational force on the filter such that:

$bv_T = mg$

where $b$ is a "drag coefficient" determined by the shape of the filter and the density of the air.

Suppose that the following six measurements of a coffee filter's terminal velocity were made:

| Trial     | $v_T$ ($m/s$) |
| ----------- | ----------- |
| 1     |  {{ params.v1 }}     |
| 2   |   {{ params.v2 }}      |
| 3     |  {{ params.v3 }}     |
| 4   |   {{ params.v4 }}      |
| 5     |  {{ params.v5 }}     |
| 6   |   {{ params.v6 }}      |

The standard deviation of this data set is {{ params.sd }} $m/s$.

## Part 1

Use the experimental data to determine the uncertainty in the average value of the terminal velocity.  State your answer using the appropriate number of significant figures.

### Answer Section

Please enter in a numeric value in {{ params.vars.unit1 }}.

## Part 2

Use the experimental data to determine the average value of the terminal velocity.  State your answer using the appropriate number of significant figures.

### Answer Section

Please enter in a numeric value in {{ params.vars.unit1 }}.

## Part 3

If the coffee filter has a mass of $m = $ {{ params.m }} $\pm$ {{ params.d_m }} $g$, determine the value of the uncertainty in the drag coefficient $b$.  State your answer using the appropriate number of significant figures. Assume that $g= 9.81 kg/s$ and has negligible uncertainty.

### Answer Section

Please enter in a numeric value in {{ params.vars.unit2 }}.

## Part 4

If the coffee filter has a mass of $m = $ {{ params.m }} $\pm$ {{ params.d_m }} $g$, determine the value of the drag coefficient $b$.  State your answer using the appropriate number of significant figures. Assume that $g= 9.81 kg/s$ and has negligible uncertainty.

### Answer Section

Please enter in a numeric value in {{ params.vars.unit2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)