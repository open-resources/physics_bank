---
title: Field Goal Kicker
topic: Kinematics(2D and 3D)
author: Firas Moosvi
source: OPUS V1 Problem 4.100
template_version: 1.4
attribution: openstax-physics-vol1
partialCredit: true
singleVariant: true
showCorrectAnswer: false
outcomes:
- 5.5.1.0
difficulty:
- hard
randomization:
- undefined
taxonomy:
- undefined
span:
- undefined
length:
- medium
tags:
- JR
assets:
- fieldgoal.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t = $
    suffix: $\rm{s}$
    comparison: relabs
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v_i = $
    suffix: $\rm{m/s}$
    comparison: relabs
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\Delta h = $
    suffix: $\rm{m}$
    comparison: relabs
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\Delta h = $
    suffix: $\rm{m}$
    comparison: relabs
myst:
  substitutions:
    params:
      vars:
        title: Field Goal Kicker
      theta: 35
      hg: 1.7
      dg: 27.4
      deltahg: 1.6
      hl: 2.53
      dl1: 5.0
      dl2: 1.0
---
# {{ params.vars.title }}
When a field goal kicker kicks a football at ${{ params.theta }}^\circ$ to the horizontal, the ball clears the crossbar of the goalposts by ${{ params.deltahg }}$ $\rm{m}$.
The crossbar of the goalpoasts is ${{ params.hg }}$ $\rm{m}$ above the field and ${{ params.dg }}$ $\rm{m}$ away from the kicker.

<img src="fieldgoal.png" width=400 alt="An image showing a field goal kicker kicking a field goal. The trajectory of the football is shown by a purple line that initially makes an angle of theta with the horizontal. A defensive lineman stands between the field goal kicker and the goalpoasts.">

## Part 1

Calculate the time it takes for the ball's horizontal position to be in line with the crossbar of the goalposts.

### Answer Section

Please enter an answer in $\rm{s}$.

## Part 2

What initial speed $v_i$ does the kicker impart to the football?

### Answer Section

Please enter an answer in $\rm{m/s}$.

## Part 3

In addition to clearing the crossbar, the football must be high enough in the air early during its flight to clear the reach of the onrushing defensive lineman.
If the lineman is ${{ params.dl1 }}$ $\rm{m}$ away and has a vertical reach of ${{ params.hl }}$ $\rm{m}$, at what height does the football pass the linesman relative to their reach $\Delta h$?
Hint: A negative answer indicates that the field goal attempt would be blocked.

### Answer Section

Please enter an answer in $\rm{m}$.

## Part 4

What if the lineman is ${{ params.dl2 }}$ $\rm{m}$ away and had the same vertical reach of ${{ params.hl }}$ $\rm{m}$ - at what height does the football pass the linesman relative to their reach $\Delta h$?

### Answer Section

Please enter an answer in $\rm{m}$.

## Attribution

Problem is from the [OpenStax University Physics Volume 1](https://openstax.org/details/books/university-physics-volume-1) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)