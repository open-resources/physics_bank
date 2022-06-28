---
title: Roller Coaster
topic: Force
author: Jake Bobowski
source: Practice Final 2012 Q16
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 5.6.1.0
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
part2:
  type: number-input
  label: $v_2=$
  pl-customizations:
    allow-blank: true
    weight: 1
    suffix: $m/s$
part3:
  type: number-input
  label: $N=$
  pl-customizations:
    allow-blank: true
    weight: 1
    suffix: $N$
substitutions:
  params:
    vars:
      title: Roller Coaster
      units: m/s
      units_2: N
    r: 10.0
    m: 239
---
# {{ params.vars.title }}
A roller-coaster car moves around a vertical circular loop of radius $R$ = {{params.r}} m.
The total mass of the car (including passengers) is {{params.m}} kg.

<img src="Q16.png" width=300>

## Part 1

What speed must the car have at the top of the loop so that it will just make it over the top without any assistance from the track?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

What speed will the car subsequently have at the bottom of the loop (after going through the loop)?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 3

What will be the normal force on a passenger at the bottom of the loop?

### Answer Section

Please enter in a numeric value in {{ params.vars.units_2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)