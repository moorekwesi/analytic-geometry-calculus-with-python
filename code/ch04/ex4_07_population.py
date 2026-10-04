# Listing 4.7: How fast is Ghana's population growing?
import numpy as np
import matplotlib.pyplot as plt

# Population and Housing Census totals (millions)
P2010, P2021 = 24.658823, 30.832019
r = np.log(P2021 / P2010) / 11          # from P2021 = P2010 * e^(11 r)
print(f"growth rate r = {r:.5f} per year  ({100*r:.2f}% per year)")

P = lambda t: P2010 * np.exp(r*t)       # t = years after 2010
dP = lambda t: r * P(t)                 # derivative of a e^(rt) is r a e^(rt)
for year in [2010, 2021, 2026]:
    t = year - 2010
    print(f"{year}: P = {P(t):6.2f} million,  P'(t) = {1e6*dP(t):,.0f} people per year")

t = np.linspace(0, 20, 100)
plt.figure(figsize=(5.5, 3.4))
plt.plot(2010 + t, P(t), label="model $P(t)=24.66\\,e^{rt}$")
plt.plot([2010, 2021], [P2010, P2021], "ro", label="census")
t0 = 11
plt.plot(2010 + t, P(t0) + dP(t0)*(t - t0), "k--", lw=1, label="tangent at 2021")
plt.xlabel("year"); plt.ylabel("millions"); plt.grid(alpha=0.3); plt.legend()
plt.show()
