---
title: Math Diagnostic 22
topic: Math
author: Simon Bates
source: Math Diagnostic
template_version: 1.2
attribution: standard
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
- AK
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Math Practice Q22
    denom: 7
    formula: $\sin{\left(\frac{x}{7} \right)}$
    part1:
      ans1:
        value: ${- 7 \cos{\left(\frac{x}{7} \right)}}$
      ans2:
        value: ${7 \cos{\left(\frac{x}{7} \right)}}$
      ans3:
        value: ${- 14 \cos{\left(\frac{x}{7} \right)}}$
      ans4:
        value: ${- \frac{7 \cos{\left(\frac{x}{7} \right)}}{2}}$
---
# {{ params.vars.title }}

## Part 1

$\int$ {{params.formula}} $dx$ is equal to a constant plus:

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)