# Listing 2.6: Where does a road cross a mast's coverage circle?
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols("x")
R = 5                                   # coverage radius (km), mast at the origin

def crossing(m, c):
    """Intersect y = m x + c with x^2 + y^2 = R^2; classify with the discriminant."""
    quad = sp.expand(x**2 + (m*x + c)**2 - R**2)
    A, B, C = [quad.coeff(x, k) for k in (2, 1, 0)]
    disc = B**2 - 4*A*C
    xs = sp.solve(quad, x)
    pts = [(float(xi), float(m*xi + c)) for xi in xs if xi.is_real]
    kind = "2 points" if disc > 0 else ("tangent" if disc == 0 else "misses")
    return kind, disc, pts

roads = {"Road 1: y = x/2 + 1": (sp.Rational(1, 2), 1),
         "Road 2: y = 5":       (0, 5),
         "Road 3: y = -x + 9":  (-1, 9)}
plt.figure(figsize=(5, 5))
t = np.linspace(0, 2*np.pi, 300)
plt.fill(R*np.cos(t), R*np.sin(t), alpha=0.15, label="coverage")
xx = np.linspace(-7, 9, 50)
for name, (m, c) in roads.items():
    kind, disc, pts = crossing(m, c)
    print(f"{name:<20} discriminant = {float(disc):8.2f}  -> {kind}", [tuple(round(v, 3) for v in p) for p in pts])
    if len(pts) == 2:
        L = np.hypot(pts[0][0] - pts[1][0], pts[0][1] - pts[1][1])
        print(f"{'':20} length of road inside coverage = {L:.3f} km")
    plt.plot(xx, float(m)*xx + c, label=name)
plt.plot(0, 0, "k^", ms=10)
plt.xlim(-7, 9); plt.ylim(-7, 9)
plt.gca().set_aspect("equal"); plt.grid(alpha=0.3); plt.legend(fontsize=7, loc="lower left")
plt.show()

# Exam question (2021): x - 2y - 1 = 0 and x^2 + y^2 + 4x - 2y - 5 = 0
X, Y = sp.symbols("X Y")
print(sp.solve([X - 2*Y - 1, X**2 + Y**2 + 4*X - 2*Y - 5], [X, Y]))
