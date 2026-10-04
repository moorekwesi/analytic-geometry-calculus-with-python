# Listing 6.7: Integrals with no formula - scipy.integrate.quad
import numpy as np
from scipy.integrate import quad

# exp(-x^2) has no elementary antiderivative, but its integral is easy to compute
val, err = quad(lambda x: np.exp(-x**2), 0, 1)
print(f"∫_0^1 exp(-x^2) dx = {val:.10f}  (error estimate {err:.1e})")

# quad also handles infinite limits
val, _ = quad(lambda x: np.exp(-x**2), -np.inf, np.inf)
print(f"∫ over all x       = {val:.10f};  sqrt(pi) = {np.sqrt(np.pi):.10f}")

# and integrands such as sin(x)/x
val, _ = quad(lambda x: np.sinc(x/np.pi), 0, 10)       # np.sinc(t) = sin(pi t)/(pi t)
print(f"∫_0^10 sin(x)/x dx = {val:.10f}")
