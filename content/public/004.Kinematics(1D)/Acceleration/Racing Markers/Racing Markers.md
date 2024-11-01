---
title: Racing Markers
topic: Kinematics(1D)
author: Firas Moosvi
source: Original
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes: null
difficulty:
- easy
randomization:
- undefined
taxonomy:
- undefined
span:
- undefined
length:
- short
tags:
- FM
assets:
- car_markers.png
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
    fixed-order: true
myst:
  substitutions:
    params:
      vars:
        vehicle: sedan
        title: Racing Markers
        v1: 58
        v2: 29.0
      part1:
        ans1:
          value: Marker 1
        ans2:
          value: Between Marker 1 and Marker 2
        ans3:
          value: Marker 2
        ans4:
          value: Between Marker 2 and Marker 3
        ans5:
          value: Marker 3
        ans6:
          value: Between Marker 3 and Marker 4
        ans7:
          value: Marker 4
        ans8:
          value: There is not enough information in the question.
---
# {{ params.vars.title }}
A {{ params.vars.vehicle }} accelerates uniformly from rest along a straight track towards the left.
The track has five markers: Start, and Markers 1-4.
Each marker is equally spaced so Marker 2 is halfway between Start and Marker 4.
The {{ params.vars.vehicle }} reaches a speed of {{ params.vars.v1 }} m/s as it passes the last marker, Marker 4.

<img src="car_markers.png" width=100%>

## Part 1

Where is the {{ params.vars.vehicle }} along the track when it is traveling at {{ params.vars.v2 }} m/?

Select the closest position from the list below...

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}
- {{ params.part1.ans5.value }}
- {{ params.part1.ans6.value }}
- {{ params.part1.ans7.value }}
- {{ params.part1.ans8.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)