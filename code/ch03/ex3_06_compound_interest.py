# Listing 3.6: Compounding more and more often - the number e
import math

P, r = 1000, 0.12            # GH¢ 1000 at 12% per year (illustrative)
print(f"{'compounded':>14} {'n':>8} {'balance after 1 year':>22}")
for label, n in [("yearly", 1), ("monthly", 12), ("weekly", 52), ("daily", 365),
                 ("hourly", 8760), ("every minute", 525600)]:
    print(f"{label:>14} {n:>8} {P*(1 + r/n)**n:>22.4f}")
print(f"{'continuously':>14} {'∞':>8} {P*math.exp(r):>22.4f}")

print()
for n in [1, 10, 100, 1000, 10**6]:
    print(f"(1 + 1/n)^n with n = {n:>7}: {(1 + 1/n)**n:.8f}")
print("e =", math.e)
