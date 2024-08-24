---
title: Football Clearing Tree
topic: Kinematics(2D and 3D)
author: Ranya Ghosh
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.5.1.3
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
- RG
- JR
- APSC181
assets:
- Football.png
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Football Clearing Tree
        units: m/s
      d: 11
      h: 6
      h2: 1.82
      v: 14
      theta: 71
      part1:
        ans1:
          value: The ball clears the tree
        ans2:
          value: The ball does not clear the tree
---
# {{ params.vars.title }}
<img src="Football.png" width=85%>

If a person throws a football towards their friend who is behind a tree, will the football hit or clear the tree?
The football is thrown from a distance $d = {{ params.d }} \ \rm{m}$ from the tree, the tree has a height of $H = {{ params.h }} \ \rm{m}$, and the football is released at a height of $h = {{ params.h2 }} \ \rm{m}$.
The velocity of the football is $v_0 = {{ params.v }} \ \rm{m/s}$ and the angle that the football is thrown relative to the ground is $\theta = {{ params.theta }}^{\circ}$.

## Part 1

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)