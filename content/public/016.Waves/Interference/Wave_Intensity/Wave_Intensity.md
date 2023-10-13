---
title: Wave Intensity
topic: Waves
author: John Hopkinson
source: Physics_2019_Midterm2_Q4
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 16.6.1.3
- 16.6.1.4
- 16.6.1.5
difficulty:
- undefined
randomization:
- 0
taxonomy:
- undefined
span:
- undefined
length:
- undefined
tags:
- L.K
assets:
- doubleslitsmall.png
part1:
  type: file-upload
  pl-customizations:
    file-names: file.png
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $ $
    suffix: λ
part3:
  type: dropdown
  pl-customizations:
    weight: 1
    blank: 'true'
part4:
  type: dropdown
  pl-customizations:
    weight: 1
    blank: 'true'
myst:
  substitutions:
    params_vars_title: Wave Intensity
    params_part3_ans1_value: ' less than the intensity of the source waves.'
    params_part3_ans1_feedback: ''
    params_part3_ans2_value: ' greater than the intensity of the source waves.'
    params_part3_ans2_feedback: Great! You got it.
    params_part4_ans1_value: ' greater than the intensity of the source waves.'
    params_part4_ans1_feedback: ''
    params_part4_ans2_value: ' less than the intensity of the source waves.'
    params_part4_ans2_feedback: Great! You got it.
---
# {{ params_vars_title }}
<img src="doubleslitsmall.png" width="400">

The two-dimensional snapshot of the interference of waves from two sources is shown in the figure, where bright lines represent wave crests.

## Part 1

With an arrow identify and label the location of the two sources (call one source 1, and the other source 2) of these waves. On the same diagram at the edge of figure identify with an arrow the location of the $m = -2$, $m = 0$ and $m = 2$ antinodal lines.

Upload your labeled diagram as png named 'file'.

### Answer Section

File upload box will be shown here.

### pl-submission-panel

### pl-answer-panel

## Part 2

Along the $m = 2$ antinodal line, what is the path length difference traveled by the wave from source 2 relative to source 1 in terms of the wavelength of the wave?

### Answer Section

{{ feedback.part2_ans }}

### pl-submission-panel

### pl-answer-panel

## Part 3

Where two troughs align along an antinodal line, the intensity of the wave is

### Answer Section

- {{ params.part3.ans1}} {{ params.vars.units}}
- {{ params.part3.ans2}} {{ params.vars.units}}

### pl-submission-panel

### pl-answer-panel

## Part 4

Where a trough and a crest align along a nodal line, the intensity of the wave is

### Answer Section

- {{ params.part4.ans1}} {{ params.vars.units}}
- {{ params.part4.ans2}} {{ params.vars.units}}

### pl-submission-panel

### pl-answer-panel

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)