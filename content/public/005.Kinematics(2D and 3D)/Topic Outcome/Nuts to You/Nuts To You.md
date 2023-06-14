---
title: Nuts To You
topic: Kinematics(2D and 3D)
author: John Hopkinson
source: PHYS 112 2020W1 GPS III
template_version: 1.2
attribution: standard
showCorrectAnswer: false
outcomes:
- 5.1.1.0
- 5.5.1.0
- 4.2.1.2
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
- tutorial
assets: null
part1:
  type: file-upload
  pl-customizations:
    file-names: motionDiag.pdf
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $v_{x_J}= $
    suffix: $m/s$
    comparison: sigfig
    digits: 3
part3:
  type: multiple-choice
  pl-customizations:
    weight: 1
part4:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $v_{yf_J}= $
    suffix: $m/s$
    comparison: sigfig
    digits: 3
part5:
  type: multiple-choice
  pl-customizations:
    weight: 1
part6:
  type: multiple-choice
  pl-customizations:
    weight: 1
part7:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\Delta t= $
    suffix: $s$
    comparison: sigfig
    digits: 3
part8:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\Delta x= $
    suffix: $m$
    comparison: sigfig
    digits: 3
myst:
  substitutions:
    params_vars_title: Nuts To You
    params_vi_hawk: 5.41
    params_h_Jed: 25.4
    params_part3_ans1_value: Jed maintains the $x$-component of their velocity. ($a_x
      = 0 \; m/s^2$)
    params_part3_ans2_value: There is no $x$-component since Jed falls in a straight
      line.
    params_part3_ans3_value: Jed's velocity decreases because the hawk is no longer
      pulling them.
    params_part3_ans4_value: Jed's velocity increases due to gravity.
    params_part5_ans1_value: Jed maintains the $y$-component of their velocity.
    params_part5_ans2_value: Jed's velocity increases due to gravity.
    params_part5_ans3_value: Jed's velocity decreases because the hawk is no longer
      pulling them.
    params_part5_ans4_value: Jed maintains the $x$-component of their velocity.
    params_part6_ans1_value: Jed travels at a higher speed after release as they accelerate
      downwards and maintain their horizontal speed.
    params_part6_ans2_value: The hawk travels at a higher speed after Jed is released
      since it is now lighter without Jed's weight.
    params_part6_ans3_value: Both the hawk and Jed travel at the same speed.
    params_part6_ans4_value: The hawk travels at a higher speed because it maintains
      its horizontal speed.
---
# {{ params_vars_title }}
In the children's book *Nuts to You*, a young squirrel named Jed is snatched up by a hawk.
While in the air Jed manages to go limp, slip through the hawk's talons and fall to the forest floor.
The hawk travels horizontally at a speed of {{ params.vi_hawk }} $m/s$.
(You may neglect any effects of air resistance as you answer the following questions).

## Part 1

Draw motion diagrams for both the hawk and Jed.  Use circles for the hawk and squares for Jed and label a legend.

Start your diagrams from the second before Jed is released and put a dot every second for 6 seconds.

Take a picture of your diagram, and upload it as a pdf.

### Answer Section

File upload box will be shown here.

## Part 2

One second after being released, what is the $x$-component of Jed's velocity?

### Answer Section

## Part 3

Explain your answer to Part 2.

### Answer Section

- {{ params_part3_ans1_value }}
- {{ params_part3_ans2_value }}
- {{ params_part3_ans3_value }}
- {{ params_part3_ans4_value }}

## Part 4

One second after being released, what is the $y$-component of Jed's velocity?

### Answer Section

## Part 5

Explain your answer to Part 4.

### Answer Section

- {{ params_part5_ans1_value }}
- {{ params_part5_ans2_value }}
- {{ params_part5_ans3_value }}
- {{ params_part5_ans4_value }}

## Part 6

Does Jed or the hawk travel at a higher speed after Jed is released?  Explain your answer.

### Answer Section

- {{ params_part6_ans1_value }}
- {{ params_part6_ans2_value }}
- {{ params_part6_ans3_value }}
- {{ params_part6_ans4_value }}

## Part 7

If Jed is released from a {{ params.h_Jed }} $m$ height, how long does it take him to hit the forest floor?

### Answer Section

## Part 8

How far has Jed travelled horizontally as he fell?

### Answer Section

Enter your answer below:

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)