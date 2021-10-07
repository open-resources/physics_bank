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
    expr: $j$ = $\dfrac{(v)}{(p - 5s)} $
    part1:
      ans1:
        value: p = ${ 5 s + \frac{v}{j}}$
      ans2:
        value: p = ${- \frac{5 j s}{v}}$
      ans3:
        value: p = ${- \frac{v}{5 j s}}$
      ans4:
        value: p = ${\frac{j + 5 s}{v}}$
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