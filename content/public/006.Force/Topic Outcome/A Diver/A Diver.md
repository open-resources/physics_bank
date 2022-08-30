---
title: A Diver
topic: Force
author: Reza Khanbabaie
source: PHYS 112 Torque Q3
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 6.4.1.4
- 6.7.1.0
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
- diver.png
part1:
  type: file-upload
  pl-customizations:
    file-names: diver.pdf
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $F_B = $
    suffix: $N$
part3:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\theta = $
    suffix: $^\circ$
substitutions:
  params:
    vars:
      title: A Diver
      unit1: $N$
      unit2: degrees
    m: 84.8
    L: 3.47
    d: 1.64
---
# {{ params.vars.title }}
A $M = $ {{ params.m }} $kg$ diver stands at the edge of a diving board with length $L = $ {{ params.L }} $m$ and negligible mass. The diving board is supported by two narrow pillars. One pillar is located at the end of the diving board furthest from the water and the other is $d = $ {{ params.d }} $m$ towards the water, as shown in the figure.

<img src="diver.png" width=400 alt="A diver stands at the right edge of a diving board of length L metres supported by two pillars A and B which are d metres apart. Pillar A touches the left end of the board.">

## Part 1

Show all forces acting on the board. In addition, indicate the pivot point you will be using in the next parts.

Your file must be a pdf.

### Answer Section

File upload box will be shown here.

## Part 2

Find the magnitude of the force exerted on the diving board by pillar $B$ ($F_B$).

### Answer Section

Please enter in a numeric value in {{ params.vars.unit1 }}.

## Part 3

Find the direction, $\theta$, of the force exerted on the diving board by pillar $B$ ($F_B$). Assume that the point where Pillar $B$ touches the board is at the origin of a Cartesian plane ($\theta > 0$ with zero being to the right).

### Answer Section

Please enter in a numeric value in {{ params.vars.unit2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)