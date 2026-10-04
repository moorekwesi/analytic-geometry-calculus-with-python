# Listing 1.10: Bisectors of the angles between two lines (with SymPy)
import sympy as sp

x, y = sp.symbols("x y")
L1 = x + y + 2
L2 = x + 7*y + 26

# A point on a bisector is equally far from both lines:
#     L1 / sqrt(1**2 + 1**2) = +/- L2 / sqrt(1**2 + 7**2)
for sign in (+1, -1):
    eq = sp.expand(L1 / sp.sqrt(2) - sign * L2 / sp.sqrt(50))
    eq = sp.expand(eq * 5 * sp.sqrt(2))      # clear the surds
    print("Bisector:", eq, "= 0   i.e.", sp.factor_terms(eq), "= 0")

# Borehole problem: two straight roads y = 0 and 4x - 3y = 0 meet at a junction O.
# The borehole must be equidistant from both roads, inside the angle between them
# (x > 0, y > 0), and 5 km from the junction.
bisector = sp.Eq(y, (4*x - 3*y) / 5)         # distances y and (4x-3y)/5 are equal
sol = sp.solve([bisector, sp.Eq(x**2 + y**2, 25)], [x, y], dict=True)
for s in sol:
    if s[x] > 0:
        print("Borehole at", (s[x], s[y]),
              "~", (round(float(s[x]), 3), round(float(s[y]), 3)))
