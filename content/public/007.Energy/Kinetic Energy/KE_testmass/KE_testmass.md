---
title: Kinetic Energy of Test Mass
topic: Energy
author: Jake Bobowski
source: 2012 Final Q5
template_version: 0.5
attribution: standard
outcomes:
- 7.2.1.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- unknown
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Kinetic Energy of Test Mass
      units: J
    m: 170
    v: 1.88
    d_m: 2
    d_v: 0.04
    part1:
      ke: 0.302
      ans1:
        value: 0.01
      ans2:
        value: 0.016
      ans3:
        value: 0.004
      ans4:
        value: 0.012
      ans5:
        value: 0.053
      ans6:
        value: 0.004
---
# {{ params.vars.title }}
## Part 1

In a lab, a test mass with $m = $ {{ params.m}} $\\pm$ {{ params.d_m}} g is measured to have a speed of {{ params.v}} $\\pm$ {{ params.d_v}} $m/s$. What is the kinetic energy of the mass?

### Answer Section

- {{ params.part1.ke }} $\\pm$ {{ params.part1.ans1.value }} {{ params.vars.units}}
- {{ params.part1.ke }} $\\pm$ {{ params.part1.ans2.value }} {{ params.vars.units}}
- {{ params.part1.ke }} $\\pm$ {{ params.part1.ans3.value }} {{ params.vars.units}}
- {{ params.part1.ke }} $\\pm$ {{ params.part1.ans4.value }} {{ params.vars.units}}
- {{ params.part1.ke }} $\\pm$ {{ params.part1.ans5.value }} {{ params.vars.units}}
- {{ params.part1.ke }} $\\pm$ {{ params.part1.ans6.value }} {{ params.vars.units}}

## Attribution

![Image representing the Creative Commons 4.0 BY-NC-SA license.](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png) Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).