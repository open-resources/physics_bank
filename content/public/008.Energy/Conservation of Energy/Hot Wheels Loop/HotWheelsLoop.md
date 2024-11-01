---
title: Toy Car Loop
topic: Energy
author: Ranya Ghosh
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- null
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
span:
- undefined
length:
- undefined
tags:
- RG
- JR
- APSC181
assets:
- HotWheelsLoop.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $h = $
    suffix: $\rm{m}$
    comparison: sigfig
    digits: 2
myst:
  substitutions:
    params:
      vars:
        title: Hot Wheels Loop
        units: m
      m: 0.09
      r: 0.24
---
# {{ params.vars.title }}
<img src="HotWheelsLoop.png" width=400>

A child creates a track to play with their toy car. The toy car has a mass of $m = {{ params.m }} \ \rm{kg}$ and goes down a drop with height $h$ which ends with a loop, before continuing onto a flat track. The loop has a radius of $r = {{ params.r }} \ \rm{m}$. The child has no clue how high the track must start for the car to make it fully through the loop without dropping.

## Part 1

Find the height the car must start at to fully pass through the loop.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)