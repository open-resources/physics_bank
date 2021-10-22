---
title: Cyclist with a Deathwish
topic: Force
author: John Hopkinson
source: PHYS 111 2013W1 MT2 Q2
template_version: 1.2
attribution: standard
outcomes:
- 6.10.1.1
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
- MP
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
substitutions:
  params:
    vars:
      title: Cyclist with a Deathwish
    v1: 156
    v2: 37
    age: 30
    part1:
      ans1:
        value: 17.8 times.
      ans2:
        value: 4.22 times.
      ans3:
        value: 0.237 times.
      ans4:
        value: 0.0563 times.
      ans5:
        value: It would be equal to their maximum thrust.
---
# {{ params.vars.title }}
A {{params.age}} year old cyclist is obsessed with trying to go as fast as humanly possible on a bicycle using their knowledge of physics.

Without any fancy tricks or techniques, a "regular" cyclist reaches a top speed of only about {{params.v2}} miles per hour due to the drag force.
You may assume this velocity is constant over time.

Our cyclist (with a deathwish) knows that the drag force is $\frac{1}{4} Av^2$, where $A$ is the cross-sectional area.
They decide to protect themselves from drag forces, they're going to "draft" behind a large rectangular truck going down the highway.
By "drafting", they are somewhat protected from drag and they can now reach speeds of {{params.v1}} miles per hour.
Unfortunately, there's just the problem of how to safely slow down if they ever exit the draft (or, if the truck slows down).

## Part 1

At this speed ({{params.v1}} miles per hour), if the cyclist suddenly has to exit the truck's draft and consequently, experiences full air resistance, how many times larger than their maximum thrust would the drag force be?

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}
- {{ params.part1.ans4.value }}
- {{ params.part1.ans5.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)