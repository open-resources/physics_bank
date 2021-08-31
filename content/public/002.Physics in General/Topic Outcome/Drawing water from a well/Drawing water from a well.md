---
title: Drawing Water from a Well
topic: Physics in General
author: Jake Bobowski
source: 2013 Practice Final Q11
template_version: 1.1
attribution: standard
outcomes:
- 6.2.1.2
- 6.1.1.4
- 10.3.2.2
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- PW
assets:
- q11_2013practiceFinal.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $T= $
    suffix: $N$
    comparison: sigfig
    digits: 3
part2:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\Delta y= $
    suffix: $m$
    comparison: sigfig
    digits: 3
substitutions:
  params:
    vars:
      title: Drawing Water from a Well
      unit1: $N$
      unit2: $m$
    M: 3.05
    m: 2.6
    R: 0.262
    t: 7.13
---
# {{ params.vars.title }}
As  shown  in  the figure,  a  solid,  uniform,  frictionless  cylindrical  reel  of  mass $M = $ {{ params.M }} $kg$ and radius $R = $ {{ params.R }} $m$ is used to draw water from a well.  A bucket of  mass $m = $ {{ params.m }} $kg$ is  attached  to  a  massless  cord  that  is  wrapped  around  the cylinder.

![Figure of a bucket attached to a cylindrical reel and a well.](q11_2013practiceFinal.png)

## Part 1

If  the  bucket  is  released  from  rest  at  the  top  of  the  well,  find  the tension $T$ in the cord and the acceleration $a$ of the bucket (the cord does not slip on the reel).

### Answer Section

Please enter in a numeric value in {{ params.vars.unit1 }}.

## Part 2

If the bucket falls for {{ params.t }} $s$ before hitting the water, how far does it fall?

### Answer Section

Please enter in a numeric value in {{ params.vars.unit2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)