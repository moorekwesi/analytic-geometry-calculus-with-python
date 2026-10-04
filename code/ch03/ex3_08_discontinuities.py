# Listing 3.8: Three ways a function can fail to be continuous
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 3, figsize=(9, 2.8))

# (a) a removable discontinuity (hole): (x^2 - 4)/(x - 2)
x = np.linspace(0, 4, 200); x = x[np.abs(x - 2) > 1e-9]
ax[0].plot(x, (x**2 - 4)/(x - 2)); ax[0].plot(2, 4, "o", mfc="white", mec="C0")
ax[0].set_title("(a) hole at x = 2")

# (b) a jump: f(x) = x for x < 1, x + 2 for x >= 1
x1 = np.linspace(-1, 1, 50, endpoint=False); x2 = np.linspace(1, 3, 50)
ax[1].plot(x1, x1, "C0"); ax[1].plot(x2, x2 + 2, "C0")
ax[1].plot(1, 1, "o", mfc="white", mec="C0"); ax[1].plot(1, 3, "o", color="C0")
ax[1].set_title("(b) jump at x = 1")

# (c) an infinite discontinuity (vertical asymptote): 1/(x - 1)^2
x = np.linspace(-1, 3, 400); x = x[np.abs(x - 1) > 0.08]
y = 1/(x - 1)**2
ax[2].plot(x[x < 1], y[x < 1], "C0"); ax[2].plot(x[x > 1], y[x > 1], "C0")
ax[2].axvline(1, ls="--", color="gray"); ax[2].set_ylim(0, 40)
ax[2].set_title("(c) asymptote at x = 1")

for a in ax:
    a.grid(alpha=0.3)
plt.tight_layout()
plt.show()
