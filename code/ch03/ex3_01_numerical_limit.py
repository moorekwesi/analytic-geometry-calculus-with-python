# Listing 3.1: Guessing a limit from a table of values
import math

def f(x):
    return (x**2 - 16) / (x - 4)      # undefined at x = 4

def g(x):
    return math.sin(x) / x            # undefined at x = 0 (x in radians)

print(f"{'h':>10} {'f(4-h)':>12} {'f(4+h)':>12} {'g(-h)':>12} {'g(h)':>12}")
for k in range(1, 7):
    h = 10**(-k)
    print(f"{h:>10.0e} {f(4-h):>12.6f} {f(4+h):>12.6f} {g(-h):>12.8f} {g(h):>12.8f}")
