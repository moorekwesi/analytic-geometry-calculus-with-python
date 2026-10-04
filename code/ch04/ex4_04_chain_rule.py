# Listing 4.4: The chain rule - symbolic examples and a fuel-cost calculation
import sympy as sp

x = sp.symbols("x")
for f in [(x**2 + x)**-5, sp.sin(x)**5, sp.tan(3*x**2 + 1), sp.cos(x**2 + 1)**3]:
    print(f"d/dx[{f}] = {sp.factor(sp.diff(f, x))}")

# Fuel cost of a Bolt driver (illustrative numbers):
#   price  p = 14 GH¢ per litre,  consumption = 0.08 litres per km,  speed = 40 km/h
dC_dF = 14          # GH¢ per litre
dF_dx = 0.08        # litres per km
dx_dt = 40          # km per hour
dC_dt = dC_dF * dF_dx * dx_dt
print(f"Fuel cost rate dC/dt = {dC_dF} x {dF_dx} x {dx_dt} = GH¢ {dC_dt:.2f} per hour")
