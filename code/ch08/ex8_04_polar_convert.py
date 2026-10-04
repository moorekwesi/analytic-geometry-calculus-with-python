# Listing 8.4: Converting between polar and Cartesian coordinates
import numpy as np

def to_cartesian(r, theta):
    return r*np.cos(theta), r*np.sin(theta)

def to_polar(x, y):
    return np.hypot(x, y), np.arctan2(y, x)       # arctan2 picks the correct quadrant

for r, deg in [(2, 30), (4, 135), (3, 270)]:
    x, y = np.round(to_cartesian(r, np.radians(deg)), 4) + 0.0   # + 0.0 removes "-0.0"
    print(f"(r, θ) = ({r}, {deg}°)  ->  (x, y) = ({x:.4f}, {y:.4f})")
for x, y in [(1, 1), (-1, 1), (-3, -4)]:
    r, th = to_polar(x, y)
    print(f"(x, y) = ({x}, {y})  ->  r = {r:.4f}, θ = {np.degrees(th):.2f}°  "
          f"(arctan(y/x) alone gives {np.degrees(np.arctan(y/x)):.2f}°)")

# An airport radar reports an aircraft at range 40 km on a BEARING of 120°
# (bearings are measured clockwise from north). Polar angle = 90° - bearing.
rng, bearing = 40, 120
x, y = to_cartesian(rng, np.radians(90 - bearing))
print(f"(x, y) = ({x:.2f}, {y:.2f}): the aircraft is {x:.2f} km east and "
      f"{-y:.2f} km south of the radar")
