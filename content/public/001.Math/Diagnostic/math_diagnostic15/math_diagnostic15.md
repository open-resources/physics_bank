---
title: Math Diagnostic 15
topic: Math
author: Simon Bates
source: Math Diagnostic Q15
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
tags:
- math_diagnostic
- MP
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
    hide-answer-panel: true
substitutions:
  params:
    vars:
      title: Math Practice 15
    expr: $8^{9} $=$ 134217728$
    part1:
      ans1:
        value: $log_8134217728 = 9$
      ans2:
        value: $log_89 = 134217728$
      ans3:
        value: $log_1342177289 = 8$
      ans4:
        value: $log_9134217728 = 8$
      ans5:
        value: Don't Know
---
# {{ params.vars.title }}
If {{params.expr}} then

## Part 1

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}
- {{ params.part1.ans5.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)