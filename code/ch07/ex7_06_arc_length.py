# Listing 7.6: Arc length L = ∫ sqrt(1 + (dy/dx)^2) dx
import numpy as np
import sympy as sp
from scipy.integrate import quad

x = sp.symbols("x", positive=True)

# (a) An exact example: y = (2/3) x^(3/2) from x = 0 to x = 3
y = sp.Rational(2, 3)*x**sp.Rational(3, 2)
L = sp.integrate(sp.sqrt(1 + sp.diff(y, x)**2), (x, 0, 3))
print("y = (2/3)x^(3/2), 0 <= x <= 3:  L =", L)

# (b) A parabolic arch spanning 240 m and rising 50 m: y = 50 - k x^2
k = 50 / 120**2
dydx = lambda s: -2*k*s
L, _ = quad(lambda s: np.sqrt(1 + dydx(s)**2), -120, 120)
print(f"length of the arch = {L:.2f} m  (span 240 m, so {L - 240:.2f} m longer)")

# (c) A curve whose arc-length integral has no formula: y = sin x, 0 <= x <= pi
L, _ = quad(lambda s: np.sqrt(1 + np.cos(s)**2), 0, np.pi)
print(f"one arch of y = sin x has length {L:.6f}")
