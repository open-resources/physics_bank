---
title: Magnetic Force on Airplane
topic: Magnetism
author: Vanshika Sharma
source: 2.11.21
template_version: 1.1
attribution: standard
outcomes:
- 19.3.2.0
- 19.3.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- OSUP
- chapter 11
- problem 21
- VS
- magnetic force
assets: null
part1:
  type: number-input
  pl-customizations:
    label: $F=$
    allow-blank: false
    show-correct-answer: false
    comparison: relabs
    rtol: 0.03
    atol: 0
    show-help-text: true
    suffix: $\rm\ N$
    weight: 1
part2:
  type: dropdown
  pl-customizations:
    blank: true
    weight: 1
substitutions:
  params:
    vars:
      title: Magnetic Force on Airplane
    q: 0.789
    v: 531
    part2:
      ans1:
        value: North
      ans2:
        value: South
      ans3:
        value: East
      ans4:
        value: West
---
# {{ params.vars.title }}
Aircrafts sometimes acquire small static charges. Suppose a supersonic jet has a ${{params.q}} \rm\ {\mu C}$ charge and flies due west at a speed of ${{params.v}} \textrm{ m/s}$ over Earths south magnetic pole, where the $\mathrm{8 \times 10^{-5}} \textrm{ T}$ magnetic field points straight down into the ground.

## Part 1

What is the magnitude of the electric force on the plane?

### Answer Section

Please enter a numeric value.

## Part 2

What is the direction of the magnetic force on the plane?

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)