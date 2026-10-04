"""
Verifies (with SymPy/SciPy) the answers printed in Appendix B.
Run:  python tools/check_answers.py
Each line prints a label and the computed value, to compare with the appendix.
"""
import numpy as np
import sympy as sp
from scipy.integrate import quad, simpson

x, y, t, r, h = sp.symbols("x y t r h", real=True)
S = sp.sqrt


def show(label, value):
    print(f"{label:<14} {value}")


# ---------------- Chapter 1 ----------------
A, B = sp.Point(-3, 5), sp.Point(5, -10)
show("1.1a", A.distance(B))
show("1.1b", A.midpoint(B))
show("1.1c", sp.Point((5*A.x + 2*B.x)/7, (5*A.y + 2*B.y)/7))
show("1.1d", sp.Point((1*A.x - 3*B.x)/(1 - 3), (1*A.y - 3*B.y)/(1 - 3)))
L = sp.Line(A, B)
show("1.1f", sp.expand(L.equation(x, y)))
show("1.1g", sp.expand(L.perpendicular_line(A.midpoint(B)).equation(x, y)))
show("1.1h", L.distance(sp.Point(2, 4)))
rr = sp.symbols("r", real=True)
show("1.2", sp.solve_univariate_inequality((3 - 2*rr - 4)/(1 - rr) < 5, rr))
show("1.7", sp.solve([3*x + 2*y - 2, 4*x + 3*y - 7], [x, y]))
mAB, mBC = sp.Rational(1, 2), sp.Rational(7, 4)
show("1.9a", sp.N(sp.deg(sp.atan(abs((mBC - mAB)/(1 + mAB*mBC)))), 6))
show("1.12", [sp.expand(13*(3*x + 4*y - 7) - s*5*(12*x - 5*y + 3)) for s in (1, -1)])
show("1.13", (sp.N(sp.Point(-1.2, 0.6).distance(sp.Point(4.1, -3.0)), 5), sp.Point(-1.2, 0.6).midpoint(sp.Point(4.1, -3.0))))
show("1.16", (sp.N(3/S(5)*100, 5), "m"))
show("1.17", sp.Point(sp.Rational(0 + 30 + 12, 3), sp.Rational(0 + 0 + 24, 3)))

# ---------------- Chapter 2 ----------------
show("2.6", sp.expand(2*y - 2*x + y + 2 - 8))
S1 = x**2 + y**2 - 2*x - 4*y
S2 = x**2 + y**2 + 4*x + 2*y - 20
chord = sp.expand(S1 - S2)
pts = sp.solve([S1, S2], [x, y])
show("2.13 chord", chord)
show("2.13 length", sp.nsimplify(sp.Point(*pts[0]).distance(sp.Point(*pts[1]))))
g, f, c = sp.symbols("g f c")
sol = sp.solve([P[0]**2 + P[1]**2 + 2*g*P[0] + 2*f*P[1] + c for P in [(0, 0), (40, 0), (10, 30)]], [g, f, c])
show("2.15", (sp.Point(-sol[g], -sol[f]), S(sol[g]**2 + sol[f]**2 - sol[c])))
d16 = 40/np.sqrt(1.25)
show("2.16", 2*np.sqrt(60**2 - d16**2))
show("2.17", (sp.N(sp.pi*400, 6), "m^2"))
show("2.18", sp.solve(sp.expand(((x-3)**2 + (y-4)**2 - 25) - ((x-10)**2 + (y-4)**2 - 16)), x))

# ---------------- Chapter 3 ----------------
lims = {
    "i": ((x**4 - 1)/(x - 1), 1), "ii": ((2 - sp.cos(3*x) - sp.cos(4*x))/x, 0),
    "iii": ((x - 8)/(sp.cbrt(x) - 2), 8), "iv": (x**2/(1 - sp.cos(x)**2), 0),
    "vi": ((1 - sp.cos(4*x))/(1 - sp.cos(6*x)), 0), "vii": ((S(2 + x) - S(2))/x, 0),
    "viii": (sp.sin(sp.sin(x))/x, 0), "x": ((1 - sp.cos(x))/x, 0),
    "xi": ((x**2 - 3*sp.sin(x))/x, 0), "xii": (sp.Abs(10 - 3*x**2), 4),
}
for k, (e, a) in lims.items():
    show(f"3.1({k})", sp.limit(e, x, a))
