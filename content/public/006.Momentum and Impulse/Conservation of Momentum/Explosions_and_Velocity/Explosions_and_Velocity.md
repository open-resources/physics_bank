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
server:
  imports: |
    import random
    import pandas as pd
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: "# Start problem code\n\ndata2 = nested_dict()\n\n# store phrases etc\n\
    data2[\"params\"][\"vars\"][\"title\"] = \"Explosions and Velocity\"\nunits =\
    \ \"m/s\"\ndata2[\"params\"][\"vars\"][\"units\"] = units\n\n# Randomize Variables\n\
    I_A = random.randint(2,8)\nI_B = random.randint(2,8)\nv_A = random.randint(10,\
    \ 40)\nv_B = random.randint(10, 40)\nm_pumpkin = random.randint(2, 10)\n\n# store\
    \ the variables in the dictionary \"params\"\ndata2[\"params\"][\"part1\"][\"\
    I_A\"] = I_A\ndata2[\"params\"][\"part1\"][\"I_B\"] = I_B   \ndata2[\"params\"\
    ][\"part1\"][\"v_A\"] = v_A\ndata2[\"params\"][\"part1\"][\"v_B\"] = v_B\ndata2[\"\
    params\"][\"part1\"][\"m_pumpkin\"] = m_pumpkin\n\n# define possible answers\n\
    data2[\"params\"][\"part1\"][\"ans1\"][\"value\"] = \"Yes, because of conservation\
    \ of momentum\"\ndata2[\"params\"][\"part1\"][\"ans1\"][\"correct\"] = True\n\n\
    data2[\"params\"][\"part1\"][\"ans2\"][\"value\"] = \"No, because we have not\
    \ accounted for how the explosion might have changed the momentum of the pumpkin.\"\
    \ndata2[\"params\"][\"part1\"][\"ans2\"][\"correct\"] = False\n\ndata2[\"params\"\
    ][\"part1\"][\"ans3\"][\"value\"] = f\"No, because the velocity should be $v =\
    \ $ {v_A+v_B} { units }\"\ndata2[\"params\"][\"part1\"][\"ans3\"][\"correct\"\
    ] = False\n\ndata2[\"params\"][\"part1\"][\"ans4\"][\"value\"] = f\"No, because\
    \ the velocity should be $v = $ {(v_A+v_B)/m_pumpkin} { units }\"\ndata2[\"params\"\
    ][\"part1\"][\"ans4\"][\"correct\"] = False\n\n# Update the data object with a\
    \ new dict\ndata.update(data2)\n"
  prepare: 'pass

    '
  parse: 'pass

    '
  grade: 'pass

    '
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
      I_A: 7
      I_B: 3
      v_A: 20
      v_B: 18
      m_pumpkin: 8
      ans1:
        value: Yes, because of conservation of momentum
        correct: true
      ans2:
        value: No, because we have not accounted for how the explosion might have
          changed the momentum of the pumpkin.
        correct: false
      ans3:
        value: No, because the velocity should be $v = $ 38 m/s
        correct: false
      ans4:
        value: No, because the velocity should be $v = $ 4.75 m/s
        correct: false
---
# {{ params.vars.title }}
I put a bunch of explosives inside of a {{ params.part1.m_pumpkin }} kg pumpkin, which explodes in two pieces.
Piece A has inertia {{ params.part1.I_A }} kg and velocity $v_A$ = {{ params.part1.v_A }} {{ params.vars.units }}.
Piece B has inertia {{ params.part1.I_B }} kg, and velocity $v_B$ = {{ params.part1.v_B }} {{ params.vars.units }}.

## Attribution

![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png) Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).