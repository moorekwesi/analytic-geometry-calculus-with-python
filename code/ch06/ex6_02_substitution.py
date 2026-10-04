# Listing 6.2: Integration by substitution, checked by differentiating
import sympy as sp

x = sp.symbols("x", positive=True)
hand_answers = {                                   # integrand: our answer by hand
    sp.sqrt(5*x + 7):                 sp.Rational(2, 15)*(5*x + 7)**sp.Rational(3, 2),
    (x**2 - 1)/(x**3 - 3*x + 1)**6:   -1/(15*(x**3 - 3*x + 1)**5),
    sp.cos(5*x)**3*sp.sin(5*x):       -sp.cos(5*x)**4/20,
    sp.exp(sp.sqrt(x))/sp.sqrt(x):    2*sp.exp(sp.sqrt(x)),
    sp.log(x)/x:                      sp.log(x)**2/2,
    sp.cos(4*x):                      sp.sin(4*x)/4,
    (2*x**3 + 1)**7*x**2:             (2*x**3 + 1)**8/48,
}
for f, F in hand_answers.items():
    ok = sp.simplify(sp.diff(F, x) - f) == 0
    print(f"∫ {str(f):<32} dx = {str(F):<30} + C   correct: {ok}")
