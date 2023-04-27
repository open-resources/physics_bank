---
title: Math Diagnostic09
topic: Math
author: Simon Bates
source: Math Diagnostic
template_version: 1.3
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
      title: Math Diagnostic09
    expr: $l$ = $\dfrac{(h)}{(k - 10x)} $
    part1:
      ans1:
        value: k = ${ \frac{h}{l} + 10 x}$
      ans2:
        value: k = ${- \frac{10 l x}{h}}$
      ans3:
        value: k = ${- \frac{h}{10 l x}}$
      ans4:
        value: k = ${\frac{l + 10 x}{h}}$
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