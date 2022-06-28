---
title: Jumping Salmon
topic: Kinematics(2D and 3D)
author: John Hopkinson
source: PHYS 112 2019W Mock Test Q1 and Q2
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 5.5.1.0
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- section
length:
- average
tags:
- PW
assets: null
part1:
  type: checkbox
  pl-customizations:
    weight: 1
    partial-credit: true
    partial-credit-method: EDC
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_{iy}= $
    suffix: $m/s$
substitutions:
  params:
    vars:
      title: Jumping Salmon
      units: $m/s$
    h_fall: 3.65
    dist: 1.17
    part1:
      ans1:
        value: Time interval for jump, $\Delta t$
      ans2:
        value: Vertical displacement, $\Delta y$
      ans3:
        value: Horizontal displacement, $\Delta x$
      ans4:
        value: Horizontal acceleration component, $a_x$
      ans5:
        value: Vertical acceleration component, $a_y$
      ans6:
        value: Vertical component of velocity at top of falls, $v_{fy}$
      ans7:
        value: Horizontal component of velocity at top of falls, $v_{fx}$
      ans8:
        value: Vertical component of velocity at bottom of falls, $v_{iy}$
      ans9:
        value: Horizontal component of velocity at bottom of falls, $v_{ix}$
---
# {{ params.vars.title }}
There are reports that salmon can only just jump over a {{ params.h_fall }} $m$ falls.

## Part 1

If a salmon starts from a horizontal distance {{ params.dist }} $m$ away from the waterfall in still water and just makes it up the falls, select the known variables for the motion of the salmon after leaving the water.

### Answer Section

Select all the choices that apply.

Note: You will be awarded full marks only if you select all the correct choices, and none of the incorrect choices. Choosing incorrect choices as well as not choosing correct choices will result in deductions.

- {{ params.part1.ans1.value}}
- {{ params.part1.ans2.value}}
- {{ params.part1.ans3.value}}
- {{ params.part1.ans4.value}}
- {{ params.part1.ans5.value}}
- {{ params.part1.ans6.value}}
- {{ params.part1.ans7.value}}
- {{ params.part1.ans8.value}}
- {{ params.part1.ans9.value}}

## Part 2

If a salmon starts from a horizontal distance {{ params.dist }} $m$ away from the waterfall in still water, what is the initial $y$-component of the velocity vector of the salmon as it leaves the water if it just makes it up the falls?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)