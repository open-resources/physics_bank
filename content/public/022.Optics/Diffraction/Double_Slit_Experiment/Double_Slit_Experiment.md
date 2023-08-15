---
title: Double Slit Experiment
topic: Optics
author: John Hopkinson
source: Physics 2019 122 GPSVII
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 22.3.2.0
- 22.3.2.1
- 22.3.2.2
- 22.4.2.1
- 22.4.2.2
- 22.4.2.3
difficulty:
- undefined
randomization:
- 2
taxonomy:
- undefined
span:
- undefined
length:
- undefined
tags:
- L.K
assets: null
part1:
  type: file-upload
  pl-customizations:
    file-names: Slit1.png
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $= $
    suffix: m
part3:
  type: dropdown
  pl-customizations:
    weight: 1
    blank: 'true'
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $m= $
    suffix: null
part5:
  type: file-upload
  pl-customizations:
    file-names: Slit2.png
myst:
  substitutions:
    params_vars_title: Double Slit Experiment
    params_l: 536
    params_w: 103
    params_s: 436
    params_d: 13
    params_part3_ans1_value: bright
    params_part3_ans2_value: dark
    params_part3_ans3_value: no pattern appears
---
# {{ params_vars_title }}
A double slit experiment with {{ params_l}}nm light has a slit width of {{ params_w}}$\mu$m, and a slit separation of {{ params_s}}nm

## Part 1

Draw a diagram showing the widths of the two slits and their separation.

Upload a file named 'Slit1' and must be a png.

### Answer Section

File upload will appear here

### pl-submission-panel

### pl-answer-panel

## Part 2

If the screen is {{ params_d}}m away, find the location of the edge of the central maximum from the centre of the single slit diffraction pattern, assuming the small angle approximation is valid.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

### pl-submission-panel

{{ feedback.part2_ans }}

### pl-answer-panel

## Part 3

When observing a double-slit pattern, you would notice a bright line at a specific location. However, in the single-slit pattern, destructive interference occurs due to the width of each slit. Given this information, at the same location, the resulting pattern will be;

### Answer Section

- {{ params.part3.ans1}} {{ params.vars.units}}
- {{ params.part3.ans2}} {{ params.vars.units}}
- {{ params.part3.ans3}} {{ params.vars.units}}

### pl-submission-panel

### pl-answer-panel

## Part 4

Is there a bright line of the double slit pattern that coincides with the underlying single slit pattern's first minimum?  If so, at what diffraction order, $m$ does this occur?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

### pl-submission-panel

{{ feedback.part4_ans }}

### pl-answer-panel

## Part 5

Draw the combined double slit single slit pattern for $m$ = -8 to $m$ = 8.

Upload a file named 'Slit2' and must be a png.

### Answer Section

File upload will appear here

### pl-submission-panel

### pl-answer-panel

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)