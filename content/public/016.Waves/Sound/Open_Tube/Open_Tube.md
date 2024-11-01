---
title: Standing Waves in Open_Closed Tube
topic: Waves
author: John Hopkinson
source: Physics 2019 122 GPSV
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 16.7.1.1
- 16.7.1.7
- 16.7.2.0
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
assets:
- openclosed.png
part1:
  type: file-upload
  pl-customizations:
    file-names: Wave.png
part2:
  type: symbolic-input
  pl-customizations:
    label: $λ =$
    variables: L
    weight: 1
    allow-blank: true
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
    label: $L= $
    suffix: m
myst:
  substitutions:
    params:
      vars:
        title: Standing Waves in Open_Closed Tube
      part3:
        ans1:
          value: First Harmonic
        ans2:
          value: Third Harmonic
          feedback: Great! You got it.
        ans3:
          value: Second Harmonic
        ans4:
          value: Fourth Harmonic
      v: 264
      f: 560
---
# {{ params.vars.title }}
<img src="openclosed.png" width="400">

In the figures above, snapshots of a standing wave in an open-closed tube are shown at $t$ = 0 s and $t = \frac{T}{4}$, where $T$ is the period of the wave's oscillation.

## Part 1

Based on these graphs, label any nodes and antinodes on the top figure, and then draw the snapshot graph at $t = \frac{T}{2}$ on the bottom graph.

Finally, draw arrows or dot diagrams representing the motion of the displacement of the atoms of the air in this harmonic on each graph.

Your file upload should be named 'Wave' and must be a png file.

### Answer Section

File upload box will be shown here.

## Part 2

What is the wavelength of this wave in terms of the length of the tube, $L$?

Use the following table as a reference:

| For      | Use   |
|----------|-------|
| $L$      | L     |

### Answer Section

## Part 3

Which harmonic is this standing wave?

### Answer Section

- {{ params.part3.ans1}} {{ params.vars.units}}
- {{ params.part3.ans2}} {{ params.vars.units}}
- {{ params.part3.ans3}} {{ params.vars.units}}
- {{ params.part3.ans4}} {{ params.vars.units}}

## Part 4

If this tube were in some medium with the speed of sound as {{params.v}}m/s, what length would it have to have to sound the note A ({{ params.f}}Hz) and it remained in this standing wave?

### Answer Section

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)