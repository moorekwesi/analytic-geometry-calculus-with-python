# Listing 5.11: L'Hôpital's rule checked with SymPy
import sympy as sp

x = sp.symbols("x")
cases = [
    ((sp.exp(x) - 1 - x), x**2, 0),
    (sp.log(x), x - 1, 1),
    (x - sp.sin(x), x**3, 0),
    (sp.log(x), x, sp.oo),
    (x**2, sp.exp(x), sp.oo),
]
for f, g, a in cases:
    ratio_of_derivs = sp.diff(f, x) / sp.diff(g, x)
    print(f"lim {str(f/g):<22} x->{str(a):<3} = {str(sp.limit(f/g, x, a)):<4}"
          f"  (f'/g' -> {sp.limit(ratio_of_derivs, x, a)})")
