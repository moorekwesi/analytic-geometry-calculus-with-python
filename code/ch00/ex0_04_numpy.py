# Listing 0.4: NumPy arrays - computing many values at once
import numpy as np

x = np.array([0, 1, 2, 3, 4])
print("x       =", x)
print("x**2    =", x**2)            # squares every entry
print("2*x + 1 =", 2*x + 1)

# 5 equally spaced points from 0 to 1 (inclusive)
print(np.linspace(0, 1, 5))

# Built-in mathematical functions act on whole arrays
t = np.linspace(0, np.pi, 5)
print("sin(t) =", np.round(np.sin(t), 4))
print("pi =", np.pi, " e =", np.e, " sqrt(2) =", np.sqrt(2))

# Summary statistics of daily Bolt trips for a driver (illustrative)
trips = np.array([14, 17, 12, 20, 22, 25, 9])   # Mon..Sun
print("mean =", trips.mean(), " max =", trips.max(), " total =", trips.sum())
