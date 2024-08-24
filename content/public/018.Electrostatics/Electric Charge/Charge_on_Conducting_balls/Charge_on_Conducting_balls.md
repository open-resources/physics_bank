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
    params:
      vars:
        title: Charge on Conducting balls
      part1:
        ans1:
          value: negative
          feedback: Not quite
        ans2:
          value: positive
          feedback: You got it!
        ans3:
          value: Zero
          feedback: Not quite!
      ball: '2'
      balls: '3'
      part2:
        ans1:
          value: Negative
          feedback: Not quite
        ans2:
          value: Positive
          feedback: You got it!
        ans3:
          value: Zero
          feedback: Not quite!
      part3:
        ans1:
          value: Ball 2 only
          feedback: Not quite
        ans2:
          value: Ball 5 only
          feedback: Not quite!
        ans3:
          value: None of the balls
          feedback: Consider the signs of the induced charges
        ans4:
          value: All of the other balls (2, 3, 4 and 5)
          feedback: Great! You Got it
        ans5:
          value: Balls 2, 3 and 4 only
          feedback: Not quite
---
# {{ params.vars.title }}
<img src="balls.png" width="400">

Five identical neutral conducting balls hanging from strings are numbered 1 to 5.  As shown in the Figure above. Balls 1 and 2 touch as they are brought near a highly charged metal sphere and then are separated, with ball 1 closer to the sphere. Ball 3 contacts both the metal sphere and ball 4.  Ball 4 is pulled away from ball 3, and then ball 3 is pulled away from the metal sphere.

## Part 1

Following these charging steps, what is the sign of the charge on ball {{ params.ball}}?

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ans3.value }} {{ params.vars.units}}

## Part 2

Following these charging steps, what is the sign of the charge on ball {{ params.balls }}?

### Answer Section

- {{ params.part2.ans1.value }} {{ params.vars.units}}
- {{ params.part2.ans2.value }} {{ params.vars.units}}
- {{ params.part2.ans3.value }} {{ params.vars.units}}

## Part 3

Following these charging steps, ball 1 is attracted to (choose the best answer):

### Answer Section

- {{ params.part3.ans1.value }} {{ params.vars.units}}
- {{ params.part3.ans2.value }} {{ params.vars.units}}
- {{ params.part3.ans3.value }} {{ params.vars.units}}
- {{ params.part3.ans4.value }} {{ params.vars.units}}
- {{ params.part3.ans5.value }} {{ params.vars.units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)