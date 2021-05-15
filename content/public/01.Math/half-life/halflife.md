---
title: Half-Life Question
topic: Math
author: Andrew Rechnitzer
source: original
tags:
- half-life
outcomes:
- LO.math.2305
- LO.math.2304
assets: null
part1:
  type: symbolic-input
  pl-options:
    allow-blank: true
substitutions:
  correct_answers: 45
  params:
    metadata:
      title: Half-Life Question
    a: '5.00000'
    b: '6.00000'
    T: '50.00000'
  vars:
    units: s
    digits_after_decimal: 5
---
# {{ params.metadata.title }}
## Question Text

A sample of a certain material is undergoing radioactive decay.
Initially the sample weighs {{ params.a }}g.
After {{ params.T }} days, the sample weighs {{ params.b }}g.
Assuming the rate of decay is proportional to the mass of the sample, compute the half-life of the material.

The half life is:
## Answer Section

Please enter in a numeric value in {{ vars.units }} to {{ vars.digits_after_decimal }} decimal places.
