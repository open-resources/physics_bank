---
title: Centre of Mass of a Baton
topic: Rotational Motion
author: Jake Bobowski
source: 2015 Practice Midterm 2 Q5
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
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
- q5_2015practiceMid2.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $x= $
    suffix: $m$
myst:
  substitutions:
    params_vars_title: Centre of Mass of a Baton
    params_vars_units: $m$
    params_m1: 0.19
    params_m2: 0.05
    params_m3: 0.053
    params_l1: 1.9
    params_l2: 1.1
---
# {{ params_vars_title }}

## Question Text

Determine the position of the centre of mass of the baton shown in the figure below.
The ball at the left end has a mass of $m_1 = $ {{ params_m1 }} $kg$, the ball at the right end has a mass of $m_3 = $ {{ params_m3 }} $kg$, and the bar has a mass of $m_2 = $ {{ params_m2 }} $kg$.
Take the point $l_1 = $ {{ params_l1 }} $m$ to the left of the {{ params_m1 }} $kg$ mass as your origin.
The length from the center of the left ball to the center of the right ball is $l_2 = $ {{ params_l2 }} $m$.

<img alt="The figure shows the origin on the left side and the baton to the right of the origin. The left ball of the baton has mass m one and is bigger than the right ball of mass m three. The bar has mass m two. The length from the origin to the center of the left ball is l one. The length from the center of the left ball to the center of the right ball is l two." src="q5_2015practiceMid2.png">

### Answer Section

Please enter in a numeric value in {{ params_vars_units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)