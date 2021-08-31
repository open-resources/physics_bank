---
title: Bouncing a Baby to Sleep
topic: Oscillations
author: Jake Bobowski
source: 2013 Practice Final Q8
template_version: 1.1
attribution: standard
outcomes:
- 15.3.1.0
- 15.2.1.3
- 13.3.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- PW
assets: null
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $k= $
    suffix: $N/m$
    comparison: sigfig
    digits: 3
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: Adjustment to $\; k= $
    suffix: $N/m$
    comparison: sigfig
    digits: 3
part3:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      person1: sister
      person2: uncle
      title: Bouncing a Baby to Sleep
      units: $N/m$
    m1: 66.1
    m2: 91.4
    m_b: 3.34
    f: 2.06
    part3:
      ans1:
        value: Add more air to increase the pressure in the ball. Increased pressure
          makes the ball 'stiffer'.
      ans2:
        value: Remove air to decrease the pressure in the ball. Decreased pressure
          makes the ball 'softer'.
      ans3:
        value: Remove air to decrease the pressure in the ball. Decreased pressure
          makes the ball 'stiffer'.
      ans4:
        value: Remove air to increase the pressure in the ball. Increased pressure
          makes the ball 'softer'.
      ans5:
        value: Remove air to increase the pressure in the ball. Increased pressure
          makes the ball 'stiffer'.
      ans6:
        value: Add more air to decrease the pressure in the ball. Decreased pressure
          makes the ball 'softer'.
      ans7:
        value: Add more air to decrease the pressure in the ball. Decreased pressure
          makes the ball 'stiffer'.
      ans8:
        value: Add more air to increase the pressure in the ball. Increased pressure
          makes the ball 'softer'.
---
# {{ params.vars.title }}
Some  babies  like  to  be  bounced  to  calm  them  down.   A  baby's  {{ params.vars.person1 }} ({{ params.m1 }} $kg$) sits on a "birthing" ball and bounces a {{ params.m_b }} $kg$ baby with them with frequency {{ params.f }} $Hz$, and finds that the baby goes to sleep.  The baby's {{ params.vars.person2 }} ({{ params.m2 }} $kg$) tries the same technique, but finds that the baby won't go to sleep.  They realize that this is because they can't bounce on the ball with the same frequency as the baby's {{ params.vars.person1 }}.

## Part 1

Assuming this to be simple harmonic motion, what is the spring constant of the ball (assume that it remains unchanged by the added weight)?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

What adjustment to the spring constant needs to be made for the father to put his child to sleep?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 3

How could such an adjustment be made to the ball, which is filled with air?

### Answer Section

- {{ params.part3.ans1.value}}
- {{ params.part3.ans2.value}}
- {{ params.part3.ans3.value}}
- {{ params.part3.ans4.value}}
- {{ params.part3.ans5.value}}
- {{ params.part3.ans6.value}}
- {{ params.part3.ans7.value}}
- {{ params.part3.ans8.value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)