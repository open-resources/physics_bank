---
title: Block on a Wall
topic: Force
author: Jake Bobowski
source: 2012 Midterm 2 Q5
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 6.9.1.0
- 6.1.1.4
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- average
tags:
- MP
assets:
- q5.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F= $
    suffix: N
substitutions:
  params:
    vars:
      title: Block on a Wall
      units: N
    theta: 41
    m: 3
    mu: 0.228
---
# {{ params.vars.title }}
A {{params.m}} kg wood block slides down a vertical wall while you push on it at a {{params.theta}}$^\circ$ angle.

<img src="q5.png" width=200px alt="Box pushed against a wall by a force at angle theta">

## Question Text

What magnitude force should you apply to cause the block to slide down at constant speed? The coefficient of kinetic friction is $\mu_k$ = {{params.mu}}.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)