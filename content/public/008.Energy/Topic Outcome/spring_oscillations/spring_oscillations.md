---
title: Simple Harmonic Spring
topic: Energy
author: Jake Bobowski
source: 2013 Final Q11
template_version: 1.0
attribution: standard
outcomes:
- 15.2.2.0
- 15.2.1.4
- 7.2.1.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- MP
assets: null
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: m/s
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $k= $
    suffix: N/m
    comparison: sigfig
    digits: 2
part3:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $A=$
    suffix: m
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Simple harmonic spring
      units1: m/s
      units2: N/m
      units3: m
    m: 333
    T: 1.9
    E: 6.5
---
# {{ params.vars.title }}
A {{params.m}} g object is attached to a spring and executes simple harmonic motion with a period of {{params.T}} s.
If the total energy of the system is {{params.E}} J, find:

## Part 1

(a) the maximum speed of the object

### Answer Section

Please enter a numeric value in {{ params.vars.units1 }}.

## Part 2

(b) the spring constant of the spring

### Answer Section

Please enter a numeric value {{ params.vars.units2 }}.

## Part 3

(c) the amplitude of the motion

### Answer Section

Please enter a numeric value in {{ params.vars.units3 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)