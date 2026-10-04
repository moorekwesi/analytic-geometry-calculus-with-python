# Listing 7.5: Volumes of revolution (disc and washer methods)
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x, y, r, h = sp.symbols("x y r h", positive=True)

# (a) Sphere: rotate y = sqrt(r^2 - x^2) about the x-axis
print("sphere :", sp.simplify(sp.integrate(sp.pi*(r**2 - x**2), (x, -r, r))))
# (b) Cone: rotate y = (r/h) x, 0 <= x <= h, about the x-axis
print("cone   :", sp.integrate(sp.pi*(r*x/h)**2, (x, 0, h)))
# (c) Washer: region between y = 2x and y = x^2 rotated about the x-axis
print("washer :", sp.integrate(sp.pi*((2*x)**2 - (x**2)**2), (x, 0, 2)))

# (d) A clay water pot. Its inside radius (cm) at height y above the base is
#     R(y) = 12 + 8 sin(pi y / 40),  0 <= y <= 40   (illustrative shape)
R = 12 + 8*sp.sin(sp.pi*y/40)
V = sp.integrate(sp.pi*R**2, (y, 0, 40))
print("pot    :", sp.simplify(V), "≈", round(float(V)), "cm^3 ≈", round(float(V)/1000, 1), "litres")

Y = np.linspace(0, 40, 200)
Rf = sp.lambdify(y, R)
plt.figure(figsize=(4, 4))
plt.plot(Rf(Y), Y, "k"); plt.plot(-Rf(Y), Y, "k")
plt.axvline(0, ls="--", color="gray")
plt.gca().set_aspect("equal"); plt.title("profile of the pot (cm)"); plt.grid(alpha=0.3)
plt.show()
