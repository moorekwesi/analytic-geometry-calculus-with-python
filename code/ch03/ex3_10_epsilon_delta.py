# Listing 3.10: Epsilon and delta - how close is close enough?
# lim_{x->2} x^2 = 4. Given a tolerance eps, find delta so that
# |x - 2| < delta guarantees |x^2 - 4| < eps.
import numpy as np

def works(delta, eps, n=100001):
    x = np.linspace(2 - delta, 2 + delta, n)[1:-1]
    return np.all(np.abs(x**2 - 4) < eps)

for eps in [1, 0.1, 0.01, 0.001]:
    delta = 1.0
    while not works(delta, eps):
        delta /= 2                       # halve delta until it works
    rule = min(1, eps/5)                 # the textbook choice, proved in the text
    print(f"eps = {eps:<6} found delta = {delta:<12.6g} textbook delta = min(1, eps/5) = {rule:g}")
