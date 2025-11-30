import json

with open('recipes.json', 'r', encoding='utf-8') as f:
    content = f.read()
    
# Find line numbers for each category
categories = ['Main Dishes', 'Breads & Breakfast', 'Cakes', 'Pies & Pastry Fillings']
lines = content.split('\n')

for cat in categories:
    in_category = False
    last_recipe_end = 0
    
    for i, line in enumerate(lines, 1):
        if f'"name": "{cat}"' in line and '"category":' in line:
            in_category = True
        elif in_category and '"category":' in line and f'"{cat}"' not in line:
            # Found next category
            print(f"{cat}: Last recipe ends around line {last_recipe_end}")
            break
        elif in_category and line.strip() == '},' and i > last_recipe_end:
            # Could be end of a recipe object
            last_recipe_end = i
    else:
        if in_category:
            print(f"{cat}: Last recipe ends around line {last_recipe_end}")
