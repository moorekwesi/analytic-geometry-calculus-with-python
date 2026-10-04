# Listing 7.7: Area of an irregular farm from a surveyor's offsets
# A straight baseline runs along the road edge of a farm. Every 20 m along it the
# surveyor measures the perpendicular width (offset) to the far boundary (illustrative).
import numpy as np
from scipy.integrate import simpson
import matplotlib.pyplot as plt

x = np.arange(0, 201, 20)                                   # 0, 20, ..., 200 m
w = np.array([0, 38, 52, 61, 70, 74, 69, 63, 55, 41, 0])    # offsets (m)

A_trap = np.trapz(w, x)
A_simp = simpson(w, x=x)
print(f"trapezium rule: {A_trap:8.0f} m^2 = {A_trap/10000:.3f} ha")
print(f"Simpson's rule: {A_simp:8.0f} m^2 = {A_simp/10000:.3f} ha")

plt.figure(figsize=(6, 2.8))
plt.fill_between(x, 0, w, alpha=0.3, color="green")
plt.plot(x, w, "go-"); plt.axhline(0, color="k", lw=3)
plt.text(80, -12, "road (baseline)")
plt.xlabel("distance along road (m)"); plt.ylabel("offset (m)")
plt.ylim(-20, 85); plt.grid(alpha=0.3); plt.show()
