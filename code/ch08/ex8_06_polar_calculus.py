# Listing 8.6: Slopes and areas in polar coordinates
import sympy as sp

th = sp.symbols("theta", real=True)
a = sp.symbols("a", positive=True)

# Slope of r = f(theta):  dy/dx = (r' sin + r cos) / (r' cos - r sin)
r = 1 + sp.cos(th)                                  # cardioid
rp = sp.diff(r, th)
slope = sp.simplify((rp*sp.sin(th) + r*sp.cos(th)) / (rp*sp.cos(th) - r*sp.sin(th)))
print("cardioid slope at theta = pi/2:", slope.subs(th, sp.pi/2))

# Area A = (1/2) ∫ r^2 dtheta
print("area of cardioid r = a(1 + cos θ):", sp.integrate((a*(1 + sp.cos(th)))**2/2, (th, 0, 2*sp.pi)))
print("one petal of r = cos 2θ          :", sp.integrate(sp.cos(2*th)**2/2, (th, -sp.pi/4, sp.pi/4)))
print("whole circle r = 2a cos θ        :", sp.integrate((2*a*sp.cos(th))**2/2, (th, -sp.pi/2, sp.pi/2)))

# Inside r = 3 sin θ but outside r = 1 + sin θ: the curves meet where sin θ = 1/2
area = sp.integrate((9*sp.sin(th)**2 - (1 + sp.sin(th))**2)/2, (th, sp.pi/6, 5*sp.pi/6))
print("inside r = 3 sin θ, outside r = 1 + sin θ:", sp.simplify(area))

# Arc length in polar form: L = ∫ sqrt(r^2 + r'^2) dθ for the cardioid r = 1 + cos θ
L = sp.integrate(2*sp.cos(th/2), (th, 0, sp.pi)) * 2      # sqrt(r^2 + r'^2) = 2|cos(θ/2)|
print("length of the cardioid r = 1 + cos θ:", L)
