---
title: Power of a Horse
topic: Work
author: Peyman Yousefi
source: APSC 181, Lecture 18, Q3
template_version: 1.2
attribution: standard
singleVariant: false
showCorrectAnswer: false
outcomes:
- 9.3.1.1
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- section
length:
- average
tags:
- APSC 181 - LA
- JR
assets:
- Power of a Biker.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $P= $
    suffix: $W$
substitutions:
  params:
    vars:
      title: Power of a Horse
      units: $W$
    v_kph: 16
    mass_kg: 159
    grade: 9
---
# {{ params.vars.title }}
<img src="Power of a Biker.png" width=400>

A horse and rider together weigh {{ params.mass_kg }} $kg$.
What power does the horse output when riding up a {{ params.grade }}% grade at a speed of {{ params.v_kph }} $km/hr$?

## Part 1

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)