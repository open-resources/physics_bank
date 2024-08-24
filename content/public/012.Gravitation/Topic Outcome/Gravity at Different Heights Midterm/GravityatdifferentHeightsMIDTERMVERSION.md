---
title: Gravity at Different Heights
topic: Gravitation
author: James Ropotar
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
- JR
- APSC181
- Midterm 2023
assets: null
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\frac{g}{g_0} = $
    suffix: null
    comparison: sigfig
    digits: 4
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\frac{g}{g_0} = $
    suffix: null
    digits: 4
myst:
  substitutions:
    params:
      vars:
        title: Gravity at Different Heights
        units: "$\rm{m/s^2}$"
      h: 3217
      h2: 14564
      r: 6371000.0
---
# {{ params.vars.title }}
In this class, we will often assume gravity to be $9.81 \ \rm{m/s^2}$ in all earthbound circumstances, including in tall buildings, with airplanes, and in many other situations at heights far above the surface level. But is this truly accurate? Take the radius at sea level of the earch to be $R = {{ params.r }} \ \rm{m}$

## Part 1

What is the ratio of gravity felt on a mountain top, $h = {{ params.h }} \ \rm{m}$ above sea level, when compared to the $9.81 \ \rm{m/s^2}$ at the surface? (Answer to 4 Significant Figures)

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

What is the ratio of gravity felt on an airplane, $h = {{ params.h2 }} \ \rm{m}$ above sea level, when compared to the $9.81 \ \rm{m/s^2}$ at the surface? (Answer to 4 Significant Figures)

### Answer Section

Please enter in a numeric value in m/s$^2$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)