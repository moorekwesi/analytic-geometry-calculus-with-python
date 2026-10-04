# Listing 5.3: When is the quickest (and slowest) time to take a Bolt across Accra?
# HYPOTHETICAL model of the trip time from Madina to Accra Central:
#   T(t) = 0.4 t^3 - 5.4 t^2 + 16.8 t + 35  minutes,
#   t = hours after 6:00 am, 0 <= t <= 9 (i.e. 6:00 am to 3:00 pm)
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

t = sp.symbols("t")
T = sp.Rational(2, 5)*t**3 - sp.Rational(27, 5)*t**2 + sp.Rational(84, 5)*t + 35
dT = sp.factor(sp.diff(T, t))
print("T'(t) =", dT)
crit = sp.solve(sp.diff(T, t), t)
print("critical numbers:", crit)

def clock(h):
    hh = 6 + int(h); mm = round(60*(h - int(h)))
    return f"{hh % 12 or 12}:{mm:02d} {'am' if hh < 12 else 'pm'}"

candidates = [0] + crit + [9]          # closed interval method
for c in candidates:
    print(f"t = {c} ({clock(float(c)):>8}):  T = {float(T.subs(t, c)):.1f} min")
best = min(candidates, key=lambda c: T.subs(t, c))
worst = max(candidates, key=lambda c: T.subs(t, c))
print("quickest trip at", clock(float(best)), "; slowest at", clock(float(worst)))

tt = np.linspace(0, 9, 300)
Tf = sp.lambdify(t, T)
plt.figure(figsize=(6, 3.4))
plt.plot(6 + tt, Tf(tt))
for c in candidates:
    plt.plot(6 + float(c), float(T.subs(t, c)), "o")
plt.xlabel("departure time (hour of day)"); plt.ylabel("trip time T (min)")
plt.grid(alpha=0.3); plt.show()
