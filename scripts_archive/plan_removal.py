import json
import re

# Load current recipes
with open('recipes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Recipes to KEEP (these are EXACT duplicates - keep first occurrence only)
duplicates_to_remove = [
    # Remove second occurrence of these exact names
    "Apple Cake",
    "Apple Pie", 
    "Banana Nut Bread",
    "Blueberry Pie Filling",
    "Cherry Pie Filling (Quick)",
    "Chocolate Oat-Chip Cookies",
    "Deluxe White Cake",
    "Fluffy Buttermilk Biscuits",  # One in Desserts, one in Breads
    "Frosted Carrot Cake",
    "Frosted Pineapple Squares",
    "Ginger Cookies",
    "Lemon Squares",
    "Oatmeal Raisin Spice Cookies",
    "Pralines, Old Fashioned",
    "Pumpkin Bread",
    "Pumpkin Pie",
    "Roasted Nuts",
    "Springerle (Preferred Recipe)",
    "The Little English Muffin Pizza"
]

# Recipes NOT on approved list (remove completely)
not_approved = [
    "Brownies",
    "Chicken Casserole (Vocla Poulet Denomandine)",
    "Chicken/Brown Rice Bake",
    "Chicken/Rice Casserole", 
    "Chili",
    "Corn Bread - Southern Style with Buttermilk",  # Keep "Cornbread - Southern Style with Buttermilk"
    "Dinner Rolls (Alma Finken Carle)",  # Not matching "DINNER ROLLS"
    "Gingerbread Men Cookies (Old Fashioned Spicy)",  # Not matching "GINGERBREAD MEN COOKIES"
    "Jumbo Shells No. 1 - Spinach-Ricotta Filling",  # Not matching "JUMBO SHELLS NO. 1"
    "Jumbo Shells No. 2 - Meat Filling",  # Not matching "JUMBO SHELLS NO. 2"
    "Lemon Meringue Pie (9-inch)",  # Not matching "LEMON MERINGUE PIE"
    "Peanut Brittle (Munching) - Microwave",  # Not matching "PEANUT BRITTLE (MUNCHING)"
    "Pfeffernusse (Pepper Nuts)",  # Not matching "PFEFFERNUSSE"
    "Popcorn Balls",
    "Spaghetti Portofino (Serves One)",  # Not matching "SPAGHETTI PORTOTINO (SERVES ONE)"
    "Spaghetti Portofino (Serves Six)",  # Not matching "SPAGHETTI PORTOTINO (SERVES SIX)"
    "Sugar Cookies (Alice Carle's)",  # Not matching "SUGAR COOKIES (ALICE CARLE)"
]

# Track which recipes we've seen
seen = {}
removal_list = []

for cat_idx, category in enumerate(data['categories']):
    for recipe_idx, recipe in enumerate(category['recipes']):
        name = recipe['original_recipe']['name']
        
        # Track duplicates
        if name in seen:
            # This is a duplicate - mark for removal
            removal_list.append({
                'category': category['name'],
                'category_idx': cat_idx,
                'recipe_idx': recipe_idx,
                'name': name,
                'reason': 'DUPLICATE (keeping first occurrence)'
            })
        else:
            seen[name] = {'category': category['name'], 'cat_idx': cat_idx, 'rec_idx': recipe_idx}
        
        # Check if not approved
        if name in not_approved:
            removal_list.append({
                'category': category['name'],
                'category_idx': cat_idx,
                'recipe_idx': recipe_idx,
                'name': name,
                'reason': 'NOT ON APPROVED LIST'
            })

print("=" * 80)
print(f"REMOVAL PLAN - {len(removal_list)} recipes to remove")
print("=" * 80)

for item in sorted(removal_list, key=lambda x: (x['category_idx'], x['recipe_idx']), reverse=True):
    print(f"Category: {item['category']}")
    print(f"  Recipe: {item['name']}")
    print(f"  Reason: {item['reason']}")
    print(f"  Index: cat[{item['category_idx']}].recipes[{item['recipe_idx']}]")
    print()

print("=" * 80)
print(f"After removal: {len(seen) - len([r for r in removal_list if r['reason'] == 'NOT ON APPROVED LIST'])} unique recipes will remain")
print("=" * 80)
