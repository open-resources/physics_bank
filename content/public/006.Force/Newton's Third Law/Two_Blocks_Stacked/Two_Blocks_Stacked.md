---
title: Two Blocks Stacked
topic: Force
author: Jake Bobowski
source: 2012 Practice Final Q14
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 6.6.1.1
- 6.1.1.4
- 6.3.1.2
- 6.4.1.4
- 6.6.1.2
- 6.7.1.0
- 6.9.1.3
difficulty:
- hard
randomization:
- 2
taxonomy:
- undefined
span:
- chapter
length:
- average
tags:
- EW
assets:
- Q14.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $\vec{P} = $
    suffix: $N$
substitutions:
  params:
    vars:
      title: Two Blocks Stacked
      units: N
    m: 11
    f: 0.31
    t: 32
---
# {{ params.vars.title }}
Blocks A and B each have a mass $m$ = {{params.m}} $kg$.
The coefficient of static friction between $A$ and $B$ is $\mu_s$ = {{params.f}}.
The angle shown is $\theta$ = {{params.t}}$^{\circ}$.
Neglect any friction between $B$ and $C$.

<img src="Q14.png" alt="Right triangle A is stacked on top of right triangle B to create a rectangular block sitting on top of surface C. The angle between the hypotenuse and adjacent in triangle B is theta. A ninety-degree force P, acting to the left, is applied to the opposite side of triangle B." width=500>

## Question Text

Determine the largest horizontal force $\vec{P}$ that can be applied so that $A$ will not slip on $B$.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)