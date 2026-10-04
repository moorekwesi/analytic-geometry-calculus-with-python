# Listing 6.5: Integration by parts, checked with SymPy
import sympy as sp

x = sp.symbols("x", positive=True)

# Our answers by hand, using  ∫ u dv = u v - ∫ v du
hand_answers = {
    x*sp.exp(x):        (x - 1)*sp.exp(x),
    x*sp.cos(x):        x*sp.sin(x) + sp.cos(x),
    sp.log(x):          x*sp.log(x) - x,
    x**2*sp.exp(x):     (x**2 - 2*x + 2)*sp.exp(x),
    sp.exp(x)*sp.sin(x): sp.exp(x)*(sp.sin(x) - sp.cos(x))/2,
}
for f, F in hand_answers.items():
    ok = sp.simplify(sp.diff(F, x) - f) == 0
    print(f"∫ {str(f):<16} dx = {str(F):<32} + C   correct: {ok}")

# A definite integral by parts
print("∫_0^pi x sin x dx =", sp.integrate(x*sp.sin(x), (x, 0, sp.pi)))
