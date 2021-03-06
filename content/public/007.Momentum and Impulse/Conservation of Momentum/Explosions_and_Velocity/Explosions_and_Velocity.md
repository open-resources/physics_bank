---
title: Explosions and Velocity
topic: Momentum and Impulse
author: Jake Bobowski
source: 2015 practice midterm 1 Q4
template_version: 1.0
attribution: standard
outcomes:
- 6.5.1.6
- 6.4.4.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- unknown
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Explosions and Velocity
      units: m/s
      name: Mateo
    part1:
      I_A: 4
      I_B: 2
      v_A: 21
      v_B: 37
      m_pumpkin: 9
      v: 17.555555555555557
      ans1:
        value: Yes, because of conservation of momentum
      ans2:
        value: No, because we have not accounted for how the explosion might have
          changed the momentum of the pumpkin.
      ans3:
        value: No, because the velocity should be $v = $ 58 m/s
      ans4:
        value: No, because the velocity should be $v = $ 6.444444444444445 m/s
---
# {{ params.vars.title }}
{{params.vars.name}} put a bunch of explosives inside of a {{ params.part1.m_pumpkin }} kg pumpkin, which explodes in two pieces.
Piece A has inertia {{ params.part1.I_A }} kg and velocity $v_A$ = {{ params.part1.v_A }} {{ params.vars.units }}.
Piece B has inertia {{ params.part1.I_B }} kg, and velocity $v_B$ = {{ params.part1.v_B }} {{ params.vars.units }}.
## Part 1

Is it true that the pumpkin must initially have had velocity $v$ = {{ params.vars.v }} {{ params.vars.units }} ?

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)