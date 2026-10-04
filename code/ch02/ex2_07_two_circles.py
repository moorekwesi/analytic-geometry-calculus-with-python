# Listing 2.7: Two coverage circles - how do they meet, and where is the common chord?
import math
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def relative_position(c1, r1, c2, r2):
    d = math.dist(c1, c2)
    if d > r1 + r2:            return d, "separate (no common point)"
    if d == r1 + r2:           return d, "touch externally"
    if d == abs(r1 - r2):      return d, "touch internally"
    if d < abs(r1 - r2):       return d, "one inside the other"
    return d, "intersect at two points"

print(relative_position((0, 0), 5, (6, 2), 4))
print(relative_position((0, 0), 5, (8, 6), 5))
print(relative_position((0, 0), 5, (1, 1), 2))

# Common chord: subtract the two equations
x, y = sp.symbols("x y")
S1 = x**2 + y**2 - 25                       # mast A at (0,0), radius 5 km
S2 = (x - 6)**2 + (y - 2)**2 - 16           # mast B at (6,2), radius 4 km
chord = sp.expand(S1 - S2)
print("Common chord:", chord, "= 0")
pts = sp.solve([S1, S2], [x, y])
pts = [(float(a), float(b)) for a, b in pts]
print("Intersection points:", [tuple(round(v, 4) for v in p) for p in pts])

t = np.linspace(0, 2*np.pi, 300)
plt.figure(figsize=(5.5, 4.5))
plt.fill(5*np.cos(t), 5*np.sin(t), alpha=0.2, label="mast A")
plt.fill(6 + 4*np.cos(t), 2 + 4*np.sin(t), alpha=0.2, label="mast B")
plt.plot(*zip(*pts), "k-o", label="common chord")
plt.gca().set_aspect("equal"); plt.grid(alpha=0.3); plt.legend(fontsize=8)
plt.show()