e = x*sp.Abs(x - 1)/(x - 1)
show("3.1(v)", (sp.limit(e, x, 1, "-"), sp.limit(e, x, 1, "+")))
e = (2*x**2 - 3*x)/sp.Abs(2*x - 3)
show("3.1(ix)", (sp.limit(e, x, sp.Rational(3, 2), "-"), sp.limit(e, x, sp.Rational(3, 2), "+")))
show("3.6", sp.limit((S(12 - x) - x)/(S(6 + x) - 3), x, 3))
show("3.7", sp.limit((1 + sp.cos(2*x))/(sp.pi - 2*x)**2, x, sp.pi/2))
a, b = sp.symbols("a b")
show("3.8", sp.solve([4*a - 2*b + 3 - 4, 9*a - 3*b + 3 - (6 - a + b)], [a, b]))
show("3.9", (sp.limit((5*x**3 - x)/(2*x**3 + 4*x**2 + 1), x, sp.oo),
             sp.limit((4*x + 1)/(x**2 + 3), x, sp.oo), sp.limit((1 + 2/x)**x, x, sp.oo)))
show("3.12", (sp.diff(0.02*t**2 + 0.3*t, t).subs(t, 10), "km/min"))
rg = np.log(30.832019/24.658823)/11
show("3.14", (rg, rg*24.658823*np.exp(11*rg)))
show("3.15", 5000*(np.exp(0.1) - (1 + 0.1/12)**12))

# ---------------- Chapter 4 ----------------
X = sp.symbols("X", positive=True)
show("4.3(iv)", sp.simplify(sp.diff(sp.log((3*X**2 + 2)**5, 10), X)))
show("4.3(v)", sp.simplify(sp.diff(sp.log(sp.sec(X) + sp.tan(X)), X)))
show("4.3(x)", sp.simplify(sp.diff(X**sp.log(X), X)))
show("4.8a", sp.simplify(sp.diff(sp.cos(sp.log(X)), X, 2)))
show("4.8b", sp.simplify(sp.diff(X**X, X, 2)))
show("4.10", sp.simplify(sp.diff(1/(X + 1), X)))
n = sp.symbols("n", positive=True)
Yp = sp.diff(2.5*sp.log(1 + 0.4*n), n)
show("4.12", (Yp.subs(n, 5), Yp.subs(n, 20)))
Tp = sp.diff(27 + 63*sp.exp(-0.08*t), t)
show("4.13", (Tp.subs(t, 0), sp.N(Tp.subs(t, 20), 4)))
s = t**3 - 12*t**2 + 45*t
show("4.14", (sp.factor(sp.diff(s, t)), sp.diff(s, t, 2)))
rates = np.array([15.10, 15.18, 15.31, 15.35, 15.52])
show("4.15", np.gradient(rates)[1:4])

