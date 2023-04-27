---
title: Figure Skater Moment of Inertia
topic: Rotational Motion
author: John Hopkinson
source: Phys 112 2018W1 Practice Final Q3
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 7.5.3.1
- 7.5.3.2
- 8.2.1.3
- 10.5.2.1
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
- JR
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
part2:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Figure Skater Moment of Inertia
      part1:
        ans1:
          value: It decreases by a factor of 2.
          feedback: Careful, moment of inertia decreases.
        ans2:
          value: It decreases by a factor of 4.
          feedback: Angular momentum $L$ is given by $L = I \omega$, where $I$ is
            the moment of inertia and $\omega$ is angular speed.
        ans3:
          value: It increases by a factor of 2.
          feedback: Great, you got it!
        ans4:
          value: It increases by a factor of 4.
          feedback: Angular momentum $L$ is given by $L = I \omega$, where $I$ is
            the moment of inertia and $\omega$ is angular speed.
        ans5:
          value: It does not change.
          feedback: Angular momentum $L$ must be conserved and is given by $L = I
            \omega$, where $I$ is moment of inertia and $\omega$ is angular speed.
      part2:
        ans1:
          value: It decreases by a factor of 2.
          feedback: Careful, moment of inertia decreases.
        ans2:
          value: It decreases by a factor of 4.
          feedback: Rotational kinetic energy $K_{rot}$ is given by $K_{rot} = 1/2
            I \omega ^2$, where $I$ is moment of inertia and $\omega$ is angular speed.
            Don't forget that both $I$ and $\omega$ change.
        ans3:
          value: It increases by a factor of 2.
          feedback: Great, you got it!
        ans4:
          value: It increases by a factor of 4.
          feedback: Rotational kinetic energy $K_{rot}$ is given by $K_{rot} = 1/2
            I \omega ^2$, where $I$ is moment of inertia and $\omega$ is angular speed.
            Don't forget that both $I$ and $\omega$ change.
        ans5:
          value: It does not change.
          feedback: Rotational kinetic energy $K_{rot}$ is given by $K_{rot} = 1/2
            I \omega ^2$, where $I$ is moment of inertia and $\omega$ is angular speed.
      arms1: out
      arms2: in
      I1: 0.8
      I2: 0.4
---
# {{ params.vars.title }}
A figure skater begins a spin with their arms {{ params.arms1 }} and during the spin, they move their arms {{ params.arms2 }}. This changes their moment of inertia from $I\_{\text{arms {{ params.arms1 }}}} = {{ params.I1 }}$ $\rm{kgm^2}$ to $I\_{\text{arms {{ params.arms2 }}}} = {{ params.I2 }}$ $\rm{kgm^2}$ during their spin.

## Part 1

What happens to their angular speed during their spin?

### Answer Section

- {{ params.part1.ans1.value}}
- {{ params.part1.ans2.value}}
- {{ params.part1.ans3.value}}
- {{ params.part1.ans4.value}}
- {{ params.part1.ans5.value}}

## Part 2

What happens to their rotational kinetic energy during their spin?

### Answer Section

- {{ params.part2.ans1.value}}
- {{ params.part2.ans2.value}}
- {{ params.part2.ans3.value}}
- {{ params.part2.ans4.value}}
- {{ params.part2.ans5.value}}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)