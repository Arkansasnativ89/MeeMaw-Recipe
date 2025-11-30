import json

with open('recipes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

all_recipes = []
for category in data["categories"]:
    for recipe in category["recipes"]:
        recipe_name = recipe["original_recipe"]["name"]
        all_recipes.append((recipe_name, category["name"]))

# Find duplicates
from collections import Counter
recipe_counts = Counter([name for name, cat in all_recipes])
duplicates = {name: count for name, count in recipe_counts.items() if count > 1}

if duplicates:
    print("DUPLICATES FOUND:")
    for name, count in duplicates.items():
        print(f"  {name}: {count} times")
        # Show which categories
        categories = [cat for n, cat in all_recipes if n == name]
        print(f"    In categories: {', '.join(categories)}")
else:
    print("No duplicates found")

print(f"\nTotal unique recipe names: {len(recipe_counts)}")
print(f"Total recipe entries: {len(all_recipes)}")
