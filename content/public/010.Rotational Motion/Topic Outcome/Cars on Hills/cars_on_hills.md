---
title: Cars on Hills
topic: Rotational Motion
author: Jake Bobowski
source: 2012 Midterm 2 Q4
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 6.9.1.0
- 5.7.1.0
- 6.12.2.0
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
- final_exam
assets:
- q4.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $a=$
    allow-blank: true
    weight: 1
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $a=$
    allow-blank: true
    weight: 1
substitutions:
  params:
    vars:
      title: Cars on Hills
      units: "$\frac{m}{s^2}"
    v: 20
    r: 131
    mu: 8.5
---
# {{ params.vars.title }}
Two cars are driving at {{params.v}} $m/s$ along the road shown in the figure.
Car B is at the bottom of a hill and car C is at the top. Both hills have a {{params.r}} $m$ radius of curvature.
Suppose both cars suddenly brake hard and start to skid.

<img src="q4.png" width=400 alt="Two cars on two hills on equal raduis of curvature">

## Part 1

What is the tangential (i.e., the acceleration parallel to the road) of car B?
Assume $\mu_k = 0.850$.

### Answer Section

Please enter in a numeric value in {{ params.vars.units}}.

## Part 2

What is the tangential (i.e., the acceleration parallel to the road) of car C?
Assume $\mu_k = 0.850$.

### Answer Section

Please enter in a numeric value in {{ params.vars.units}}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)