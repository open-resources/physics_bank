---
title: Lennard Jones Potential
topic: Energy
author: John Hopkinson
source: Physics 122 W2 2019 GPSIX
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 8.3.1.2
difficulty:
- medium
randomization:
- 0
taxonomy:
- undefined
span:
- chapter
length:
- average
tags:
- L.K
assets: null
part1:
  type: file-upload
  pl-customizations:
    file-names: potential.png
part2:
  type: symbolic-input
  pl-customizations:
    label: $F_r = $
    variables: R, r, u
    weight: 1
    allow-blank: false
myst:
  substitutions:
    params_vars_title: Lennard Jones Potential
---
# {{ params_vars_title }}
The Lennard-Jones 6-12 potential energy, which describes the potential energy between neutral gases, is $u(r) = u_0(\frac{r_0}{r})^{12} - 2( \frac{r_0}{r})^6$, where $ r $ is the separation between atoms.
For Ar, $ r_0 = 3.9 \times 10^{-10} $ m and $ u_0 = 1.6 \times 10^{-21} $ J (according to D. V. Schroeder, An Introduction to Thermal Physics).

## Part 1

Roughly sketch the form of the potential energy as a function of $r$.
On your diagram indicate the value of $r$ and $u$ at the minimum energy in terms of $r_0$ and $u_0$ (note: $\frac{du}{dr} = 0$ at this point).
Also indicate where the potential energy starts to become positive, and its behavior as $r\rightarrow{\infty}$.

upload your work as a png file named '$\textbf{potential}$'.

### Answer Section

File upload will appear here

## Part 2

Derive an expression for the force between the atoms as a function of $r$.

On your diagram from part 1 above, label the regions where the force is negative (attractive) between atoms, and where the force is positive (repulsive) between atoms.

| For  | Use   |
|------|-------|
| $r_o$  | R  |
| $r$    | r  |
| $u_o$  | u  |

### Answer Section

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)