# ---------------- Chapter 5 ----------------
F = x**3 - x*sp.log(y) + y**3 - 2*x - 5
show("5.1 y'", sp.idiff(F, y, x).subs({x: 2, y: 1}))
show("5.2 f'(e)", sp.diff(x*sp.log(sp.E/x), x).subs(x, sp.E))
show("5.4 b", sp.nsimplify(8*S(3) + 2*S(3)/12))
a_ = sp.symbols("a")
fa = a_**3 + a_**2 - 9*a_ - 9
show("5.5", [(s_, fa.subs(a_, s_)) for s_ in sp.solve(fa + sp.diff(fa, a_)*(4 - a_) + 1, a_)])
ga = a_**5 + 4*a_ - 3
show("5.6", [(s_, ga.subs(a_, s_)) for s_ in sp.solve(ga + sp.diff(ga, a_)*(0 - a_) - 1, a_) if s_.is_real])
show("5.7", sp.Rational(8, 27) - sp.Rational(1, 3)*sp.Rational(8, 27))
hh = sp.symbols("hh", positive=True)
show("5.10", sp.N(sp.Rational(3, 10)*25/(4*sp.pi*1**2), 4))
show("5.11", sp.N(sp.Rational(283, 100)/(9*sp.pi), 4))
tt = 10
D = np.hypot(1800, 2400)
show("5.13", 2400/D*(400 - 32*tt))
yy = x*sp.exp(x) - sp.exp(x) - 2*x**2
show("5.14", [(c_, sp.N(yy.subs(x, c_), 5)) for c_ in sp.solve(sp.diff(yy, x), x)])
show("5.15", sp.N((sp.Rational(3, 2))**sp.Rational(3, 5)*sp.Rational(5, 2), 5))
f17b = (2*x + 5)/(x**2 - 4)**2
cands = [-5, -3] + [c_ for c_ in sp.solve(sp.diff(f17b, x), x) if c_.is_real and -5 <= c_ <= -3]
show("5.17b", [(c_, sp.N(f17b.subs(x, c_), 5)) for c_ in cands])
V = x*(20 - 2*x)*(12 - 2*x)
xc = min(sp.solve(sp.diff(V, x), x), key=lambda v: abs(v - 2.4))
show("5.21", (sp.N(xc, 5), sp.N(20 - 2*xc, 5), sp.N(12 - 2*xc, 5), sp.N(V.subs(x, xc), 5)))
show("5.23", (sp.N(2*336/(4 + sp.pi), 5), sp.N((336 - (2 + sp.pi)*336/(4 + sp.pi))/2, 5),
              sp.N((336 - (2 + sp.pi)*42)/2, 5)))
show("5.25", (sp.Rational(28, 3), S(sp.Rational(28, 3)*(14 - sp.Rational(28, 3)))))
show("5.26", (np.sqrt(300), 2*np.sqrt(300), 4*np.sqrt(300)))
show("5.28", np.sqrt(7.2))

# ---------------- Chapter 6 ----------------
show("6.5", [sp.integrate(e_, X) for e_ in [X*(X**2 + 4)**10, X/S(1 - X**2), (sp.log(X))**3/X,
                                              sp.exp(X)/(1 + sp.exp(X)), sp.cos(S(X))/S(X)]])
show("6.6", [sp.integrate(x**2 - 2*x, (x, 0, 3)), sp.integrate(sp.cos(x), (x, 0, sp.pi/2)),
             sp.integrate(1/x, (x, 1, sp.E)), sp.integrate(x*sp.exp(x**2), (x, 0, 1)),
             sp.integrate(x/S(x**2 + 9), (x, 0, 4))])
show("6.9", [sp.factor(sp.integrate(X*sp.exp(2*X), X)), sp.integrate(X*sp.sin(X), X),
             sp.integrate(X**2*sp.log(X), X), sp.integrate(X*sp.exp(-X), (X, 0, 1))])
f610 = lambda s: np.exp(-s**2)
xs4 = np.linspace(0, 1, 5)
show("6.10", (np.trapz(f610(xs4), xs4), simpson(f610(xs4), x=xs4)))
v611 = sp.integrate(6 - sp.Rational(6, 5)*t, (t, 0, t))
show("6.11", (v611, sp.integrate(v611, (t, 0, t))))
q = sp.symbols("q")
show("6.12", 500 + sp.integrate(12 - sp.Rational(1, 50)*q, (q, 0, q)))

# ---------------- Chapter 7 ----------------
show("7.1", [sp.integrate(x + 2 - x**2, (x, -1, 2)), sp.integrate(sp.sin(x), (x, 0, sp.pi)),
             2*sp.integrate(x - x**3, (x, 0, 1))])
show("7.2", (sp.integrate(3*x**2 - 2*x, (x, 1, 4))/3, sp.integrate(sp.sin(x), (x, 0, sp.pi))/sp.pi))
show("7.3", [sp.integrate(sp.pi*x, (x, 0, 4)), sp.integrate(sp.pi*sp.exp(2*x), (x, 0, 1)),
             sp.integrate(sp.pi*(x**2 - x**4), (x, 0, 1))])
