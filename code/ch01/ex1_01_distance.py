# Listing 1.1: The distance formula in Python
import math

def distance(A, B):
    """Distance between points A=(x1, y1) and B=(x2, y2)."""
    (x1, y1), (x2, y2) = A, B
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Checking the worked example: which of P or Q is closer to A?
A, P, Q = (3, 5), (-1, -2), (8, 9)
print(f"d(P,A) = {distance(P, A):.4f}  (sqrt(65) = {math.sqrt(65):.4f})")
print(f"d(Q,A) = {distance(Q, A):.4f}  (sqrt(41) = {math.sqrt(41):.4f})")

# Approximate positions (km) on a simple grid of Cape Coast:
# origin at Cape Coast Castle, x-axis pointing east, y-axis pointing north.
places = {
    "Cape Coast Castle": (0.0, 0.0),
    "Kotokuraba Market": (-0.4, 0.5),
    "UCC Science":       (-4.4, 1.5),
    "Abura":             (-1.6, 2.4),
}
start = "UCC Science"
for name, pt in places.items():
    if name != start:
        print(f"{start} -> {name:<18}: {distance(places[start], pt):5.2f} km")
