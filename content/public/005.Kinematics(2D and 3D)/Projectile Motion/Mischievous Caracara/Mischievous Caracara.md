---
title: A Mischievous Caracara
topic: Kinematics(2D and 3D)
author: Reza Khanbabaie
source: PHYS 112 Projectile Motion Q1
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 5.1.1.0
- 5.4.1.1
- 5.5.1.0
- 5.2.1.0
- 5.2.1.1
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
assets:
- sample.html
part1:
  type: file-upload
  pl-customizations:
    file-names: part1Diagram.pdf
part2:
  type: longtext
  gradingMethod: Manual
  pl-customizations:
    placeholder: Type your answer here...
    file-name: part2answer.html
    quill-theme: snow
    directory: clientFilesQuestion
    source-file-name: sample.html
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v = $
    suffix: $\rm{m/s}$
part4:
  type: multiple-choice
  pl-customizations:
    weight: 1
part5:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    blank-value: false
    label: $\vec{a} = $
    suffix: $\rm{m/s^2}$
part6:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\vec{a} = $
    suffix: $\rm{m/s^2}$
part7:
  type: multiple-choice
  pl-customizations:
    weight: 1
part8:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\Delta t = $
    suffix: $\rm{s}$
part9:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\Delta x = $
    suffix: $\rm{m}$
substitutions:
  params:
    vars:
      title: A Mischievous Caracara
    v: 6
    h: 6
    part4:
      ans1:
        value: East
        feedback: Great! You got it.
      ans2:
        value: West and down
        feedback: Hmh...Try again!
      ans3:
        value: East and down
        feedback: The nut does not start moving down immediately
      ans4:
        value: South and up
        feedback: Hmh...Try again!
      ans5:
        value: East and up
        feedback: Hmh...Try again!
      ans6:
        value: South and down
        feedback: Hmh...Try again!
    part7:
      ans1:
        value: Down
        feedback: Great! You got it.
      ans2:
        value: West and down
        feedback: Hmh...Try again!
      ans3:
        value: North and up
        feedback: Hmh...Try again!
      ans4:
        value: West and up
        feedback: Hmh...Try again!
      ans5:
        value: West
        feedback: Gravity is the only source of acceleration!
      ans6:
        value: Up
        feedback: 'Hint: acceleration due to gravity.'
---
# {{ params.vars.title }}
A mischievous caracara sees a fisherman unscrew a shiny steel nut from a bolt on his ship while doing repairs in a harbor off the Falkland Islands.  The fisherman watches helplessly as the bird picks up the nut and flies toward the shore.  The bird flies due east at a constant speed of {{ params.v }} $\rm{m/s}$ and constant height of {{ params.h }} $\rm{m}$.  The bird flies directly over a person on the shoreline, dropping the nut at the instant they are above the person.

## Part 1

Prepare:

Draw a pictorial representation of this problem showing the location of the person on the shore, the path travelled by the bird and the path travelled by the nut.  On your diagram label the position, velocity, acceleration, and time at **three important positions** for each of the bird and the nut.  Use a dashed line to indicate the trajectory of the nut after it has been released.

### Answer Section

## Part 2

Prepare: Explain why the air resistance of the nut can be neglected in this problem.

### Answer Section

Answer in 1-2 sentences, and try to use full sentences.

## Part 3

Prepare: At the instant the caracara releases the nut, what is the magnitude of the velocity vector of the nut?

### Answer Section

Please enter in a numeric value in $\rm{m/s}$.

## Part 4

Prepare: At the instant the caracara releases the nut, in which directions does the velocity vector of the nut have components along?

### Answer Section

- {{ params.part4.ans1.value }}
- {{ params.part4.ans2.value }}
- {{ params.part4.ans3.value }}
- {{ params.part4.ans4.value }}

## Part 5

Prepare: While travelling with the bird, what is the nut's acceleration vector?

### Answer Section

Please enter in a numeric value in $\rm{m/s^2}$.

## Part 6

Prepare: Once the nut has been released, what is the magnitude of its acceleration vector?

### Answer Section

Please enter in a numeric value in $\rm{m/s^2}$.

## Part 7

Prepare: Once the nut has been released, in which directions does the acceleration vector have components along?

### Answer Section

- {{ params.part7.ans1.value }}
- {{ params.part7.ans2.value }}

## Part 8

Solve: How long does it take the nut to fall to the ground?

### Answer Section

Please enter in a numeric value in $\rm{s}$.

## Part 9

Solve: How far from the person on the shoreline does the nut land?

### Answer Section

Please enter in a numeric value in $\rm{m}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)