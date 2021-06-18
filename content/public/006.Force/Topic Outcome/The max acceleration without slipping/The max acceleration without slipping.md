---
title: A Crate's Maximum Acceleration without Slipping
topic: Force
author: Jake Bobowski
source: 2012 Final Q12
template_version: 1.0
attribution: standard
outcomes:
- 6.1.1.4
- 6.3.1.2
- 6.3.1.3
- 6.7.1.0
- 6.9.1.3
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- PW
assets: null
server:
  imports: |
    import random
    import pandas as pd
    import math
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
  generate: "# Start problem code\n\ndata2 = nested_dict()\n\n# define or load names/items/objects\n\
    vehicles = pd.read_csv(\"data/vehicles.csv\")[\"Vehicles\"].tolist()\n\n# store\
    \ phrases etc\ndata2[\"params\"][\"vars\"][\"vehicle\"] = random.choice(vehicles)\n\
    data2[\"params\"][\"vars\"][\"title\"] = \"A Crate's Maximum Acceleration without\
    \ Slipping\"\ndata2[\"params\"][\"vars\"][\"units\"] = \"$m/s^2$\"\n\n# define\
    \ bounds of the variables\nmu_k = pbh.roundp(random.uniform(0.2, 0.5), decimals\
    \ = 2)\nmu_s = pbh.roundp(random.uniform(mu_k + 0.1, 1.0), decimals = 2) \ntheta\
    \ = random.randint(10, 30)\n\n# store the variables in the dictionary \"params\"\
    \ndata2[\"params\"][\"mu_s\"] = mu_s\ndata2[\"params\"][\"mu_k\"] = mu_k\ndata2[\"\
    params\"][\"theta\"] = theta\n\n# define g\ng = 9.81\n\n# calculate a_max\ntheta_r\
    \ = math.radians(theta)                           # convert to radians\na_max\
    \ = g*(mu_s*math.cos(theta_r) - math.sin(theta_r))\n\n# define correct answers\n\
    data2[\"correct_answers\"][\"part1_ans\"] = a_max\n\n# Update the data object\
    \ with a new dict\ndata.update(data2)\n"
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
    label: $a_{max} = $
    suffix: $m/s^2$
    comparison: sigfig
    digits: 2
substitutions:
  params:
    vars:
      vehicle: sedan
      title: A Crate's Maximum Acceleration without Slipping
      units: $m/s^2$
    mu_s: 0.69
    mu_k: 0.33
    theta: 17
  correct_answers:
    part1_ans: 3.604964839308143
---
# {{ params.vars.title }}
A wood crate sits in the back of a {{ params.vars.vehicle }}.
The coefficients of friction between the crate and the {{ params.vars.vehicle }} are $\mu_s = $ {{ params.mu_s }} and $\mu_k = $ {{ params.mu_k }}.
The {{ params.vars.vehicle }} starts moving up a {{ params.theta }}$^{\circ}$ slope.

## Attribution

Problem is licensed under the [CC-BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
![The Creative Commons 4.0 license requiring attribution-BY, non-commercial-NC, and share-alike-SA license.](https://raw.githubusercontent.com/firasm/bits/master/by-nc-sa.png)