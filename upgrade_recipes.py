import json
import os

def upgrade_recipes():
    file_path = 'recipes.json'
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 2. Update Metadata
    if 'metadata' in data:
        data['metadata']['version'] = "4.0 - Heirloom Edition"
        data['metadata']['note'] = "Recipes restored to original ingredients (butter, eggs, whole milk) and categories consolidated."

    # 3. Consolidate Categories
    # Create new category list
    
    # Target category for consolidation
    appetizers_dips_snacks = {
        "name": "Appetizers, Dips & Snacks",
        "recipes": []
    }
    
    # Find existing categories
    cat_map = {c['name']: c for c in data['categories']}
    
    # Create "Appetizers, Dips & Snacks" if not exists
    if "Appetizers, Dips & Snacks" not in cat_map:
        cat_map["Appetizers, Dips & Snacks"] = appetizers_dips_snacks
        data['categories'].insert(0, appetizers_dips_snacks)
    
    target_cat = cat_map["Appetizers, Dips & Snacks"]
    
    # Merge Appetizers
    if "Appetizers" in cat_map:
        for r in cat_map["Appetizers"]['recipes']:
            r['category'] = "Appetizers, Dips & Snacks"
            target_cat['recipes'].append(r)
        data['categories'].remove(cat_map["Appetizers"])
        del cat_map["Appetizers"]

    # Merge Snacks
    if "Snacks" in cat_map:
        for r in cat_map["Snacks"]['recipes']:
            r['category'] = "Appetizers, Dips & Snacks"
            target_cat['recipes'].append(r)
        data['categories'].remove(cat_map["Snacks"])
        del cat_map["Snacks"]

    # 4. Move Recipes
    moves = {
        "Fluffy Buttermilk Biscuits": "Breads, Rolls & Breakfast",
        "Pizza Dough (Crusty)": "Breads, Rolls & Breakfast",
        "Frosted Pineapple Squares": "Cookies & Bars"
    }
    
    # Normalize category names if needed
    if "Breads & Breakfast" in cat_map:
        cat_map["Breads & Breakfast"]['name'] = "Breads, Rolls & Breakfast"
        cat_map["Breads, Rolls & Breakfast"] = cat_map["Breads & Breakfast"]
        del cat_map["Breads & Breakfast"]
        
    # Now perform moves
    for cat in data['categories']:
        for r in list(cat['recipes']):
            if r['name'] in moves:
                target_cat_name = moves[r['name']]
                target_cat_obj = next((c for c in data['categories'] if c['name'] == target_cat_name), None)
                
                if target_cat_obj:
                    cat['recipes'].remove(r)
                    r['category'] = target_cat_name
                    target_cat_obj['recipes'].append(r)
                    print(f"Moved '{r['name']}' to '{target_cat_name}'")
                else:
                    print(f"Warning: Target category '{target_cat_name}' not found for '{r['name']}'")

    # 5. Restore Ingredients
    replacements = {
        "Margarine": "Unsalted Butter",
        "margarine": "unsalted butter",
        "Egg substitute": "Large Eggs",
        "egg substitute": "large eggs",
        "Egg Substitute": "Large Eggs",
        "Skim milk": "Whole milk",
        "skim milk": "whole milk",
        "Low-fat milk": "Whole milk",
        "low-fat milk": "whole milk",
        "Non-fat milk": "Whole milk",
        "non-fat milk": "whole milk",
        "Low-fat": "",
        "low-fat": "",
        "Fat-free": "",
        "fat-free": "",
        "Non-fat": "",
        "non-fat": ""
    }
    
    def clean_text(text):
        if not isinstance(text, str): return text
        for old, new in replacements.items():
            text = text.replace(old, new)
        text = " ".join(text.split())
        return text

    for cat in data['categories']:
        for r in cat['recipes']:
            r['ingredients'] = [clean_text(i) for i in r['ingredients']]
            r['instructions'] = [clean_text(i) for i in r['instructions']]
            if 'notes' in r:
                 r['notes'] = [clean_text(n) for n in r['notes']]

    # 6. Specific Recipe Update: Corn Bread
    corn_bread_restored = {
        "name": "Corn Bread - Southern Style (Restored)",
        "category": "Breads, Rolls & Breakfast",
        "servings": "9 servings (9-inch square)",
        "ingredients": [
            "1 1/2 cups (250g) Yellow cornmeal (stone-ground preferred)",
            "1/2 cup (65g) All-purpose flour",
            "2 tablespoons (25g) Granulated sugar",
            "1 tablespoon (15g) Baking powder",
            "1 teaspoon (5g) Salt",
            "1 1/4 cups (300ml) Whole buttermilk",
            "2 Large eggs (lightly beaten)",
            "1/3 cup (80ml) Melted butter or bacon drippings"
        ],
        "instructions": [
            "Preheat oven to 425°F (220°C). Place 1 tablespoon of butter or bacon drippings in a 9-inch square cast iron skillet or baking pan and place in the oven to heat.",
            "In a large mixing bowl, whisk together the cornmeal, flour, sugar, baking powder, and salt.",
            "In a separate bowl, whisk together the buttermilk, beaten eggs, and melted butter (or remaining bacon drippings).",
            "Pour the wet ingredients into the dry ingredients and stir with a wooden spoon just until moistened. Do not overmix.",
            "Carefully remove the hot skillet from the oven. Swirl to coat the bottom with the melted fat.",
            "Pour the batter into the hot skillet (it should sizzle).",
            "Bake for 20-25 minutes, or until the top is golden brown and a toothpick inserted in the center comes out clean.",
            "Serve warm with butter."
        ],
        "notes": [
            "Restored to original family version using whole ingredients and metric measurements."
        ]
    }

    found_cornbread = False
    for cat in data['categories']:
        for i, r in enumerate(cat['recipes']):
            if r['name'] == "Corn Bread - Southern Style With Buttermilk":
                cat['recipes'][i] = corn_bread_restored
                found_cornbread = True
                break
        if found_cornbread: break
    
    if not found_cornbread:
        print("Warning: 'Corn Bread - Southern Style With Buttermilk' not found.")

    # 7. Add Historical Notes: Spice Cake
    spice_cake_note = "Grandmother Walters used 1/2 cup of shortening, probably lard. Grandmother baked this cake in a heavy cake pan or an iron skillet. Eggs WERE NOT USED. Cake was not iced."
    
    found_spicecake = False
    for cat in data['categories']:
        for r in cat['recipes']:
            if r['name'] == "Spice Cake":
                if 'notes' not in r:
                    r['notes'] = []
                r['notes'].append(spice_cake_note)
                found_spicecake = True
                break
        if found_spicecake: break

    # 8. Save
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    
    print("Successfully upgraded recipes.json")

if __name__ == "__main__":
    upgrade_recipes()