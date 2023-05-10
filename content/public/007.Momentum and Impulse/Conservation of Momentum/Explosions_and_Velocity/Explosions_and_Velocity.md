---
title: Explosions and Velocity
topic: Momentum and Impulse
author: Jake Bobowski
source: 2015 Practice Midterm 1 Q4
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 7.4.1.0
- 7.5.1.1
- 7.5.1.4
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
- HZ
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params_vars_title: Explosions and Velocity
    params_vars_name: Abbas
    params_part1_m_A: 6
    params_part1_m_B: 2
    params_part1_v_A: 39
    params_part1_v_B: 19
    params_part1_v: 34.0
    params_part1_m_pumpkin: 8
    params_part1_ans1_value: Yes, because of conservation of momentum
    params_part1_ans1_feedback: Great! You got it.
    params_part1_ans2_value: No, because we have not accounted for how the explosion
      might have changed the momentum of the pumpkin.
    params_part1_ans2_feedback: Hmm, does the unit make sense?
    params_part1_ans3_value: No, because the velocity should be $v$ = 58 $\rm{m/s}$
    params_part1_ans4_value: No, because the velocity should be $v$ = 7.3 $\rm{m/s/kg}$
---
# {{ params_vars_title }}
{{params_vars_name}} put a bunch of explosives inside of a {{ params.part1.m_pumpkin }} $\rm{kg}$ pumpkin, which explodes in two pieces, traveling in the same direction.
Piece A has mass $m_A$ = {{ params.part1.m_A }} $\rm{kg}$ and velocity $v_A$ = {{ params_part1_v_A }} $\rm{m/s}$.
Piece B has mass $m_B$ = {{ params.part1.m_B }} $\rm{kg}$ and velocity $v_B$ = {{ params_part1_v_B }} $\rm{m/s}$.

## Part 1

Is it true that the pumpkin must initially have had velocity $v$ = {{ params_part1_v }} $\rm{m/s}$ ?

### Answer Section

- {{ params_part1_ans1_value }}
- {{ params_part1_ans2_value }}
- {{ params_part1_ans3_value }}
- {{ params_part1_ans4_value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)