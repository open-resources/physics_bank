---
title: Lifting Machine Conceptual
topic: Rotational Dynamics
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 11.3.1.0
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
- PJ
- APSC181
assets:
- LiftingMachine.png
part1:
  type: checkbox
  pl-customizations:
    weight: 1
    partial-credit: true
    partial-credit-method: EDC
myst:
  substitutions:
    params:
      vars:
        title: Lifting Machine Conceptual
      choice: increases
      part1:
        ans1:
          value: Increase $r_4$
          feedback: Correct!
        ans2:
          value: Increase $r_2$
          feedback: Correct!
        ans3:
          value: Decrease $r_2$
          feedback: Nope.
        ans4:
          value: Decrease $r_4$
          feedback: Nope.
        ans5:
          value: Increase $r_3$
          feedback: Nope.
---
# {{ params.vars.title }}

## Question Text

The machine illustrated below lifts a mass $m$ by turning a pedal.
The pedal rotates a gear system, which pulls a rope along a pulley system that lifts the mass.
Select all modifications to the system that {{ params.choice }} the amount of force required to lift the object.

<img src="LiftingMachine.png" width=600 alt="A mass is suspended on a double pulley system. The rope is pulled by a large gear with r3, which is spun by a smaller gear with r2. The smaller gear is spun with a pedal of r1. The rope makes contact with the larger gear at r4." >

### Answer Section

Select all the choices that apply.

Note: You will be awarded full marks only if you select all the correct choices, and none of the incorrect choices. Choosing incorrect choices as well as not choosing correct choices will result in deductions.

- {{ params.part1.ans1.value}}
- {{ params.part1.ans2.value}}
- {{ params.part1.ans3.value}}
- {{ params.part1.ans4.value}}
- {{ params.part1.ans5.value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)