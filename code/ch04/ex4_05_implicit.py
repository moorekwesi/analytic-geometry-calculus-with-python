# Listing 4.5: Implicit differentiation with sp.idiff
import sympy as sp

x, y = sp.symbols("x y")

# Worked examples
print("x y^2 + 6y + x = 0   : dy/dx =", sp.simplify(sp.idiff(x*y**2 + 6*y + x, y, x)))
print("cos(xy) + sin x = 1  : dy/dx =", sp.simplify(sp.idiff(sp.cos(x*y) + sp.sin(x) - 1, y, x)))

# The circle x^2 + y^2 = 25: slope of the tangent at (3, 4)
dydx = sp.idiff(x**2 + y**2 - 25, y, x)
print("x^2 + y^2 = 25       : dy/dx =", dydx, "; at (3, 4) it is", dydx.subs({x: 3, y: 4}))

# Second derivative of x^2 + y^2 = 1  (compare the worked example y^3 y'' + 1 = 0)
d2 = sp.idiff(x**2 + y**2 - 1, y, x, 2)
print("x^2 + y^2 = 1        : y'' =", sp.simplify(d2), "-> y^3 y'' =", sp.simplify((y**3*d2).subs(x**2, 1 - y**2)))
