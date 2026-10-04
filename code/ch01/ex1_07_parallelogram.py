# Listing 1.7: The parallelogram ABCD solved with SymPy
import sympy as sp

x, y, t = sp.symbols("x y t")
A = sp.Point(1, 2)
AB = sp.Line(sp.Point(-3, 0), sp.Point(1, 2))      # 2y = x + 3 passes through these
BD = sp.Line(sp.Point(17, 0), sp.Point(2, 5))      # 3y + x = 17 passes through these

B = AB.intersection(BD)[0]
print("B =", B)

# D is the point of BD (other than B) with |AD| = |BD|.
D_general = sp.Point(17 - 3*t, t)                 # every point of BD: x = 17 - 3y
sols = sp.solve(sp.Eq(A.distance(D_general)**2, B.distance(D_general)**2), t)
D = D_general.subs(t, sols[0])
print("D =", D)

M = B.midpoint(D)                                 # diagonals bisect each other
C = sp.Point(2*M.x - A.x, 2*M.y - A.y)
print("M =", M, "  C =", C)

mid_AB = A.midpoint(B)
perp = AB.perpendicular_line(mid_AB)
print("Perpendicular bisector of AB:", sp.expand(perp.equation(x, y)), "= 0")
