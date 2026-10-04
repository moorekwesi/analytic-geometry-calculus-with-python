# Listing 9.5: Elliptical orbits - the Earth, and Ghana's first satellite
import numpy as np
from scipy.integrate import quad

# Earth's orbit: closest to the Sun 147.1 million km, furthest 152.1 million km
peri, aph = 147.1, 152.1
a = (peri + aph) / 2                  # semi-major axis
c = a - peri                          # centre-to-focus distance (Sun at a focus)
e = c / a
b = np.sqrt(a**2 - c**2)
print(f"a = {a:.2f}, b = {b:.3f} (million km), e = {e:.4f}")

# Length of the orbit: arc length of x = a cos t, y = b sin t (an integral, Ch. 6)
L, _ = quad(lambda t: np.sqrt((a*np.sin(t))**2 + (b*np.cos(t))**2), 0, 2*np.pi)
print(f"orbit length = {L:.2f} million km;  2*pi*a = {2*np.pi*a:.2f}")
print(f"average orbital speed = {L*1e6/(365.256*24*3600):.1f} km/s")

# GhanaSat-1 orbited about 400 km above the Earth (radius 6371 km).
# Kepler's third law: period T = 2 pi sqrt(a^3 / GM), GM = 398600 km^3/s^2
GM, a_sat = 398600, 6371 + 400
T = 2*np.pi*np.sqrt(a_sat**3 / GM)
print(f"period at 400 km altitude = {T/60:.1f} minutes, i.e. {24*3600/T:.1f} orbits per day")
