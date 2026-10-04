# Listing 2.1: Centre and radius from the general equation of a circle
import sympy as sp

def centre_radius(g2, f2, c):
    """For x^2 + y^2 + (2g)x + (2f)y + c = 0, given 2g, 2f and c."""
    g, f = sp.Rational(g2) / 2, sp.Rational(f2) / 2
    r2 = g**2 + f**2 - c
    if r2 < 0:
        return (-g, -f), None          # no real circle
    return (-g, -f), sp.sqrt(r2)

# Checking the worked example: x^2 + y^2 + 3x - 6y - 1 = 0
print(centre_radius(3, -6, -1))

# Exercise-style checks
for coeffs in [(6, -10, -9), (0, 4, 0), (2, 2, 10)]:
    centre, r = centre_radius(*coeffs)
    print(f"2g={coeffs[0]:>3}, 2f={coeffs[1]:>3}, c={coeffs[2]:>3}  ->  centre {centre}, radius {r}")

# SymPy can complete the square for us too
x, y = sp.symbols("x y")
expr = x**2 + y**2 + 3*x - 6*y - 1
print(sp.expand((x + sp.Rational(3, 2))**2 + (y - 3)**2 - sp.Rational(49, 4)) == expr)
