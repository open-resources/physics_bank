---
title: Potato Volume
topic: Physics in General
author: John Hopkinson
source: GPSI 2020 Q1
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 13.2.1.2
difficulty:
- Easy
randomization:
- undefined
taxonomy:
- undefined
span:
- undefined
length:
- undefined
tags:
- AP
- Short
- Chapter
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $m= $
    allow-blank: true
    weight: 1
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $m= $
    allow-blank: true
    weight: 1
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    label: $V= $
    allow-blank: true
    weight: 1
substitutions:
  params:
    vars:
      name: Emilia
      title: Potato Volume
      mass_units: kg
      volume_units: m^3
      mass_potato: 182
      mass_cube: 28
      cube_side_length: 1.1348863707847383
---
# {{ params.vars.title }}
For our first lab, {{params.vars.name}} decides to measure the density of a potato.
They notice that it is an unsual shape and floats, so it is hard to calculate its volume.
The potato's mass is measured to be {{params.vars.mass_potato}} g.
They then cut the potato into a cube and measure that sides of the cube have length {{params.vars.cube_side_length}} inches and it's mass is {{params.vars.mass_cube}} g.
For a uniform density potato, the mass and volume are proportional. (Useful conversions: 1 inch = 2.54cm, 1cm = $10^{-2}$m, 1g = $10^{-3}$kg)

## Part 1

In SI units, what is the uncut potato's mass?

### Answer Section

Please enter in a numeric value in {{ params.vars.mass_units }}.

## Part 2

In SI units, what is the mass of the potato cube?

### Answer Section

Please enter in a numeric value in {{ params.vars.mass_units }}.

## Part 3

In SI units, what is the volume of the potato cube after it has been cut?

### Answer Section

Please enter in a numeric value in {{ params.vars.volume_units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)