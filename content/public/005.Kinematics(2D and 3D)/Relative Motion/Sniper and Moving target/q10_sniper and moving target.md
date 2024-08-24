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
    params:
      v_t: 91
      b_t: 2.26
      r: 4700.0
      v_b: 206.0
      part2:
        ans1:
          value: 'True'
          feedback: Great! You got it.
        ans2:
          value: 'False'
          feedback: The correct answer is True, because the angle the velocity of
            the bullet relative to the criminal makes with the line of sight of the
            criminal is always acute measured clockwise from the line of sight and
            the range of rotation of the criminal's head is acute, hence the criminal
            can always see the trajectory as it is within his field of view.
      part3:
        ans1:
          value: 'True'
          feedback: The correct answer is False, because the angle the velocity of
            the bullet relative to the criminal makes with the line of sight of the
            criminal is always obtuse measured anti-clockwise but the range of rotation
            of the criminal's head is acute.
        ans2:
          value: 'False'
          feedback: Great! You got it.
---
# Sniper and Moving Target
A sniper has been ordered a hit on a dangerous criminal. It has been determined that the fugitive is being transported on a train and is seated in carriage B. The sniper plans to shoot during the time the train spends on the curve.

<img src="part1.png" width=700>

## Part 1

If the train moves with a constant speed of $v\_{train} = {{ params.v_t }}\ \rm{m/s}$ on the curve what is the angle $\theta$ measured relative to the horizontal that the sniper has to aim to hit the criminal?
<br>
Assume the bullet and train are on the same plane and neglect any resistive forces.
<br>
$v\_{bullet} = {{ params.v_b }}\ \rm{m/s}$, $R = {{ params.r }}\ \rm{m}$

### Answer Section

Please enter in the angle in degrees.

## Part 2

The sniper is not informed of the exact position and seating arrangement of the criminal in carriage B. If the position and line of sight of the criminal is as in the figure below, can the criminal see the trajectory of the bullet, allowing him to escape?

<img src="part2.png" width=700>

Assume the criminal can only rotate his head a maximum of **$90^{\circ}$ clockwise** from his **line of sight**. Also assume his line of sight is **collinear** with the velocity of the train.
<br>Assume the criminal has "laser vision in his line of sight".
<br>
Use the angle calculated in the previous part of this question for $\theta$.
<br><br>
<i>Hint: Start by calculating the relative velocity of the bullet to the criminal.</i>

### Answer Section

- {{ params.part2.ans1.value}}
- {{ params.part2.ans2.value}}

## Part 3

If the criminal is, however, in the opposite seat, can the criminal see the trajectory of the bullet, allowing him to escape?

<img src="part3.png" width=700>

Assume the criminal can only rotate his head a maximum of **$90^{\circ}$ anti-clockwise** from his **line of sight**. Also assume his line of sight is **collinear** with the velocity of the train.

### Answer Section

- {{ params.part3.ans1.value}}
- {{ params.part3.ans2.value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)