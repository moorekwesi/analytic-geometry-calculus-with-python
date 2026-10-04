# Listing 4.3: The rules of differentiation, checked with sp.diff
import sympy as sp

x = sp.symbols("x")
examples = {
    "x^5":                       x**5,
    "1/cbrt(x)":                 1/sp.cbrt(x),
    "x^7 + sqrt(x)":             x**7 + sp.sqrt(x),
    "3 sqrt(x) + 5x^2":          3*sp.sqrt(x) + 5*x**2,
    "(x^2+x-1)(2x+4)":           (x**2 + x - 1)*(2*x + 4),
    "(x^4+2x-1)/(3x^2+5)":       (x**4 + 2*x - 1)/(3*x**2 + 5),
    "x sin x - cos x":           x*sp.sin(x) - sp.cos(x),
    "(x^2+2)/(1+sin x)":         (x**2 + 2)/(1 + sp.sin(x)),
    "tan x/(1 + 2 sec x)":       sp.tan(x)/(1 + 2*sp.sec(x)),
}
for name, f in examples.items():
    d = sp.diff(f, x)
    print(f"d/dx[{name}] = {sp.simplify(d)}")
