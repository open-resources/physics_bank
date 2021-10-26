---
title: Rolling Disk of Spruce and Steel
topic: Rotational Motion
author: Jake Bobowski
source: 2013 Practice Final Q10
template_version: 1.2
attribution: standard
outcomes:
- 10.4.1.1
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
substitutions:
  params:
    vars:
      title: Rolling Disk of Spruce and Steel
      units: $kg$
    rho_spruce: 433.0
    rho_steel: 7880.0
    w_disk: 10.2
    part3:
      ans1:
        value: $x$ = 1 $cm$, $y$ = 0 $cm$
      ans2:
        value: $x$ = 0 $cm$, $y$ = 1.0 $cm$
      ans3:
        value: $x$ = 0 $cm$, $y$ = 2.0 $cm$
      ans4:
        value: $x$ = 0 $cm$, $y$ = 3.0 $cm$
      ans5:
        value: $x$ = 0 $cm$, $y$ = 4.0 $cm$
      ans6:
        value: $x$ = 0 $cm$, $y$ = 0.0 $cm$
---
# {{ params.vars.title }}
A disk that will appear to roll uphill is made from spruce ($\rho\_{\text{spruce}} = $ {{ params.rho_spruce }} $kg/m^3$) and steel ($\rho\_{\text{steel}} = $ {{ params.rho_steel }} $kg/m^3$) by drilling a 3 $cm$ diameter hole, centred 8 $cm$ above the centre of a 30 $cm$ diameter spruce cylinder, as shown in the figure.  Into this hole is inserted a piece of steel of identical dimensions.  The disk has a {{ params.w_disk }} $cm$ width.

<img longdesc="Spruce and Steel Disk.md#desc" alt="Disk of spruce and steel." src="q10_2013practiceFinal.png">

<div id="desc">
<h5>Long Description of image: Disk of spruce and steel.</h5>
The figure shows a disk centred at the origin of a cartesian plane with diameter 30 cm.
There is a hole of diameter 3cm centred 8 cm above the centre of the disk.
<p>Long description ends.</p>
<div>

## Part 1

Calculate the mass of the spruce removed from this disk.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

Calculate the mass of the steel that replaces the spruce.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 3

The location of the centre of mass of the weighted disk is closest to:

### Answer Section

- {{ params.part3.ans1.value}}
- {{ params.part3.ans2.value}}
- {{ params.part3.ans3.value}}
- {{ params.part3.ans4.value}}
- {{ params.part3.ans5.value}}
- {{ params.part3.ans6.value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)