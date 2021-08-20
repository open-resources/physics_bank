---
title: Acceleration Based On Graph
topic: Math
author: Jake Bobowski
source: 2014 Final Q1
template_version: 1.1
attribution: standard
outcomes:
- 1.7.2.3
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- EW
assets:
- Q1&Q2image.png
server: 
    imports: |
        import problem_bank_helpers as pbh
    generate: |
        data2 = pbh.create_data2()

        # store phrases etc
        data2["params"]["vars"]["title"] = 'Acceleration Based On Graph'
        data2["params"]["vars"]["units"] = "$m/s^2$"

        # define possible answers
        data2["params"]["part1"]["ans1"]["value"] = "-4.0"
        data2["params"]["part1"]["ans1"]["correct"] = False

        data2["params"]["part1"]["ans2"]["value"] = "-3.0"
        data2["params"]["part1"]["ans2"]["correct"] = True

        data2["params"]["part1"]["ans3"]["value"] = "0"
        data2["params"]["part1"]["ans3"]["correct"] = False

        data2["params"]["part1"]["ans4"]["value"] = "1.8"
        data2["params"]["part1"]["ans4"]["correct"] = False

        data2["params"]["part1"]["ans5"]["value"] = "3.0"
        data2["params"]["part1"]["ans5"]["correct"] = False

        # Update the data object with a new dict
        data.update(data2)
    prepare: |
        pass
    parse: |
        pass
    grade: |
        pass
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
---
# {{ params.vars.title }}

<img src="Q1&Q2image.png" alt = "A graph of velocity versus time. At 0 seconds, the velocity is 4 meters per second. At 1 second, the veleocity decreases to 1 meter per second. The velocity increases and at 3 seconds the velocity is 3 meters per second. From 3 to 5 seconds, the velocity is 3 meters per second. The graph has a point labelled A and C. A is labelled at 1 second, with a velocity of 1 meters per second. C is labelled at 4 seconds with a velocity of 3 meters per second." width = 300>

## Part 1

What is the acceleration of the object at point A? 

### Answer Section

- {{ params.part1.ans1.value }} {{ params.vars.units}} 
- {{ params.part1.ans2.value }} {{ params.vars.units}} 
- {{ params.part1.ans3.value }} {{ params.vars.units}} 
- {{ params.part1.ans4.value }} {{ params.vars.units}} 
- {{ params.part1.ans5.value }} {{ params.vars.units}} 

## pl-submission-panel

## pl-answer-panel

## Rubric

This should be hidden from students until after the deadline.

## Solution

This should never be revealed to students.

## Comments

These are random comments associated with this question.
