---
title: Rolling Disk of Spruce and Steel
topic: Rotational Motion
author: Jake Bobowski
source: 2013 Practice Final Q10
template_version: 1.2
attribution: standard
showCorrectAnswer: false
outcomes:
- 10.4.1.1
difficulty:
- medium
randomization:
- 2
taxonomy:
- undefined
span:
- section
length:
- average
tags:
- PW
assets:
- q10_2013practiceFinal.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $m= $
    suffix: $kg$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $m= $
    suffix: $kg$
part3:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params_vars_title: Rolling Disk of Spruce and Steel
    params_vars_units: $kg$
    params_rho_spruce: 416.0
    params_rho_steel: 7860.0
    params_w_disk: 21.6
    params_part3_ans1_value: $x$ = 1 $cm$, $y$ = 0 $cm$
    params_part3_ans2_value: $x$ = 0 $cm$, $y$ = 1.0 $cm$
    params_part3_ans3_value: $x$ = 0 $cm$, $y$ = 2.0 $cm$
    params_part3_ans4_value: $x$ = 0 $cm$, $y$ = 3.0 $cm$
    params_part3_ans5_value: $x$ = 0 $cm$, $y$ = 4.0 $cm$
    params_part3_ans6_value: $x$ = 0 $cm$, $y$ = 0.0 $cm$
---
# {{ params_vars_title }}
A disk that will appear to roll uphill is made from spruce ($\rho\_{\text{spruce}} = $ {{ params.rho_spruce }} $kg/m^3$) and steel ($\rho\_{\text{steel}} = $ {{ params.rho_steel }} $kg/m^3$) by drilling a 3 $cm$ diameter hole, centred 8 $cm$ above the centre of a 30 $cm$ diameter spruce cylinder, as shown in the figure.  Into this hole is inserted a piece of steel of identical dimensions.  The disk has a thickness of {{ params.w_disk }} $cm$.

<img alt="The figure shows a disk centred at the origin of a cartesian plane with diameter 30 cm. There is a hole of diameter 3cm centred 8 cm above the centre of the disk." src="q10_2013practiceFinal.png">

## Part 1

Calculate the mass of the spruce removed from this disk.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 2

Calculate the mass of the steel that replaces the spruce.

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Part 3

The location of the centre of mass of the weighted disk is closest to:

### Answer Section

- {{ params_part3_ans1_value}}
- {{ params_part3_ans2_value}}
- {{ params_part3_ans3_value}}
- {{ params_part3_ans4_value}}
- {{ params_part3_ans5_value}}
- {{ params_part3_ans6_value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)