# Listing 1.8: Dividing a line segment in a given ratio
from fractions import Fraction as F

def divide(A, B, n, m, external=False):
    """Point R with AR:RB = n:m (internal) or n:-m (external)."""
    (x1, y1), (x2, y2) = A, B
    if external:
        m = -m
    return (F(m*x1 + n*x2, m + n), F(m*y1 + n*y2, m + n))

A, B = (1, 2), (3, 1)
R = divide(A, B, 1, 2)
print("Internal 1:2 ->", tuple(str(v) for v in R))
S = divide(A, B, 1, 2, external=True)
print("External 1:2 ->", tuple(str(v) for v in S))

# A water pipeline runs from a treatment plant W(0, 0) to a town T(12, 9) (km).
# A booster pump must be placed at P with WP : PT = 2 : 3.
P = divide((0, 0), (12, 9), 2, 3)
print("Pump position:", tuple(float(v) for v in P))
