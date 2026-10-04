# Listing 8.1: Plotting parametric curves x = f(t), y = g(t)
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 400)
fig, ax = plt.subplots(1, 4, figsize=(10, 2.8))
ax[0].plot(np.cos(t), np.sin(t));           ax[0].set_title("circle")
ax[1].plot(2*np.cos(t), 3*np.sin(t), "C1");  ax[1].set_title("ellipse")
T = np.linspace(0, 4*np.pi, 400)
ax[2].plot(T - np.sin(T), 1 - np.cos(T), "C2"); ax[2].set_title("cycloid")
ax[3].plot(np.sin(3*t), np.sin(2*t), "C3");  ax[3].set_title("Lissajous")
for a in ax:
    a.set_aspect("equal"); a.grid(alpha=0.3)
plt.tight_layout(); plt.show()

# Eliminating the parameter with SymPy: x = 2 cos t, y = 3 sin t
s = sp.symbols("t")
x, y = 2*sp.cos(s), 3*sp.sin(s)
print("(x/2)^2 + (y/3)^2 =", sp.simplify((x/2)**2 + (y/3)**2))
