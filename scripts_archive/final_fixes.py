import json

# Load current recipes
with open('recipes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Fixing recipe name spellings to match approved list...")

# Fix spellings
for category in data["categories"]:
    for recipe in category["recipes"]:
        original_name = recipe["original_recipe"]["name"]
        
        # Fix "Chili" to "Chil"
        if original_name == "Chili":
            print(f"  Renaming: {original_name} -> Chil")
            recipe["original_recipe"]["name"] = "Chil"
            recipe["improved_recipe"]["name"] = "MeeMaw's Chil"
        
        # Fix "Portofino" to "Portotino"
        elif original_name == "Spaghetti Portofino (Serves One)":
            print(f"  Renaming: {original_name} -> Spaghetti Portotino (Serves One)")
            recipe["original_recipe"]["name"] = "Spaghetti Portotino (Serves One)"
            recipe["improved_recipe"]["name"] = "Spaghetti Portotino (Serves One)"
        
        elif original_name == "Spaghetti Portofino (Serves Six)":
            print(f"  Renaming: {original_name} -> Spaghetti Portotino (Serves Six)")
            recipe["original_recipe"]["name"] = "Spaghetti Portotino (Serves Six)"
            recipe["improved_recipe"]["name"] = "Spaghetti Portotino (Serves Six)"

print("\nAdding missing recipe: Dinner Rolls and Shapes...")

# Add "Dinner Rolls and Shapes" - this is a combination recipe
dinner_rolls_and_shapes = {
    "original_recipe": {
        "name": "Dinner Rolls and Shapes",
        "subtitle": "Complete recipe with multiple shaping options",
        "source": None,
        "category": "Breads & Breakfast",
        "servings": "18-24 rolls",
        "ingredients": [
            {
                "item": "Warm water",
                "quantity": "1 cup",
                "notes": "105-115°F",
                "metric": {
                    "quantity": 240,
                    "unit": "ml"
                }
            },
            {
                "item": "Active dry yeast",
                "quantity": "1 package",
                "notes": "",
                "metric": {
                    "quantity": 7,
                    "unit": "g"
                }
            },
            {
                "item": "Sugar",
                "quantity": "1/4 cup",
                "notes": "",
                "metric": {
                    "quantity": 50,
                    "unit": "g"
                }
            },
            {
                "item": "Salt",
                "quantity": "1 teaspoon",
                "notes": "",
                "metric": {
                    "quantity": 5,
                    "unit": "ml"
                }
            },
            {
                "item": "Margarine",
                "quantity": "2 tablespoons",
                "notes": "softened",
                "metric": {
                    "quantity": 30,
                    "unit": "ml"
                }
            },
            {
                "item": "Egg",
                "quantity": "1",
                "notes": "",
                "metric": {
                    "quantity": 1,
                    "unit": "egg"
                }
            },
            {
                "item": "All purpose flour",
                "quantity": "3 to 3 & 1/2 cups",
                "notes": "",
                "metric": {
                    "min": 360,
                    "max": 420,
                    "unit": "g"
                }
            }
        ],
        "instructions": [
            "Dissolve yeast in warm water. Add sugar, salt, margarine, egg, and 2 cups flour. Beat until smooth.",
            "Stir in enough remaining flour to make dough easy to handle.",
            "Turn dough onto lightly floured surface; knead until smooth and elastic, about 5 minutes.",
            "Place in greased bowl; turn greased side up. Cover; let rise in warm place until double, about 1 hour.",
            "Punch down dough. Shape into desired forms:",
            "- Cloverleaf: Form into 1/2\" balls, place 3 in each greased muffin cup",
            "- Crescents: Roll into circles, cut into wedges, brush with margarine, roll from wide end, curve into crescents",
            "- Parkerhouse: Cut with 3\" cutter, make crease below center, brush with margarine, fold over",
            "- Fantans: Roll into rectangle, cut into 1\" strips, brush with margarine, stack 6-7 strips, cut into 1 & 1/4\" pieces, place in muffin cups cut side up",
            "Let rise until double, about 30 minutes.",
            "Bake at 375°F for 12-15 minutes until golden brown."
        ]
    },
    "improved_recipe": {
        "name": "Dinner Rolls with Various Shapes",
        "category": "Breads & Breakfast",
        "servings": "18-24 rolls (varies by shape)",
        "ingredients": [
            {
                "item": "Warm water",
                "quantity": "1 cup",
                "notes": "105-115°F (40-46°C)",
                "metric": {
                    "quantity": 240,
                    "unit": "ml"
                }
            },
            {
                "item": "Active dry yeast",
                "quantity": "1 packet (2 1/4 teaspoons)",
                "notes": "",
                "metric": {
                    "quantity": 7,
                    "unit": "g"
                }
            },
            {
                "item": "Granulated sugar",
                "quantity": "1/4 cup",
                "notes": "",
                "metric": {
                    "quantity": 50,
                    "unit": "g"
                }
            },
            {
                "item": "Salt",
                "quantity": "1 teaspoon",
                "notes": "",
                "metric": {
                    "quantity": 5,
                    "unit": "ml"
                }
            },
            {
                "item": "Margarine or butter",
                "quantity": "2 tablespoons",
                "notes": "softened",
                "metric": {
                    "quantity": 28,
                    "unit": "g"
                }
            },
            {
                "item": "Large egg",
                "quantity": "1",
                "notes": "at room temperature",
                "metric": {
                    "quantity": 1,
                    "unit": "egg"
                }
            },
            {
                "item": "All-purpose flour",
                "quantity": "3 to 3 1/2 cups",
                "notes": "plus more for kneading",
                "metric": {
                    "min": 360,
                    "max": 420,
                    "unit": "g"
                }
            },
            {
                "item": "Additional margarine",
                "quantity": "2-3 tablespoons",
                "notes": "melted, for brushing",
                "metric": {
                    "quantity": 30,
                    "unit": "ml"
                }
            }
        ],
        "instructions": [
            "In a large bowl, dissolve the yeast in warm water. Let stand 5 minutes until foamy.",
            "Add the sugar, salt, softened margarine, egg, and 2 cups of the flour to the yeast mixture. Beat with a mixer or wooden spoon until smooth.",
            "Gradually stir in enough of the remaining flour (1 to 1 1/2 cups) to make a soft dough that pulls away from the sides of the bowl.",
            "Turn the dough out onto a lightly floured surface and knead for about 5 minutes, until smooth and elastic.",
            "Place the dough in a greased bowl, turning once to coat all sides. Cover with a clean towel and let rise in a warm place until doubled in size, about 1 hour.",
            "Punch down the dough to release air bubbles. At this point, you can shape the rolls in various forms:",
            "",
            "FOR CLOVERLEAF ROLLS: Pinch off dough and form into small balls about 1/2 inch in diameter. Place 3 balls in each greased muffin cup.",
            "",
            "FOR CRESCENT ROLLS: Roll dough to 1/4-inch thickness and cut into 6-inch circles. Cut each circle into 6-8 wedges. Brush with melted margarine. Starting at the wide end, roll up each wedge and curve into a crescent shape. Place on greased baking sheet.",
            "",
            "FOR PARKERHOUSE ROLLS: Roll dough to 1/4-inch thickness. Cut with a 3-inch biscuit cutter. Make a crease just below the center of each circle with a knife handle or spoon. Brush with melted margarine. Fold the top half over the bottom half (bottom should be slightly larger). Place on greased baking sheet.",
            "",
            "FOR FANTAN ROLLS: Roll dough into a rectangle about 1/8-inch thick. Cut into 1-inch-wide strips. Brush with melted margarine. Stack 6-7 strips on top of each other. Cut the stack into 1 1/4-inch pieces. Place each piece cut-side up in a greased muffin cup.",
            "",
            "Cover shaped rolls and let rise in a warm place until doubled, about 30 minutes.",
            "Preheat oven to 375°F (190°C).",
            "Bake for 12-15 minutes, or until golden brown.",
            "Brush with additional melted butter if desired. Serve warm."
        ]
    }
}

# Add to Breads & Breakfast category
for category in data["categories"]:
    if category["name"] == "Breads & Breakfast":
        category["recipes"].append(dinner_rolls_and_shapes)
        break

# Save updated recipes
with open('recipes.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\nSuccessfully completed final adjustments:")
print("  Name spelling fixes:")
print("    - Chili -> Chil")
print("    - Spaghetti Portofino -> Spaghetti Portotino (both versions)")
print("  Added 1 recipe:")
print("    - Dinner Rolls and Shapes (Breads & Breakfast)")
print("\nShould now have exactly 112 recipes!")
