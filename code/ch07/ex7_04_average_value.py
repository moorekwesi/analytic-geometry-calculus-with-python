# Listing 7.4: Average value of a function - the average temperature of a day
# Illustrative model of the temperature in Tamale on a hot day (°C), t = hours after midnight:
#   T(t) = 30 + 6 sin(pi (t - 9) / 12)
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

t = sp.symbols("t", real=True)
T = 30 + 6*sp.sin(sp.pi*(t - 9)/12)

avg_day = sp.integrate(T, (t, 0, 24)) / 24
avg_work = sp.integrate(T, (t, 8, 18)) / (18 - 8)
print("average over the whole day       =", avg_day, "°C")
print("average from 8 am to 6 pm        ≈", round(float(avg_work), 2), "°C")

# Mean value theorem for integrals: T(c) equals the average at some time c
cs = sp.solve(sp.Eq(T, avg_work), t)
print("times when T equals the 8-6 average:", [round(float(c), 2) for c in cs if 8 <= c <= 18])

tt = np.linspace(0, 24, 300)
Tf = sp.lambdify(t, T)
plt.figure(figsize=(6, 3.2))
plt.plot(tt, Tf(tt), label="T(t)")
plt.axhline(float(avg_day), color="C1", ls="--", label="daily average")
plt.xlabel("hour of the day"); plt.ylabel("°C"); plt.grid(alpha=0.3); plt.legend()
plt.show()
