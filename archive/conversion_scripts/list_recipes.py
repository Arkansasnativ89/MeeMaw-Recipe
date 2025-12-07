import json

# Load recipes
with open('recipes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract all recipe names
all_recipes = []
for category in data['categories']:
    for recipe in category['recipes']:
        name = recipe['original_recipe']['name']
        all_recipes.append(name)

# Sort and print
all_recipes.sort()
for recipe in all_recipes:
    print(recipe)
