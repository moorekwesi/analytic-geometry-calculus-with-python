# Listing 7.3: Total rainfall from rainfall intensity (an accumulation problem)
# Intensity r(t) in mm/hour during an afternoon storm in Kumasi, every 10 min (illustrative)
import numpy as np

t = np.arange(0, 121, 10) / 60                      # hours: 0, 1/6, ..., 2
r = np.array([0, 4, 15, 42, 60, 38, 25, 18, 10, 6, 3, 1, 0])   # mm/h

total = np.trapz(r, t)                              # ∫ r(t) dt  (mm)
print(f"total rainfall ≈ {total:.1f} mm over {t[-1]:.0f} hours")
print(f"average intensity ≈ {total/t[-1]:.1f} mm/h;  peak = {r.max()} mm/h")

# Volume of water falling on a 12 m x 10 m roof (1 mm on 1 m^2 = 1 litre)
roof = 12 * 10
print(f"rainwater on a {roof} m^2 roof ≈ {total*roof:,.0f} litres")