L5a = sp.integrate(S(1 + sp.Rational(9, 4)*X), (X, 0, 4))
y5b = X**3/6 + 1/(2*X)
L5b = sp.integrate(sp.simplify(S(sp.factor(1 + sp.diff(y5b, X)**2))), (X, 1, 2))
show("7.5", (sp.nsimplify(L5a), sp.N(L5a, 5), sp.nsimplify(L5b)))
v = 3*t**2 - 12*t + 9
show("7.6", (sp.integrate(v, (t, 0, 4)), sp.integrate(sp.Abs(v), (t, 0, 4))))
show("7.7", sp.integrate(200 + 50*sp.sin(sp.pi*t/6), (t, 0, 12)))
show("7.8", sp.integrate(12 - 0.02*q, (q, 100, 300)))
w = np.array([0, 9.5, 12.0, 13.4, 14.0, 13.1, 11.2, 7.8, 0])
xs = np.arange(0, 33, 4)
show("7.9", (np.trapz(w, xs), simpson(w, x=xs)))
show("7.10", quad(lambda s: 1200*s*np.exp(-0.5*s), 0, 8)[0])
Vb = sp.integrate(sp.pi*8*y, (y, 0, 8))
show("7.11", (Vb, sp.N(Vb, 5), "cm^3"))
pdf = lambda s: np.exp(-((s - 55)/12)**2/2)/(12*np.sqrt(2*np.pi))
show("7.12", quad(pdf, 50, 60)[0])

# ---------------- Chapter 8 ----------------
tt = sp.symbols("tt", real=True)
xp, yp = tt**2 + 1, tt**3 - 3*tt
d1 = sp.simplify(sp.diff(yp, tt)/sp.diff(xp, tt))
show("8.2", (d1, sp.simplify(sp.diff(d1, tt)/sp.diff(xp, tt))))
xe, ye = 2*sp.cos(tt), 3*sp.sin(tt)
m3 = (sp.diff(ye, tt)/sp.diff(xe, tt)).subs(tt, sp.pi/4)
show("8.3", sp.expand(ye.subs(tt, sp.pi/4) + m3*(x - xe.subs(tt, sp.pi/4))))
show("8.4", sp.integrate(2*tt*S(1 + tt**2), (tt, 0, S(3))))
th = sp.symbols("theta", real=True)
show("8.9", [sp.integrate((4*sp.cos(th))**2/2, (th, -sp.pi/2, sp.pi/2)),
             sp.integrate(sp.sin(3*th)**2/2, (th, 0, sp.pi/3)),
             sp.integrate((2 - 2*sp.cos(th))**2/2, (th, 0, 2*sp.pi))])
r10 = 2*sp.sin(th); r10p = sp.diff(r10, th)
show("8.10", sp.simplify(((r10p*sp.sin(th) + r10*sp.cos(th))/(r10p*sp.cos(th) - r10*sp.sin(th))).subs(th, sp.pi/6)))
g_, v_ = 9.8, 20
al = np.radians(35)
show("8.11", (2*v_*np.sin(al)/g_, v_**2*np.sin(2*al)/g_, (v_*np.sin(al))**2/(2*g_)))
from scipy.optimize import brentq
hgt = lambda a: 15*np.tan(a) - g_*15**2/(2*18**2*np.cos(a)**2) - 2
show("8.12", np.degrees(brentq(hgt, np.radians(5), np.radians(40))))
P1 = 12*np.array([np.cos(np.radians(45)), np.sin(np.radians(45))])
P2 = 8*np.array([np.cos(np.radians(150)), np.sin(np.radians(150))])
show("8.13", np.linalg.norm(P1 - P2))
show("8.14", sp.integrate((4 + 2*sp.cos(th))**2/2, (th, 0, 2*sp.pi)))

# ---------------- Chapter 9 ----------------
show("9.2c", sp.expand(2*((x - 1)**2 + (y - 1)**2) - (x + y)**2))
show("9.9", 30**2/(4*8))
k = 6/15**2
show("9.10", np.sqrt((6 - 2)/k) - 1.5)
aa, bb = 60, 40
show("9.11", (np.sqrt(aa**2 - bb**2)/aa, 2*np.sqrt(aa**2 - bb**2),
              quad(lambda s: np.hypot(aa*np.sin(s), bb*np.cos(s)), 0, 2*np.pi)[0]))
show("9.12", (300000*200e-6/2, 50**2 - (300000*200e-6/2)**2))
