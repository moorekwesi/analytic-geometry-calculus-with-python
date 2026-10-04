# Listing 6.1: Indefinite integrals with sp.integrate (SymPy omits the + C)
import sympy as sp

x = sp.symbols("x", positive=True)
examples = [
    3*x**2, sp.cos(x), x**8, 1/x**3, sp.cbrt(x**2), sp.tan(x)/sp.sec(x),
    5*x**3 + 2*sp.cos(x), 8*x**3 - 6*sp.sqrt(x) + 1/x**3, (x**2 - 1)**2/x**2,
    1/(sp.cos(x)*sp.cot(x)),
]
for f in examples:
    F = sp.integrate(f, x)
    ok = sp.simplify(sp.diff(F, x) - f) == 0      # always check: F' = f
    print(f"∫ {str(f):<28} dx = {str(sp.simplify(F)):<34} check: {ok}")
