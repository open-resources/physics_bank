---
title: Vole Position
topic: Kinematics(1D)
author: John Hopkinson
source: PHYS 112 2019W1 GPS III
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 4.4.1.1
- 4.6.1.3
- 4.6.1.1
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
- JR
assets:
- vole_position_axes.png
- sample.html
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x(-2) = $
    suffix: $\rm{cm}$
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x(-1) = $
    suffix: $\rm{cm}$
    comparison: sigfig
    digits: 2
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x(0) = $
    suffix: $\rm{cm}$
    comparison: sigfig
    digits: 2
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x(1) = $
    suffix: $\rm{cm}$
    comparison: sigfig
    digits: 2
part5:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x(2) = $
    suffix: $\rm{cm}$
    comparison: sigfig
    digits: 2
part6:
  type: file-upload
  pl-customizations:
    file-names: part6.pdf
part7:
  type: symbolic-input
  pl-customizations:
    label: $v(t) = $
    variables: t
    weight: 1
    allow-blank: false
part8:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t_8 = $
    suffix: $\rm{s}$
    comparison: sigfig
    digits: 2
part9:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t_9 = $
    suffix: $\rm{s}$
    comparison: sigfig
    digits: 2
part10:
  type: longtext
  gradingMethod: Manual
  pl-customizations:
    placeholder: Type your answer here...
    file-name: answer.html
    quill-theme: snow
    directory: clientFilesQuestion
    source-file-name: sample.html
part11:
  type: checkbox
  pl-customizations:
    weight: 1
    partial-credit: true
    partial-credit-method: EDC
part12:
  type: checkbox
  pl-customizations:
    weight: 1
    partial-credit: true
    partial-credit-method: EDC
part13:
  type: symbolic-input
  pl-customizations:
    label: $a(t) = $
    variables: t
    weight: 1
    allow-blank: false
part14:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t_{14} = $
    suffix: $\rm{s}$
    comparison: sigfig
    digits: 2
part15:
  type: checkbox
  pl-customizations:
    weight: 1
    partial-credit: true
    partial-credit-method: EDC
part16:
  type: checkbox
  pl-customizations:
    weight: 1
    partial-credit: true
    partial-credit-method: EDC
myst:
  substitutions:
    params_vars_title: Vole Position
    params_part11_ans1_value: $t = -2 \rm{s}$ to $t = t_8$
    params_part11_ans2_value: $t = t_8$ to $t = t_9$
    params_part11_ans3_value: $t = t_9$ to $t = 2 \rm{s}$
    params_part12_ans1_value: $t = -2 \rm{s}$ to $t = t_8$
    params_part12_ans2_value: $t = t_8$ to $t = t_9$
    params_part12_ans3_value: $t = t_9$ to $t = 2 \rm{s}$
    params_part15_ans1_value: $t = -2 \rm{s}$ to $t = t_8$
    params_part15_ans2_value: $t = t_8$ to $t = t_{14}$
    params_part15_ans3_value: $t = t_{14}$ to $t = t_9$
    params_part15_ans4_value: $t = t_9$ to $t = 2 \rm{s}$
    params_part16_ans1_value: $t = -2 \rm{s}$ to $t = t_8$
    params_part16_ans2_value: $t = t_8$ to $t = t_{14}$
    params_part16_ans3_value: $t = t_{14}$ to $t = t_9$
    params_part16_ans4_value: $t = t_9$ to $t = 2 \rm{s}$
---
# {{ params_vars_title }}
The position of a vole as it runs toward a garden is given by the expression $x(t) = t^3 - t + 10$, where $x(t)$ is position expressed as a function of time $t$. The units of $x(t)$ are $\rm{cm}$ and the units of $t$ are $\rm{s}$.

## Part 1

Determine $x(t)$ when $t = -2 \rm{s}$.

### Answer Section

Please enter in a numeric value in $\rm{cm}$.

## Part 2

