---
title: Flywheel
topic: Rotational Motion
author: Patrick Jilek-Rodriguez
source: original
template_version: 1.4
attribution: standard
partialCredit: false
singleVariant: false
outcomes:
- 10.5.1.0
- 11.3.1.4
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
- APSC181
- PJ
assets:
- Flywheel.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $E= $
    suffix: $\rm{kJ}$
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $t= $
    suffix: $\rm{hours}$
myst:
  substitutions:
    params:
      vars:
        title: Flywheel
      Crr: 0.004
      m: 276
      RPM: 2725
      R: 23
      r: 4
---
# {{ params.vars.title }}
A flywheel is a wheel with a high moment of inertia that spins to store kinetic energy.
It has applications in cars, gyroscopes, and electrical power systems.

<img src="Flywheel.png" alt="A wheel." >

A flywheel of mass ${{params.m}}\ \rm{kg}$, and radius of gyration ${{params.R}}\ \rm{cm}$ is spinning at ${{params.RPM}}\ \rm{RPM}$.

## Part 1

How much kinetic energy is stored in the wheel?

### Answer Section

Please enter in a numeric value in kJ.

## Part 2

If the coefficient of rolling friction of the bearing is ${{params.Crr}}$, for how long will the flywheel spin?
This friction occurs at an inner radius of ${{params.r}}\ \rm{cm}$.
Note that the rolling resistance force is analogous to the force of friction, where $F\_{friction} = {\mu}\_rF_N$.

### Answer Section

Please enter in a numeric value in hours.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)