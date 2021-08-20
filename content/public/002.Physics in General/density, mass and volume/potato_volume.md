---
title: Potato Volume
topic: Physics in General
author: John Hopkinson
source: GPSI 2020 Q1
template_version: 1.1
attribution: standard
outcomes:
- 13.2.1.2
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- AP
assets: null
part1:
  type: number-input
  pl-customizations:
    label: $m= $
    allow-blank: true
    weight: 1
part2:
  type: number-input
  pl-customizations:
    label: $m= $
    allow-blank: true
    weight: 1
part3:
  type: number-input
  pl-customizations:
    label: $V= $
    allow-blank: true
    weight: 1
substitutions:
  params:
    vars:
      name: Maya
      title: Potato Volume
      mass_units: kg
      volume_units: m^3
      mass_potato: 382
      mass_cube: 68
      cube_side_length: 3.37
---
# {{ params.vars.title }}
For our first lab, {{params.vars.name}} decides to measure the density of a potato.
They notice that it's an unsual shape and floats, so it's hard to calculate it's volume.
The potato's mass is measured to be {{params.vars.mass_potato}} g.
They then cut the potato into a cube and measure that sides of the cube have length {{params.vars.cube_side_length}} inches and it's mass is {{params.vars.mass_cube}} g.
For a uniform density potato, the mass and volume are proportional. (Useful conversions: 1 inch = 2.54cm, 1cm = $10^{-2}$m, 1g = $10^{-3}$kg)
## Part 1

In SI units, what is the potato's mass?

### Answer Section

Please enter in a numeric value in {{ params.vars.mass_units }}.
## Part 2

In SI units, what is the cube of the potato's mass?

### Answer Section

Please enter in a numeric value in {{ params.vars.mass_units }}.
## Part 3

In SI units, what is the volume of the cube of potato after it has been cut?

### Answer Section

- {{ params.correct_answers.part1_ans}} {{ params.vars.mass_units}}
- {{ params.correct_answers.part2_ans}} {{ params.vars.mass_units}}
- {{ params.correct_answers.part3_ans}} {{ params.vars.volume_units}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)