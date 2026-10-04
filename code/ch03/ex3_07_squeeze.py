# Listing 3.7: The squeeze (sandwich) theorem: -x^2 <= x^2 sin(1/x) <= x^2
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-0.4, 0.4, 4001)
x = x[x != 0]
plt.figure(figsize=(5.5, 3.4))
plt.plot(x, x**2, "k--", lw=1, label="$x^2$")
plt.plot(x, -x**2, "k--", lw=1, label="$-x^2$")
plt.plot(x, x**2*np.sin(1/x), "C3", lw=0.8, label="$x^2\\sin(1/x)$")
plt.legend(); plt.grid(alpha=0.3)
plt.show()

for h in [0.1, 0.01, 0.001]:
    print(f"x = {h}:  x^2 sin(1/x) = {h**2*np.sin(1/h):+.2e}  (between ±{h**2:.0e})")
