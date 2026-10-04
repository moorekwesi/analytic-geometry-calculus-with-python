# Listing 5.5: The first derivative test for f(x) = x^(1/3) (8 - x)
import sympy as sp

x = sp.symbols("x", positive=True)       # differentiate where x > 0 ...
f = x**sp.Rational(1, 3) * (8 - x)
df = sp.factor(sp.diff(f, x))
print("f'(x) =", df)                     # ... the same formula holds for x < 0

def fprime(v):                           # real cube roots, valid for negative v too
    return (8 - 4*v) / (3 * sp.real_root(v, 3)**2)

print("f'(x) = 0 at x =", sp.solve(8 - 4*x, x), "; f'(x) undefined at x = 0")
for lo, hi, test in [("-oo", 0, -1), (0, 2, 1), (2, "oo", 3)]:
    s = fprime(test)
    print(f"on ({lo}, {hi}):  f'({test}) = {float(s):+.3f}  ->",
          "increasing" if s > 0 else "decreasing")
print("local maximum f(2) =", f.subs(x, 2), "≈", round(float(f.subs(x, 2)), 3))
