---
title: Centre of Mass of a Baton
topic: Rotational Motion
author: Jake Bobowski
source: 2015 Practice Midterm 2 Q5
template_version: 1.1
attribution: standard
outcomes:
- 10.4.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- PW
assets:
- q5_2015practiceMid2.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: $m$
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Centre of Mass of a Baton
      units: $m$
    m1: 0.2
    m2: 0.13
    m3: 0.072
    l1: 1.3
    l2: 0.86
---
# {{ params.vars.title }}

## Question Text

Determine the position of the centre of mass of the baton shown in the figure below.
The ball at the left end has a mass of $m_1 = $ {{ params.m1 }} $kg$, the ball at the right end has a mass of $m_3 = $ {{ params.m3 }} $kg$, and the bar has a mass of $m_2 = $ {{ params.m2 }} $kg$.
Take the point $l_1 = $ {{ params.l1 }} $m$ to the left of the {{ params.m1 }} $kg$ mass as your origin.
The length from the center of the left ball to the center of the right ball is $l_2 = $ {{ params.l2 }} $m$.

<img longdesc="Centre of Mass of a Baton.md#desc" alt="Figure of the system." src="q5_2015practiceMid2.png">

<div id="desc">
<h5>Long Description of image: Figure of the system.</h5>
The figure shows the origin on the left side and the baton to the right of the origin.<br>
The left ball of the baton has mass m one and is bigger than the right ball of mass m three. The bar has mass m two.<br>
The length from the origin to the center of the left ball is l one.<br>
The length from the center of the left ball to the center of the right ball is l two.
<p>Long description ends.</p>
<div>

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)