Determine $x(t)$ when $t = -1 \rm{s}$.

### Answer Section

Please enter in a numeric value in $\rm{cm}$.

## Part 3

Determine $x(t)$ when $t = 0 \rm{s}$.

### Answer Section

Please enter in a numeric value in $\rm{cm}$.

## Part 4

Determine $x(t)$ when $t = 1 \rm{s}$.

### Answer Section

Please enter in a numeric value in $\rm{cm}$.

## Part 5

Determine $x(t)$ when $t = 2 \rm{s}$.

### Answer Section

Please enter in a numeric value in $\rm{cm}$.

## Part 6

On the coordinate system below, plot each of the points from parts 1-5 and connect them with a smooth line.

Do this by downloading the image (right-click $\to$ save image as) and drawing on it. Upload your graph as a pdf titled "part6.pdf".

<img src="vole_position_axes.png" width=400 alt="Axes for a position versus time graph. The vertical axis is labelled position in centimetres, with 0 centimetres at the origin and each tick mark denoting a 2 centimetre interval. The horizontal axis is labelled time in seconds, with 0 seconds at the origin and each tick mark denoting a 1 second interval.">

### Answer Section

File upload box will be shown here.

## Part 7

Find an expression for the velocity of the vole as a function of time.

Note that it may not be necessary to use every variable. Use the following table as a reference for each variable:

| For | Use |
|-----|-----|
| $t$ | t   |

### Answer Section

## Part 8

What is the first time that the vole is at rest? (Enter the lowest value of $t$ even if it is less than $0$)

### Answer Section

Please enter in a numeric value in $\rm{s}$.

## Part 9

What time is the next time that the vole is at rest? (Enter the other value of $t$)

### Answer Section

Please enter in a numeric value in $\rm{s}$.

## Part 10

What does it mean for $t$ to be less than $0$?

### Answer Section

Answer in 1-2 sentences and try to use full sentences.

## Part 11

Select the interval(s) over which the velocity of the vole is positive.

Note: You will be awarded full marks only if you select all the correct choices, and none of the incorrect choices. Choosing incorrect choices as well as not choosing correct choices will result in deductions.

### Answer Section

- {{ params_part11_ans1_value}}
- {{ params_part11_ans2_value}}
- {{ params_part11_ans3_value}}
- {{ params.part11.ans4.value}}

## Part 12

Select the interval(s) over which the velocity of the vole is negative.

Note: You will be awarded full marks only if you select all the correct choices, and none of the incorrect choices. Choosing incorrect choices as well as not choosing correct choices will result in deductions.

### Answer Section

- {{ params_part12_ans1_value}}
- {{ params_part12_ans2_value}}
- {{ params_part12_ans3_value}}
- {{ params.part12.ans4.value}}

## Part 13

Find an expression for the acceleration of the vole as a function of time.

Note that it may not be necessary to use every variable. Use the following table as a reference for each variable:

| For | Use |
|-----|-----|
| $t$ | t   |

### Answer Section

## Part 14

At what time is the acceleration of the vole zero?

### Answer Section

Please enter in a numeric value in $\rm{s}$.

## Part 15

Select the intervals over which the speed of the vole is increasing.

Note: You will be awarded full marks only if you select all the correct choices, and none of the incorrect choices. Choosing incorrect choices as well as not choosing correct choices will result in deductions.

### Answer Section

- {{ params_part15_ans1_value}}
- {{ params_part15_ans2_value}}
- {{ params_part15_ans3_value}}
- {{ params_part15_ans4_value}}

## Part 16

Select the intervals over which the speed of the vole is decreasing.

Note: You will be awarded full marks only if you select all the correct choices, and none of the incorrect choices. Choosing incorrect choices as well as not choosing correct choices will result in deductions.

### Answer Section

- {{ params_part16_ans1_value}}
- {{ params_part16_ans2_value}}
- {{ params_part16_ans3_value}}
- {{ params_part16_ans4_value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)