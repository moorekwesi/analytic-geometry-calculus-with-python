# Listing 2.9: From the Rhind papyrus to Archimedes - approximating pi
import math

print(f"Rhind papyrus (c. 1550 BCE): (16/9)^2 = {(16/9)**2:.6f}")
print(f"Archimedes' bounds: 223/71 = {223/71:.6f} < pi < 22/7 = {22/7:.6f}")

# Archimedes: perimeters of regular polygons inside and outside a circle of diameter 1.
# Start with hexagons and keep doubling the number of sides.
n = 6
inner = 3.0                       # inscribed hexagon: perimeter 6 * (1/2)
outer = 2 * math.sqrt(3)          # circumscribed hexagon
print(f"{'sides':>6} {'inscribed':>12} {'circumscribed':>14}")
for _ in range(5):
    print(f"{n:>6} {inner:>12.6f} {outer:>14.6f}")
    outer = 2 * inner * outer / (inner + outer)   # harmonic mean
    inner = math.sqrt(inner * outer)              # geometric mean
    n *= 2
print(f"{n:>6} {inner:>12.6f} {outer:>14.6f}")
print(f"{'pi':>6} {math.pi:>12.6f}")
