---
title: Math Diagnostic21
topic: Math
author: Simon Bates
source: Math Diagnostic
template_version: 1.3
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
- math_diagnostic
- MP
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Math Diagnostic21
      formula: $\sin{\left(x^{2} \right)}$
      part1:
        ans1:
          value: ${2 x \cos{\left(x^{2} \right)}}$
        ans2:
          value: ${2 \cos{\left(x^{2} \right)}}$
        ans3:
          value: ${\cos{\left(x^{2} \right)}}$
        ans4:
          value: ${2 x \sin{\left(x^{2} \right)}}$
        ans5:
          value: Don't Know
---
# {{ params.vars.title }}
The derivative of {{params.formula}} is:

## Part 1

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}
- {{ params.part1.ans5.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)