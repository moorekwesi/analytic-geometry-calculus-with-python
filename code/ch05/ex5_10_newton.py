# Listing 5.10: Newton's method x_{n+1} = x_n - f(x_n)/f'(x_n)
import math

def newton(f, df, x0, tol=1e-12, max_steps=50, show=False):
    x = x0
    for n in range(1, max_steps + 1):
        x_new = x - f(x)/df(x)
        if show:
            print(f"  step {n}: x = {x_new:.15f}")
        if abs(x_new - x) < tol:
            return x_new, n
        x = x_new
    raise RuntimeError("Newton's method did not converge")

# (a) Heron of Alexandria's square root of 2:  f(x) = x^2 - 2
print("sqrt(2):")
root, n = newton(lambda x: x*x - 2, lambda x: 2*x, 1.0, show=True)
print(f"  math.sqrt(2) = {math.sqrt(2):.15f}")

# (b) x^3 - x - 2 = 0 (compare the bisection method of Listing 3.9: 20 steps)
root, n = newton(lambda x: x**3 - x - 2, lambda x: 3*x**2 - 1, 1.5)
print(f"x^3 - x - 2 = 0:  x = {root:.10f} after {n} steps")

# (c) cos x = x
root, n = newton(lambda x: math.cos(x) - x, lambda x: -math.sin(x) - 1, 1.0)
print(f"cos x = x:        x = {root:.10f} after {n} steps")
