---
title: Toboggan Hill
topic: Work
author: Jake Bobowski
source: original
template_version: 1.1
attribution: standard
outcomes:
- 9.2.1.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- AK
assets: null
part1:
  type: number-input
  pl-customizations:
    label: $W_g=$
    allow-blank: true
    weight: 1
    suffix: $kJ$
    comparison: decdig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    label: $W_{fr}=$
    allow-blank: true
    weight: 1
    suffix: $kJ$
    comparison: decdig
    digits: 2
part3:
  type: number-input
  pl-customizations:
    label: $W_w=$
    allow-blank: true
    weight: 1
    suffix: $kJ$
    comparison: decdig
    digits: 2
part4:
  type: number-input
  pl-customizations:
    label: $V_f=$
    allow-blank: true
    weight: 1
    suffix: $m/s$
    comparison: decdig
    digits: 2
substitutions:
  params:
    vars:
      name: Emilia
      title: Toboggan hill
      units1_2_3: $kJ$
      units_4: $m/s$
    m: 75
    l: 99
    ang_horiz: 30
    fr: 89
    fwind: 24
    theta: 25
    v_i: 1
---
# {{ params.vars.title }}
{{params.vars.name}} ({{params.m}}$kg$) slides on their toboggan down a hill. The hill is {{params.l}} long and at an angle of {{params.ang_horiz}} $^\circ$ to the horizontal. They feel a friction force from the snow of $F\_{fr} = {{params.fr}} N$, and another force from the wind $F\_{wind} = {{params.fwind}} N$ blowing {{params.theta}}$^\circ$ below the horizontal. The system is {{params.vars.name}} and their sled.

## Part 1

How much work is down by gravity by the time {{params.vars.name}} gets to the bottom of the hill?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1_2_3 }}.

## Part 2

How much work is down by friction by the time {{params.vars.name}} gets to the bottom of the hill?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1_2_3 }}.

## Part 3

How much work is down by the wind by the time {{params.vars.name}} gets to the bottom of the hill?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1_2_3 }}.

## Part 4

If her inital speed at the top of the hill is $v = {{params.v_i}} {m\over s}$, what is her speed at the bottom of the hill?

### Answer Section

Please enter in a numeric value in {{ params.vars.units_4 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)