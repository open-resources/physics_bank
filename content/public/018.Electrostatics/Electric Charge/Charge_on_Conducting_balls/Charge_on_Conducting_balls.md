---
title: Charge on Conducting balls
topic: Electrostatics
author: John Hopkinson
source: Physics_2019_Midterm_2_Q3
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 18.4.1.0
- 18.3.1.0
difficulty:
- undefined
randomization:
- 2
taxonomy:
- undefined
span:
- undefined
length:
- undefined
tags:
- L.K
assets:
- balls.png
part1:
  type: dropdown
  pl-customizations:
    weight: 1
    blank: 'true'
part2:
  type: dropdown
  pl-customizations:
    weight: 1
    blank: 'true'
part3:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params_vars_title: Charge on Conducting balls
    params_part1_ans1_value: negative
    params_part1_ans1_feedback: You got it!
    params_part1_ans2_value: positive
    params_part1_ans2_feedback: Not quite!
    params_part1_ans3_value: Zero
    params_part1_ans3_feedback: Not quite!
    params_ball: '1'
    params_balls: '3'
    params_part2_ans1_value: Negative
    params_part2_ans1_feedback: Not quite
    params_part2_ans2_value: Positive
    params_part2_ans2_feedback: You got it!
    params_part2_ans3_value: Zero
    params_part2_ans3_feedback: Not quite!
    params_part3_ans1_value: Ball 2 only
    params_part3_ans1_feedback: Not quite
    params_part3_ans2_value: Ball 5 only
    params_part3_ans2_feedback: Not quite!
    params_part3_ans3_value: None of the balls
    params_part3_ans3_feedback: Consider the signs of the induced charges
    params_part3_ans4_value: All of the other balls (2, 3, 4 and 5)
    params_part3_ans4_feedback: Great! You Got it
    params_part3_ans5_value: Balls 2, 3 and 4 only
    params_part3_ans5_feedback: Not quite
---
# {{ params_vars_title }}
<img src="balls.png" width="400">

Five identical neutral conducting balls hanging from strings are numbered 1 to 5.  As shown in the Figure above. Balls 1 and 2 touch as they are brought near a highly charged metal sphere and then are separated, with ball 1 closer to the sphere. Ball 3 contacts both the metal sphere and ball 4.  Ball 4 is pulled away from ball 3, and then ball 3 is pulled away from the metal sphere.

## Part 1

Following these charging steps, what is the sign of the charge on ball {{ params_ball}}?

### Answer Section

- {{ params_part1_ans1_value }} {{ params.vars.units}}
- {{ params_part1_ans2_value }} {{ params.vars.units}}
- {{ params_part1_ans3_value }} {{ params.vars.units}}

### pl-submission-panel

### pl-answer-panel

## Part 2

Following these charging steps, what is the sign of the charge on ball {{ params_balls }}?

### Answer Section

- {{ params_part2_ans1_value }} {{ params.vars.units}}
- {{ params_part2_ans2_value }} {{ params.vars.units}}
- {{ params_part2_ans3_value }} {{ params.vars.units}}

### pl-submission-panel

### pl-answer-panel

## Part 3

Following these charging steps, ball 1 is attracted to (choose the best answer):

### Answer Section

- {{ params_part3_ans1_value }} {{ params.vars.units}}
- {{ params_part3_ans2_value }} {{ params.vars.units}}
- {{ params_part3_ans3_value }} {{ params.vars.units}}
- {{ params_part3_ans4_value }} {{ params.vars.units}}
- {{ params_part3_ans5_value }} {{ params.vars.units}}

### pl-submission-panel

### pl-answer-panel

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)