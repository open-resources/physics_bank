---
title: Rock Powered Rocket
topic: Momentum and Impulse
author: Jake Bobowski
source: 2015 Practice Midterm 1 Q7
template_version: 0.4
outcomes:
- 6.2.1.1
- 7.2.2.0
- 7.2.2.1
tags:
- super-randomizer
- quiz
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
    i: 396
    m: 26
    v_1: 23
    v_2: 18
---
# {{ params.vars.title }}
## Part 1

I am an astronaut caveman, floating in space.
My rocket is powered by throwing rocks out of a hole in the back of the spaceship.
The total inertia of me and my rocket is {{ params.i }} kg.
I also have two {{ params.m }} kg rocks on board.
We are initially at rest.
I throw the first rock, and then we are moving with velocity {{ params.v_1 }}$\\frac{m}{s}$ .
Then I throw the second rock out of the back and we are moving with velocity {{ params.v_2 }} $\\frac{m}{s}$ .

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

![Image representing the Creative Commons 4.0 BY-NC-SA license.](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png) Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).