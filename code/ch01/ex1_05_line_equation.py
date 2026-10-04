# Listing 1.5: Finding a fare formula (a straight line) from two trips
import sympy as sp

x, y = sp.symbols("x y")

def line_through(P, Q):
    """Return the line through P and Q in the form y = m x + c."""
    m = sp.Rational(Q[1] - P[1], Q[0] - P[0])
    return sp.Eq(y, sp.expand(m * (x - P[0]) + P[1]))

# Checking the worked example: line through (1, 3) with gradient 5
print(sp.Eq(y, sp.expand(5 * (x - 1) + 3)))

# Two trips with the same driver (distance km, fare GH¢), illustrative
trip1, trip2 = (4, 18), (10, 33)
L = line_through(trip1, trip2)
print("Fare line:", L)
m = L.rhs.coeff(x)
c = L.rhs.subs(x, 0)
print("per-km rate =", m, "  base fare =", c)
print("Predicted fare for a 15 km trip:", L.rhs.subs(x, 15))

# The same line in general form ax + by + c = 0 with integer coefficients
num, den = sp.fraction(sp.together(L.rhs - y))
print("General form:", sp.Eq(sp.expand(num), 0))
