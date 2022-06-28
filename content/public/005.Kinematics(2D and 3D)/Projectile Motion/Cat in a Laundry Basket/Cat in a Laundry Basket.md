---
title: Cat in a Laundry Basket
topic: Kinematics(2D and 3D)
author: John Hopkinson
source: PHYS 112 2020W Midterm 1 Q3
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
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
substitutions:
  params:
    vars:
      title: Cat in a Laundry Basket
    w: 20
    h: 57
    part1:
      ans1:
        value: $\Delta t_1 > \Delta t_2 > \Delta t_3$
      ans2:
        value: $\Delta t_1 > \Delta t_3 > \Delta t_2$
      ans3:
        value: $\Delta t_2 > \Delta t_1 > \Delta t_3$
      ans4:
        value: $\Delta t_2 > \Delta t_3 > \Delta t_1$
      ans5:
        value: $\Delta t_3 > \Delta t_1 > \Delta t_2$
      ans6:
        value: $\Delta t_3 > \Delta t_2 > \Delta t_1$
      ans7:
        value: $\Delta t_3 = \Delta t_2 = \Delta t_1$
    part2:
      ans1:
        value: $v_{x1} > v_{x2}$
      ans2:
        value: $v_{x2} > v_{x1}$
      ans3:
        value: $v_{x1} = v_{x2}$
---
# {{ params.vars.title }}
A cat jumps out of a laundry basket, travelling $w = $ {{ params.w }} $cm$ horizontally before just clearing the $h =$ {{ params.h }} $cm$ high edge of the basket.
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

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}
- {{ params.part1.ans5.value }}
- {{ params.part1.ans6.value }}

## Part 2

Rank the relative sizes of the $x-$components of the velocity vectors for path 1 ($v\_{x1}$) and path 2 ($v\_{x2}$).

### Answer Section

- {{ params.part2.ans1.value }}
- {{ params.part2.ans2.value }}
- {{ params.part2.ans3.value }}
- {{ params.part2.ans4.value }}
- {{ params.part2.ans5.value }}
- {{ params.part2.ans6.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)