---
title: Collision of a Cart with a Spring
topic: Energy
author: Jake Bobowski
source: 2015 Final Q11
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 8.3.3.0
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- average
tags:
- PW
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $m/s$
substitutions:
  params:
    vars:
      title: Collision of a Cart with a Spring
      units: m/s
    m: 49
    k: 353
    x: 75
---
# {{ params.vars.title }}
A  {{ params.m }}  $kg$  runaway  grocery  cart  runs  into  a  spring  with a spring  constant $k = $  {{ params.k }}  $N/m$  and compresses it by {{ params.x }} $cm$ before momentarily coming to rest.

## Question Text

What was the speed of the cart just before it hit the spring?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)