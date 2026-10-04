# Listing 4.9: Numerical differentiation - derivatives from data
import numpy as np

# (a) How accurate are difference quotients?  f(x) = sin x at x = 1, exact f'(1) = cos 1
f, x0, exact = np.sin, 1.0, np.cos(1.0)
print(f"{'h':>8} {'forward error':>15} {'central error':>15}")
for h in [0.1, 0.01, 0.001, 0.0001]:
    fwd = (f(x0 + h) - f(x0)) / h
    cen = (f(x0 + h) - f(x0 - h)) / (2*h)
    print(f"{h:>8} {abs(fwd - exact):>15.2e} {abs(cen - exact):>15.2e}")

# (b) Speed from GPS data logged by a ride-hailing app every 10 s (illustrative)
time = np.array([0, 10, 20, 30, 40, 50, 60])            # s
dist = np.array([0, 60, 210, 420, 640, 830, 960])       # m
speed = np.gradient(dist, time)                         # central differences inside
for t, v in zip(time, speed):
    print(f"t = {t:>2} s   speed ~ {v:5.1f} m/s = {3.6*v:5.1f} km/h")
