---
title: Cat in a Laundry Basket
topic: Kinematics(2D and 3D)
author: John Hopkinson
source: PHYS 112 2020W Midterm 1 Q3
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 5.5.1.0
- 1.1.1.0
difficulty:
- easy
randomization:
- 2
taxonomy:
- undefined
span:
- section
length:
- short
tags:
- PW
assets:
- catbasket.png
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
part2:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params_vars_title: Cat in a Laundry Basket
    params_w: 37
    params_h: 36
    params_part1_ans1_value: $\Delta t_1 > \Delta t_2 > \Delta t_3$
    params_part1_ans2_value: $\Delta t_1 > \Delta t_3 > \Delta t_2$
    params_part1_ans3_value: $\Delta t_2 > \Delta t_1 > \Delta t_3$
    params_part1_ans4_value: $\Delta t_2 > \Delta t_3 > \Delta t_1$
    params_part1_ans5_value: $\Delta t_3 > \Delta t_1 > \Delta t_2$
    params_part1_ans6_value: $\Delta t_3 > \Delta t_2 > \Delta t_1$
    params_part1_ans7_value: $\Delta t_3 = \Delta t_2 = \Delta t_1$
    params_part2_ans1_value: $v_{x1} > v_{x2}$
    params_part2_ans2_value: $v_{x2} > v_{x1}$
    params_part2_ans3_value: $v_{x1} = v_{x2}$
---
# {{ params_vars_title }}
A cat jumps out of a laundry basket, travelling $w = $ {{ params_w }} $cm$ horizontally before just clearing the $h =$ {{ params_h }} $cm$ high edge of the basket.
The parabolic trajectories of three different jumps labelled 1, 2, and 3 are shown below.

<img longdesc="Cat in Laundry Basket.md#desc" alt="The parabolic trajectories of three different jumps." src="catbasket.png" width = "500px">

<div id="desc">
<h5>Long Description of image: The parabolic trajectories of three different jumps.</h5>
Trajectory 1 has the highest peak and smallest range. <br>
Trajectory 2 has the lowest peak and the second largest range. <br>
Trajectory 3 has the second highest peak and the largest range. <br>
<p>Long description ends.</p>
<div>

## Part 1

Rank the time in the air ($\Delta t_1, \Delta t_2, and \Delta t_3$, respectively) of the cat on each path.

### Answer Section

- {{ params_part1_ans1_value }}
- {{ params_part1_ans2_value }}
- {{ params_part1_ans3_value }}
- {{ params_part1_ans4_value }}
- {{ params_part1_ans5_value }}
- {{ params_part1_ans6_value }}

## Part 2

Rank the relative sizes of the $x-$components of the velocity vectors for path 1 ($v\_{x1}$) and path 2 ($v\_{x2}$).

### Answer Section

- {{ params_part2_ans1_value }}
- {{ params_part2_ans2_value }}
- {{ params_part2_ans3_value }}
- {{ params.part2.ans4.value }}
- {{ params.part2.ans5.value }}
- {{ params.part2.ans6.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)