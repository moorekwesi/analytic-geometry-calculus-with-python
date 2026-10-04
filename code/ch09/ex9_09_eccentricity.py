# Listing 9.9: One equation for all conics: r = e d / (1 + e cos(theta))
import numpy as np
import matplotlib.pyplot as plt

d = 1.0                                      # distance from the focus to the directrix
theta = np.linspace(0, 2*np.pi, 2000)
plt.figure(figsize=(5.5, 4.5))
for e, style in [(0.5, "C0"), (0.8, "C2"), (1.0, "C3"), (1.5, "C1")]:
    r = e*d / (1 + e*np.cos(theta))
    r[(1 + e*np.cos(theta)) <= 0.02] = np.nan         # skip points at infinity
    plt.plot(r*np.cos(theta), r*np.sin(theta), style, label=f"e = {e}")
plt.axvline(d, color="k", ls="--", lw=1, label="directrix")
plt.plot(0, 0, "k*", ms=10, label="focus")
plt.xlim(-4, 1.5); plt.ylim(-3, 3); plt.gca().set_aspect("equal")
plt.grid(alpha=0.3); plt.legend(fontsize=8)
plt.show()
