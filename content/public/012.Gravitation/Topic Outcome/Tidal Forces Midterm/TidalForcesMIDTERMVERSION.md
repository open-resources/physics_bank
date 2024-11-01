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
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\theta = $
    suffix: $^{\circ}$
part3:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Tidal Forces
        units: "$\rm{m/s^2}$"
      Me: 5.975999999999999e+24
      Dse: 145
      Dme: 384252
      part3:
        ans1:
          value: $\rm{A}$
        ans2:
          value: $\rm{B}$
        ans3:
          value: $\rm{C}$
---
# {{ params.vars.title }}
<img src="Tides1.png" width=700>

The height of the ocean tides periodically vary according to the time of day due to the orbital motion of the Earth around the Moon coupled with that of the Earth around the Sun, and the changing gravitational forces acting on the Earth.

$G = 6.67 \times 10^{-11} \ \rm{m^3. kg^{-1}. s^{-2}}$ <br> $M\_{earth} = 5.976 \times 10^{24} \ \rm{kg}, \ M\_{sun} = 333000 \ . \ M\_{earth}, \ M\_{moon} = 0.0123 \ . \ M\_{earth}$ <br>
$D\_{MoonEarth} = {{ params.Dme }} \ \rm{km}, D\_{SunEarth} = {{ params.Dse }} \times 10^6 \ \rm{km}$

## Part 1

In the relative configuration given below, determine the magnitude of the resultant gravitational force acting on the Earth. Use e+XX for powers of 10 notation, ie 4 * 10^10 = 4e+10.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

In the relative configuration given below, determine the direction of the resultant gravitational force acting on the Earth.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 3

<img src="Tides2.png" width=700>

If the depth of the tides are measured normal to the Earth's surface with the surface of the Earth being that of zero displacement, at what point along the orbit of the Moon around the Earth causes the highest tides?

### Answer Section

Choose the best answer.

- {{ params.part2.ans1.value }}
- {{ params.part2.ans2.value }}
- {{ params.part2.ans3.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)