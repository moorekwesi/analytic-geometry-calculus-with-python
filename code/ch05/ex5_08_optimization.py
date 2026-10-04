# Listing 5.8: Three optimisation problems solved with SymPy
import sympy as sp

x, r, p = sp.symbols("x r p", positive=True)

# (a) Farm beside the Pra River: 2400 m of fencing, no fence along the river.
A = x*(2400 - 2*x)
xs = sp.solve(sp.diff(A, x), x)[0]
print(f"(a) x = {xs} m, y = {2400 - 2*xs} m, area = {A.subs(x, xs)} m^2")

# (b) A closed tin can holding 400 cm^3 using the least metal.
h = 400 / (sp.pi*r**2)                        # from the volume constraint
S = 2*sp.pi*r**2 + 2*sp.pi*r*h                # surface area
rs = sp.solve(sp.diff(S, r), r)[0]
print(f"(b) r = {float(rs):.3f} cm, h = {float(h.subs(r, rs)):.3f} cm,"
      f" h/r = {sp.simplify(h.subs(r, rs)/rs)}, S = {float(S.subs(r, rs)):.1f} cm^2")

# (c) A waakye seller sells q = 400 - 10p plates a day at price p (GH¢). Max revenue?
R = p*(400 - 10*p)
ps = sp.solve(sp.diff(R, p), p)[0]
print(f"(c) price p = GH¢ {ps}, plates sold = {400 - 10*ps}, revenue = GH¢ {R.subs(p, ps)}")
