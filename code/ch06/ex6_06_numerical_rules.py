# Listing 6.6: Trapezium rule versus Simpson's rule on ∫_0^pi sin x dx = 2
import numpy as np

def trapezium(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    h = (b - a) / n
    y = f(x)
    return h/2 * (y[0] + 2*y[1:-1].sum() + y[-1])

def simpson(f, a, b, n):                 # n must be even
    x = np.linspace(a, b, n + 1)
    h = (b - a) / n
    y = f(x)
    return h/3 * (y[0] + 4*y[1:-1:2].sum() + 2*y[2:-1:2].sum() + y[-1])

print(f"{'n':>4} {'trapezium':>12} {'error':>10} {'Simpson':>12} {'error':>10}")
for n in [2, 4, 8, 16, 32]:
    T, S = trapezium(np.sin, 0, np.pi, n), simpson(np.sin, 0, np.pi, n)
    print(f"{n:>4} {T:>12.8f} {abs(T - 2):>10.2e} {S:>12.8f} {abs(S - 2):>10.2e}")
