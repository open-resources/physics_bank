---
title: Space Velocity
topic: Momentum and Impulse
author: Jake Bobowski
source: Final 2016 P2 Q7
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 7.2.1.2
- 7.2.1.4
- 7.2.1.5
- 7.5.1.3
- 7.5.1.4
- 7.5.1.5
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- HZ
assets: null
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\hat{\imath} = $
    suffix: $\rm{m/s}$
    comparison: sigfig
    digits: 3
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\hat{\jmath} = $
    suffix: $\rm{m/s}$
    comparison: sigfig
    digits: 3
part3:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\Delta K=$
    suffix: $\rm{J}$
    comparison: sigfig
    digits: 1
part4:
  type: number-input
  pl-customizations:
    allow-blank: true
    weight: 1
    label: $\Delta K=$
    suffix: $\rm{J}$
    comparison: sigfig
    digits: 1
part5:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params_vars_title: Space Velocity
    params_vars_units1: $\rm{m/s}$
    params_vars_units2: $\rm{J}$
    params_m: 104
    params_left_arm: 6
    params_head: 13
    params_V_L_i: 14
    params_V_L_j: 6
    params_V_H_i: -22
    params_V_H_j: -14
    params_t: 1.0
    params_part5_ans1_value: His head required more force
    params_part5_ans2_value: His left arm required more force
    params_part5_ans3_value: There is not enough information.
---
# {{ params_vars_title }}
Bender the robot ({{params_m}} $\rm{kg}$) is floating out in deep space.
Does it matter what velocity he has?
It doesn't.
His velocity is zero.
He decides that he wants to throw his head towards home.
First his right arm removes his left arm ({{params.left_arm}} $\rm{kg}$) and throws it so that it has a final velocity of $V_L = {{params.V_L_i}} \rm{m\over s} \hat i + {{params.V_L_j}} \rm{m \over s} \hat j$.
Then his right arm removes his head ({{params_head}} $\rm{kg}$) and throws it so that it has final velocity $V_H = {{params.V_H_i}} \rm{m\over s} \hat i + {{params.V_H_j}} \rm{m \over s} \hat j$.
Velocities are given in terms of an observer who is also at rest.

## Part 1

What is the final velocity $\hat{\imath}$ vector of his torso?

### Answer Section

Please enter in a numeric value in {{ params_vars_units1 }}.

## Part 2

What is the final velocity $\hat{\jmath}$ vector of his torso?

### Answer Section

Please enter in a numeric value in {{ params_vars_units1 }}.

## Part 3

How much source energy does he expend when he throws his left arm?

### Answer Section

Please enter in a numeric value in {{ params_vars_units2 }}.

## Part 4

How much source energy does he expend when he throws his head?

### Answer Section

Please enter in a numeric value in {{ params_vars_units2 }}.

## Part 5

The throwing of his left arm and the throwing of his head both take only $\Delta T = {{ params_t }}$ $\rm{s}$, which one required more average force?

### Answer Section

- {{ params_part5_ans1_value }}
- {{ params_part5_ans2_value }}
- {{ params_part5_ans3_value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)