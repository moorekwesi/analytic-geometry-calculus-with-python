# Listing 0.2: Lists and for-loops - populations of some regions of Ghana
regions = ["Greater Accra", "Ashanti", "Eastern", "Central", "Northern", "Volta"]
# Populations in thousands, rounded, from the 2021 Population and Housing Census
pop = [5456, 5440, 2926, 2860, 2311, 1659]

for region, p in zip(regions, pop):
    print(f"{region:<14} {p:>6} thousand")

print("Number of regions:", len(regions))
print("Total:", sum(pop), "thousand")
print("Largest:", regions[pop.index(max(pop))])

# A loop that builds a new list: square numbers 1..10
squares = []
for n in range(1, 11):
    squares.append(n ** 2)
print(squares)

# The same thing as a one-line "list comprehension"
print([n ** 2 for n in range(1, 11)])
