# Listing 7.8: Probability as area under a density curve
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Examination marks modelled by a normal density with mean 55, standard deviation 12
mu, sigma = 55, 12
pdf = lambda x: np.exp(-((x - mu)/sigma)**2 / 2) / (sigma*np.sqrt(2*np.pi))

total, _ = quad(pdf, -np.inf, np.inf)
print(f"total area under the density = {total:.6f}")
for lo, hi in [(40, 70), (70, 100), (0, 40)]:
    p, _ = quad(pdf, lo, hi)
    print(f"P({lo} <= mark <= {hi}) ≈ {p:.3f}")

X = np.linspace(10, 100, 300)
plt.figure(figsize=(6, 3.2))
plt.plot(X, pdf(X), "k")
Xs = np.linspace(70, 100, 100)
plt.fill_between(Xs, pdf(Xs), alpha=0.4, label="P(mark ≥ 70)")
plt.xlabel("mark"); plt.grid(alpha=0.3); plt.legend()
plt.show()
