# Listing 1.4: Gradients - parallel and perpendicular lines, and road slopes
from fractions import Fraction
import math

def gradient(A, B):
    (x1, y1), (x2, y2) = A, B
    return Fraction(y2 - y1, x2 - x1)   # exact fraction, no rounding

A, B, C, D = (1, 2), (4, 8), (0, 5), (2, 4)
mAB, mCD = gradient(A, B), gradient(C, D)
print("m_AB =", mAB, "  m_CD =", mCD)
print("Parallel?      ", mAB == mCD)
print("Perpendicular? ", mAB * mCD == -1)

# A road rises 45 m over a horizontal distance of 600 m
rise, run = 45, 600
m = rise / run
print(f"gradient = {m:.3f}, i.e. a {100*m:.1f}% grade")
print(f"angle of inclination = {math.degrees(math.atan(m)):.2f} degrees")
