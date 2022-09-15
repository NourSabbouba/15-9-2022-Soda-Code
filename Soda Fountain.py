soft_drinks= ["coke", "diet coke", "pepsi", "sprite"]

Sizes = ["small", "medium", "large", "extra large"]

for drink in soft_drinks:
  for size in Sizes:
    print(f"Press here for a {size} {drink.title()}")

soft_drinks.sort()
print(f"This is the sorted soft drinks {soft_drinks}")
Sizes.sort()
print(f"This is the sorted sizes {Sizes}")