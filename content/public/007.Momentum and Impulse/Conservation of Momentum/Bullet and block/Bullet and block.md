---
title: Bullet and Block
topic: Template
author: Firas Moosvi
source: original
template_version: 1.3
attribution: standard
partialCredit: true
singleVariant: false
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
    label: $v= $
    suffix: m/s
part2:
  type: number-input
  pl-customizations:
    rtol: 0.03
    weight: 1
    allow-blank: true
    label: $m= $
    suffix: kg
substitutions:
  params:
    vars:
      title: Bullet and Block
      name: Ximena
      units1: m/s
      units2: kg
    m_bullet: 30
    m_block: 28
    bullet_v: 706
    slide_d: 2
    slide_dnew: 2.8
    coeff_k: 0.2
---
# {{ params.vars.title }}
{{ params.vars.name }} fires a bullet of mass {{ params.m_bullet }}g into a block of mass {{ params.m_block }}kg that is initially at rest on a table.

The block, with the bullet embedded in it, slides across the table horizontally a distance of {{ params.slide_d }} cm.
The coefficient of kinetic friction between the table and the block is {{ params.coeff_k }}.

## Part 1

What is the bullet's initial speed before it hits the block?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1 }}.

## Part 2

{{ params.vars.name }} decides to repeat the experiment with a new block of wood.
Unfortunately, {{ params.vars.name }} does not have a weighing scale and does not know the mass of the new block.
But because they took an undergraduate physics course, they know they can figure it out if they have the initial velocity of the bullet.
They happen to have a ballistic chronograph that can capture the velocity of fast moving bullet.
Just before it collides with the block, the bullet's velocity is {{ params.bullet_v }} {{ params.vars.units1 }}.

What is the mass of the new block (in kg) if it moves {{ params.slide_dnew }}cm ?

### Answer Section

Please enter in a numeric value in {{ params.vars.units2 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)