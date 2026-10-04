# Listing 5.4: From trip data to a model - Bolt trips UCC -> Kotokuraba (illustrative data)
import numpy as np
import matplotlib.pyplot as plt

# departure time (hours after 6:00 am) and observed trip time (minutes)
dep = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
mins = np.array([14, 17, 22, 25, 26, 24, 21, 17, 15, 15, 17, 21])

coef = np.polyfit(dep, mins, 3)          # best-fitting cubic (least squares)
T = np.poly1d(coef)
dT = T.deriv()                           # derivative of the polynomial
print("model:  T(t) =", np.round(coef, 3))
crit = dT.roots
print("critical numbers:", np.round(crit, 3))
for c in crit:
    kind = "maximum" if T.deriv(2)(c) < 0 else "minimum"
    h = 6 + c
    print(f"local {kind} at about {int(h)}:{int(60*(h % 1)):02d}, T = {T(c):.1f} min")

tt = np.linspace(0, 8, 200)
plt.figure(figsize=(6, 3.4))
plt.plot(6 + dep, mins, "o", label="observed trips")
plt.plot(6 + tt, T(tt), label="cubic model")
plt.xlabel("departure time (hour of day)"); plt.ylabel("minutes")
plt.grid(alpha=0.3); plt.legend(); plt.show()
