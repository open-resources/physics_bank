---
title: testlatex
topic: Template
author: Firas Moosvi
source: 5.45
template_version: 1.4
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
outcomes:
- 6.1.1.0
- 6.1.1.1
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
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    frac: "$\frac{1}{2}$"
    frac2: $\frac{1}{2}$
    part1:
      ans1:
        value: 42
      ans2:
        value: 855
---
# {{ params.vars.title }}
| Test | Display   |
|----------|-------|
| Fraction - triple braces  | {{{ params.frac }}} |
| Fraction - double braces  | {{ params.frac }} |
| Fraction - old method | {{ params.frac2 }} |

## Part 1

Part 1

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)