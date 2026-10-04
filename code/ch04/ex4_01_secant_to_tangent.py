# Listing 4.1: Secant lines turning into the tangent line
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x**2
a = 1.0
x = np.linspace(-0.5, 3, 200)

plt.figure(figsize=(5.5, 4))
plt.plot(x, f(x), "k", lw=2, label="$y = x^2$")
for h, c in zip([1.5, 1.0, 0.5], ["C1", "C2", "C4"]):
    m = (f(a + h) - f(a)) / h                  # gradient of the secant
    plt.plot(x, f(a) + m*(x - a), c, lw=1, label=f"secant, h = {h}: m = {m:.2f}")
    plt.plot(a + h, f(a + h), "o", color=c)
plt.plot(x, f(a) + 2*(x - a), "C3--", lw=2, label="tangent: m = 2")
plt.plot(a, f(a), "ko")
plt.ylim(-1, 9); plt.grid(alpha=0.3); plt.legend(fontsize=8)
plt.show()

for h in [1, 0.1, 0.01, 0.001]:
    print(f"h = {h:<6} secant gradient = {(f(a + h) - f(a))/h:.4f}")
