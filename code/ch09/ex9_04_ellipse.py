# Listing 9.4: Analysing the ellipse 3x^2 + 4y^2 + 24x - 16y + 52 = 0
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x, y = sp.symbols("x y")
E = 3*x**2 + 4*y**2 + 24*x - 16*y + 52
# Completing the square: 3(x+4)^2 + 4(y-2)^2 = 12
print("check:", sp.expand(3*(x + 4)**2 + 4*(y - 2)**2 - 12 - E) == 0)
h, k, a, b = -4, 2, 2, np.sqrt(3)
c = np.sqrt(a**2 - b**2)
print(f"centre ({h}, {k}), a = {a}, b = {b:.4f}, c = {c:.0f}, e = c/a = {c/a}")
F1, F2 = np.array([h - c, k]), np.array([h + c, k])
print("foci:", F1, F2)

t = np.linspace(0, 2*np.pi, 7)[:-1]
for P in zip(h + a*np.cos(t), k + b*np.sin(t)):          # sample points on the ellipse
    P = np.array(P)
    print(f"P = ({P[0]:6.3f}, {P[1]:6.3f}):  PF1 + PF2 = "
          f"{np.linalg.norm(P - F1) + np.linalg.norm(P - F2):.6f}")

T = np.linspace(0, 2*np.pi, 300)
plt.figure(figsize=(5, 3.4))
plt.plot(h + a*np.cos(T), k + b*np.sin(T), "k")
plt.plot(*F1, "r*", ms=10); plt.plot(*F2, "r*", ms=10)
plt.gca().set_aspect("equal"); plt.grid(alpha=0.3); plt.show()
