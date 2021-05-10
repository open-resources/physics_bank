---
title: Half-Life Question
type: symbolic-input
author: Andrew Rechnitzer
source: original
tags:
- half-life
outcomes:
- LO.math.2305
- LO.math.2304
assets:
server: |

    from sympy import *
    import random
    #import prairielearn as pl

    data = {'correct_answers':{}}
    x = S('x')

    unparam = random.choice(["True","False"])

    if unparam:
        T,a,b = S('T,a,b')
        ans = T
        #data["correct_answers"]['symbolic_math'] = pl.to_json()
        data["correct_answers"] = ans
    else:
        T = random.randint(2,9)
        a = random.randint(20,30)
        b = (a//2)-random.randint(1,5)

        r = S(b)/S(a)
        kcon = (S(1)/T*log(r))
        lam = (-log(2)/kcon)

        ans = 42

        data["correct_answers"] = "ans1"
substitutions:
  params:
    a: 100000
    b: 200000
    T: 365
    k: 400
    lambda: 600
    A: 1000000
  vars:
    units: s
    title: Half-Life Problem from Andrew
    digits_after_decimal: 2
---
# {{ vars.title }}

## Question Text

A sample of a certain material is undergoing radioactive decay.
Initially the sample weighs {{ params.a }}g.
After {{ params.T }} days, the sample weighs {{ params.b }}g.
Assuming the rate of decay is proportional to the mass of the sample, compute the half-life of the material.

The half life is:

## Answer Section

Please enter in a numeric value in {{ vars.units }} to {{ vars.digits_after_decimal }} decimal places.

## Solution

Since the rate of decay is proportional to the mass of the sample, we know that the mass has a simple exponential form

$$ 
\begin{equation}
m(t) = A e^{kt}
\end{equation}
$$

Further, since the initial mass is {{ params.a }} g, it follows that


$$ 
\begin{equation}
m(0) = A e^0 = A = a
\end{equation}
$$

Then since the mass after {{ params.T }} days is {{ params.b }}g, we know that

$$ 
\begin{equation}
m(T) = a e^{k T} = b
\end{equation}
$$

and so the constant {{ params.k }} is

$$ 
\begin{equation}
k = \frac{1}{T} \ln(r)
\end{equation}
$$

The half life, {{ params.lambda }} is the time for the mass to halve, and can be computed by solving

$$ 
\begin{equation}
m(\lambda) = \frac{A}{2} = A e^{k\lambda}
\end{equation}
$$

Cancelling the {{ params.A }} and taking the logarithm of both sides gives:

$$ 
\begin{equation}
\log\frac{1}{2} = \lambda \cdot \frac{\log r}{T}\end{equation}
$$

and so

$$ 
\begin{equation}
\lambda = T \cdot \frac{\log(1/2)}{\log r} = \lambda
\end{equation}
$$

