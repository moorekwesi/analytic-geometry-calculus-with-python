# Listing 5.1: Tangent and normal lines to a curve
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols("x")
f = x**2 + 4*x - 3
a = 1
m = sp.diff(f, x).subs(x, a)              # gradient of the tangent
b = f.subs(x, a)
tangent = sp.expand(b + m*(x - a))
normal = sp.expand(b - (x - a)/m)
print("point:", (a, b), " gradient f'(1) =", m)
print("tangent: y =", tangent)
print("normal : y =", normal, "   i.e. x + 6y = 13")

X = np.linspace(-3, 3, 200)
F, T, N = (sp.lambdify(x, e) for e in (f, tangent, normal))
plt.figure(figsize=(4.8, 4.8))
plt.plot(X, F(X), "k", lw=2, label="$y=x^2+4x-3$")
plt.plot(X, T(X), "C3", label="tangent")
plt.plot(X, N(X), "C0--", label="normal")
plt.plot(a, b, "ko"); plt.ylim(-8, 12)
plt.gca().set_aspect("equal"); plt.grid(alpha=0.3); plt.legend(fontsize=8)
plt.show()
