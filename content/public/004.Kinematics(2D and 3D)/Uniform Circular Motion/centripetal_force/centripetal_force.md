---
title: Centripetal Motion
topic: centripetal motion
author: Michael Kudla
source: original
template_version: 0.2
outcomes:
- LO.kinematics.2305
- LO.kinematics.2304
tags:
- quiz
- homework
assets: null
part1:
  type: symbolic-input
  label: $F_r = $
  pl-customizations:
    variables: m, v, r
    weight: 1
    allow-blank: false
substitutions:
  params:
    vars:
      title: Centripetal Motion
  correct_answers:
    part1_ans:
      _type: sympy
      _value: m*v**2/r
      _variables:
      - v
      - r
      - m
---
# {{ params.vars.title }}
## Question Text

Write the centripetal force $F_r$ in terms of the mass $m$, velocity $v$, and radius $r$.

Note that it may not be necessary to use every variable. Use the following table as a reference for each variable:

| $\\LaTeX$ | Use   |
|----------|-------|
| $m$  | m  |
| $v$  | v  |
| $r$  | r  |

### Answer Section
