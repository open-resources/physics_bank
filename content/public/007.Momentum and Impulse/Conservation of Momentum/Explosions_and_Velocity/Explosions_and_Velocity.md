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
substitutions:
  params:
    vars:
      title: Explosions and Velocity
      name: Ahmed
    part1:
      m_A: 7
      m_B: 4
      v_A: 26
      v_B: 18
      v: 23.0
      m_pumpkin: 11
      ans1:
        value: Yes, because of conservation of momentum
        feedback: Great! You got it.
      ans2:
        value: No, because we have not accounted for how the explosion might have
          changed the momentum of the pumpkin.
        feedback: Hmm, does the unit make sense?
      ans3:
        value: No, because the velocity should be $v$ = 44 $\rm{m/s}$
      ans4:
        value: No, because the velocity should be $v$ = 4.0 $\rm{m/s/kg}$
---
# {{ params.vars.title }}
{{params.vars.name}} put a bunch of explosives inside of a {{ params.part1.m_pumpkin }} $\rm{kg}$ pumpkin, which explodes in two pieces, traveling in the same direction.
Piece A has mass $m_A$ = {{ params.part1.m_A }} $\rm{kg}$ and velocity $v_A$ = {{ params.part1.v_A }} $\rm{m/s}$.
Piece B has mass $m_B$ = {{ params.part1.m_B }} $\rm{kg}$ and velocity $v_B$ = {{ params.part1.v_B }} $\rm{m/s}$.

## Part 1

Is it true that the pumpkin must initially have had velocity $v$ = {{ params.part1.v }} $\rm{m/s}$ ?

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)