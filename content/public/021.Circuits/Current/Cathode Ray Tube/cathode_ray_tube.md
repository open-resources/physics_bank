---
title: Cathode Ray Tube
topic: Circuits
author: Vanshika Sharma
source: 2.9.22
template_version: 1.1
attribution: standard
outcomes:
- 21.2.1.0
- 21.2.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- OSUP
- VS
assets: null
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: false
    label: Number of electrons =
    comparison: relabs
    rtol: 0.03
    atol: 0
substitutions:
  params:
    vars:
      title: Cathode Ray Tube
    I: 4
    t: 2
---
# {{ params.vars.title }}
A cathode ray tube (CRT) is a device that produces a focused beam of electrons in a vacuum.
The electrons strike a phosphor-coated glass screen at the end of the tube, which produces a bright spot of light.
The position of the bright spot on the screen can be adjusted by deflecting the electrons with electrical fields, magnetic fields, or both.
## Question Text

Consider a CRT with an electron beam average current of ${{params.I}}\rm\ \mu A$.
How many electrons strike the screen every {{params.t}} minutes?

### Answer Section

Please enter in a numeric value.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)