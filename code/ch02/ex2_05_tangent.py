# Listing 2.5: Tangent and normal to a circle at a point
import sympy as sp

x, y = sp.symbols("x y")
S = x**2 + y**2 - 4*x + 2*y            # circle x^2 + y^2 - 4x + 2y = 0
P = (0, 0)
print("P on circle?", S.subs({x: P[0], y: P[1]}) == 0)

# The normal at P passes through the centre (-g, -f) = (2, -1)
centre = (2, -1)
m_radius = sp.Rational(centre[1] - P[1], centre[0] - P[0])
m_tangent = -1 / m_radius
tangent = sp.expand(y - P[1] - m_tangent*(x - P[0]))
normal = sp.expand(y - P[1] - m_radius*(x - P[0]))
print("gradient of radius =", m_radius, ",  gradient of tangent =", m_tangent)
print("tangent:", tangent, "= 0")
print("normal :", normal, "= 0")

# The 'replace one x by x1' rule: x x1 + y y1 + g(x + x1) + f(y + y1) + c = 0
g, f, c = -2, 1, 0
rule = sp.expand(x*P[0] + y*P[1] + g*(x + P[0]) + f*(y + P[1]) + c)
print("by the rule:", rule, "= 0")
