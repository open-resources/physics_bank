---
title: Bullet and Block
topic: Template
author: Firas Moosvi
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes: null
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
- unknown
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v = $
    suffix: $\rm{m/s}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.03
    weight: 1
    allow-blank: true
    label: $m = $
    suffix: $\rm{kg}$
myst:
  substitutions:
    params:
      vars:
        title: Bullet and Block
        name: Abbas
      m_bullet: 39
      m_block: 10
      bullet_v: 888
      slide_d: 3
      slide_dnew: 3.9
      coeff_k: 0.2
---
# {{ params.vars.title }}
{{ params.vars.name }} fires a ${{ params.m_bullet }} \rm{g}$ bullet into a ${{ params.m_block }} \rm{kg}$ block of wood that is initially at rest on a table.

The block, with the bullet embedded in it, slides across the table horizontally a distance of ${{ params.slide_d }} \rm{cm}$.
The coefficient of kinetic friction between the table and the block is ${{ params.coeff_k }}$.

Hint: Remember to convert things from $\rm{cm}$ to $\rm{m}$.

## Part 1

What is the bullet's initial speed before it hits the block?

### Answer Section

Please enter in a numeric value in $\rm{m/s}$.

## Part 2

{{ params.vars.name }} decides to repeat the experiment with a new block of wood, using the same bullet and table.
Unfortunately, {{ params.vars.name }} does not have a weighing scale and does not know the mass of the new block, but, because they took an undergraduate physics course, they know they can figure it out if they have the initial velocity of the bullet.
They happen to have a ballistic chronograph that can capture the velocity of a fast moving bullet.
Just before it collides with the block, the bullet's velocity is ${{ params.bullet_v }} \rm{m/s}$.

What is the mass of the new block if it slides ${{ params.slide_dnew }} \rm{cm}$?

### Answer Section

Please enter in a numeric value in $\rm{kg}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)