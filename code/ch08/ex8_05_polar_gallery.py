# Listing 8.5: A gallery of polar curves r = f(theta)
import numpy as np
import matplotlib.pyplot as plt

th = np.linspace(0, 2*np.pi, 1000)
curves = {
    "r = 2":                  2 + 0*th,
    "r = 2 cos θ":            2*np.cos(th),
    "r = 1 + cos θ (cardioid)": 1 + np.cos(th),
    "r = cos 3θ (3 petals)":  np.cos(3*th),
    "r = cos 2θ (4 petals)":  np.cos(2*th),
    "r = θ/π (spiral)":       th/np.pi,
}
fig, ax = plt.subplots(2, 3, figsize=(9, 6), subplot_kw={"projection": "polar"})
for a, (name, r) in zip(ax.flat, curves.items()):
    a.plot(th, r)                    # matplotlib's polar axes accept negative r
    a.set_title(name, fontsize=9)
    a.set_yticklabels([])
plt.tight_layout(); plt.show()
