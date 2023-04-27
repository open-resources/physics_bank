---
title: Magnetic field of a coaxial cable
topic: Magnetism
author: Jake Bobowksi
source: 2.12.48
template_version: 1.3
attribution: openstax-physics-vol2
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 19.2.4.1
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
- OSUP
- volume 2
- chapter 12
- problem 48
- magnetic field
- current source
- Ampere law
- coaxial cable
- symbolic
- JB
assets:
- OSUPv2p12_48.png
part1:
  type: symbolic-input
  pl-customizations:
    label: $B_1 = $
    variables: r, r1, r2, r3, I, μ0
    weight: 1
    allow-blank: false
part2:
  type: dropdown
  pl-customizations:
    sort: fixed
    weight: 1
    blank: true
part3:
  type: symbolic-input
  pl-customizations:
    label: $B_2 = $
    variables: r, r1, r2, r3, I, μ0
    weight: 1
    allow-blank: false
part4:
  type: dropdown
  pl-customizations:
    sort: fixed
    weight: 1
    blank: true
part5:
  type: symbolic-input
  pl-customizations:
    label: $B_3 = $
    variables: r, r1, r2, r3, I, μ0
    weight: 1
    allow-blank: false
part6:
  type: dropdown
  pl-customizations:
    sort: fixed
    weight: 1
    blank: true
part7:
  type: symbolic-input
  pl-customizations:
    label: $B_4 = $
    variables: r, r1, r2, r3, I, μ0
    weight: 1
    allow-blank: true
part8:
  type: dropdown
  pl-customizations:
    sort: fixed
    weight: 1
    blank: true
myst:
  substitutions:
    params:
      vars:
        title: Magnetic field of a coaxial cable
      part2:
        ans1:
          value: clockwise
        ans2:
          value: counterclockwise
        ans3:
          value: the magnetic field is zero
      part4:
        ans1:
          value: clockwise
        ans2:
          value: counterclockwise
        ans3:
          value: the magnetic field is zero
      part6:
        ans1:
          value: clockwise
        ans2:
          value: counterclockwise
        ans3:
          value: the magnetic field is zero
      part8:
        ans1:
          value: clockwise
        ans2:
          value: counterclockwise
        ans3:
          value: the magnetic field is zero
---
# {{ params.vars.title }}
A portion of a long, cylindrical coaxial cable is shown in the figure.
A current $I$ flows down the centre conductor, and this current is returned in the outer conductor.

<img src="OSUPv2p12_48.png" width=400 alt="Section of a cylindrical coaxial cable">

## Part 1

Determine the magnitude of the magnetic field in the region $r\\< r_1$.

In your symbolic expression, you may copy and paste the Greek symbol `Î¼0`. Use `pi` to represent Ï.

### Answer Section

## Part 2

What is the direction of the magnetic field calculated in Part 1?

### Answer Section

- {{ params.part2.ans1.value }}
- {{ params.part2.ans2.value }}
- {{ params.part2.ans3.value }}

## Part 3

Determine the magnitude of the magnetic field in the region $r_1\\< r\\< r_2$.

In your symbolic expression, you may copy and paste the Greek symbol `Î¼0`. Use pi to represent `Ï`.

### Answer Section

## Part 4

What is the direction of the magnetic field calculated in Part 3?

### Answer Section

- {{ params.part4.ans1.value }}
- {{ params.part4.ans2.value }}
- {{ params.part4.ans3.value }}

## Part 5

Determine the magnitude of the magnetic field in the region $r_2\\< r\\< r_3$.

In your symbolic expression, you may copy and paste the Greek symbol `Î¼0`. Use `pi` to represent `Ï`.

### Answer Section

## Part 6

What is the direction of the magnetic field calculated in Part 5?

### Answer Section

- {{ params.part6.ans1.value }}
- {{ params.part6.ans2.value }}
- {{ params.part6.ans3.value }}

## Part 7

Determine the magnitude of the magnetic field in the region $r > r_3$.

In your symbolic expression, you may copy and paste the Greek symbol `Î¼0`. Use `pi` to represent Ï.

### Answer Section

## Part 8

What is the direction of the magnetic field calculated in Part 7?

### Answer Section

- {{ params.part8.ans1.value }}
- {{ params.part8.ans2.value }}
- {{ params.part8.ans3.value }}

## Attribution

Problem is from the [OpenStax University Physics Volume 2](https://openstax.org/details/books/university-physics-volume-2) textbook, licensed under the [CC-BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).<br>![Image representing the Creative Commons 4.0 BY license.](https://raw.githubusercontent.com/firasm/bits/master/by.png)