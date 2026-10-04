# Listing 9.7: Locating a lightning strike from arrival-time differences (hyperbolas)
import numpy as np
from scipy.optimize import fsolve

v = 3.0e5                                           # radio waves travel at 300 000 km/s
S = np.array([[0.0, 0.0], [40.0, 0.0], [10.0, 35.0]])   # three weather stations (km)

true = np.array([25.0, 18.0])                       # used only to simulate the data
arrival = np.linalg.norm(S - true, axis=1) / v      # arrival times (s)
dt12, dt13 = arrival[0] - arrival[1], arrival[0] - arrival[2]
print(f"time differences: {dt12*1e6:.3f} and {dt13*1e6:.3f} microseconds")

# Each time difference puts the strike on one branch of a hyperbola with foci at
# two stations:  |PS1| - |PS2| = v * dt12  and  |PS1| - |PS3| = v * dt13
def equations(P):
    d = np.linalg.norm(S - P, axis=1)
    return [d[0] - d[1] - v*dt12, d[0] - d[2] - v*dt13]

estimate = fsolve(equations, x0=[20, 20])
print("estimated strike position:", np.round(estimate, 4), "km")
