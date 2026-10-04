# Listing 1.9: Shortest feeder road from a village to a straight highway
import math
import matplotlib.pyplot as plt
import numpy as np

def point_line_distance(P, a, b, c):
    """Distance from P=(x1, y1) to the line ax + by + c = 0."""
    x1, y1 = P
    return abs(a*x1 + b*y1 + c) / math.sqrt(a**2 + b**2)

def foot_of_perpendicular(P, a, b, c):
    x1, y1 = P
    k = (a*x1 + b*y1 + c) / (a**2 + b**2)
    return (x1 - a*k, y1 - b*k)

# Checking the worked example: P(3, 2) and 12x + 5y - 11 = 0
print("Distance =", point_line_distance((3, 2), 12, 5, -11))

# Highway: 3x + 4y - 12 = 0 (km grid).  Village V(6, 8).
V = (6, 8)
d = point_line_distance(V, 3, 4, -12)
F = foot_of_perpendicular(V, 3, 4, -12)
print(f"Feeder road length = {d:.2f} km, meeting the highway at ({F[0]:.2f}, {F[1]:.2f})")

x = np.linspace(-2, 8, 50)
plt.figure(figsize=(5, 4.5))
plt.plot(x, (12 - 3*x)/4, "k", lw=3, label="highway 3x + 4y = 12")
plt.plot([V[0], F[0]], [V[1], F[1]], "g--o", label=f"feeder road, {d:.1f} km")
plt.annotate("village V", V, textcoords="offset points", xytext=(5, 5))
plt.gca().set_aspect("equal")
plt.grid(alpha=0.3)
plt.legend(loc="lower left")
plt.show()
