---
title: Throwing a Rock
topic: Kinematics(1D)
author: John Hopkinson
source: Phys 112 2020W1 Midterm 1 Q4
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 1.1.1.0
- 4.10.1.0
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
- NR
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    t1: $2$
    t2: $4$
    t3: $5$
    dv1: $\Delta v_{y 2 \to 4 }$
    dv2: $\Delta v_{y 4 \to 5 }$
    vars:
      title: Throwing a Rock
    part1:
      ans1:
        value: $\Delta v_{y 2 \to 4 } = \Delta v_{y 4 \to 5 } + 1 $
        feedback: Hmm, not quite. Try relating the change in velocity to the time
          interval and compare those.
      ans2:
        value: $\Delta v_{y 2 \to 4 }=0$ ; $\Delta v_{y 4 \to 5 }<0$
        feedback: Remember, the rock is accelerating down. These statements would
          imply the rock slows down as it falls!
      ans3:
        value: $\Delta v_{y 2 \to 4 } = \frac{ 1 }{ 2 }\Delta v_{y 4 \to 5 }$
        feedback: Close! Try double-checking your algebra.
      ans4:
        value: $\Delta v_{ y 2 \to 4 } = 2\Delta v_{y 4 \to 5 }$
        feedback: Great! You got it.
      ans5:
        value: $\Delta v_{y 2 \to 4 } = \frac{ 2 }{ 3 }\Delta v_{y 4 \to 5 }$
        feedback: Hmm, try relating the time intervals to the change in velocity.
---
# {{ params.vars.title }}
A rock is thrown vertically upward from an initial height of $1 \; \rm{m}$. It reaches its maximum height at $t = ${{ params.t1 }}$.5 \; \rm{s}$ after its release.

## Part 1

Compare the change in the $y$-component of the velocity of the rock in the time interval from $t = ${{ params.t1 }} $\rm{s}$ to $t =${{ params.t2 }} $\rm{s}$, {{ params.dv1 }}, to the change in the $y$-component of the velocity of the rock from $t = ${{ params.t2 }} $\rm{s}$ to $t = ${{ params.t3 }} $\rm{s}$, {{ params.dv2 }}

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}
- {{ params.part1.ans5.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)