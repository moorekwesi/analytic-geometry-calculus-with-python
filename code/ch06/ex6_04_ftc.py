# Listing 6.4: Definite integrals and the Fundamental Theorem of Calculus
import sympy as sp

x, t = sp.symbols("x t")
print("∫_1^2 x dx                =", sp.integrate(x, (x, 1, 2)))
print("∫_2^10 3/sqrt(5x-1) dx    =", sp.integrate(3/sp.sqrt(5*x - 1), (x, 2, 10)))
print("∫_0^pi sin x dx           =", sp.integrate(sp.sin(x), (x, 0, sp.pi)))
print("∫_0^2pi sin x dx          =", sp.integrate(sp.sin(x), (x, 0, 2*sp.pi)), " (signed area!)")

# FTC part 1: d/dx of ∫_0^x f(t) dt is f(x)
G = sp.integrate(t**3 + 1, (t, 0, x))
print("G(x) = ∫_0^x (t^3 + 1) dt =", G, ";  G'(x) =", sp.diff(G, x))

# Archimedes: the parabolic segment cut from y = x^2 by y = 1 has area 4/3 of
# the triangle with the same base and vertex.
segment = sp.integrate(1 - x**2, (x, -1, 1))
triangle = sp.Rational(1, 2) * 2 * 1
print("segment =", segment, ", triangle =", triangle, ", ratio =", segment/triangle)
