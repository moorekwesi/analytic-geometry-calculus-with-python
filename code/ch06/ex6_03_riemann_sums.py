# Listing 6.3: Riemann sums for the area under y = x^2 on [0, 1]
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x**2
a, b = 0, 1

def riemann(f, a, b, n, rule="left"):
    dx = (b - a) / n
    left = a + dx*np.arange(n)                 # left endpoints x_0 ... x_{n-1}
    pts = {"left": left, "right": left + dx, "mid": left + dx/2}[rule]
    return np.sum(f(pts)) * dx

print(f"{'n':>6} {'left':>10} {'right':>10} {'midpoint':>10}")
for n in [4, 10, 100, 1000, 10000]:
    print(f"{n:>6} {riemann(f, a, b, n):>10.6f} {riemann(f, a, b, n, 'right'):>10.6f}"
          f" {riemann(f, a, b, n, 'mid'):>10.6f}")
print("exact area = 1/3 =", 1/3)

# Picture of the right-endpoint rectangles for n = 8
n = 8; dx = (b - a)/n; xr = a + dx*np.arange(1, n + 1)
X = np.linspace(a, b, 200)
plt.figure(figsize=(5, 3.4))
plt.bar(xr - dx, f(xr), width=dx, align="edge", alpha=0.35, edgecolor="k", label="right sums, n = 8")
plt.plot(X, f(X), "C3", lw=2, label="$y = x^2$")
plt.legend(); plt.grid(alpha=0.3); plt.show()
