# Listing 0.6: SymPy - exact (symbolic) mathematics
import sympy as sp

x = sp.symbols("x")
f = x**2 - 4*x + 3

print("f(x)       =", f)
print("factorised =", sp.factor(f))
print("roots      =", sp.solve(f, x))
print("(x+1)^3    =", sp.expand((x + 1)**3))
print("f(5)       =", f.subs(x, 5))

# Exact arithmetic: no rounding errors
print(sp.Rational(1, 3) + sp.Rational(1, 6))
print(sp.sqrt(8))

# A preview of the calculus to come
print("limit of sin(x)/x as x->0:", sp.limit(sp.sin(x)/x, x, 0))
print("derivative of f:", sp.diff(f, x))
print("integral of f:", sp.integrate(f, x))
