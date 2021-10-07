---
title: Math Diagnostic 9
topic: Math
author: Simon Bates
source: Math Diagnostic
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
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
- math_diagnostic
- MP
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Math Practice 9
    expr: $c$ = $\dfrac{(f)}{(t - 7p)} $
    part1:
      ans1:
        value: t = ${ 7 p + \frac{f}{c}}$
      ans2:
        value: t = ${- \frac{7 c p}{f}}$
      ans3:
        value: t = ${- \frac{f}{7 c p}}$
      ans4:
        value: t = ${\frac{c + 7 p}{f}}$
      ans5:
        value: Don't Know
---
# {{ params.vars.title }}
If {{params.expr}}

## Part 1

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}
- {{ params.part1.ans5.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)