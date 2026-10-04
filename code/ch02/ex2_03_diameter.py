# Listing 2.3: The circle on a given diameter - two methods
import sympy as sp

x, y = sp.symbols("x y")
A, B = (10, 2), (3, 8)

# Method 1: angle in a semicircle is 90 degrees -> (x-x1)(x-x2) + (y-y1)(y-y2) = 0
eq1 = sp.expand((x - A[0])*(x - B[0]) + (y - A[1])*(y - B[1]))
print("Method 1:", eq1, "= 0")

# Method 2: centre = midpoint, radius = half the diameter
C = sp.Point(A).midpoint(sp.Point(B))
r2 = C.distance(sp.Point(B))**2
eq2 = sp.expand((x - C.x)**2 + (y - C.y)**2 - r2)
print("Method 2:", eq2, "= 0   centre", C, " radius^2 =", r2)
print("Same circle?", sp.simplify(eq1 - eq2) == 0)
