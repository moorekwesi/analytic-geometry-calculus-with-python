# Listing 3.5: One-sided limits of a tariff with a jump (illustrative prices)
# Monthly electricity bill B(u) in GH¢ for u units (kWh):
#   up to 30 units: 0.65 per unit (a "lifeline" band, no service charge)
#   above 30 units: 1.20 per unit plus a fixed service charge of GH¢ 10
import numpy as np
import matplotlib.pyplot as plt

def bill(u):
    return np.where(u <= 30, 0.65*u, 10 + 1.20*u)

for u in [29.9, 29.99, 29.999, 30, 30.001, 30.01, 30.1]:
    print(f"B({u}) = {float(bill(u)):.4f}")
print("Left-hand limit at 30  :", 0.65*30)
print("Right-hand limit at 30 :", 10 + 1.20*30)

u1 = np.linspace(0, 30, 50); u2 = np.linspace(30.0001, 60, 50)
plt.figure(figsize=(5.5, 3.4))
plt.plot(u1, bill(u1), "C0"); plt.plot(u2, bill(u2), "C0")
plt.plot(30, 19.5, "o", color="C0"); plt.plot(30, 46, "o", mfc="white", mec="C0")
plt.xlabel("units used (kWh)"); plt.ylabel("bill (GH¢)"); plt.grid(alpha=0.3)
plt.show()
