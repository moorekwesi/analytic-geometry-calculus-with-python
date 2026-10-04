# Listing 5.6: Curve sketching with SymPy: f(x) = 12 + 2x^2 - x^4
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols("x", real=True)
f = 12 + 2*x**2 - x**4
f1, f2 = sp.diff(f, x), sp.diff(f, x, 2)

for c in sp.solve(f1, x):
    test = f2.subs(x, c)
    kind = "local max" if test < 0 else ("local min" if test > 0 else "test fails")
    print(f"critical x = {c}: f'' = {test} -> {kind}, f = {f.subs(x, c)}")
for p in sp.solve(f2, x):
    print(f"possible inflection at x = {p}, f = {f.subs(x, p)}")

X = np.linspace(-2, 2, 400)
F = sp.lambdify(x, f)
plt.figure(figsize=(5.5, 3.6))
plt.plot(X, F(X), "k")
for c in sp.solve(f1, x):
    plt.plot(float(c), float(f.subs(x, c)), "ro")
for p in sp.solve(f2, x):
    plt.plot(float(p), float(f.subs(x, p)), "gs")
plt.ylim(4, 14); plt.grid(alpha=0.3)
plt.title("red: extrema, green: inflection points")
plt.show()
