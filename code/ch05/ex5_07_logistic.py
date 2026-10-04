# Listing 5.7: The inflection point of an S-shaped (logistic) adoption curve
# ILLUSTRATIVE model of active mobile-money accounts in a country (millions):
#   N(t) = 40 / (1 + e^(-0.6 (t - 8))),   t = years after 2010
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

t = sp.symbols("t", real=True)
N = 40 / (1 + sp.exp(-sp.Rational(3, 5)*(t - 8)))
N1, N2 = sp.diff(N, t), sp.diff(N, t, 2)
tp = sp.solve(sp.simplify(N2), t)
print("N''(t) = 0 at t =", tp, "-> year", 2010 + tp[0])
print("N at inflection =", N.subs(t, tp[0]), "million (half of 40)")
print("fastest growth N'(8) =", N1.subs(t, 8), "million per year")

T = np.linspace(0, 16, 300)
fig, ax = plt.subplots(1, 2, figsize=(9, 3))
ax[0].plot(2010 + T, sp.lambdify(t, N)(T)); ax[0].set_title("N(t)")
ax[1].plot(2010 + T, sp.lambdify(t, N1)(T), "C1"); ax[1].set_title("N'(t)")
for a in ax:
    a.axvline(2018, ls="--", color="gray"); a.grid(alpha=0.3)
plt.tight_layout(); plt.show()
