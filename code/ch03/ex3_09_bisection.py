# Listing 3.9: The Intermediate Value Theorem at work - the bisection method
def bisection(f, a, b, tol=1e-6):
    """Find a root of a continuous f on [a, b], where f(a) and f(b) differ in sign."""
    if f(a) * f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    steps = 0
    while b - a > tol:
        m = (a + b) / 2
        if f(a) * f(m) <= 0:      # sign change in the left half
            b = m
        else:                      # sign change in the right half
            a = m
        steps += 1
    return (a + b) / 2, steps

f = lambda x: x**3 - x - 2
root, n = bisection(f, 1, 2)
print(f"root of x^3 - x - 2 = 0: {root:.6f}  ({n} halvings)")

# A kenkey seller's daily profit (GH¢) when she makes x hundred balls (illustrative):
#   P(x) = -4x^3 + 30x^2 - 20x - 15.  When does she first break even (P = 0)?
P = lambda x: -4*x**3 + 30*x**2 - 20*x - 15
print("P(0) =", P(0), ", P(2) =", P(2))
root, n = bisection(P, 0, 2)
print(f"break-even at about {100*root:.0f} balls")
