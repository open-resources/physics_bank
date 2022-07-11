---
title: Archery Competition
topic: Template
author: Firas Moosvi
source: original
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes: null
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
- unknown
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.03
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: m/s
part2:
  type: number-input
  pl-customizations:
    rtol: 0.03
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: m
substitutions:
  params:
    vars:
      name: Santiago
      title: Archery Competition
      units: m/s
    x: 77
    arrow_v: 119
    theta: 15
    height: 208
---
# {{ params.vars.title }}
{{ params.vars.name }} is reading a novel that describes an athelete participating in an archery competition.
The athlete is {{ params.height }}cm tall and hits an amazing shot where they fire an arrow completely horizontally, and it lands {{ params.x }} m away from them.

The arrow is found embedded in the ground, at an angle of {{ params.theta }} degrees to the horizontal.

## Part 1

Neglecting air resistance and drag, what is the initial speed the arrow must have been fired at (to land {{ params.x }} m away)?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

If the arrow was instead fired at a 45 degree angle (instead of being shot horizontally), how far would it have gone if it was launched at a speed of {{ params.arrow_v }} m/s.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)