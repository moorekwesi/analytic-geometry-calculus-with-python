# Listing 4.2: Differentiation from first principles with SymPy
import sympy as sp

x, h = sp.symbols("x h")

def derivative_from_definition(f):
    return sp.simplify(sp.limit((f.subs(x, x + h) - f) / h, h, 0))

for f in [4*x - 2, 1/x**2, sp.sqrt(x), x**3, sp.sin(x), 4*x/(x + 1)]:
    print(f"f(x) = {str(f):<12}  f'(x) = {derivative_from_definition(f)}")

# Not differentiable: |x| at 0. The one-sided limits of the difference quotient differ.
q = sp.Abs(h) / h
print("|x| at 0: left limit =", sp.limit(q, h, 0, "-"), ", right limit =", sp.limit(q, h, 0, "+"))
