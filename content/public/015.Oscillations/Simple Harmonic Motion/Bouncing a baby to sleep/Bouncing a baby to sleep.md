---
title: Bouncing a Baby to Sleep
topic: Oscillations
author: Jake Bobowski
source: 2013 Practice Final Q8
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
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
span:
- undefined
length:
- undefined
tags:
- PW
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $k= $
    suffix: $\rm{N/m}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: Adjustment to $\; k= $
    suffix: $\rm{N/m}$
part3:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params_vars_person1: grandfather
    params_vars_person2: cousin
    params_vars_title: Bouncing a Baby to Sleep
    params_vars_units: $N/m$
    params_m1: 94.9
    params_m2: 75.2
    params_m_b: 5.84
    params_f: 1.94
    params_part3_ans1_value: Remove air to decrease the pressure in the ball. Decreased
      pressure makes the ball 'softer'.
    params_part3_ans2_value: Remove air to decrease the pressure in the ball. Decreased
      pressure makes the ball 'stiffer'.
    params_part3_ans2_feedback: Hmm, not quite. How would adding air affect pressure
      of the ball?
    params_part3_ans3_value: Remove air to increase the pressure in the ball. Increased
      pressure makes the ball 'softer'.
    params_part3_ans3_feedback: Hmm, not quite. How would adding air affect pressure
      of the ball?
    params_part3_ans4_value: Remove air to increase the pressure in the ball. Increased
      pressure makes the ball 'stiffer'.
    params_part3_ans4_feedback: Hmm, not quite. How would adding air affect pressure
      of the ball?
    params_part3_ans5_value: Add more air to decrease the pressure in the ball. Decreased
      pressure makes the ball 'softer'.
    params_part3_ans5_feedback: Hmm, not quite. How would adding air affect pressure
      of the ball?
    params_part3_ans6_value: Add more air to decrease the pressure in the ball. Decreased
      pressure makes the ball 'stiffer'.
    params_part3_ans6_feedback: Hmm, not quite. How would adding air affect pressure
      of the ball?
    params_part3_ans7_value: Add more air to increase the pressure in the ball. Increased
      pressure makes the ball 'softer'.
    params_part3_ans7_feedback: Hmm, not quite. How would adding air affect pressure
      of the ball?
    params_part3_ans8_value: Add more air to increase the pressure in the ball. Increased
      pressure makes the ball 'stiffer'.
    params_part3_ans8_feedback: Hmm, not quite. How would adding air affect pressure
      of the ball?
---
# {{ params_vars_title }}
Some  babies  like  to  be  bounced  to  calm  them  down.   A  baby's  {{ params_vars_person1 }} ({{ params_m1 }} kg) sits on a "birthing" ball and bounces a {{ params.m_b }} kg baby with them with frequency {{ params_f }} Hz, and finds that the baby goes to sleep.  The baby's {{ params_vars_person2 }} ({{ params_m2 }} kg) tries the same technique, but finds that the baby won't go to sleep.  They realize that this is because they can't bounce on the ball with the same frequency as the baby's {{ params_vars_person1 }}.

## Part 1

Assuming this to be simple harmonic motion, what is the spring constant of the ball (assume that it remains unchanged by the added weight)?

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 2

What adjustment to the spring constant needs to be made for the father to put his child to sleep?

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 3

How could such an adjustment be made to the ball, which is filled with air?

### Answer Section

- {{ params_part3_ans1_value}}
- {{ params_part3_ans2_value}}
- {{ params_part3_ans3_value}}
- {{ params_part3_ans4_value}}
- {{ params_part3_ans5_value}}
- {{ params_part3_ans6_value}}
- {{ params_part3_ans7_value}}
- {{ params_part3_ans8_value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)