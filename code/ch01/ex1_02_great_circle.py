# Listing 1.2: Flat-map distance versus true (great-circle) distance in Ghana
import math

R = 6371.0   # mean radius of the Earth in km
towns = {    # (latitude, longitude) in degrees; west is negative
    "Accra":      (5.6037, -0.1870),
    "Kumasi":     (6.6885, -1.6244),
    "Cape Coast": (5.1053, -1.2466),
    "Tamale":     (9.4008, -0.8393),
}

def flat_distance(P, Q):
    """Treat (lat, lon) as x-y coordinates on a flat map.
    East-west distances are shrunk by cos(latitude) because meridians converge."""
    lat0 = math.radians((P[0] + Q[0]) / 2)
    dx = math.radians(Q[1] - P[1]) * R * math.cos(lat0)
    dy = math.radians(Q[0] - P[0]) * R
    return math.sqrt(dx**2 + dy**2)        # the distance formula!

def great_circle(P, Q):
    """Haversine formula: distance along the surface of a sphere."""
    p1, p2 = math.radians(P[0]), math.radians(Q[0])
    dphi = p2 - p1
    dlam = math.radians(Q[1] - P[1])
    a = math.sin(dphi/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dlam/2)**2
    return 2 * R * math.asin(math.sqrt(a))

for B in ["Kumasi", "Cape Coast", "Tamale"]:
    f = flat_distance(towns["Accra"], towns[B])
    g = great_circle(towns["Accra"], towns[B])
    print(f"Accra -> {B:<10}  flat map: {f:6.1f} km   sphere: {g:6.1f} km")
