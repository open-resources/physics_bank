---
title: Roller Coaster
topic: Kinematics(2D and 3D)
author: Jake Bobowski
source: Practice Final 2012 Q16
template_version: 1.1
attribution: standard
outcomes:
- 5.6.1.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- EW
assets:
- Q16.png
part1:
  type: number-input
  label: $v_1=$
  pl-customizations:
    allow-blank: true
    weight: 1
    suffix: $m/s$
    comparison: sigfig
    digits: 3
part2:
  type: number-input
  label: $v_2=$
  pl-customizations:
    allow-blank: true
    weight: 1
    suffix: $m/s$
    comparison: sigfig
    digits: 3
part3:
  type: number-input
  label: $N=$
  pl-customizations:
    allow-blank: true
    weight: 1
    suffix: $N$
    comparison: sigfig
    digits: 3
substitutions:
  params:
    vars:
      title: Roller Coaster
      units: m/s
      units_2: N
    r: 14.0
    m: 246
---
# {{ params.vars.title }}
A roller-coaster car moves around a vertical circular loop of radius $R$ = {{params.r}} m.
The total mass of the car (including passengers) is {{params.m}} kg.

<img src="Q16.png" width=300>

## Part 1

What speed must the car have so that it will just make it over the top without any assistance from the track?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

What speed will the car subsequently have at the bottom of the loop?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 3

What will be the normal force on a passenger at the bottom of the loop?

### Answer Section

Please enter in a numeric value in {{ params.vars.units_2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)