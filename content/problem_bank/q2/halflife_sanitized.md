---
title: Half-Life Question
type: symbolic-input
author: Andrew Rechnitzer
source: original
tags:
- half-life
outcomes:
- LO.math.2305
- LO.math.2304
assets:
substitutions:
  params:
    a: 100000
    b: 200000
    T: 365
    k: 400
    lambda: 600
    A: 1000000
  vars:
    units: s
    title: Half-Life Problem from Andrew
    digits_after_decimal: 2
---
# {{ vars.title }}

## Question Text

A sample of a certain material is undergoing radioactive decay.
Initially the sample weighs {{ params.a }}g.
After {{ params.T }} days, the sample weighs {{ params.b }}g.
Assuming the rate of decay is proportional to the mass of the sample, compute the half-life of the material.

The half life is:

## Answer Section

Please enter in a numeric value in {{ vars.units }} to {{ vars.digits_after_decimal }} decimal places.