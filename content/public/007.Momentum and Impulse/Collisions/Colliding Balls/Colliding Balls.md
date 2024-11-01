---
title: Colliding Balls
topic: Momentum and Impulse
author: Jake Bobowski
source: 2013 Midterm 2 Section 001 Q2
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 7.2.1.1
- 7.4.1.0
- 7.4.1.1
- 7.4.1.2
- 7.5.1.3
difficulty:
- medium
randomization:
- 4
taxonomy:
- undefined
span:
- section
length:
- average
tags:
- PW
assets:
- Conservation-1.png
- Conservation-2.png
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Colliding Balls
      m1: 162
      m2: 101
      v1_i: 5.39
      v2_i: -2.72
      v1_f: -4.58
      v2_f: 3.41
      part1:
        ans1:
          value: This is not possible as momentum is not conserved.
        ans2:
          value: This is an inelastic collision because only momentum is conserved.
        ans3:
          value: This is an inelastic collision because energy and momentum are conserved.
        ans4:
          value: This is not possible because kinetic energy is not conserved.
        ans5:
          value: This is an elastic collision, as both kinetic energy and momentum
            are conserved.
---
# {{ params.vars.title }}
A ball of mass {{ params.m1 }} $g$ with initial velocity {{ params.v1_i }} $\frac{m}{s}\hat{\imath}$ collides with a ball of mass {{ params.m2 }} $g$ with initial velocity {{ params.v2_i }} $\frac{m}{s}\hat{\imath}$. The final velocity of the {{ params.m1 }} $g$ ball is {{ params.v1_f }} $\frac{m}{s}\hat{\imath}$, while the final velocity of the {{ params.m2 }} $g$ ball is {{ params.v2_f }} $\frac{m}{s}\hat{\imath}$.

## Part 1

Choose the correct statement.

**Note**: When comparing total momenta and total energies, consider them equal if the final is within 2% (inclusive) of the initial.

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}
- {{ params.part1.ans5.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)