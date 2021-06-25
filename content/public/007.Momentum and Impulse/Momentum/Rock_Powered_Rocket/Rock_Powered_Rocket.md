---
title: Rock Powered Rocket
topic: Momentum and Impulse
author: Jake Bobowski
source: 2015 Practice Midterm 1 Q7
template_version: 1.0
attribution: standard
outcomes:
- 6.2.1.1
- 7.2.2.0
- 7.2.2.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- EW
assets: null
part1:
  type: number-input
  label: $P_{total}=$
  pl-customizations:
    allow-blank: true
    weight: 1
part2:
  type: number-input
  label: $v_{f}=$
  pl-customizations:
    allow-blank: true
    weight: 1
part3:
  type: number-input
  label: $v_{rock f}=$
  pl-customizations:
    allow-blank: true
    weight: 1
substitutions:
  params:
    vars:
      title: Rock Powered Rocket
      units1: m/s
      units2: kg
    i: 322
    m: 38
    v_1: 16
    v_2: 16
---
# {{ params.vars.title }}
I am an astronaut caveman, floating in space.
My rocket is powered by throwing rocks out of a hole in the back of the spaceship.
The total inertia of me and my rocket is {{ params.i }} kg.
I also have two {{ params.m }} kg rocks on board.
We are initially at rest.
I throw the first rock, and then we are moving with velocity {{ params.v_1 }} {{ params.vars.units1 }}.
Then I throw the second rock out of the back and we are moving with velocity {{ params.v_2 }} {{ params.vars.units1 }} .
## Part 1

(a) What is the total momentum of the system?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1 }}{{ params.vars.units2 }}.
## Part 2

(b) With what velocity is the first rock I threw moving through space?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1 }}.
## Part 3

(c) With what velocity is the second rock I threw moving through space?

### Answer Section

Please enter in a numeric value in {{ params.vars.units1 }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)