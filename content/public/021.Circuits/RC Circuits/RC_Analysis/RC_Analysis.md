---
title: RC Circuit Analysis
topic: Circuits
author: John Hopkinson
source: Physics 122 2019 GPSXI
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 21.7.3.0
- 21.7.4.0
- 21.7.5.1
- 21.7.1.1
difficulty:
- undefined
randomization:
- 2
taxonomy:
- undefined
span:
- undefined
length:
- undefined
tags:
- L.K
assets:
- RC.png
part1:
  type: file-upload
  pl-customizations:
    file-names: circuit1.png
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $τ= $
    suffix: µs
part3:
  type: file-upload
  pl-customizations:
    file-names: circuit2.png
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $E= $
    suffix: J
myst:
  substitutions:
    params:
      vars:
        title: RC Circuit Analysis
      capacitor: '4'
---
# {{ params.vars.title }}
<img src="RC.png" width="400">

## Part 1

Identify any capacitors in the circuit shown in figure that are in series or in parallel by circling them with a dashed line and labelling them.

Show a calculation of the effective capacitance of this part of the circuit, and replace the series or parallel capacitors with a single effective capacitor, redrawing the resulting circuit.  On the redrawn circuit repeat this process unit the circuit is fully simplified to a single capacitor, a single resistor and a battery.

Finally, upload your work as a png file named "circuit1"

### Answer Section

File upload box will be shown here.

## Part 2

Find the time constant for this circuit.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 3

Now step by step rebuild your circuit to find the charge on each capacitor when the capacitors are fully charged (i.e. for $t >> \tau$ after closing the circuit).

Upload your work as a png file named "circuit2"

### Answer Section

File upload box will be shown here.

## Part 4

Find the energy stored on the {{ params.capacitor}} $\mu$F capacitor when it is fully charged.

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)