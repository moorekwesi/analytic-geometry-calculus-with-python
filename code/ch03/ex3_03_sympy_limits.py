# Listing 3.3: Checking the worked examples with sp.limit
import sympy as sp

x, t = sp.symbols("x t")
examples = [
    ("2x^2 + 1, x->1",                2*x**2 + 1,                      x, 1),
    ("(x^2-2x+1)/(3x-2), x->3",       (x**2 - 2*x + 1)/(3*x - 2),      x, 3),
    ("(x^2-16)/(x-4), x->4",          (x**2 - 16)/(x - 4),             x, 4),
    ("(sqrt(x+9)-3)/x, x->0",         (sp.sqrt(x + 9) - 3)/x,          x, 0),
    ("tan(x)/x, x->0",                sp.tan(x)/x,                     x, 0),
    ("sin(4x)/x, x->0",               sp.sin(4*x)/x,                   x, 0),
    ("(cos3x - cos x)/x^2, x->0",     (sp.cos(3*x) - sp.cos(x))/x**2,  x, 0),
    ("(1 - cos x)/x^2, x->0",         (1 - sp.cos(x))/x**2,            x, 0),
]
for name, expr, var, a in examples:
    print(f"{name:<28} = {sp.limit(expr, var, a)}")

# One-sided limits
expr = sp.Abs(x - 8)/(x - 8)
print("|x-8|/(x-8): left =", sp.limit(expr, x, 8, dir="-"), ", right =", sp.limit(expr, x, 8, dir="+"))
