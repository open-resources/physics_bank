---
title: A Flying Arrow
topic: Momentum and Impulse
author: Jake Bobowski
source: 2015 Practice Midterm 2 Q4
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 7.2.1.1
- 5.8.1.3
- 8.2.1.0
- 8.2.1.1
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- multi-chapter
length:
- long
tags:
- PW
- final_exam
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $p_x= $
    suffix: $kg\cdot m/s$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $K= $
    suffix: $J$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_x= $
    suffix: $m/s$
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $p_x= $
    suffix: $kg\cdot m/s$
part5:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $K= $
    suffix: $J$
myst:
  substitutions:
    params_vars_name1: Maya
    params_vars_name2: Ximena
    params_vars_title: A Flying Arrow
    params_vars_unit1: $kg\cdot m/s$
    params_vars_unit2: $J$
    params_vars_unit3: $m/s$
    params_m: 0.228
    params_v_x: -96.0
    params_x1: 7.25
    params_x2: 18.1
---
# {{ params_vars_title }}
{{ params_vars_name1 }} and {{ params_vars_name2 }} watch an arrow fly past them.
The arrow has mass $m = $ {{ params_m }} $kg$.
{{ params_vars_name1 }} is sitting on a stump and sees the arrow move with velocity $v_x = $ {{ params.v_x }} $m/s$.
{{ params_vars_name1 }} also notes that {{ params_vars_name2 }} is riding a horse and measures {{ params_vars_name2 }}'s position to be $x(t) = $ {{ params_x1 }} $m$ + ({{ params_x2 }} $m/s$) $t$, where $t$ is time measured in seconds.

## Part 1

According to {{ params_vars_name1 }}, what is the arrow's momentum?

### Answer Section

Please enter in a numeric value in {{ params_vars_unit1 }}.

## Part 2

According to {{ params_vars_name1 }}, what is the arrow's kinetic energy?

### Answer Section

Please enter in a numeric value in {{ params_vars_unit2 }}.

## Part 3

According to {{ params_vars_name2 }}, what is the arrow's velocity?

### Answer Section

Please enter in a numeric value in {{ params_vars_unit3 }}.

## Part 4

According to {{ params_vars_name2 }}, what is the arrow's momentum?

### Answer Section

Please enter in a numeric value in {{ params_vars_unit1 }}.

## Part 5

According to {{ params_vars_name2 }}, what is the arrow's kinetic energy?

### Answer Section

Please enter in a numeric value in {{ params_vars_unit2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)