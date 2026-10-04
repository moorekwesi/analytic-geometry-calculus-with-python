# Listing 0.5: Plotting with Matplotlib - comparing two fare plans
import numpy as np
import matplotlib.pyplot as plt

d = np.linspace(0, 30, 200)          # distance in km
plan_A = 6.0 + 2.5 * d               # higher per-km rate
plan_B = 12.0 + 2.0 * d              # higher base fare, cheaper per km

plt.figure(figsize=(6, 3.6))
plt.plot(d, plan_A, label="Plan A: 6 + 2.5d")
plt.plot(d, plan_B, "--", label="Plan B: 12 + 2.0d")
plt.plot(12, 36, "ko")               # the plans cost the same at d = 12 km
plt.annotate("equal cost at 12 km", (12, 36), (15, 25), arrowprops=dict(arrowstyle="->"))
plt.xlabel("distance d (km)")
plt.ylabel("fare (GH¢)")
plt.title("Two illustrative fare plans")
plt.grid(alpha=0.3)
plt.legend()
plt.show()
