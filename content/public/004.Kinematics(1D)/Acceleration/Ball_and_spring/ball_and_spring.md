---
title: Ball and a Spring
topic: Kinematics(1D)
author: Jake Bobowski
source: 2016 Final Q3 P2
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.11.2.1
- 4.1.1.1
- 4.3.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- AK
- MP
assets:
- sample.html
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: m/s
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: m/s
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $d= $
    suffix: m
part4:
  type: symbolic-input
  label: $a=$
  pl-customizations:
    variables: i_hat, j_hat, g
    allow-blank: true
    weight: 1
part5:
  type: longtext
  gradingMethod: Manual
  pl-customizations:
    placeholder: Type your answer here...
    file-name: answer.html
    quill-theme: snow
    directory: clientFilesQuestion
    source-file-name: sample.html
substitutions:
  params:
    vars:
      title: Ball and a spring
      units1_2: "$\rm{m/s}$"
      units3: "$\rm{m}$"
      units4: "$\rm{m/s^2}$"
    m: 0.30000000000000004
    deg: 29
    h: 0
    x: 5
    k: 500
    a_a: 0.03
    a_b: 0.06
---
# {{ params.vars.title }}
I have built a game that involves a spring, a smooth slope, and a little ball of $m = ${{params.m}} kg.
The slope is {{params.deg}}$^{\circ}$ above the horizontal.
The spring is placed into a small hole such that when it is compressed to the proper starting position, and the ball is placed upon it, the ball will be at the height $h = ${{params.h}} m. The spring has been compressed by 3 cm and has a spring constant of $k = ${{params.k}} N/m.

## Part 1

When I press a button, the ball is pushed up the slope by the spring.
How fast is the ball traveling when it is {{params.a_a}} m up the slope?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1_2 }}.

## Part 2

How fast is the ball traveling when it is {{params.a_b}} m up the slope?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1_2 }}.

## Part 3

What is the maximum DISTANCE the ball reaches from the bottom of the slope?

### Answer Section

Please enter in a numeric value in {{ params.vars.units3 }}.

## Part 4

Calculate the acceleration of the ball as it goes UP the slope once it is beyond the spring?

You may draw a free body diagram in order to help you write the final acceleration vector in terms of $\hat\imath$ (pointing down-slope) and $\hat\jmath$ (pointing perpendicular to the slope). Enter answer as a symbolic expression (sin(30) instead of 0.86602).

| For  | Use   |
|----------|-------|
| $\hat\imath$  | i_hat |
| $\hat\jmath$  | j_hat  |
| $g$  | g  |

### Answer Section

## Part 5

What is the acceleration of the ball as it goes DOWN the slope? Justify your answer.

### Answer Section

Answer in the box below.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)