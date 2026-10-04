# Listing 9.2: Where should the receiver of a satellite dish go?
import numpy as np
import matplotlib.pyplot as plt

D, depth = 90.0, 12.0                  # dish diameter and depth (cm)
# Dish cross-section: x^2 = 4cy passes through (D/2, depth)
c = (D/2)**2 / (4*depth)
print(f"focal length c = D^2/(16 depth) = {c:.2f} cm above the centre of the dish")

# Reflect vertical incoming rays off y = x^2/(4c): they all pass through (0, c)
X = np.linspace(-D/2, D/2, 200)
plt.figure(figsize=(5, 4))
plt.plot(X, X**2/(4*c), "k", lw=3)
for x0 in np.linspace(-40, 40, 9):
    y0 = x0**2/(4*c)
    plt.plot([x0, x0], [60, y0], "C1", lw=0.8)            # incoming ray
    plt.plot([x0, 0], [y0, c], "C0", lw=0.8)              # reflected ray
plt.plot(0, c, "r*", ms=14)
plt.gca().set_aspect("equal"); plt.ylim(-2, 62); plt.grid(alpha=0.3)
plt.title("all reflected rays meet at the focus")
plt.show()
