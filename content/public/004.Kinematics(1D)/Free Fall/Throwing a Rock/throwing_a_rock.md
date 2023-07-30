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
myst:
  substitutions:
    params_t1: $1$
    params_t2: $4$
    params_t3: $6$
    params_dv1: $\Delta v_{y 1 \to 4 }$
    params_dv2: $\Delta v_{y 4 \to 6 }$
    params_vars_title: Throwing a Rock
    params_part1_ans1_value: $\Delta v_{y 1 \to 4 } = \Delta v_{y 4 \to 6 } + 1 $
    params_part1_ans1_feedback: Hmm, not quite. Try relating the change in velocity
      to the time interval and compare those.
    params_part1_ans2_value: $\Delta v_{y 1 \to 4 }=0$ ; $\Delta v_{y 4 \to 6 }<0$
    params_part1_ans2_feedback: Remember, the rock is accelerating down. These statements
      would imply the rock slows down as it falls!
    params_part1_ans3_value: $\Delta v_{y 1 \to 4 } = \frac{ 2 }{ 3 }\Delta v_{y 4
      \to 6 }$
    params_part1_ans3_feedback: Close! Try double-checking your algebra.
    params_part1_ans4_value: $\Delta v_{ y 1 \to 4 } = \frac{ 3 }{ 2 }\Delta v_{y
      4 \to 6 }$
    params_part1_ans4_feedback: Great! You got it.
    params_part1_ans5_value: $\Delta v_{y 1 \to 4 } = \frac{ 3 }{ 5 }\Delta v_{y 4
      \to 6 }$
    params_part1_ans5_feedback: Hmm, try relating the time intervals to the change
      in velocity.
---
# {{ params_vars_title }}
A rock is thrown vertically upward from an initial height of $1 \; \rm{m}$. It reaches its maximum height at $t = ${{ params_t1 }}$.5 \; \rm{s}$ after its release.

## Part 1

Compare the change in the $y$-component of the velocity of the rock in the time interval from $t = ${{ params_t1 }} $\rm{s}$ to $t =${{ params_t2 }} $\rm{s}$, {{ params_dv1 }}, to the change in the $y$-component of the velocity of the rock from $t = ${{ params_t2 }} $\rm{s}$ to $t = ${{ params_t3 }} $\rm{s}$, {{ params_dv2 }}

### Answer Section

- {{ params_part1_ans1_value }}
- {{ params_part1_ans2_value }}
- {{ params_part1_ans3_value }}
- {{ params_part1_ans4_value }}
- {{ params_part1_ans5_value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)