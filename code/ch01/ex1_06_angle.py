# Listing 1.6: Angle between two lines
import math

def acute_angle(m1, m2):
    """Acute angle (degrees) between lines with gradients m1 and m2."""
    if 1 + m1 * m2 == 0:
        return 90.0
    return math.degrees(math.atan(abs((m1 - m2) / (1 + m1 * m2))))

print(f"y=2x+1 and y=3x+2: {acute_angle(3, 2):.4f} degrees")

# Two roads meet at a junction: one along y = 0.5x, the other along y = -3x + 14.
print(f"Junction angle: {acute_angle(0.5, -3):.1f} degrees")

# Check with angles of inclination: theta = atan(m)
t1, t2 = math.atan(3), math.atan(2)
print(f"Check: {math.degrees(t1 - t2):.4f} degrees")
