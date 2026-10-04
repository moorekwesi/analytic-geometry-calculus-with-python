# Listing 9.3: A parabolic arch bridge (illustrative dimensions)
# The arch spans 240 m and rises 50 m above its springing points.
# Put the vertex at (0, 50): the arch is y = 50 - k x^2 with y = 0 at x = +/-120.
k = 50 / 120**2
print(f"arch: y = 50 - {k:.6f} x^2   (i.e. x^2 = -4c(y - 50) with c = {1/(4*k):.1f} m)")
for x in [0, 30, 60, 90, 110, 120]:
    print(f"x = {x:>3} m from the centre: height of arch = {50 - k*x**2:6.2f} m")
