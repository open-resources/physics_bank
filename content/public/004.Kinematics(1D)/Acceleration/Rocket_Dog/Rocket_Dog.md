---
title: Rocket Dog
topic: Kinematics(1D)
author: Jake Bobowski
source: 2015 Midterm 1 001 Q4
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
outcomes:
- 1.7.2.0
- 1.7.2.2
- 1.7.2.4
- 4.4.1.0
- 4.6.3.0
- 4.7.2.0
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
- EW
- PW
assets:
- sample.html
part1:
  type: symbolic-input
  pl-customizations:
    label: $\rm{v (t)} = $
    variables: t
    weight: 1
    allow-blank: false
part2:
  type: symbolic-input
  pl-customizations:
    label: $\rm{a (t)} = $
    variables: t
    weight: 1
    allow-blank: false
part3:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $\rm{v_{avg}} = $
    suffix: $\rm{m/s}$
    comparison: sigfig
    digits: 3
part4:
  type: multiple-choice
  pl-customizations:
    weight: 1
part5:
  type: longtext
  gradingMethod: Manual
  pl-customizations:
    placeholder: Type your answer here...
    file-name: answer.html
    quill-theme: snow
    directory: clientFilesQuestion
    source-file-name: sample.html
substitutions:
  params:
    vars:
      title: Rocket Dog
      units: $\rm{m/s}$
    x: $-2t^2 + 2t$
    time: 3
    part4:
      ans1:
        value: The rocket dog is moving towards the origin.
        feedback: 'Hint: Consider the signs of the dog''s position and velocity at
          the given time.'
      ans2:
        value: The rocket dog is moving away from the origin.
        feedback: Great! You got it.
---
# {{ params.vars.title }}
A rocket dog has a position along a straight track given by:

$x(t)$ = {{ params.x }}

where $x$ is in metres and $t$ is in seconds.

## Part 1

What is the velocity of the rocket dog as a function of time?

Use the following table as a reference:
| $Variable$ | Use   |
|----------|-------|
| $t$  | t  |

### Answer Section

Please enter the equation for velocity.

## Part 2

What is the acceleration of the rocket dog as a function of time?

Use the following table as a reference:
| $Variable$ | Use   |
|----------|-------|
| $t$  | t  |

### Answer Section

Please enter the equation for acceleration.

## Part 3

Calculate the average velocity of the rocket dog between $t = 0$ $\rm{s}$ and $t$ = {{params.time}} $\rm{s}$.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 4

At time $t = $ {{params.time}} $\rm{s}$, is the rocket dog moving towards the origin or away from the origin?

### Answer Section

- {{ params.part4.ans1.value }}
- {{ params.part4.ans2.value }}

## Part 5

Justify your answer to Part 4.

### Answer Section

Answer in 1-2 sentences, and try to use full sentences.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)