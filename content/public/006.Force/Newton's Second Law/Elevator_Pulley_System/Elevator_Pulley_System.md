---
title: Elevator Pulley System
topic: Force
author: John Hopkinson
source: Phys 112 2018W1 GPS VIII
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.1.1.5
- 6.1.1.7
- 6.2.1.1
- 6.2.1.2
- 6.3.1.3
- 6.3.1.1
- 6.5.1.1
- 6.6.1.2
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
- elevatorperson2.png
- sample.html
part1:
  type: dropdown
  pl-customizations:
    weight: 1
    blank: true
part2:
  type: longtext
  gradingMethod: Manual
  pl-customizations:
    placeholder: Type your answer here...
    file-name: answer.html
    quill-theme: snow
    directory: clientFilesQuestion
    source-file-name: sample.html
part3:
  type: file-upload
  pl-customizations:
    file-names: fid.pdf
part4:
  type: file-upload
  pl-customizations:
    file-names: fbd.pdf
part5:
  type: symbolic-input
  pl-customizations:
    label: $Ma = $
    variables: m, M, theta, g, T, n_pe, n_ep
    weight: 1
    allow-blank: true
part6:
  type: symbolic-input
  pl-customizations:
    label: $ma = $
    variables: m, M, theta, g, T, n_pe, n_ep
    weight: 1
    allow-blank: true
part7:
  type: checkbox
  pl-customizations:
    weight: 1
    partial-credit: true
    partial-credit-method: EDC
part8:
  type: dropdown
  pl-customizations:
    weight: 1
    blank: 'true'
part9:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $T = $
    suffix: $\rm{N}$
part10:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $n_{\text{pe}} = $
    suffix: $\rm{N}$
myst:
  substitutions:
    params_vars_title: Elevator Pulley System
    params_m_p: 86
    params_M_e: 27
    params_ang: 20
    params_part1_ans1_value: 'Yes'
    params_part1_ans2_value: 'No'
    params_part7_ans1_value: $Mg$
    params_part7_ans2_value: $mg$
    params_part7_ans3_value: $n_{ep}$
    params_part7_ans4_value: $n_{pe}$
    params_part7_ans5_value: $T$
    params_part8_ans1_value: 'Yes'
    params_part8_ans2_value: 'No'
---
# {{ params_vars_title }}
A $m = {{ params.m_p }} \rm{kg}$ person in a $M = {{ params.M_e }} \rm{kg}$ elevator lifts themselves at constant velocity by pulling on the rope shown in the figure below. The rope passes over a pulley attached to the top of the elevator shaft, back over a pulley attached to the top of the elevator, over a second pulley attached to the top of the elevator shaft, and attaches to the top of the elevator. Treat the rope as if it is massless and the pulleys as if they are frictionless and massless. At the instant shown in the figure below, the rope passing over the elevator's pulley makes a $\theta = {{ params_ang }}^\circ$ angle with the vertical.

<img src="elevatorperson2.png" width=400 alt="An image of a person in an elevator. The person is holding on to a rope that passes through the top of the elevator and over a pulley attached to the top of the elevator shaft, making an angle of 20 degrees with itself. The rope then passes over a pulley attached to the top of the elevator, making an angle of 40 degrees with itself. The rope again passes over a pulley connected to the top of the elevator shaft and connects directly to the top of the elevator, making an angle of 20 degrees with itself. The portion of the rope that is held by the person and passes over the pulley connected to the top of the elevator shaft runs vertically. The portion of the rope that is connected directly to the top of the elevator and passes over the pulley connected to the top of the elevator shaft also runs vertically.">

## Part 1

Should the tension in the rope be the same in all portions of the rope?

### Answer Section

- {{ params.part1.ans1 }}
- {{ params.part1.ans2 }}

## Part 2

Explain your answer to Part 1.

### Answer Section

Answer in 1-2 full sentences.

## Part 3

Draw force identification diagrams for the elevator and the person.

Be sure to label the weight of the person $mg$, the weight of the elevator $Mg$, the tension $T$, the normal force of the person acting on the elevator $n\_{\text{pe}}$, and the normal force of the elevator acting on the person $n\_{\text{ep}}$.

Save your force identification diagrams as "fid.pdf" and upload the file below.

### Answer Section

File upload box will be shown here.

## Part 4

Draw free body diagrams for the elevator and the person.

Be sure to label the weight of the person $mg$, the weight of the elevator $Mg$, the tension $T$, the normal force of the person acting on the elevator $n\_{\text{pe}}$, and the normal force of the elevator acting on the person $n\_{\text{ep}}$. Specify the net force beside your diagrams.

Save your free body diagrams as "fbd.pdf" and upload the file below.

### Answer Section

File upload box will be shown here.

## Part 5

Write Newton's second law in the vertical direction for the elevator.

Note that it may not be necessary to use every variable. Use the following table as a reference for using each variable:

| For             | Use   |
|-----------------|-------|
| $m$             | m     |
| $M$             | M     |
| $\theta$        | theta |
| $T$             | T     |
| $g$             | g     |
| $n\_{\text{pe}}$ | n_pe  |
| $n\_{\text{ep}}$ | n_ep  |

### Answer Section

## Part 6

Write Newton's second law in the vertical direction for the person.

Note that it may not be necessary to use every variable. Use the following table as a reference for using each variable:

| For             | Use   |
|-----------------|-------|
| $m$             | m     |
| $M$             | M     |
| $\theta$        | theta |
| $T$             | T     |
| $g$             | g     |
| $n\_{\text{pe}}$ | n_pe  |
| $n\_{\text{ep}}$ | n_ep  |

### Answer Section

## Part 7

Which two forces are related by Newton's third law?

### Answer Section

Select all the choices that apply.

Note: You will be awarded full marks only if you select all the correct choices, and none of the incorrect choices. Choosing incorrect choices as well as not choosing correct choices will result in deductions.

- {{ params_part7_ans1_value}}
- {{ params_part7_ans2_value}}
- {{ params_part7_ans3_value}}
- {{ params_part7_ans4_value}}
- {{ params_part7_ans5_value}}

## Part 8

Are the two forces identified in Part 8 on the same free body diagram?

### Answer Section

- {{ params.part8.ans1 }}
- {{ params.part8.ans2 }}

## Part 9

Solve the equations in Part 5 and Part 6 for the tension in the rope.

### Answer Section

Please enter in a numeric value in $\rm{N}$.

## Part 10

Solve the equations in Part 5 and Part 6 for the apparent weight of the person as measured by a scale under their feet while they are pulling up on the rope.

### Answer Section

Please enter in a numeric value in $\rm{N}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)