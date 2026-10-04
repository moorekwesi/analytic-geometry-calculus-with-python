# Listing 4.6: Derivatives of exponential and logarithmic functions
import sympy as sp

x = sp.symbols("x", positive=True)
examples = {
    "e^(x^2)":                    sp.exp(x**2),
    "e^x sin 2x + e^(cos x)":     sp.exp(x)*sp.sin(2*x) + sp.exp(sp.cos(x)),
    "ln(sin x)":                  sp.log(sp.sin(x)),
    "sin(x^2+1) ln x + ln(4x^3+3)": sp.sin(x**2 + 1)*sp.log(x) + sp.log(4*x**3 + 3),
    "4^x":                        4**x,
    "6^(sin x)":                  6**sp.sin(x),
    "log_4 x":                    sp.log(x, 4),
    "x^(sin x)":                  x**sp.sin(x),
}
for name, f in examples.items():
    print(f"d/dx[{name}] = {sp.diff(f, x)}")
