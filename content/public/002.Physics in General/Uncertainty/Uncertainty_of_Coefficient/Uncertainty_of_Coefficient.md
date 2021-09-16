---
title: Uncertainty of Coefficient
topic: Physics in General
author: Jake Bobowski
source: 2012 Practice Final Q7
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 2.4.1.2
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
- EW
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Uncertainty of Coefficient
      name: Mateo
      units: $kg/s$
    m: 137
    v: 2.4
    b: 0.69
    part1:
      ans1:
        value: ' $\pm$ 0.1'
      ans2:
        value: ' $\pm$ 0.07'
      ans3:
        value: ' $\pm$ 0.01'
      ans4:
        value: ' $\pm$ 0.68'
---
# {{ params.vars.title }}
The drag force on an object of interest can be accurately modelled as $\vec{D}$ = -$b\vec{v}$ such that its terminal velocity in free fall is given by $v_T$ = $mg/b$.
{{ params.vars.name }} measures $m$ = {{ params.m }} $\pm$ 2 $g$ and $v_T$ = {{ params.v }} $\pm$ 0.2 $m/s$.
Based on these measurements {{ params.vars.name }} determines the drag coefficient to be $b$ = {{ params.b }} $kg/s$.

## Part 1

What is the uncertainty in your determination of $b$?

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ans4.value }} {{ params.vars.units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)