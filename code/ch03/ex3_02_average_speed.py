# Listing 3.2: From average speed to instantaneous speed
# A Bolt car pulls away from the traffic lights at Kotokuraba.
# Distance travelled (metres) after t seconds:  s(t) = 1.5 t^2   (0 <= t <= 10)

def s(t):
    return 1.5 * t**2

t0 = 4.0
print(f"{'interval':>22} {'average speed (m/s)':>20}")
for h in [1, 0.5, 0.1, 0.01, 0.001, 0.0001]:
    avg = (s(t0 + h) - s(t0)) / h
    print(f"[{t0}, {t0 + h:<9}] {avg:>20.6f}")
print("The averages approach 12 m/s =", 12 * 3.6, "km/h: the speedometer reading at t = 4 s.")
