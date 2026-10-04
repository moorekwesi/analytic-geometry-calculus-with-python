# Listing 5.2: Related rates - differentiate a relation with respect to time
import sympy as sp

t = sp.symbols("t")
r = sp.Function("r")(t)

# (a) Balloon: V = (4/3) pi r^3, dV/dt = 100 cm^3/s. Find dr/dt when r = 25 cm.
V = sp.Rational(4, 3)*sp.pi*r**3
dVdt = sp.diff(V, t)                                  # 4 pi r^2 dr/dt
drdt = sp.solve(sp.Eq(dVdt, 100), sp.diff(r, t))[0]
print("balloon: dr/dt =", sp.simplify(drdt.subs(r, 25)), "≈", float(drdt.subs(r, 25)), "cm/s")

# (b) An oil slick near an offshore field spreads in a circle. Its radius grows at
#     0.5 m/min. How fast is its AREA growing when the radius is 300 m?
A = sp.pi*r**2
dAdt = sp.diff(A, t).subs(sp.diff(r, t), sp.Rational(1, 2)).subs(r, 300)
print("oil slick: dA/dt =", dAdt, "≈", round(float(dAdt), 1), "m^2/min")
