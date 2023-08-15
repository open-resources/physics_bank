---
title: Cars on Hills
topic: Rotational Motion
author: Jake Bobowski
source: 2012 Midterm 2 Q4
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.9.1.3
- 5.7.1.1
- 6.12.1.1
- 10.3.2.2
difficulty:
- hard
randomization:
- 2
taxonomy:
- undefined
span:
- multi-chapter
length:
- long
tags:
- MP
- NR
- final_exam
assets:
- q4.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $a=$
    suffix: $\rm{\frac{m}{s^2}}$
    allow-blank: true
    weight: 1
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $a=$
    suffix: $\rm{\frac{m}{s^2}}$
    allow-blank: true
    weight: 1
myst:
  substitutions:
    params_vars_title: Cars on Hills
    params_vars_units: "$\rm{\frac{m}{s^2}}$"
    params_v: 21
    params_r: 167
    params_mu: 6.12
---
# {{ params_vars_title }}
Two cars are driving at {{params_v}} $\rm{m/s}$ along the road shown in the figure.
Car B is at the bottom of a hill and car C is at the top. Both hills have a {{params_r}} $\rm{m}$ radius of curvature.
Suppose both cars suddenly brake hard and start to skid.

<img src="q4.png" width=400 alt="Two cars on two hills on equal raduis of curvature">

## Part 1

What is the tangential (parallel to the road) acceleration of car B?
Assume $\mu_k = 0.850$ and car B has velocity in the positive direction.

### Answer Section

Please enter in a numeric value in {{ params_vars_units}}.

## Part 2

What is the tangential (parallel to the road) acceleration of car C?
Assume $\mu_k = 0.850$ and car C has velocity in the positive direction.

### Answer Section

Please enter in a numeric value in {{ params_vars_units}}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)