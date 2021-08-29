---
title: A Flying Arrow
topic: Kinematics(2D and 3D)
author: Jake Bobowski
source: 2015 Practice Midterm 2 Q4
template_version: 1.1
attribution: standard
outcomes:
- 7.2.1.1
- 5.8.1.3
- 8.2.1.0
- 8.2.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- PW
assets: null
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $p_x= $
    suffix: $kg\cdot m/s$
    comparison: sigfig
    digits: 3
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $K= $
    suffix: $J$
    comparison: sigfig
    digits: 3
part3:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $v_x= $
    suffix: $m/s$
    comparison: sigfig
    digits: 3
part4:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $p_x= $
    suffix: $kg\cdot m/s$
    comparison: sigfig
    digits: 3
part5:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $K= $
    suffix: $J$
    comparison: sigfig
    digits: 3
substitutions:
  params:
    vars:
      name1: Mateo
      name2: Santiago
      title: A Flying Arrow
      unit1: $kg\cdot m/s$
      unit2: $J$
      unit3: $m/s$
    m: 0.127
    v_x: -112.0
    x1: 10.1
    x2: 15.5
---
# {{ params.vars.title }}
{{ params.vars.name1 }} and {{ params.vars.name2 }} watch an arrow fly past them.  The arrow has mass $m = $ {{ params.m }} $kg$.  {{ params.vars.name1 }} is sitting on a stump and sees the arrow move with velocity $v_x = $ {{ params.v_x }} $m/s$. {{ params.vars.name1 }} also notes that {{ params.vars.name2 }} is riding a horse and measures {{ params.vars.name2 }}'s position to be $x = $ {{ params.x1 }} $m$ + ({{ params.x2 }} $m/s$) $t$ where $t$ is time measured in seconds.

## Part 1

According to {{ params.vars.name1 }}, what is the arrow's momentum?

### Answer Section

Please enter in a numeric value in {{ params.vars.unit1 }}.

## Part 2

According to {{ params.vars.name1 }}, what is the arrow's kinetic energy?

### Answer Section

Please enter in a numeric value in {{ params.vars.unit2 }}.

## Part 3

According to {{ params.vars.name2 }}, what is the arrow's velocity?

### Answer Section

Please enter in a numeric value in {{ params.vars.unit3 }}.

## Part 4

According to {{ params.vars.name2 }}, what is the arrow's momentum?

### Answer Section

Please enter in a numeric value in {{ params.vars.unit1 }}.

## Part 5

According to {{ params.vars.name2 }}, what is the arrow's kinetic energy?

### Answer Section

Please enter in a numeric value in {{ params.vars.unit2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)