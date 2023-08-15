---
title: Moment of Inertia
topic: Rotational Motion
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 10.5.2.1
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
- APSC181
- PJ
assets:
- MomentOfInertia.png
part1:
  type: dropdown
  pl-customizations:
    weight: 1
    blank: 'true'
myst:
  substitutions:
    params_vars_title: Moment of Inertia
    params_part1_ans1_value: Rod
    params_part1_ans1_feedback: Good job!
    params_part1_ans2_value: Hoop
    params_part1_ans2_feedback: Think of keeping most of the mass close to the axis
      of rotation.
    params_part1_ans3_value: Disk
    params_part1_ans3_feedback: Think of keeping most of the mass close to the axis
      of rotation.
    params_part1_ans4_value: Point Mass
    params_part1_ans4_feedback: Think of keeping most of the mass close to the axis
      of rotation.
---
# {{ params_vars_title }}

## Question Text

Each of the mass distributions below are drawn to the same scale, and have equal mass.
The same moment is applied to each of them.
Which shape experiences the highest angular acceleration?

<img src="MomentOfInertia.png" width=800 alt="A rod, a hoop, a disk and a point mass." >

### Answer Section

- {{ params.part1.ans1}}
- {{ params.part1.ans2}}
- {{ params.part1.ans3}}
- {{ params.part1.ans4}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)