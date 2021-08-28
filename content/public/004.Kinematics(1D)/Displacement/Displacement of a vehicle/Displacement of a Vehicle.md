---
title: Displacement of a Vehicle
topic: Kinematics(1D)
author: Jake Bobowski
source: 2012 Midterm 1 Q1 Section 002
template_version: 1.1
attribution: standard
outcomes:
- 4.1.1.0
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
    label: $\Delta r = $
    suffix: blocks
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      vehicle: car
      title: Displacement of a Vehicle
      units: blocks
    c1: 85
    c2: 42
    c3: 24
    dir1: east
    dir2: west
    dir3: east
---
# {{ params.vars.title }}
A {{ params.vars.vehicle }} moves {{ params.c1}} blocks due {{ params.dir1}}, {{ params.c2 }} blocks due {{ params.dir2}}, and another {{ params.c3 }} blocks due {{ params.dir3}}.

## Question Text

Assume all blocks are of equal size. What is the magnitude of the {{ params.vars.vehicle }}'s displacement, start to finish?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)