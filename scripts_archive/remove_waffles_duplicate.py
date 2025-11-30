import json

# Load the current recipes.json
with open('recipes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find and remove duplicate Waffles from Breads & Breakfast
for category in data["categories"]:
    if category["name"] == "Breads & Breakfast":
        waffles_count = 0
        recipes_to_keep = []
        for recipe in category["recipes"]:
            if recipe["original_recipe"]["name"] == "Waffles":
                waffles_count += 1
                if waffles_count == 1:
                    # Keep the first instance
                    recipes_to_keep.append(recipe)
                    print(f"Keeping first Waffles recipe")
                else:
                    print(f"Removing duplicate Waffles recipe #{waffles_count}")
            else:
                recipes_to_keep.append(recipe)
        
        category["recipes"] = recipes_to_keep
        print(f"Breads & Breakfast now has {len(recipes_to_keep)} recipes")

# Save the updated recipes.json
with open('recipes.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\nSuccessfully removed duplicate Waffles")
