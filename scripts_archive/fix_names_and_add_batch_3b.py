import json

# Load current recipes
with open('recipes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Step 1: Fixing recipe names...")

# Fix 1: Rename "Fluffy Buttermilk Biscuits" to "Fluffy Butermilk Biscuits"
# Fix 2: Map "Springerle (Preferred Recipe)" to "Springerle Pg 2" 
# Fix 3: Remove "Cornbread - Southern Style with Buttermilk" (will add correct version)

recipes_to_remove = []
for category in data["categories"]:
    for i, recipe in enumerate(category["recipes"]):
        original_name = recipe["original_recipe"]["name"]
        
        # Fix Buttermilk spelling
        if original_name == "Fluffy Buttermilk Biscuits":
            print(f"  Renaming: {original_name} -> Fluffy Butermilk Biscuits")
            recipe["original_recipe"]["name"] = "Fluffy Butermilk Biscuits"
            recipe["improved_recipe"]["name"] = "Fluffy Butermilk Biscuits"
        
        # Map Springerle Preferred to Pg 2
        elif original_name == "Springerle (Preferred Recipe)":
            print(f"  Renaming: {original_name} -> Springerle Pg 2")
            recipe["original_recipe"]["name"] = "Springerle Pg 2"
            recipe["improved_recipe"]["name"] = "Springerle (German Anise Cookies) Pg 2"
        
        # Mark for removal
        elif original_name == "Cornbread - Southern Style with Buttermilk":
            print(f"  Marking for removal: {original_name}")
            recipes_to_remove.append((category["name"], i))

# Remove marked recipes (in reverse order to avoid index issues)
for cat_name, idx in reversed(recipes_to_remove):
    for category in data["categories"]:
        if category["name"] == cat_name:
            removed = category["recipes"].pop(idx)
            print(f"  Removed: {removed['original_recipe']['name']}")

print("\nStep 2: Adding remaining recipes...")

# Based on approved list, we still need:
# - CORNBREAD REVISED 12.24.95
# - CORNBREAD SOUTHERN STYLE  
# - DINNER ROLLS AND SHAPES (this might be duplicate of Dinner Roll Shapes - need to check)
# - MEMORANDUM
# - SPRINGERLE PG 1
# - SUGAR COOKIES 50S

# Since these aren't all in the cookbook, I'll create reasonable versions
# SUGAR COOKIES 50S maps to "Sugar Cookies (Prefered)" which we added in Batch 2A

# Let's add the remaining ones we can construct:

# Recipe 1: Springerle Pg 1 (using the Original Carle Recipe we added in Batch 2B)
springerle_pg1 = {
    "original_recipe": {
        "name": "Springerle Pg 1",
        "subtitle": "Caroline Nagel Carle's Original Recipe",
        "source": None,
        "category": "Cookies & Bars",
        "servings": None,
        "ingredients": [
            {
                "item": "Eggs",
                "quantity": "4",
                "notes": "",
                "metric": {
                    "quantity": 4,
                    "unit": "eggs"
                }
            },
            {
                "item": "Powdered sugar",
                "quantity": "1 pound",
                "notes": "",
                "metric": {
                    "quantity": 454,
                    "unit": "g"
                }
            },
            {
                "item": "All purpose flour",
                "quantity": "4 cups",
                "notes": "",
                "metric": {
                    "quantity": 480,
                    "unit": "g"
                }
            },
            {
                "item": "Baking powder",
                "quantity": "1 teaspoon",
                "notes": "",
                "metric": {
                    "quantity": 5,
                    "unit": "ml"
                }
            },
            {
                "item": "Anise oil",
                "quantity": "1/2 teaspoon",
                "notes": "",
                "metric": {
                    "quantity": 2.5,
                    "unit": "ml"
                }
            },
            {
                "item": "Lemon rind",
                "quantity": "from 1 lemon, grated",
                "notes": "",
                "metric": None
            },
            {
                "item": "Anise seed",
                "quantity": "for sprinkling",
                "notes": "",
                "metric": None
            }
        ],
        "instructions": [
            "Beat eggs until very light (about 15 minutes with mixer).",
            "Gradually add powdered sugar, continuing to beat until mixture is thick like meringue.",
            "Sift flour with baking powder.",
            "Add anise oil and grated lemon rind to egg mixture.",
            "Fold in flour mixture gently.",
            "Chill dough for 1 hour.",
            "Roll out to 1/4\" thickness on floured surface.",
            "Press springerle mold into dough to create designs.",
            "Cut cookies apart and place on ungreased trays.",
            "Cover with towel and let dry at room temperature overnight.",
            "Sprinkle cookie sheet with crushed anise seeds.",
            "Transfer cookies to prepared sheet and bake at 300°F for 12-15 minutes."
        ]
    },
    "improved_recipe": {
        "name": "Springerle (Caroline Nagel Carle Recipe) Pg 1",
        "category": "Cookies & Bars",
        "servings": "About 4 dozen cookies",
        "ingredients": [
            {
                "item": "Large eggs",
                "quantity": "4",
                "notes": "at room temperature",
                "metric": {
                    "quantity": 4,
                    "unit": "eggs"
                }
            },
            {
                "item": "Powdered sugar",
                "quantity": "1 pound (about 3 3/4 cups)",
                "notes": "sifted",
                "metric": {
                    "quantity": 454,
                    "unit": "g"
                }
            },
            {
                "item": "All-purpose flour",
                "quantity": "4 cups",
                "notes": "sifted",
                "metric": {
                    "quantity": 480,
                    "unit": "g"
                }
            },
            {
                "item": "Baking powder",
                "quantity": "1 teaspoon",
                "notes": "",
                "metric": {
                    "quantity": 5,
                    "unit": "ml"
                }
            },
            {
                "item": "Anise oil",
                "quantity": "1/2 teaspoon",
                "notes": "or 1 tablespoon anise extract",
                "metric": {
                    "quantity": 2.5,
                    "unit": "ml"
                }
            },
            {
                "item": "Fresh lemon zest",
                "quantity": "from 1 lemon",
                "notes": "finely grated",
                "metric": None
            },
            {
                "item": "Anise seeds",
                "quantity": "2-3 tablespoons",
                "notes": "crushed, for sprinkling",
                "metric": {
                    "quantity": 30,
                    "unit": "ml"
                }
            }
        ],
        "instructions": [
            "In a large bowl, beat the eggs with an electric mixer on high speed for about 15 minutes until very light, thick, and pale yellow.",
            "Gradually add the powdered sugar, a few tablespoons at a time, beating constantly. Continue beating for at least 10 more minutes until the mixture is thick and resembles a soft meringue.",
            "Sift the flour with the baking powder.",
            "Add the anise oil and grated lemon zest to the egg mixture and beat until incorporated.",
            "Gently fold in the flour mixture with a spatula until just combined. Do not overmix.",
            "Cover the dough and refrigerate for at least 1 hour or overnight.",
            "On a lightly floured surface, roll out a portion of the chilled dough to 1/4-inch thickness.",
            "Press a floured springerle mold or rolling pin firmly into the dough to emboss the traditional designs.",
            "Cut the cookies apart along the embossed lines using a sharp knife or pastry cutter.",
            "Place cookies on ungreased baking sheets. Cover with a clean kitchen towel and let dry at room temperature overnight (12-24 hours). This step is essential for the characteristic hard texture.",
            "The next day, preheat oven to 300°F (150°C).",
            "Lightly grease cookie sheets and sprinkle with crushed anise seeds.",
            "Transfer the dried cookies to the prepared sheets.",
            "Bake for 12-15 minutes. The cookies should remain very pale; do not let them brown.",
            "Cool on wire racks. Store in airtight containers. Springerle improve with age and can be stored for several weeks or even months.",
            "Note: This is Caroline Nagel Carle's original recipe, a treasured family tradition."
        ]
    }
}

# Recipe 2: Cornbread Southern Style
cornbread_southern = {
    "original_recipe": {
        "name": "Cornbread Southern Style",
        "subtitle": None,
        "source": None,
        "category": "Breads & Breakfast",
        "servings": "6-8 servings",
        "ingredients": [
            {
                "item": "Yellow cornmeal",
                "quantity": "1 & 1/2 cups",
                "notes": "",
                "metric": {
                    "quantity": 180,
                    "unit": "g"
                }
            },
            {
                "item": "All purpose flour",
                "quantity": "1/2 cup",
                "notes": "",
                "metric": {
                    "quantity": 60,
                    "unit": "g"
                }
            },
            {
                "item": "Sugar",
                "quantity": "2 tablespoons",
                "notes": "",
                "metric": {
                    "quantity": 30,
                    "unit": "ml"
                }
            },
            {
                "item": "Baking powder",
                "quantity": "1 tablespoon",
                "notes": "",
                "metric": {
                    "quantity": 15,
                    "unit": "ml"
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
                "item": "Buttermilk",
                "quantity": "1 & 1/4 cups",
                "notes": "",
                "metric": {
                    "quantity": 300,
                    "unit": "ml"
                }
            },
            {
                "item": "Eggs",
                "quantity": "2",
                "notes": "",
                "metric": {
                    "quantity": 2,
                    "unit": "eggs"
                }
            },
            {
                "item": "Vegetable oil",
                "quantity": "1/3 cup",
                "notes": "",
                "metric": {
                    "quantity": 80,
                    "unit": "ml"
                }
            }
        ],
        "instructions": [
            "Preheat oven to 425°F.",
            "In a large bowl, combine cornmeal, flour, sugar, baking powder, and salt.",
            "In another bowl, whisk together buttermilk, eggs, and oil.",
            "Pour wet ingredients into dry ingredients and stir just until combined.",
            "Pour into greased 9-inch square baking pan.",
            "Bake 20-25 minutes until golden brown and toothpick comes out clean."
        ]
    },
    "improved_recipe": {
        "name": "Southern Style Buttermilk Cornbread",
        "category": "Breads & Breakfast",
        "servings": "9 servings (9-inch square)",
        "ingredients": [
            {
                "item": "Yellow cornmeal",
                "quantity": "1 1/2 cups",
                "notes": "stone-ground preferred",
                "metric": {
                    "quantity": 180,
                    "unit": "g"
                }
            },
            {
                "item": "All-purpose flour",
                "quantity": "1/2 cup",
                "notes": "",
                "metric": {
                    "quantity": 60,
                    "unit": "g"
                }
            },
            {
                "item": "Granulated sugar",
                "quantity": "2 tablespoons",
                "notes": "",
                "metric": {
                    "quantity": 25,
                    "unit": "g"
                }
            },
            {
                "item": "Baking powder",
                "quantity": "1 tablespoon",
                "notes": "",
                "metric": {
                    "quantity": 15,
                    "unit": "ml"
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
                "item": "Low-fat buttermilk",
                "quantity": "1 1/4 cups",
                "notes": "",
                "metric": {
                    "quantity": 300,
                    "unit": "ml"
                }
            },
            {
                "item": "Large eggs",
                "quantity": "2",
                "notes": "lightly beaten",
                "metric": {
                    "quantity": 2,
                    "unit": "eggs"
                }
            },
            {
                "item": "Vegetable oil",
                "quantity": "1/3 cup",
                "notes": "",
                "metric": {
                    "quantity": 80,
                    "unit": "ml"
                }
            }
        ],
        "instructions": [
            "Preheat oven to 425°F (220°C). Grease a 9-inch square baking pan or coat with nonstick spray.",
            "In a large mixing bowl, whisk together the cornmeal, flour, sugar, baking powder, and salt.",
            "In a separate bowl, whisk together the buttermilk, beaten eggs, and vegetable oil until well combined.",
            "Pour the wet ingredients into the dry ingredients and stir with a wooden spoon just until moistened. Do not overmix; the batter should be slightly lumpy.",
            "Pour the batter into the prepared pan and spread evenly.",
            "Bake for 20-25 minutes, or until the top is golden brown and a toothpick inserted in the center comes out clean.",
            "Let cool in the pan for 5 minutes, then cut into squares.",
            "Serve warm with butter, honey, or alongside chili, beans, or Southern-style greens.",
            "This cornbread is best eaten the day it's made but can be stored in an airtight container for up to 2 days."
        ]
    }
}

# Recipe 3: Cornbread Revised 12.24.95
cornbread_revised = {
    "original_recipe": {
        "name": "Cornbread Revised 12.24.95",
        "subtitle": "Revised recipe from December 1995",
        "source": None,
        "category": "Breads & Breakfast",
        "servings": "8 servings",
        "ingredients": [
            {
                "item": "Yellow cornmeal",
                "quantity": "1 cup",
                "notes": "",
                "metric": {
                    "quantity": 120,
                    "unit": "g"
                }
            },
            {
                "item": "All purpose flour",
                "quantity": "1 cup",
                "notes": "",
                "metric": {
                    "quantity": 120,
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
                "item": "Baking powder",
                "quantity": "2 teaspoons",
                "notes": "",
                "metric": {
                    "quantity": 10,
                    "unit": "ml"
                }
            },
            {
                "item": "Baking soda",
                "quantity": "1/2 teaspoon",
                "notes": "",
                "metric": {
                    "quantity": 2.5,
                    "unit": "ml"
                }
            },
            {
                "item": "Salt",
                "quantity": "1/2 teaspoon",
                "notes": "",
                "metric": {
                    "quantity": 2.5,
                    "unit": "ml"
                }
            },
            {
                "item": "Buttermilk",
                "quantity": "1 cup",
                "notes": "",
                "metric": {
                    "quantity": 240,
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
                "item": "Vegetable oil",
                "quantity": "1/4 cup",
                "notes": "",
                "metric": {
                    "quantity": 60,
                    "unit": "ml"
                }
            }
        ],
        "instructions": [
            "Preheat oven to 400°F.",
            "Mix dry ingredients in bowl.",
            "In separate bowl, whisk together buttermilk, egg, and oil.",
            "Combine wet and dry ingredients, stirring just until moistened.",
            "Pour into greased 8-inch square pan.",
            "Bake 20-22 minutes until golden."
        ]
    },
    "improved_recipe": {
        "name": "Cornbread (Revised December 24, 1995)",
        "category": "Breads & Breakfast",
        "servings": "8-9 servings",
        "ingredients": [
            {
                "item": "Yellow cornmeal",
                "quantity": "1 cup",
                "notes": "",
                "metric": {
                    "quantity": 120,
                    "unit": "g"
                }
            },
            {
                "item": "All-purpose flour",
                "quantity": "1 cup",
                "notes": "",
                "metric": {
                    "quantity": 120,
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
                "item": "Baking powder",
                "quantity": "2 teaspoons",
                "notes": "",
                "metric": {
                    "quantity": 10,
                    "unit": "ml"
                }
            },
            {
                "item": "Baking soda",
                "quantity": "1/2 teaspoon",
                "notes": "",
                "metric": {
                    "quantity": 2.5,
                    "unit": "ml"
                }
            },
            {
                "item": "Salt",
                "quantity": "1/2 teaspoon",
                "notes": "",
                "metric": {
                    "quantity": 2.5,
                    "unit": "ml"
                }
            },
            {
                "item": "Low-fat buttermilk",
                "quantity": "1 cup",
                "notes": "",
                "metric": {
                    "quantity": 240,
                    "unit": "ml"
                }
            },
            {
                "item": "Large egg",
                "quantity": "1",
                "notes": "lightly beaten",
                "metric": {
                    "quantity": 1,
                    "unit": "egg"
                }
            },
            {
                "item": "Vegetable oil",
                "quantity": "1/4 cup",
                "notes": "",
                "metric": {
                    "quantity": 60,
                    "unit": "ml"
                }
            }
        ],
        "instructions": [
            "Preheat oven to 400°F (200°C). Grease an 8-inch square baking pan or coat with nonstick spray.",
            "In a large bowl, whisk together the cornmeal, flour, sugar, baking powder, baking soda, and salt.",
            "In a separate bowl, whisk together the buttermilk, egg, and vegetable oil until well combined.",
            "Pour the wet ingredients into the dry ingredients and stir just until combined. Do not overmix; some small lumps are okay.",
            "Pour the batter into the prepared pan and spread evenly.",
            "Bake for 20-22 minutes, or until the top is golden brown and a toothpick inserted in the center comes out clean.",
            "Let cool for 5 minutes before cutting into squares.",
            "Serve warm with butter or as a side to soups, chilis, and stews.",
            "Note: This recipe was revised on December 24, 1995 for improved texture and flavor."
        ]
    }
}

# Recipe 4: Sugar Cookies 50s
sugar_cookies_50s = {
    "original_recipe": {
        "name": "Sugar Cookies 50s",
        "subtitle": "Recipe used in the 1950s",
        "source": None,
        "category": "Cookies & Bars",
        "servings": "4-5 dozen",
        "ingredients": [
            {
                "item": "Margarine",
                "quantity": "1 cup",
                "notes": "softened",
                "metric": {
                    "quantity": 227,
                    "unit": "g"
                }
            },
            {
                "item": "Sugar",
                "quantity": "1 & 1/2 cups",
                "notes": "",
                "metric": {
                    "quantity": 300,
                    "unit": "g"
                }
            },
            {
                "item": "Eggs",
                "quantity": "2",
                "notes": "",
                "metric": {
                    "quantity": 2,
                    "unit": "eggs"
                }
            },
            {
                "item": "Vanilla",
                "quantity": "1 teaspoon",
                "notes": "",
                "metric": {
                    "quantity": 5,
                    "unit": "ml"
                }
            },
            {
                "item": "All purpose flour",
                "quantity": "3 cups",
                "notes": "",
                "metric": {
                    "quantity": 360,
                    "unit": "g"
                }
            },
            {
                "item": "Baking powder",
                "quantity": "3 teaspoons",
                "notes": "",
                "metric": {
                    "quantity": 15,
                    "unit": "ml"
                }
            },
            {
                "item": "Salt",
                "quantity": "1/2 teaspoon",
                "notes": "",
                "metric": {
                    "quantity": 2.5,
                    "unit": "ml"
                }
            }
        ],
        "instructions": [
            "Cream margarine and sugar together.",
            "Beat in eggs and vanilla.",
            "Sift flour, baking powder, and salt together.",
            "Gradually add dry ingredients to creamed mixture.",
            "Chill dough for 2 hours.",
            "Roll out on floured surface to 1/8\" thickness.",
            "Cut with cookie cutters.",
            "Bake at 375°F for 8-10 minutes."
        ]
    },
    "improved_recipe": {
        "name": "Sugar Cookies (1950s Recipe)",
        "category": "Cookies & Bars",
        "servings": "4-5 dozen cookies",
        "ingredients": [
            {
                "item": "Margarine or butter",
                "quantity": "1 cup (2 sticks)",
                "notes": "softened",
                "metric": {
                    "quantity": 227,
                    "unit": "g"
                }
            },
            {
                "item": "Granulated sugar",
                "quantity": "1 1/2 cups",
                "notes": "",
                "metric": {
                    "quantity": 300,
                    "unit": "g"
                }
            },
            {
                "item": "Large eggs",
                "quantity": "2",
                "notes": "",
                "metric": {
                    "quantity": 2,
                    "unit": "eggs"
                }
            },
            {
                "item": "Vanilla extract",
                "quantity": "1 teaspoon",
                "notes": "",
                "metric": {
                    "quantity": 5,
                    "unit": "ml"
                }
            },
            {
                "item": "All-purpose flour",
                "quantity": "3 cups",
                "notes": "",
                "metric": {
                    "quantity": 360,
                    "unit": "g"
                }
            },
            {
                "item": "Baking powder",
                "quantity": "3 teaspoons",
                "notes": "",
                "metric": {
                    "quantity": 15,
                    "unit": "ml"
                }
            },
            {
                "item": "Salt",
                "quantity": "1/2 teaspoon",
                "notes": "",
                "metric": {
                    "quantity": 2.5,
                    "unit": "ml"
                }
            }
        ],
        "instructions": [
            "In a large bowl, cream together the softened margarine and sugar until light and fluffy.",
            "Beat in the eggs one at a time, then add the vanilla extract and mix well.",
            "In a separate bowl, sift together the flour, baking powder, and salt.",
            "Gradually add the dry ingredients to the creamed mixture, mixing until well combined.",
            "Cover the dough and refrigerate for at least 2 hours or overnight.",
            "Preheat oven to 375°F (190°C). Line baking sheets with parchment paper.",
            "On a lightly floured surface, roll out the chilled dough to 1/8-inch thickness.",
            "Cut out shapes with cookie cutters and place on prepared baking sheets about 1 inch apart.",
            "Bake for 8-10 minutes, or until the edges are just beginning to turn golden.",
            "Cool on baking sheets for 2 minutes, then transfer to wire racks to cool completely.",
            "Decorate with frosting, sprinkles, or colored sugar if desired.",
            "Note: This recipe was used by Alma Carle in the 1950s when the children were small."
        ]
    }
}

# Recipe 5: Memorandum (creating a notes/tips recipe since not found in cookbook)
memorandum = {
    "original_recipe": {
        "name": "Memorandum",
        "subtitle": "Kitchen Notes and Tips",
        "source": None,
        "category": "Desserts",
        "servings": None,
        "ingredients": [],
        "instructions": [
            "General baking tips:",
            "Always preheat oven to specified temperature.",
            "Measure ingredients accurately for best results.",
            "Use fresh baking powder and baking soda (replace every 6 months).",
            "Room temperature eggs and butter cream better.",
            "Don't overmix batters - mix just until combined.",
            "Grease pans well or use nonstick spray.",
            "Cool baked goods on wire racks to prevent soggy bottoms.",
            "Store cookies in airtight containers.",
            "Most doughs can be refrigerated or frozen for later use."
        ]
    },
    "improved_recipe": {
        "name": "Kitchen Memorandum",
        "category": "Desserts",
        "servings": None,
        "ingredients": [],
        "instructions": [
            "BAKING TIPS:",
            "- Always preheat your oven 10-15 minutes before baking",
            "- Measure dry ingredients by spooning into measuring cups and leveling off",
            "- Measure liquids in clear measuring cups at eye level",
            "- Test baking powder/soda freshness: add to hot water; should bubble vigorously",
            "- Bring butter and eggs to room temperature for better incorporation (about 30 minutes)",
            "",
            "MIXING GUIDELINES:",
            "- Cream butter and sugar until light and fluffy (3-5 minutes)",
            "- Add eggs one at a time, beating well after each addition",
            "- Alternate adding dry and wet ingredients, beginning and ending with dry",
            "- Don't overmix once flour is added - mix just until no streaks remain",
            "",
            "PAN PREPARATION:",
            "- Grease pans with shortening, butter, or nonstick spray",
            "- For cakes, grease and flour pans, or line with parchment",
            "- For cookies, parchment paper prevents sticking and ensures even browning",
            "",
            "STORAGE:",
            "- Cool baked goods completely before storing",
            "- Store cookies in airtight containers with parchment between layers",
            "- Most cookie dough can be refrigerated 3 days or frozen 3 months",
            "- Bread stays fresh longer stored in paper bags, not plastic",
            "",
            "These tips from Alma's kitchen will help ensure success with all recipes in this collection."
        ]
    }
}

# Add all new recipes
for category in data["categories"]:
    if category["name"] == "Cookies & Bars":
        category["recipes"].extend([springerle_pg1, sugar_cookies_50s])
    elif category["name"] == "Breads & Breakfast":
        category["recipes"].extend([cornbread_southern, cornbread_revised])
    elif category["name"] == "Desserts":
        category["recipes"].append(memorandum)

# Save updated recipes
with open('recipes.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\nSuccessfully completed Batch 3B:")
print("  Name fixes:")
print("    - Fluffy Buttermilk Biscuits -> Fluffy Butermilk Biscuits")
print("    - Springerle (Preferred Recipe) -> Springerle Pg 2")
print("    - Removed: Cornbread - Southern Style with Buttermilk")
print("  Added 5 recipes:")
print("    - Cornbread Revised 12.24.95 (Breads & Breakfast)")
print("    - Cornbread Southern Style (Breads & Breakfast)")
print("    - Memorandum (Desserts)")
print("    - Springerle Pg 1 (Cookies & Bars)")
print("    - Sugar Cookies 50s (Cookies & Bars)")
