---
title: Math Diagnostic12
topic: Math
author: Simon Bates
source: Math Diagnostic
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 1.5.1.5
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
- AK
- math_diagnostic
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Math Diagnostic12
      expr: $1\over 1- x$ > $ 6$
      part1:
        ans1:
          value: (5/6 < x) & (x < 1)
        ans2:
          value: (5/6 > x) & (x > 1)
        ans3:
          value: x > 1/6
        ans4:
          value: (0 < x) & (x < 6)
        ans5:
          value: Do not know
---
# {{ params.vars.title }}

## Part 1

If {{ params.expr }} then:

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}
- {{ params.part1.ans5.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)