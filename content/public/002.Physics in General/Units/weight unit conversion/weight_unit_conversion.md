---
title: Weight Unit Conversion
topic: Physics in General
author: Peyman Yousefi
source: APSC 181, Lecture 2, Q1
template_version: 1.1
attribution: standard
outcomes:
- 2.2.1.3
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- A.P.
- APSC 181 - LA
assets: null
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $W= $
    suffix: $N$
    rtol: 0.02
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $m= $
    suffix: $slug$
    rtol: 0.02
part3:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $m= $
    suffix: $kg$
    rtol: 0.02
substitutions:
  params:
    vars:
      title: Weight units conversion
    w_lbs: 168
---
# {{ params.vars.title }}
A students has a mass of {{params.w_lbs}} $lbs$.

## Part 1

What is their weight in Newtons?

### Answer Section

Please enter in a numeric value in Newtons.

## Part 2

What is their mass in $slug$?

### Answer Section

Please enter in a numeric value in $slug$.

## Part 3

What is their mass in kilograms?

### Answer Section

Please enter in a numeric value in kilograms.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)