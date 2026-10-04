# Listing 0.3: Functions and if-statements - a fare with a minimum charge
def bolt_fare(distance_km, minutes, base=6.0, per_km=2.5, per_min=0.4, minimum=15.0):
    """Return an (illustrative) ride-hailing fare in GH¢."""
    fare = base + per_km * distance_km + per_min * minutes
    if fare < minimum:
        fare = minimum
    return round(fare, 2)

print(bolt_fare(1.0, 4))     # a very short trip pays the minimum
print(bolt_fare(7.2, 18))
print(bolt_fare(25, 55))     # Kasoa to Accra Mall, say

# A function of x, written exactly as in mathematics
def f(x):
    return x**2 - 4*x + 3

for x in [0, 1, 2, 3, 4]:
    print("f(", x, ") =", f(x))
