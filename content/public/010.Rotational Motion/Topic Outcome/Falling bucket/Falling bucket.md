---
title: Falling Bucket
topic: Rotational Motion
author: Jake Bobowski
source: 2015 Final Q17
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 8.5.1.1
- 8.5.1.2
- 10.5.2.2
- 10.5.2.3
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
- q17_2015Final.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v = $
    suffix: m/s
substitutions:
  params:
    vars:
      title: Falling Bucket
      units: m/s
    m_b: 13.8
    m_c: 4.65
    h: 36.3
    r: 58.6
---
# {{ params.vars.title }}
A bucket of mass $m_b$ = {{ params.m_b }} $kg$ is knocked off the side of a well.  The bucket falls {{ params.h }} $m$ to the bottom of the well.  Attached to the bucket is a light rope that wraps around a cylinder of radius $r = $ {{ params.r}} $cm$ and mass $m_c$ = {{ params.m_c }} $kg$.

![](q17_2015Final.png)

## Question Text

How fast is the bucket falling just before it hits the ground?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)