---
title: Thin Film
topic: Waves
author: John Hopkinson
source: Physics 122 2019 GPSVI
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 22.3.4.0
- 22.3.4.1
- 22.3.4.2
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
assets: null
part1:
  type: dropdown
  pl-customizations:
    weight: 1
    blank: 'true'
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    comparison: sigfig
    digits: '4'
    weight: 1
    allow-blank: true
    label: $= $
    suffix: nm
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $lower= $
    suffix: null
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $upper= $
    suffix: null
part5:
  type: number-input
  pl-customizations:
    rtol: 0.05
    comparison: sigfig
    digits: '4'
    weight: 1
    allow-blank: true
    label: $= $
    suffix: nm
part6:
  type: number-input
  pl-customizations:
    rtol: 0.05
    comparison: sigfig
    digits: '4'
    weight: 1
    allow-blank: true
    label: $= $
    suffix: nm
part7:
  type: dropdown
  pl-customizations:
    weight: 1
    blank: 'true'
part8:
  type: number-input
  pl-customizations:
    rtol: 0.05
    comparison: sigfig
    digits: '4'
    weight: 1
    allow-blank: true
    label: $= $
    suffix: nm
myst:
  substitutions:
    params:
      vars:
        title: Thin Film
      v: 611
      t: 148
      part1:
        ans1:
          value: 'in phase causing constructive interference of the reflected light. '
        ans2:
          value: 'out of phase causing destructive interference of the reflected light. '
      part7:
        ans1:
          value: 'in phase causing constructive interference of the reflected light. '
        ans2:
          value: 'out of phase causing destructive interference of the reflected light. '
---
# {{ params.vars.title }}
Light of wavelength $\lambda\_{\text{air}}$ = {{ params.v}} nm is incident (from the air, $n\_{air} = 1.00$) on a thin film of unknown index of refraction and thickness. The film is attached to a glass surface ($n\_{\text{glass}} = 1.5$).  The path length difference traveled by the light reflecting from the front and back surfaces of the film corresponds to $\frac{\lambda\_{\text{film}}}{2}$ (half a wavelength). Light reflecting off both the front and back surfaces of the film experiences a $\pi$ rad (initial) phase shift.

## Part 1

This implies that the reflected light from these two reflections will be;

### Answer Section

- {{ params.part1.ans1}} {{ params.vars.units}}
- {{ params.part1.ans2}} {{ params.vars.units}}

## Part 2

What must the product of the film thickness and the film's index of refraction be?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 3

In order for both reflections to experience $\pi$ rad phase shifts, what range of values can $n\_{\text{film}}$ take?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## 

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 4

What is the lower limit on how thick the film could be, given your answers to on the previous questions?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 5

If the thin film had a thickness of {{ params.t }}nm, what index of refraction would the thin film have to have?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Part 6

If the film thickness was now doubled, the reflected light from the front and back surfaces of the film would be;

### Answer Section

- {{ params.part7.ans1}} {{ params.vars.units}}
- {{ params.part7.ans2}} {{ params.vars.units}}

## Part 7

If you were to design anti-reflective coatings for glasses with this thin film material and this color of light, which film thickness would you choose?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)