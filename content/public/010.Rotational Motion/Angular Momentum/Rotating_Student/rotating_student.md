---
title: Rotating Student
topic: Rotational Motion
author: John Hopkinson
source: Phys 112 2018W1 GPS XI
template_version: 1.4
attribution: standard
partialCredit: true
singleVariant: false
showCorrectAnswer: false
outcomes:
- 7.5.3.0
- 7.5.3.1
- 10.2.1.1
- 10.5.2.2
- 10.5.2.3
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
- JR
assets: null
part1:
  type: file-upload
  pl-customizations:
    file-names: diagrams.pdf
part2:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $I_{\text{in}} = $
    suffix: $\rm{kgm^2}$
part3:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $I_{\text{out}} = $
    suffix: $\rm{kgm^2}$
part4:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $\omega_{\text{out}} = $
    suffix: $\rm{rad/s}$
part5:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $\omega_{\text{in}} = $
    suffix: $\rm{rad/s}$
part6:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $\omega_{\text{massless}} = $
    suffix: $\rm{rad/s}$
part7:
  type: number-input
  pl-customizations:
    rtol: 0.05
    weight: 1
    allow-blank: false
    show-correct-answer: false
    label: $p_{\text{mass}} = $
    suffix: $\rm{kgm/s}$
myst:
  substitutions:
    params_vars_title: Rotating Student
    params_m_t: 90
    params_m_a: 11
    params_m_m: 6
    params_r_t: 1.0
    params_r_ao: 0.86
    params_r_ai: 0.18
    params_h_t: 2.0
    params_dt: 6.1
---
# {{ params_vars_title }}
In class, we had a student standing on a platform with their arms outstretched while holding masses. The student was rotated in this position and then pulled their arms in and we observed how their angular velocity changed. For this problem we will assume that the student's torso has a cylindrical (rather than rectangular) cross-section with a radius of $r\_{\text{t}} = {{ params.r_t }} \rm{m}$ and mass $m\_{\text{t}} = {{ params.m_t }} \rm{kg}$. The student's two arms have a total mass of $m\_{\text{a}} = {{ params.m_a }} \rm{kg}$, a radius of $r\_{\text{a,out}} = {{ params.r_ao }} \rm{m}$ when outstretched, and a radius of $r\_{\text{a,in}} = {{ params.r_ai }} \rm{m}$ when held in. The student holds $m\_{\text{m}} = {{ params.m_m }} \rm{kg}$ masses in each hand. Treat the student's arms as point masses when held in and as thin rods when outstreched. The student's torso may be modelled as a solid cylinder with a height of $h\_{\text{t}} = {{ params.h_t }} \rm{m}$.

## Part 1

Draw two diagrams for this problem showing the student before and after bringing their arms in.

Save your diagams and "diagrams.pdf" and upload the file below.

### Answer Section

File upload box will be shown here.

## Part 2

Calculate the total moment of inertia of the student with their arms held in while holding the two masses $I\_{\text{in}}$.

### Answer Section

Please enter in a numeric value in $\rm{kgm^2}$.

## Part 3

Calculate the total moment of inertia of the student with their arms outstretched while holding the two masses $I\_{\text{out}}$.

### Answer Section

Please enter in a numeric value in $\rm{kgm^2}$.

## Part 4

If it takes the student $\Delta t = {{ params_dt }} \rm{s}$ to fully rotate on a frictionless platform with their arms outstretched, calculate their angular speed $\omega\_{\text{out}}$.

### Answer Section

Please enter in a numeric value in $\rm{rad/s}$.

## Part 5

After the student pulls their arms in, calculate their new angular speed $\omega\_{\text{in}}$.

### Answer Section

Please enter in a numeric value in $\rm{rad/s}$.

## Part 6

If the student dropped both masses while turning with their arms outstretched, what angular speed $\omega\_{\text{massless}}$ would they have after letting go of the masses?

### Answer Section

Please enter in a numeric value in $\rm{rad/s}$.

## Part 7

After the student let go of the masses with their arms outstretched, what magnitude of linear momentum $p\_{\text{mass}}$ would each mass carry away?

### Answer Section

Please enter in a numeric value in $\rm{kgm/s}$.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)