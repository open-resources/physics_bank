---
title: Centre of Mass of a Baton
topic: Rotational Motion
author: Jake Bobowski
source: 2015 Practice Midterm 2 Q5
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
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
- q5_2015practiceMid2.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: $m$
substitutions:
  params:
    vars:
      title: Centre of Mass of a Baton
      units: $m$
    m1: 0.22
    m2: 0.11
    m3: 0.11
    l1: 0.63
    l2: 0.9
---
# {{ params.vars.title }}

## Question Text

Determine the position of the centre of mass of the baton shown in the figure below.
The ball at the left end has a mass of $m_1 = $ {{ params.m1 }} $kg$, the ball at the right end has a mass of $m_3 = $ {{ params.m3 }} $kg$, and the bar has a mass of $m_2 = $ {{ params.m2 }} $kg$.
Take the point $l_1 = $ {{ params.l1 }} $m$ to the left of the {{ params.m1 }} $kg$ mass as your origin.
The length from the center of the left ball to the center of the right ball is $l_2 = $ {{ params.l2 }} $m$.

<img alt="The figure shows the origin on the left side and the baton to the right of the origin. The left ball of the baton has mass m one and is bigger than the right ball of mass m three. The bar has mass m two. The length from the origin to the center of the left ball is l one. The length from the center of the left ball to the center of the right ball is l two." src="q5_2015practiceMid2.png">

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)