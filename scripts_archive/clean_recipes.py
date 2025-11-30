import json

# Load current recipes
with open('recipes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Recipes to completely remove (NOT on approved list)
not_approved = {
    "Brownies",
    "Chicken Casserole (Vocla Poulet Denomandine)",
    "Chicken/Brown Rice Bake",
    "Chicken/Rice Casserole", 
    "Chili",
    "Corn Bread - Southern Style with Buttermilk",
    "Dinner Rolls (Alma Finken Carle)",
    "Gingerbread Men Cookies (Old Fashioned Spicy)",
    "Jumbo Shells No. 1 - Spinach-Ricotta Filling",
    "Jumbo Shells No. 2 - Meat Filling",
    "Lemon Meringue Pie (9-inch)",
    "Peanut Brittle (Munching) - Microwave",
    "Pfeffernusse (Pepper Nuts)",
    "Popcorn Balls",
    "Spaghetti Portofino (Serves One)",
    "Spaghetti Portofino (Serves Six)",
    "Sugar Cookies (Alice Carle's)",
}

# Track which recipes we've seen to handle duplicates
seen = set()
removed_count = 0
kept_count = 0

# Clean each category
for category in data['categories']:
    cleaned_recipes = []
    
    for recipe in category['recipes']:
        name = recipe['original_recipe']['name']
        
        # Skip if not on approved list
        if name in not_approved:
            print(f"REMOVED (not approved): {name} from {category['name']}")
            removed_count += 1
            continue
        
        # Skip if we've already seen this recipe (duplicate)
        if name in seen:
            print(f"REMOVED (duplicate): {name} from {category['name']}")
            removed_count += 1
            continue
        
        # Keep this recipe
        seen.add(name)
        cleaned_recipes.append(recipe)
        kept_count += 1
    
    # Update category with cleaned recipes
    category['recipes'] = cleaned_recipes

# Save cleaned data
with open('recipes.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 80)
print(f"CLEANUP COMPLETE")
print("=" * 80)
print(f"Recipes removed: {removed_count}")
print(f"Recipes kept: {kept_count}")
print(f"Backup saved to: recipes_backup_before_cleanup.json")
print("=" * 80)
