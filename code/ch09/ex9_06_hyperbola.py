# Listing 9.6: The hyperbola 16x^2 - 9y^2 - 128x - 18y + 103 = 0 and its asymptotes
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x, y = sp.symbols("x y")
H = 16*x**2 - 9*y**2 - 128*x - 18*y + 103
standard = 16*(x - 4)**2 - 9*(y + 1)**2 - 144
print("16(x-4)^2 - 9(y+1)^2 = 144 is the same curve:", sp.expand(standard - H) == 0)
h, k, a, b = 4, -1, 3, 4
c = np.sqrt(a**2 + b**2)
print(f"centre ({h}, {k}), a = {a}, b = {b}, c = {c:.0f}, e = {c/a:.4f}")
print(f"foci ({h - c:.0f}, {k}) and ({h + c:.0f}, {k}); asymptotes y + 1 = ±(4/3)(x - 4)")

t = np.linspace(-2, 2, 200)                       # x = h ± a cosh t, y = k + b sinh t
plt.figure(figsize=(5, 4))
plt.plot(h + a*np.cosh(t), k + b*np.sinh(t), "k")
plt.plot(h - a*np.cosh(t), k + b*np.sinh(t), "k")
X = np.linspace(-6, 14, 2)
plt.plot(X, k + b/a*(X - h), "C3--", lw=1); plt.plot(X, k - b/a*(X - h), "C3--", lw=1)
plt.plot([h - c, h + c], [k, k], "b*", ms=10)
plt.xlim(-6, 14); plt.ylim(-12, 10); plt.gca().set_aspect("equal"); plt.grid(alpha=0.3)
plt.show()
