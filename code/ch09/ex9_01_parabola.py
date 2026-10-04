# Listing 9.1: A parabola is the set of points equidistant from a focus and a directrix
import numpy as np
import matplotlib.pyplot as plt

c = 2                                   # x^2 = 4cy = 8y: focus (0, 2), directrix y = -2
x = np.linspace(-6, 6, 13)
y = x**2 / (4*c)
d_focus = np.sqrt(x**2 + (y - c)**2)
d_directrix = y + c
print(" x      y   dist to focus   dist to directrix")
for row in zip(x[::3], y[::3], d_focus[::3], d_directrix[::3]):
    print("{:>3.0f} {:>6.2f} {:>15.4f} {:>19.4f}".format(*row))

X = np.linspace(-6, 6, 200)
plt.figure(figsize=(5, 3.8))
plt.plot(X, X**2/(4*c), "k", lw=2, label="$x^2 = 8y$")
plt.axhline(-c, color="C3", ls="--", label="directrix $y=-2$")
plt.plot(0, c, "C3*", ms=12, label="focus (0, 2)")
P = (4, 2)                              # a sample point on the parabola
plt.plot([P[0], 0], [P[1], c], "C0"); plt.plot([P[0], P[0]], [P[1], -c], "C0")
plt.plot(*P, "C0o")
plt.gca().set_aspect("equal"); plt.ylim(-3, 6); plt.grid(alpha=0.3); plt.legend(fontsize=8)
plt.show()
