---
title: Geostationary Orbits
topic: Force
author: Ammar Zavahir
source: original
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 12.2.1.0
- 6.12.2.0
- 12.4.4.0
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- APSC181
- A.Z
assets:
- part1.png
- part2.png
part1:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $r= $
    suffix: $\rm{m}$
    comparison: sigfig
    digits: 2
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: true
    label: $r= $
    suffix: $\rm{m}$
    comparison: sigfig
    digits: 2
myst:
  substitutions:
    params_m: 4335
    params_v: 907
---
# Geostationary Orbits
A communications satellite is orbiting the Earth with constant speed $v\ \rm{km/h}$.

<img src="part1.png" width=800>

## Part 1

If there are no other forces acting on the satellite except for the mutual gravitational force acting between the satellite and the Earth, calculate the effective radius ($R$) of the orbit of the satellite.<br><br> Treat the earth and satellite as particles.

$v = {{ params_v }}\ \rm{km/h}$, $M\_{earth} = 5.976\times 10^{24}\ \rm{kg}$, $M\_{satellite} = {{ params_m }}\ \rm{kg}$

### Answer Section

Please enter in a numeric value in m.

## Part 2

For rapid communication between satellites in orbit and receivers on the ground, these communication satellites are stationed in 'geostationary' orbits around the Earth, with both the Earth and satellite sharing the same plane and axis of rotation.

<img src="part2.png" width=800>

By showing that the period of revolution of the satellite satisfies the following relationship,
<br>
$T= ({\frac{4\pi^{2}R^{3}}{GM\_{Earth}}})^{\frac{1}{3}}$
<br>
<br>
Calculate the height, $h$ above the surface of the earth for the satellite to be in a 'geostationary' orbit.
<br>
$R\_{Earth} = 6371\ \rm{km}$

### Answer Section

Please enter in a numeric value in m.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)