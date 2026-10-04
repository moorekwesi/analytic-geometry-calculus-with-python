# Listing 8.2: The path of a kicked football (no air resistance)
#   x = v cos(a) t,   y = v sin(a) t - g t^2 / 2
import numpy as np
import matplotlib.pyplot as plt

g, v = 9.8, 25.0                     # m/s^2, kick speed in m/s
plt.figure(figsize=(6.5, 3))
for deg in [20, 30, 45, 60]:
    a = np.radians(deg)
    T = 2*v*np.sin(a)/g              # time of flight (y = 0 again)
    t = np.linspace(0, T, 200)
    x, y = v*np.cos(a)*t, v*np.sin(a)*t - g*t**2/2
    print(f"angle {deg:>2}°: flight {T:4.2f} s, range {x[-1]:6.2f} m, "
          f"max height {(v*np.sin(a))**2/(2*g):5.2f} m")
    plt.plot(x, y, label=f"{deg}°")
plt.xlabel("x (m)"); plt.ylabel("y (m)"); plt.gca().set_aspect("equal")
plt.grid(alpha=0.3); plt.legend(fontsize=8); plt.show()

# A free kick 20 m from goal at 30°: how high is the ball when it reaches the goal line?
a = np.radians(30)
t_goal = 20 / (v*np.cos(a))
print(f"at the goal line: t = {t_goal:.3f} s, height = {v*np.sin(a)*t_goal - g*t_goal**2/2:.2f} m"
      " (crossbar 2.44 m)")
