# Listing 8.3: Calculus of parametric curves - the cycloid x = r(t - sin t), y = r(1 - cos t)
import sympy as sp

t = sp.symbols("t", real=True)
r = sp.symbols("r", positive=True)
x, y = r*(t - sp.sin(t)), r*(1 - sp.cos(t))

dydx = sp.simplify(sp.diff(y, t) / sp.diff(x, t))
print("dy/dx =", dydx)
print("slope at t = pi/2:", dydx.subs(t, sp.pi/2))
d2 = sp.simplify(sp.diff(dydx, t) / sp.diff(x, t))
print("d2y/dx2 =", d2)

# Tangent line at t = pi/2 when r = 1
P = (x.subs({t: sp.pi/2, r: 1}), y.subs({t: sp.pi/2, r: 1}))
X = sp.symbols("X")
print("tangent at t = pi/2 (r = 1): y =", sp.expand(P[1] + dydx.subs(t, sp.pi/2)*(X - P[0])))

# Arc length of one arch: ∫_0^{2 pi} sqrt(x'^2 + y'^2) dt
speed = sp.sqrt(sp.diff(x, t)**2 + sp.diff(y, t)**2)
speed = 2*r*sp.sin(t/2)          # simplification of speed, valid for 0 <= t <= 2 pi
print("check speed formula:", sp.simplify((sp.diff(x, t)**2 + sp.diff(y, t)**2) - speed**2))
print("length of one arch =", sp.integrate(speed, (t, 0, 2*sp.pi)))
