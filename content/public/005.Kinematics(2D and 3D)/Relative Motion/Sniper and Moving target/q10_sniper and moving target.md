---
title: Sniper and Moving Target
topic: Kinematics(2D and 3D)
author: Ammar Zavahir
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 4.1.1.1
- 5.8.1.3
- 4.3.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- APSC181
- A.Z
assets:
- part1.png
- part2.png
- part3.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\theta= $
    suffix: $^{\circ}$
    comparison: sigfig
    digits: 2
part2:
  type: multiple-choice
  pl-customizations:
    weight: 1
    hide-letter-keys: true
part3:
  type: multiple-choice
  pl-customizations:
    weight: 1
    hide-letter-keys: true
myst:
  substitutions:
    params_v_t: 84
    params_b_t: 2.77
    params_r: 4000.0
    params_v_b: 233.0
    params_part2_ans1_value: true
    params_part2_ans1_feedback: Great! You got it.
    params_part2_ans2_value: false
    params_part2_ans2_feedback: The correct answer is true, because the angle the
      velocity of the bullet relative to the criminal makes with the line of sight
      of the criminal is always acute measured clockwise from the line of sight and
      the range of rotation of the criminal's head is acute, hence the criminal can
      always see the trajectory as it is within his field of view.
    params_part3_ans1_value: true
    params_part3_ans1_feedback: Great! You got it.
    params_part3_ans2_value: false
    params_part3_ans2_feedback: The correct answer is True, because the angle the
      velocity of the bullet relative to the criminal makes with the line of sight
      of the criminal is always obtuse measured anti-clockwise but the range of rotation
      of the criminal's head is acute.
---
# Sniper and Moving Target
A sniper has been ordered a hit on a dangerous criminal. It has been determined that the fugitive is being transported on a train and is seated in carriage B. The sniper plans to shoot during the time the train spends on the curve.

<img src="part1.png" width=500>

## Part 1

If the train moves with a constant speed of $v\_{train} = {{ params.v_t }}\ \rm{ms^{-1}}$ on the curve what is the angle $\theta$ measured relative to the horizontal that the sniper has to aim to hit the criminal?
<br>
Assume the bullet and train are on the same plane and neglect any resistive forces.
<br>
$v\_{bullet} = {{ params.v_b }}\ \rm{ms^{-1}}$, $R = {{ params_r }}\ \rm{m}$

### Answer Section

Please enter in the angle in degrees.

## Part 2

The sniper is not informed of the exact position and seating arrangement of the criminal in carriage B. If the position and line of sight of the criminal is as in the figure below, can the criminal see the trajectory of the bullet, allowing him to escape?

<img src="part2.png" width=500>

Assume the criminal can only rotate his head a maximum of **$90^{\circ}$ clockwise** from his **line of sight**. Also assume his line of sight is **collinear** with the velocity of the train.
<br>Assume the criminal has "laser vision acute vision in his line of sight".
<br>
Use the angle calculated in the previous part of this question for $\theta$.
<br><br>
<i>Hint: Start by calculating the relative velocity of the bullet to the criminal.</i>

### Answer Section

- {{ params_part2_ans1_value}}
- {{ params_part2_ans2_value}}

## Part 3

If the criminal is, however, in the opposite seat, can the sniper shoot at any point along the curve without the criminal being able to see the trajectory of the bullet?

<img src="part3.png" width=500>

Assume the criminal can only rotate his head a maximum of **$90^{\circ}$ anti-clockwise** from his **line of sight**. Also assume his line of sight is **collinear** with the velocity of the train.

### Answer Section

- {{ params_part3_ans1_value}}
- {{ params_part3_ans2_value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)