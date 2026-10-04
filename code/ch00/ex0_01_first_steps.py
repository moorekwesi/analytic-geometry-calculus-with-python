# Listing 0.1: Python as a calculator - a Bolt fare in Cape Coast
# Illustrative fare structure (NOT official Bolt prices)
base_fare = 6.00        # GH¢ charged as soon as the trip starts
per_km = 2.50           # GH¢ per kilometre
per_min = 0.40          # GH¢ per minute

distance = 7.2          # km, e.g. UCC Science to Kotokuraba Market
time = 18               # minutes

fare = base_fare + per_km * distance + per_min * time
print("Trip fare in GH¢:", fare)
print(f"Rounded to 2 d.p.: GH¢ {fare:.2f}")

# Powers, integer division and remainder
print(2 ** 10)       # 2 to the power 10
print(17 // 5)       # whole-number division
print(17 % 5)        # remainder
