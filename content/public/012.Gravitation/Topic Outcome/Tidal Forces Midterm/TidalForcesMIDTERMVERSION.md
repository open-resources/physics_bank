---
title: Tidal Forces
topic: Gravitation
author: Ammar Zavahir
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- null
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
- APSC181
- Midterm 2023
assets:
- Tides1.png
- Tides2.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F = $
    suffix: $\rm{N}$
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\theta = $
    suffix: $^{\circ}$
    comparison: sigfig
    digits: 2
part3:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params_vars_title: Tidal Forces
    params_vars_units: "$\rm{m/s^2}$"
    params_Me: 5.975999999999999e+24
    params_Dse: 146
    params_Dme: 384413
    params_part3_ans1_value: A
    params_part3_ans2_value: B
    params_part3_ans3_value: C
---
# {{ params_vars_title }}
<img src="Tides1.png" width=400>

The height of the ocean tides periodically vary according to the time of day due to the orbital motion of the Earth around the Moon coupled with that of the Earth around the Sun, and the changing gravitational forces acting on the Earth.

$G = 6.67 \times 10^{-11}, M\_{earth} = 5.976 \times 10^{24} \ \rm{kg}, M\_{sun} = 333000 M\_{earth}, M\_{moon} = 0.0123 M\_{earth}$
$D\_{MoonEarth} = {{ params_Dme }} \ \rm{km}, D\_{SunEarth} = {{ params_Dse }} \times 10^6 \ \rm{km}$

## Part 1

In the relative configuration given below, determine the magnitude of the resultant gravitational force acting on the Earth.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 2

In the relative configuration given below, determine the direction of the resultant gravitational force acting on the Earth.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 3

<img src="Tides2.png" width=400>

If the depth of the tides are measured normal to the Earth's surface with the surface of the Earth being that of zero displacement, at what point along the orbit of the Moon around the Earth causes the highest tides?

### Answer Section

Choose the best answer.

- {{ params.part2.ans1.value }}
- {{ params.part2.ans2.value }}
- {{ params.part2.ans3.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)