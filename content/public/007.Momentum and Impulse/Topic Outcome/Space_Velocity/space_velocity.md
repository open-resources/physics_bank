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
- undefined
taxonomy:
- undefined
span:
- undefined
length:
- medium
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
substitutions:
  params:
    vars:
      title: Space Velocity
      units1: $\rm{m/s}$
      units2: $\rm{J}$
    m: 101
    left_arm: 6
    head: 14
    V_L_i: 14
    V_L_j: 7
    V_H_i: -22
    V_H_j: -12
    t: 0.7
    part5:
      ans1:
        value: His head required more force
      ans2:
        value: His left arm required more force
      ans3:
        value: There is not enough information.
---
# {{ params.vars.title }}
Bender the robot ({{params.m}} $\rm{kg}$) is floating out in deep space.
Does it matter what velocity he has?
It doesn't.
His velocity is zero.
He decides that he wants to throw his head towards home.
First his right arm removes his left arm ({{params.left_arm}} $\rm{kg}$) and throws it so that it has a final velocity of $V_L = {{params.V_L_i}} \rm{m\over s} \hat i + {{params.V_L_j}} \rm{m \over s} \hat j$.
Then his right arm removes his head ({{params.head}} $\rm{kg}$) and throws it so that it has final velocity $V_H = {{params.V_H_i}} \rm{m\over s} \hat i + {{params.V_H_j}} \rm{m \over s} \hat j$.
Velocities are given in terms of an observer who is also at rest.

## Part 1

What is the final velocity $\hat{\imath}$ vector of his torso?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1 }}.

## Part 2

What is the final velocity $\hat{\jmath}$ vector of his torso?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1 }}.

## Part 3

How much source energy does he expend when he throws his left arm?

### Answer Section

Please enter in a numeric value in {{ params.vars.units2 }}.

## Part 4

How much source energy does he expend when he throws his head?

### Answer Section

Please enter in a numeric value in {{ params.vars.units2 }}.

## Part 5

The throwing of his left arm and the throwing of his head both take only $\Delta T = {{ params.t }}$ $\rm{s}$, which one required more average force?

### Answer Section

- {{ params.part5.ans1.value }}
- {{ params.part5.ans2.value }}
- {{ params.part5.ans3.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)