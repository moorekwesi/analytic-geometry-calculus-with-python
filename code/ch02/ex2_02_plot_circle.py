# Listing 2.2: Drawing circles with the parametric form x = a + r cos t, y = b + r sin t
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 300)

plt.figure(figsize=(5, 5))
# Lake Bosomtwe is roughly circular, about 8 km across (radius ~ 4 km).
a, b, r = 0, 0, 4
plt.fill(a + r*np.cos(t), b + r*np.sin(t), color="tab:blue", alpha=0.25,
         label="Lake Bosomtwe (approx.), r = 4 km")

# Circle of Example 2.1: centre (-3/2, 3), radius 7/2
a, b, r = -1.5, 3, 3.5
plt.plot(a + r*np.cos(t), b + r*np.sin(t), "r", label="x²+y²+3x−6y−1=0")
plt.plot(a, b, "r+")

plt.gca().set_aspect("equal")
plt.grid(alpha=0.3)
plt.legend(loc="lower right", fontsize=8)
plt.show()

print(f"Area of a circular lake of radius 4 km: {np.pi*4**2:.1f} km^2")
