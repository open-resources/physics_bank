---
title: Football Runner
topic: Kinematics(1D)
author: Tarek Alkabbani
source: Original
template_version: 1.4
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
- TA
- APSC181
assets:
- Football_Runner.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a = $
    suffix: $\rm{m/s^2}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $a = $
    suffix: $\rm{m/s^2}$
myst:
  substitutions:
    params:
      vars:
        title: Football Runner
      dT: 400.0
      vM: 10.0
      d1: 160.0
      d2: 220.0
      vF: 7.5
---
# {{ params.vars.title }}
<img src="Football_Runner.png" width=600>

A football player participates in a ${{params.dT}} \ \rm{m}$ sprint. They starts accelerating uniformly from rest in a straight line, where they reach a top speed of ${{params.vM}} \ \rm{m/s}$ at the ${{params.d1}} \ \rm{m}$ mark. He then maintains this speed for the next ${{params.d2}} \ \rm{m}$. After that he slows down uniformly to a final speed of ${{params.vF}} \ \rm{m/s}$ at the finish line.

## Part 1

What is the acceleration just before the ${{params.d1}} \ \rm{m}$ mark?

### Answer Section

Please enter in a numeric value in $\rm{m/s^2}$.

## Part 2

What is the acceleration just before the finish line?

### Answer Section

Please enter in a numeric value in $\rm{m/s^2}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)