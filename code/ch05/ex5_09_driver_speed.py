# Listing 5.9: The cheapest cruising speed for a driver on the Accra-Cape Coast highway
# Illustrative cost per km at speed v km/h:
#   C(v) = 0.6 + 0.01 v + 40 / v   GH¢/km
#   (fixed costs + fuel, which rises with speed + driver's time at GH¢ 40/hour)
import numpy as np
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt

C = lambda v: 0.6 + 0.01*v + 40/v

# Calculus: C'(v) = 0.01 - 40/v^2 = 0  ->  v = sqrt(4000)
v_star = np.sqrt(40/0.01)
print(f"calculus : v* = {v_star:.2f} km/h,  C(v*) = GH¢ {C(v_star):.3f} per km")

# Numerical check with SciPy
res = minimize_scalar(C, bounds=(20, 120), method="bounded")
print(f"scipy    : v* = {res.x:.2f} km/h,  C(v*) = GH¢ {res.fun:.3f} per km")
print(f"cost of the 145 km trip at 63 km/h: GH¢ {145*C(63):.2f};  at 100 km/h: GH¢ {145*C(100):.2f}")

v = np.linspace(20, 120, 200)
plt.figure(figsize=(5.5, 3.3))
plt.plot(v, C(v)); plt.plot(v_star, C(v_star), "ro")
plt.xlabel("speed v (km/h)"); plt.ylabel("cost (GH¢ per km)"); plt.grid(alpha=0.3)
plt.show()
