---
title: Cut The Rope
topic: Energy
author: Jake Bobowski
source: 2012 Final Q11
template_version: 1.0
attribution: standard
outcomes:
- 8.5.1.1
- 8.5.1.3
- 5.1.1.0
- 5.5.1.0
- 5.5.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- PW
assets:
- q11_2012Final.png
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $d= $
    suffix: m
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      title: Cut The Rope
      units: m
    l: 0.2
    theta_0: 44
    theta_c: 13
---
# {{ params.vars.title }}
In the mobile app "Cut the Rope", a mass (of candy) swings on a rope and the game player selects a point to cut the rope so it lands in a cute little monster's mouth.
Imagine that the mass is suspended from a fixed pivot point by a massless string of length $L = $  {{ params.l }} m.
It is released from an angle $\theta_0 = $ {{ params.theta_0 }} $^{\circ}$, swings through its lowest point, and is then cut on the other side at $\theta\_{cut} = $ {{ params.theta_c }} $^{\circ}$.
Once cut, the mass flies free (no drag) and lands on a surface a distance $d$ away from the point where it was when the rope was cut.
The surface is at the same height as the mass when the rope is cut.

The figure below shows the situation described above.

![A mass is suspended from a fixed pivot point by a massless string of length L. It is displaced to the left at an angle theta naught from equilibrium.  After swinging through its lowest point, the rope is then cut on the right at an angle theta cut. The mass lands on a surface at the same height as the mass when the rope is cut. ](q11_2012Final.png)
## Question Text

What is the distance $d$?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).<br> ![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)