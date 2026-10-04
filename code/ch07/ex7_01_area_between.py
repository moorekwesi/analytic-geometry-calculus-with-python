# Listing 7.1: Area between two curves: y = 2x and y = x^2
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols("x")
top, bottom = 2*x, x**2
a, b = sp.solve(sp.Eq(top, bottom), x)          # intersection points
area = sp.integrate(top - bottom, (x, a, b))
print("curves meet at x =", a, "and x =", b, ";  area =", area)

X = np.linspace(-0.3, 2.3, 200)
plt.figure(figsize=(4.5, 3.6))
plt.plot(X, 2*X, label="$y = 2x$"); plt.plot(X, X**2, label="$y = x^2$")
Xf = np.linspace(0, 2, 100)
plt.fill_between(Xf, Xf**2, 2*Xf, alpha=0.3, label=f"area = {area}")
plt.legend(); plt.grid(alpha=0.3); plt.show()
