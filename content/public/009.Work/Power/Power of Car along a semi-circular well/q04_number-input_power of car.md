---
title: Power of car along a semi-circular well
topic: Work
author: Ammar Zavahir
source: original
template_version: 1.0
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 9.3.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- APSC181
- A.Z
assets:
- part1.png
- part2.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $P= $
    suffix: $\rm{kW}$
    comparison: sigfig
    digits: 2
part2:
  type: multiple-choice
  pl-customizations:
    weight: 1
    fixed-order: true
    hide-letter-keys: true
myst:
  substitutions:
    params:
      vars:
        title: Power of car along a circular arc
      m: 9200.0
      v: 97
      a: 74
      part2:
        ans1:
          value: "$\rm{A}$"
        ans2:
          value: "$\rm{B}$"
        ans3:
          value: "$\rm{C}$"
---
# {{ params.vars.title }}
A car is travelling up a smooth semi-circular slope with a constant speed of ${{ params.v }}\ \rm{km/h}$.

<img src="part1.png" width=800>

## Question Text

What is the additional power which has to be developed in the engine to keep the car moving at this speed at $\alpha = {{ params.a }}^{\circ}$ mark?
<br>
Neglect air resistance. Treat the car as a particle with mass $M= {{ params.m }}\ \rm{kg}$

### Answer Section

Please enter in a numeric value in W.

## Part 2

At what point along the circular arc is the power developed by the engine the maximum if the speed is kept constant?

<img src="part2.png" width=800>

### Answer Section

- {{ params.part2.ans1.value}}
- {{ params.part2.ans2.value}}
- {{ params.part2.ans3.value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)