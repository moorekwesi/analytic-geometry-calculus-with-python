# Listing 9.8: Classifying Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0 and plotting it
import numpy as np
import matplotlib.pyplot as plt

def classify(A, B, C):
    disc = B**2 - 4*A*C
    if disc < 0:
        return "circle" if (A == C and B == 0) else "ellipse"
    return "parabola" if disc == 0 else "hyperbola"

curves = {                                     # (A, B, C, D, E, F)
    "x²+y²+3x−6y−1=0":         (1, 0, 1, 3, -6, -1),
    "3x²+4y²+24x−16y+52=0":    (3, 0, 4, 24, -16, 52),
    "x²+4y+8x+4=0":            (1, 0, 0, 8, 4, 4),
    "16x²−9y²−128x−18y+103=0": (16, 0, -9, -128, -18, 103),
    "x²+2xy+y²+6x−34y−71=0":   (1, 2, 1, 6, -34, -71),
}
X, Y = np.meshgrid(np.linspace(-12, 16, 600), np.linspace(-12, 16, 600))
plt.figure(figsize=(5.5, 5.5))
for i, (name, (A, B, C, D, E, F)) in enumerate(curves.items()):
    kind = classify(A, B, C)
    print(f"{name:<26} B²−4AC = {B**2 - 4*A*C:>5}  -> {kind}")
    Z = A*X**2 + B*X*Y + C*Y**2 + D*X + E*Y + F
    plt.contour(X, Y, Z, levels=[0], colors=f"C{i}")
    plt.plot([], [], color=f"C{i}", label=f"{kind}")
plt.gca().set_aspect("equal"); plt.grid(alpha=0.3); plt.legend(fontsize=8, loc="lower left")
plt.show()
