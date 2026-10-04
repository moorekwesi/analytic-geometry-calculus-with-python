# Listing 2.4: The circle through three points - a linear system for g, f, c
import numpy as np
import sympy as sp

def circle_through(P1, P2, P3):
    """Solve x^2+y^2+2gx+2fy+c=0 through three points. Returns (g, f, c)."""
    M, rhs = [], []
    for (x, y) in (P1, P2, P3):
        M.append([2*x, 2*y, 1])          # unknowns g, f, c
        rhs.append(-(x**2 + y**2))
    return np.linalg.solve(np.array(M, float), np.array(rhs, float))

# Checking the worked example: (2,1), (0,2), (1,0)
g, f, c = circle_through((2, 1), (0, 2), (1, 0))
print(f"g = {g:.4f}, f = {f:.4f}, c = {c:.4f}")

# The same, exactly, with SymPy
G, F, Cc, x, y = sp.symbols("g f c x y")
circle = x**2 + y**2 + 2*G*x + 2*F*y + Cc
sol = sp.solve([circle.subs({x: px, y: py}) for px, py in [(2, 1), (0, 2), (1, 0)]], [G, F, Cc])
print("Exact:", sol, " ->", sp.expand(3*circle.subs(sol)), "= 0")

# A telecom mast equidistant from three towns A(0,0), B(10,2), C(4,8)  (km)
g, f, c = circle_through((0, 0), (10, 2), (4, 8))
centre = (-g, -f)
radius = np.sqrt(g**2 + f**2 - c)
print(f"Mast at ({centre[0]:.3f}, {centre[1]:.3f}); each town is {radius:.3f} km away")
