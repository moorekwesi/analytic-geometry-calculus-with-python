# Listing 7.2: Distance travelled from speedometer readings (trapezium rule)
# A trotro's speed (km/h) read every 5 minutes on the Kasoa - Accra road (illustrative)
import numpy as np

t_min = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])
speed = np.array([0, 18, 35, 12, 8, 30, 52, 47, 25, 0])     # km/h
t_hr = t_min / 60

distance = np.trapz(speed, t_hr)                           # ∫ v dt
print(f"distance travelled ≈ {distance:.2f} km in {t_min[-1]} minutes")
print(f"average speed     ≈ {distance/t_hr[-1]:.1f} km/h")

# Same thing 'by hand': each strip is a trapezium with area h*(v_i + v_{i+1})/2
h = 5/60
by_hand = sum(h*(speed[i] + speed[i + 1])/2 for i in range(len(speed) - 1))
print(f"by hand           ≈ {by_hand:.2f} km")
