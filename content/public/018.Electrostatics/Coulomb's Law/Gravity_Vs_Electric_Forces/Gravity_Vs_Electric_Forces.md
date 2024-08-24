---
title: Gravity Vs Electric Forces
topic: Electrostatics
author: John Hopkinson
source: PHYS122 2018W2 Q4
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: true
outcomes:
- 12.2.1.0
- 18.5.1.0
difficulty:
- easy
randomization:
- 0
taxonomy:
- undefined
span:
- undefined
length:
- short
tags:
- JR
assets: null
part1:
  type: multiple-choice
  pl-customizations:
    weight: 1
myst:
  substitutions:
    params:
      vars:
        title: Gravity Vs Electric Forces
      part1:
        ans1:
          value: $2.3 \times 10^{39}$
          feedback: Yes, note that the gravitational force between fundamental particles
            is insignificantly small relative to the electric force, so we are justified
            in neglecting it when dealing with small charged particles. Also note
            that this answer is independent of distance!
        ans2:
          value: $1.7 \times 10^{19}$
          feedback: No, click the 'Helpful Information' button to see the formulae
            for the gravitational force $F_G$ and the electric force $F_E$. Find the
            ratio of these two forces.
        ans3:
          value: $0.13$
          feedback: No, click the 'Helpful Information' button to see the formulae
            for the gravitational force $F_G$ and the electric force $F_E$. Find the
            ratio of these two forces.
        ans4:
          value: $5.9 \times 10^{-20}$
          feedback: No, click the 'Helpful Information' button to see the formulae
            for the gravitational force $F_G$ and the electric force $F_E$. Find the
            ratio of these two forces.
        ans5:
          value: $13000$
          feedback: No, click the 'Helpful Information' button to see the formulae
            for the gravitational force $F_G$ and the electric force $F_E$. Find the
            ratio of these two forces.
---
# {{ params.vars.title }}
The gravitational force $F_G$ has the same form as Coulomb's law for the electric force $F_E$ , but it is always an attractive force.

## Useful Info

The gravitational force between two objects with masses $m_1$ and $m_2$ separated by a distance $r$ is given by $F_G = \frac{Gm_1m_2}{r^2}$, where $G = 6.67 \times 10^{-11}$ $\rm{\frac{Nm^2}{kg^2}}$.
The electric force between two objects with charges $q_1$ and $q_2$ separated by a distance $r$ is given by $F_E = \frac{kq_1q_2}{r^2}$, where $k = 8.99 \times 10^9$ $\rm{\frac{Nm^2}{C^2}}$.

## Part 1

Find the ratio of the electric force to the gravitational force between a proton ($m_p = 1.67 \times 10^{-27}$ $\rm{kg}$, $q_p = 1.602 \times 10^{-19}$ $\rm{C}$) and an electron ($m_e = 9.11 \times 10^{-31}$ $\rm{kg}$, $q_e = -1.602 \times 10^{-19}$ $\rm{C}$).

### Answer Section

- {{ params.part1.ans1.value }}
- {{ params.part1.ans2.value }}
- {{ params.part1.ans3.value }}

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)