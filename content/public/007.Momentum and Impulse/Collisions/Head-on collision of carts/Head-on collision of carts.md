---
title: Head-on Collision of Carts
topic: Momentum and Impulse
author: Jake Bobowski
source: 2017 Midterm 2 Section 002 Q3
template_version: 1.1
attribution: standard
outcomes:
- 7.5.1.3
- 7.5.1.4
- 7.5.1.8
- 7.5.1.9
- 7.4.1.0
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
    label: $v= $
    suffix: $(m/s)\; \hat{\imath}$
    comparison: sigfig
    digits: 3
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $v_f= $
    suffix: $(m/s)\; \hat{\imath}$
    comparison: sigfig
    digits: 3
part3:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $v_f= $
    suffix: $(m/s)\; \hat{\imath}$
    comparison: sigfig
    digits: 3
substitutions:
  params:
    vars:
      title: Head-on Collision of Carts
      units: $(m/s)\; \hat{\imath}$
    c1: 6
    c2: 2
    v0: 14.0
---
# {{ params.vars.title }}
A cart of mass ${{ params.c1 }}m$ moving with velocity $\vec{v_0} = ( {{ params.v0 }} m/s)\hat{\imath}$ collides head-on with a cart of mass ${{ params.c2 }}m$ that is initially at rest.
Ignore friction.

## Part 1

If the collision is perfectly inelastic, what is the final velocity of each cart?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

If the collision is elastic, what is the final velocity of each cart?
Enter the final velocity of the cart with mass ${{ params.c1 }}m$.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 3

If the collision is elastic, what is the final velocity of each cart?
Enter the final velocity of the cart with mass ${{ params.c2 }}m$.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)