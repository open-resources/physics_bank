---
title: Explosions and Velocity
topic: Momentum and Impulse
author: Jake Bobowski
source: 2015 practice midterm 1 Q4
template_version: 0.3
outcomes:
- 6.5.1.6
- 6.4.4.0
tags:
- quiz
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
    part1:
      I_A: 6
      I_B: 5
      v_A: 19
      v_B: 40
      m_pumpkin: 4
      ans1:
        value: Yes, because of conservation of momentum
      ans2:
        value: No, because we have not accounted for how the explosion might have
          changed the momentum of the pumpkin.
      ans3:
        value: No, because the velocity should be $v = $ 59 m/s
      ans4:
        value: No, because the velocity should be $v = $ 14.75 m/s
---
# {{ params.vars.title }}
## Part 1

I put a bunch of explosives inside of a {{params.part1.m_pumpkin}}kg pumpkin, which explodes in two pieces.
Piece A has inertia {{params.part1.I_A}}kg and velocity $v_A$ = {{params.part1.v_A}} {{ params.vars.units }}.
Piece B has inertia {{params.part1.I_B}}kg, and velocity $v_B$ = {{params.part1.v_B}} {{ params.vars.units }}.
Is it true that the pumpkin must initially have had velocity $v$ = {{ (params.part1.I_A*params.part1.v_A +  params.part1.I_B*params.part1.v_B)/params.part1.m_pumpkin }} {{ params.vars.units }} ?

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}

## Attribution

![Image representing the Creative Commons 4.0 BY-NC-SA license.](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png) Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).