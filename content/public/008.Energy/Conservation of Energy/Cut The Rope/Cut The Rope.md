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
server:
  imports: |
    import random as rd
    import sympy as sp
    import math
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: "# Start problem code\n\ndata2 = nested_dict()\n\n# store phrases etc\n\
    data2[\"params\"][\"vars\"][\"title\"] = \"Cut The Rope\"\ndata2[\"params\"][\"\
    vars\"][\"units\"] = \"m\"\n\n# define bounds of the variables\n# need [cos(theta_0)\
    \ - cos (theta_c)] < 0 for v_cut to be positive\nl = pbh.roundp(rd.uniform(0.1,\
    \ 0.9), decimals=1)\ntheta_0 = rd.randint(35,45)\ntheta_c = rd.randint(10,30)\n\
    \n# store the variables in the dictionary \"params\"\ndata2[\"params\"][\"l\"\
    ] = l\ndata2[\"params\"][\"theta_0\"] = theta_0\ndata2[\"params\"][\"theta_c\"\
    ] = theta_c\n\n# define g\ng = 9.81\n\n# calculate v_cut, v_x and v_y \ndiff =\
    \ math.cos(math.radians(theta_0)) - math.cos(math.radians(theta_c))\nv_c = math.sqrt(-2*g*l*diff)\n\
    vx = v_c * math.cos(math.radians(theta_c))\nvy = v_c * math.sin(math.radians(theta_c))\n\
    \n# calculate d (in metres)\nd = (2*vx*vy)/g\n\n# define correct answers\ndata2[\"\
    correct_answers\"][\"part1_ans\"] = d\n\n# Update the data object with a new dict\n\
    data.update(data2)\n"
  prepare: 'pass

    '
  parse: 'pass

    '
  grade: 'pass

    '
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
    l: 0.6
    theta_0: 37
    theta_c: 21
  correct_answers:
    part1_ans: 0.1083549285230076
---
# {{ params.vars.title }}
In the mobile app "Cut the Rope", a mass (of candy) swings on a rope and the game player selects a point to cut the rope so it lands in a cute little monster's mouth.
Imagine that the mass is suspended from a fixed pivot point by a massless string of length $L = $  {{ params.l }} m.
It is released from an angle $\theta_0 = $ {{ params.theta_0 }} $^{\circ}$, swings through its lowest point, and is then cut on the other side at $\theta\_{cut} = $ {{ params.theta_c }} $^{\circ}$.
Once cut, the mass flies free (no drag) and lands on a surface a distance $d$ away from the point where it was when the rope was cut.
The surface is at the same height as the mass when the rope is cut.

The figure below shows the situation described above.

![A mass is suspended from a fixed pivot point by a massless string of length L. It is displaced to the left at an angle theta naught from equilibrium.  After swinging through its lowest point, the rope is then cut on the right at an angle theta cut. The mass lands on a surface at the same height as the mass when the rope is cut. ](q11_2012Final.png)

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)