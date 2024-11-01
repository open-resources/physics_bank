---
title: Particle Collision
topic: Momentum and Impulse
author: Jake Bobowski
source: 2013 Midterm 2 Section 001 Q1
template_version: 1.2
attribution: standard
showCorrectAnswer: false
outcomes:
- 7.2.1.1
- 7.2.1.2
- 7.2.1.3
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
- PW
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Particle Collision
      choice: $x$-component of the
      m1: 6
      m2: 2
      v1: 14
      v2: 15
      part1:
        ans1:
          value: 84 $kg$ $\dfrac{m}{s}\hat{\imath}$
          feedback: Great! You got it.
        ans2:
          value: 30 $kg$ $\dfrac{m}{s}\hat{\imath}$
          feedback: Hmm... Try again.
        ans3:
          value: 30 $kg$ $\dfrac{m}{s}\hat{\jmath}$
          feedback: Close! Double check the directions of the unit vectors.
        ans4:
          value: 30 $kg$ $\dfrac{m}{s}\hat{\imath}$ + 84 $kg$ $\dfrac{m}{s}\hat{\jmath}$
          feedback: Hmm... Try again.
        ans5:
          value: 84 $kg$ $\dfrac{m}{s}\hat{\jmath}$
          feedback: Hmm... Try again.
        ans6:
          value: 84 $kg$ $\dfrac{m}{s}\hat{\imath}$ + 30 $kg$ $\dfrac{m}{s}\hat{\jmath}$
          feedback: Careful! Only one component is asked for.
---
# {{ params.vars.title }}
A particle of mass {{ params.m1 }} $kg$ is travelling with velocity {{ params.v1 }} $\frac{m}{s}\hat{\imath}$ when it collides with another particle of mass {{ params.m2 }} $kg$ travelling with velocity {{ params.v2 }} $\frac{m}{s}\hat{\jmath}$.

## Part 1

The {{ params.choice }} **initial** momentum of this system is:

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}
- {{ params.part1.ans5.value }}
- {{ params.part1.ans6.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)