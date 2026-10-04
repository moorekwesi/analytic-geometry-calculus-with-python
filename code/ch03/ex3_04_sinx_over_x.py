# Listing 3.4: sin(x)/x near 0 - and why radians matter
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
x = x[x != 0]                              # avoid dividing by zero
plt.figure(figsize=(6, 3.2))
plt.plot(x, np.sin(x)/x, label="sin(x)/x")
plt.plot(0, 1, "o", mfc="white", mec="C0")   # the 'hole' at x = 0
plt.axhline(0, color="k", lw=0.5)
plt.grid(alpha=0.3); plt.legend()
plt.show()

# If x is measured in DEGREES the limit is not 1:
for d in [10, 1, 0.1, 0.01]:
    print(f"x = {d:>5} degrees:  sin(x)/x = {np.sin(np.radians(d))/d:.8f}")
print("pi/180 =", np.pi/180)
