---
title: Transverse String Wave
topic: Waves
author: John Hopkinson
source: Phys122 2019W2 GPS 3
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 16.1.1.1
- 16.1.1.3
difficulty:
- medium
randomization:
- 2
- 4
taxonomy:
- undefined
span:
- chapter
length:
- long
tags:
- L.K
assets: null
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $A= $
    suffix: $\rm\ cm$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $λ= $
    suffix: $\rm\ cm$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: '{{params.vars.labels}}'
    suffix: '{{params.vars.units}}'
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $v= $
    suffix: $\rm\ m/s$
part5:
  type: file-upload
  pl-customizations:
    file-names: wave.png
myst:
  substitutions:
    params:
      vars:
        title: Transverse String Wave
        units: "$\r{Hz}$"
        labels: $ f $
      amplitude: 10
      wavelength: 5
      period: 7
      wave_equation: cos
      wave: frequency
---
# {{ params.vars.title }}
The transverse displacement of a traveling wave on a string is described by the formula $D(x,t) = {{ params.amplitude}} cm \, {{  params.wave_equation }}(\frac{2\pi}{({{ params.wavelength}}) \text{cm}} x - \frac{2\pi}{({{ params.period}})  \text{s}} t + \frac{\pi}{2})$

## Part 1

What is the amplitude of this wave?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 2

What is the wavelength of this wave?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 3

What is this wave's {{ params.wave}}?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 4

What is the speed at which energy travels down this wave?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 5

A. Draw a snapshot graph for this wave taken at $t = 0$ s, from $x = 0$ cm to $x = 2$ cm.
Indicate and label the wavelength on your graph.

B. Draw a history graph of the motion of the string at $x = 0.5$ cm from $t = 0$ s to $t = 4$ s.
Indicate and label the period on your graph.

C. Draw a graph of the velocity of the piece of string at $x = 0.5$ cm as a function of time.

Finally, upload your graphs as a png file named '$\textbf{wave}$'.

### Answer Section

A file upload box will appear here.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)