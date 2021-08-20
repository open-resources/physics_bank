---
title: Two Blocks Stacked
topic: Force
author: Jake Bobowski
source: 2012 Practice Final Q14
template_version: 1.1
attribution: standard
outcomes:
- 6.6.1.1
- 6.1.1.4
- 6.3.1.2
- 6.4.1.4
- 6.6.1.2
- 6.7.1.0
- 6.9.1.3
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- EW
assets:
- Q14.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\vec{P} = $
    suffix: $N$
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Two Blocks Stacked
      units: N
    m: 12
    f: 0.3
    t: 46
---
# {{ params.vars.title }}
Blocks A and B each have a mass $m$ = {{params.m}} $kg$.
The coefficient of static friction between $A$ and $B$ is $\mu_s$ = {{params.f}}.
The angle shown is $\theta$ = {{params.t}}$^{\circ}$.
Neglect any friction between $B$ and $C$.

![Right triangle A is stacked on top of right triangle B to create a rectangular block sitting on top of surface C. The angle between the hypotenuse and adjacent in triangle B is theta. A ninety-degree force P, acting to the left, is applied to the opposite side of triangle B.](Q14.png)
## Question Text

Determine the largest horizontal force $\vec{P}$ that can be applied so that $A$ will not slip on $B$.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)