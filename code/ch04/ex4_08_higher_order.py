# Listing 4.8: Position, velocity and acceleration of a car (higher derivatives)
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

t = sp.symbols("t")
s = sp.Rational(6, 5)*t**2 - sp.Rational(1, 25)*t**3     # metres, 0 <= t <= 20 s
v = sp.diff(s, t)
a = sp.diff(s, t, 2)
print("s(t) =", s, "\nv(t) =", v, "\na(t) =", a)
t_max = sp.solve(a, t)[0]
print("maximum speed at t =", t_max, "s:  v =", v.subs(t, t_max), "m/s =",
      float(v.subs(t, t_max))*3.6, "km/h")

T = np.linspace(0, 20, 200)
funcs = [sp.lambdify(t, e) for e in (s, v, a)]
fig, ax = plt.subplots(1, 3, figsize=(9, 2.6))
for axis, f, name in zip(ax, funcs, ["s (m)", "v (m/s)", "a (m/s²)"]):
    axis.plot(T, f(T) * np.ones_like(T)); axis.set_title(name); axis.set_xlabel("t (s)")
    axis.grid(alpha=0.3)
plt.tight_layout(); plt.show()
