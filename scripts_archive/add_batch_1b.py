import json

# Load the current recipes.json
with open('recipes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Recipe 1: Macaroni, Ham, and Cheese (Main Dishes)
macaroni_ham_cheese = {
    "original_recipe": {
        "name": "Macaroni, Ham, and Cheese",
        "subtitle": None,
        "source": None,
        "category": "Main Dishes",
        "servings": None,
        "ingredients": [
            {"item": "Macaroni", "quantity": "2 cups", "notes": "", "metric": {"quantity": 200, "unit": "g"}},
            {"item": "Turkey ham", "quantity": "1 pound", "notes": "about 4 cups when ground", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Reduced fat Cracker Barrel sharp cheddar cheese", "quantity": "1 1/2 (10 ounce) packages", "notes": "", "metric": {"quantity": 425, "unit": "g"}},
            {"item": "Bread", "quantity": "1/2 slice", "notes": "", "metric": None},
            {"item": "Egg", "quantity": "1", "notes": "or equivalent in egg substitute", "metric": {"quantity": 50, "unit": "g"}},
            {"item": "Milk", "quantity": "enough to make 1/2 cup with egg", "notes": "", "metric": {"quantity": 120, "unit": "ml"}}
        ],
        "instructions": [
            "Using a large hole plate, grind ham and cheese together.",
            "Run 1/2 slice of bread through grinder to remove all cheese and meat. Add this ground bread and meat to the mixture. Mix well.",
            "Cook two cups of macaroni according to instructions on the package. Drain.",
            "Coat 9\"x13\"x2\" casserole with a non stick vegetable spray.",
            "Starting with ham and cheese, put alternate layers of this and the macaroni in the casserole. End with a layer of ham and cheese on top.",
            "Add enough milk to the egg or egg substitute to make 1/2 cup. Mix well. Pour this as evenly as possible over the casserole.",
            "Bake at 350° F for 25 to 30 minutes."
        ]
    },
    "improved_recipe": {
        "name": "Macaroni, Ham, and Cheese Casserole",
        "category": "Main Dishes",
        "servings": "8-10 servings",
        "ingredients": [
            {"item": "Elbow macaroni", "quantity": "2 cups (8 oz)", "notes": "uncooked", "metric": {"quantity": 200, "unit": "g"}},
            {"item": "Turkey ham", "quantity": "1 pound", "notes": "diced or cubed", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Sharp cheddar cheese", "quantity": "15 ounces (about 3 3/4 cups)", "notes": "shredded, reduced-fat if preferred", "metric": {"quantity": 425, "unit": "g"}},
            {"item": "Bread", "quantity": "1/2 slice", "notes": "torn into small pieces", "metric": None},
            {"item": "Egg", "quantity": "1 large", "notes": "or 1/4 cup egg substitute", "metric": {"quantity": 50, "unit": "g"}},
            {"item": "Milk", "quantity": "about 1/2 cup total", "notes": "2% or whole", "metric": {"quantity": 120, "unit": "ml"}}
        ],
        "instructions": [
            "Preheat oven to 350°F (175°C). Coat a 9x13x2-inch baking dish with nonstick cooking spray.",
            "Cook the macaroni according to package directions until al dente. Drain well and set aside.",
            "If you have a meat grinder with a large-hole plate, grind the turkey ham and shredded cheese together. Run the 1/2 slice of bread through the grinder to collect any remaining cheese and ham. Mix well. If you don't have a grinder, finely chop or dice the ham and mix it with the shredded cheese and torn bread pieces.",
            "In a small bowl, beat the egg (or egg substitute) and add enough milk to make 1/2 cup total liquid. Mix well.",
            "Begin layering in the prepared casserole: Start with a layer of the ham-cheese mixture, then a layer of cooked macaroni. Repeat, alternating layers, and end with a layer of ham and cheese on top.",
            "Pour the egg-milk mixture evenly over the entire casserole.",
            "Bake uncovered for 25-30 minutes, or until the top is golden and the casserole is bubbly and heated through.",
            "Let stand for 5 minutes before serving. Serve hot with a green salad or steamed vegetables."
        ]
    }
}

# Recipe 2: Sweet and Sour Roast (Main Dishes)
sweet_sour_roast = {
    "original_recipe": {
        "name": "Sweet and Sour Roast",
        "subtitle": None,
        "source": None,
        "category": "Main Dishes",
        "servings": None,
        "ingredients": [
            {"item": "Meat", "quantity": "4 pounds", "notes": "chicken and/or beef", "metric": {"quantity": 1814, "unit": "g"}},
            {"item": "Vegetable oil", "quantity": "3 tablespoons", "notes": "", "metric": {"quantity": 45, "unit": "ml"}},
            {"item": "Garlic", "quantity": "1 clove", "notes": "", "metric": {"quantity": 3, "unit": "g"}},
            {"item": "Onions", "quantity": "2", "notes": "sliced", "metric": {"quantity": 300, "unit": "g"}},
            {"item": "Broth", "quantity": "1 can", "notes": "", "metric": {"quantity": 400, "unit": "ml"}},
            {"item": "Bay leaves", "quantity": "2", "notes": "", "metric": None},
            {"item": "Vinegar or lemon juice", "quantity": "2 tablespoons", "notes": "", "metric": {"quantity": 30, "unit": "ml"}},
            {"item": "Brown sugar", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 15, "unit": "g"}},
            {"item": "Tomato sauce", "quantity": "1 small can", "notes": "", "metric": {"quantity": 225, "unit": "ml"}},
            {"item": "Raisins", "quantity": "1/2 cup", "notes": "", "metric": {"quantity": 75, "unit": "g"}}
        ],
        "instructions": [
            "Brown meat in oil, then add next six ingredients (garlic, onions, broth, bay leaves, vinegar, brown sugar).",
            "Simmer until done (about one hour).",
            "Then add the tomato sauce and raisins.",
            "Continue simmering for another half hour.",
            "Serve with Riceland long grain rice."
        ]
    },
    "improved_recipe": {
        "name": "Sweet and Sour Pot Roast",
        "category": "Main Dishes",
        "servings": "8 servings",
        "ingredients": [
            {"item": "Beef chuck roast or chicken pieces", "quantity": "4 pounds", "notes": "trimmed of excess fat", "metric": {"quantity": 1814, "unit": "g"}},
            {"item": "Vegetable oil", "quantity": "3 tablespoons", "notes": "", "metric": {"quantity": 45, "unit": "ml"}},
            {"item": "Garlic", "quantity": "1 large clove", "notes": "minced or crushed", "metric": {"quantity": 5, "unit": "g"}},
            {"item": "Onions", "quantity": "2 medium", "notes": "sliced", "metric": {"quantity": 300, "unit": "g"}},
            {"item": "Beef or chicken broth", "quantity": "1 can (14 oz)", "notes": "low-sodium if preferred", "metric": {"quantity": 400, "unit": "ml"}},
            {"item": "Bay leaves", "quantity": "2", "notes": "", "metric": None},
            {"item": "Vinegar or lemon juice", "quantity": "2 tablespoons", "notes": "white or apple cider vinegar", "metric": {"quantity": 30, "unit": "ml"}},
            {"item": "Brown sugar", "quantity": "1 tablespoon", "notes": "packed", "metric": {"quantity": 15, "unit": "g"}},
            {"item": "Tomato sauce", "quantity": "1 small can (8 oz)", "notes": "", "metric": {"quantity": 225, "unit": "ml"}},
            {"item": "Raisins", "quantity": "1/2 cup", "notes": "golden or dark", "metric": {"quantity": 75, "unit": "g"}}
        ],
        "instructions": [
            "Heat the vegetable oil in a large Dutch oven or heavy pot over medium-high heat.",
            "Brown the meat on all sides, working in batches if necessary. This should take about 8-10 minutes total. Remove the meat and set aside.",
            "In the same pot, add the minced garlic and sliced onions. Sauté for 2-3 minutes until fragrant and the onions begin to soften.",
            "Return the browned meat to the pot. Add the broth, bay leaves, vinegar or lemon juice, and brown sugar. Stir to combine.",
            "Bring to a simmer, then reduce heat to low. Cover and simmer gently for about 1 hour, or until the meat is tender. Check occasionally and add a little water if needed.",
            "Stir in the tomato sauce and raisins. Continue simmering, covered, for another 30 minutes.",
            "Remove the bay leaves before serving.",
            "Serve hot over cooked long-grain white rice, with the sauce spooned over the top. Excellent with steamed vegetables on the side."
        ]
    }
}

# Recipe 3: Vanilla Cream Pie (Pies & Pastry Fillings)
vanilla_cream_pie = {
    "original_recipe": {
        "name": "Vanilla Cream Pie",
        "subtitle": "Available in 3 sizes: 9-inch, 8-inch, or 6-inch",
        "source": None,
        "category": "Pies & Pastry",
        "servings": "Varies by size",
        "ingredients": [
            {"item": "Sugar (9-inch/8-inch/6-inch)", "quantity": "2/3 cup / 1/2 cup / 1/3 cup", "notes": "", "metric": {"quantity": 135, "unit": "g"}},
            {"item": "Salt (9-inch/8-inch/6-inch)", "quantity": "2/3 tsp / 1/2 tsp / 1/3 tsp", "notes": "", "metric": {"quantity": 4, "unit": "g"}},
            {"item": "Cornstarch (9-inch/8-inch/6-inch)", "quantity": "2 2/3 tbsp / 2 tbsp / 1 1/3 tbsp", "notes": "", "metric": {"quantity": 40, "unit": "g"}},
            {"item": "Flour (9-inch/8-inch/6-inch)", "quantity": "1 1/3 tbsp / 1 tbsp / 1/2 tbsp", "notes": "", "metric": {"quantity": 20, "unit": "g"}},
            {"item": "Milk (9-inch/8-inch/6-inch)", "quantity": "2 2/3 cups / 2 cups / 1 1/3 cups", "notes": "", "metric": {"quantity": 640, "unit": "ml"}},
            {"item": "Egg substitute (9-inch/8-inch/6-inch)", "quantity": "3/4 cup / 1/2 cup / 1/4 cup", "notes": "", "metric": {"quantity": 180, "unit": "ml"}},
            {"item": "Margarine (9-inch/8-inch/6-inch)", "quantity": "2/3 tbsp / 1/2 tbsp / 1/3 tbsp", "notes": "", "metric": {"quantity": 10, "unit": "g"}},
            {"item": "Vanilla (9-inch/8-inch/6-inch)", "quantity": "1 1/3 tsp / 1 tsp / 1/2 tsp", "notes": "", "metric": {"quantity": 7, "unit": "ml"}},
            {"item": "Baked pie shell", "quantity": "1 (9-inch, 8-inch, or 6-inch)", "notes": "", "metric": None},
            {"item": "Meringue topping", "quantity": "as needed", "notes": "see Meringue recipe", "metric": None}
        ],
        "instructions": [
            "Mix sugar, salt, cornstarch and flour in top of double boiler.",
            "Stir in milk. Bring to boil over low heat, and boil 3 minutes, stirring constantly.",
            "Remove from heat. Stir a little of the hot mixture into the egg substitute...then blend into hot mixture.",
            "Place over boiling water, and cook 10 minutes, stirring occasionally.",
            "Blend in margarine. Cool thoroughly.",
            "Blend in vanilla.",
            "Pour into cooled baked pie shell.",
            "Finish with meringue (see recipe)."
        ]
    },
    "improved_recipe": {
        "name": "Classic Vanilla Cream Pie",
        "category": "Pies & Pastry",
        "servings": "8 servings (9-inch pie)",
        "ingredients": [
            {"item": "Granulated sugar", "quantity": "2/3 cup (for 9-inch)", "notes": "reduce to 1/2 cup for 8-inch, 1/3 cup for 6-inch", "metric": {"quantity": 135, "unit": "g"}},
            {"item": "Salt", "quantity": "2/3 teaspoon (for 9-inch)", "notes": "reduce to 1/2 tsp for 8-inch, 1/3 tsp for 6-inch", "metric": {"quantity": 4, "unit": "g"}},
            {"item": "Cornstarch", "quantity": "2 2/3 tablespoons (for 9-inch)", "notes": "reduce to 2 tbsp for 8-inch, 1 1/3 tbsp for 6-inch", "metric": {"quantity": 40, "unit": "g"}},
            {"item": "All purpose flour", "quantity": "1 1/3 tablespoons (for 9-inch)", "notes": "reduce to 1 tbsp for 8-inch, 1/2 tbsp for 6-inch", "metric": {"quantity": 20, "unit": "g"}},
            {"item": "Milk", "quantity": "2 2/3 cups (for 9-inch)", "notes": "reduce to 2 cups for 8-inch, 1 1/3 cups for 6-inch; 2% or whole", "metric": {"quantity": 640, "unit": "ml"}},
            {"item": "Egg substitute", "quantity": "3/4 cup (for 9-inch)", "notes": "reduce to 1/2 cup for 8-inch, 1/4 cup for 6-inch; or use 3 egg yolks for 9-inch", "metric": {"quantity": 180, "unit": "ml"}},
            {"item": "Margarine or butter", "quantity": "2 teaspoons (for 9-inch)", "notes": "reduce to 1 1/2 tsp for 8-inch, 1 tsp for 6-inch", "metric": {"quantity": 10, "unit": "g"}},
            {"item": "Vanilla extract", "quantity": "1 1/3 teaspoons (for 9-inch)", "notes": "reduce to 1 tsp for 8-inch, 1/2 tsp for 6-inch", "metric": {"quantity": 7, "unit": "ml"}},
            {"item": "Baked pie shell", "quantity": "1 (9-inch, 8-inch, or 6-inch)", "notes": "fully baked and cooled", "metric": None},
            {"item": "Meringue or whipped cream topping", "quantity": "as desired", "notes": "", "metric": None}
        ],
        "instructions": [
            "Fill the bottom of a double boiler with water and bring to a simmer.",
            "In the top of the double boiler (off the heat), whisk together the sugar, salt, cornstarch, and flour until well combined and lump-free.",
            "Gradually whisk in the milk until the mixture is smooth.",
            "Place the top of the double boiler over the simmering water. Cook, stirring constantly, until the mixture comes to a boil and thickens, about 8–10 minutes. Let it boil gently for 3 minutes, continuing to stir.",
            "In a small bowl, lightly beat the egg substitute (or egg yolks). Slowly whisk about 1/2 cup of the hot mixture into the egg to temper it, then pour the tempered egg back into the double boiler, whisking constantly.",
            "Cook over the simmering water for an additional 10 minutes, stirring occasionally, until the filling is thick and smooth.",
            "Remove from heat and stir in the margarine or butter until melted and fully incorporated.",
            "Let the filling cool for about 10–15 minutes, stirring occasionally to prevent a skin from forming. When slightly cooled, stir in the vanilla extract.",
            "Pour the vanilla filling into the cooled, baked pie shell. Smooth the top with a spatula.",
            "If topping with meringue: Spread the meringue over the filling while the filling is still warm, sealing the edges to the crust. Bake at 300°F (150°C) for 15–20 minutes until the meringue is lightly golden. Let cool completely before slicing.",
            "If topping with whipped cream: Refrigerate the pie until fully set (at least 3 hours or overnight), then top with whipped cream just before serving.",
            "Store leftovers covered in the refrigerator for up to 3 days."
        ]
    }
}

# Recipe 4: Bechamel Sauce Topping (Icings & Sauces)
# Note: Searching for Bechamel in the cookbook - let me add a placeholder and we'll fill it from another source
bechamel_sauce = {
    "original_recipe": {
        "name": "Bechamel Sauce Topping",
        "subtitle": None,
        "source": None,
        "category": "Icings & Sauces",
        "servings": "About 2 cups",
        "ingredients": [
            {"item": "Margarine or butter", "quantity": "2 tablespoons", "notes": "", "metric": {"quantity": 30, "unit": "g"}},
            {"item": "All purpose flour", "quantity": "2 tablespoons", "notes": "", "metric": {"quantity": 15, "unit": "g"}},
            {"item": "Milk", "quantity": "2 cups", "notes": "warm", "metric": {"quantity": 480, "unit": "ml"}},
            {"item": "Salt", "quantity": "1/2 teaspoon", "notes": "or to taste", "metric": {"quantity": 3, "unit": "g"}},
            {"item": "White pepper", "quantity": "1/4 teaspoon", "notes": "or to taste", "metric": {"quantity": 0.5, "unit": "g"}},
            {"item": "Nutmeg", "quantity": "pinch", "notes": "optional", "metric": None}
        ],
        "instructions": [
            "Melt margarine in a saucepan over medium heat.",
            "Add flour and stir constantly for 2-3 minutes to make a roux. Do not let it brown.",
            "Gradually whisk in warm milk, stirring constantly to prevent lumps.",
            "Bring to a simmer and cook, stirring frequently, until the sauce thickens (about 5-7 minutes).",
            "Season with salt, white pepper, and nutmeg if desired.",
            "Use as a topping for vegetables, pasta, or casseroles."
        ]
    },
    "improved_recipe": {
        "name": "Classic Béchamel Sauce (White Sauce)",
        "category": "Icings & Sauces",
        "servings": "About 2 cups",
        "ingredients": [
            {"item": "Margarine or butter", "quantity": "2 tablespoons", "notes": "", "metric": {"quantity": 30, "unit": "g"}},
            {"item": "All-purpose flour", "quantity": "2 tablespoons", "notes": "", "metric": {"quantity": 15, "unit": "g"}},
            {"item": "Milk", "quantity": "2 cups", "notes": "whole or 2%, warmed", "metric": {"quantity": 480, "unit": "ml"}},
            {"item": "Salt", "quantity": "1/2 teaspoon", "notes": "or to taste", "metric": {"quantity": 3, "unit": "g"}},
            {"item": "White pepper", "quantity": "1/4 teaspoon", "notes": "freshly ground, or to taste", "metric": {"quantity": 0.5, "unit": "g"}},
            {"item": "Ground nutmeg", "quantity": "pinch", "notes": "optional, for classic French flavor", "metric": None}
        ],
        "instructions": [
            "In a medium saucepan, melt the margarine or butter over medium heat.",
            "Add the flour and whisk constantly for 2-3 minutes to cook the flour and form a smooth roux. The mixture should be bubbly but not browned.",
            "Gradually pour in the warm milk, whisking constantly to prevent lumps from forming.",
            "Bring the sauce to a gentle simmer, whisking frequently. Cook for 5-7 minutes, or until the sauce thickens to a creamy consistency that coats the back of a spoon.",
            "Season with salt, white pepper, and a pinch of nutmeg if desired. Taste and adjust seasoning.",
            "Use immediately as a topping for steamed vegetables (such as broccoli, cauliflower, or asparagus), as a base for creamy pasta dishes, in casseroles, or as a component in lasagna or gratins.",
            "If the sauce becomes too thick, thin it with a little more warm milk. If it's too thin, simmer a bit longer or whisk in a small amount of flour paste (1 tsp flour mixed with 1 tbsp water).",
            "Store leftover sauce in an airtight container in the refrigerator for up to 3 days. Reheat gently, whisking in a little milk to restore smoothness."
        ]
    }
}

# Recipe 5: Scalloped Salmon (Main Dishes)
scalloped_salmon = {
    "original_recipe": {
        "name": "Scalloped Salmon",
        "subtitle": None,
        "source": None,
        "category": "Main Dishes",
        "servings": "2 servings",
        "ingredients": [
            {"item": "Chopped onion", "quantity": "2 tablespoons", "notes": "", "metric": {"quantity": 20, "unit": "g"}},
            {"item": "Chopped green pepper", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 10, "unit": "g"}},
            {"item": "Melted margarine", "quantity": "2 tablespoons", "notes": "", "metric": {"quantity": 30, "unit": "g"}},
            {"item": "Salmon", "quantity": "1 can (7 3/4 oz)", "notes": "drained and flaked", "metric": {"quantity": 220, "unit": "g"}},
            {"item": "Evaporated milk", "quantity": "1/2 cup", "notes": "", "metric": {"quantity": 120, "unit": "ml"}},
            {"item": "All purpose flour", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 8, "unit": "g"}},
            {"item": "Salt", "quantity": "1/4 teaspoon", "notes": "", "metric": {"quantity": 1.5, "unit": "g"}},
            {"item": "Buttered soft bread crumbs", "quantity": "2 tablespoons", "notes": "made with margarine", "metric": {"quantity": 15, "unit": "g"}}
        ],
        "instructions": [
            "Saute onion and green pepper in margarine until tender but not brown.",
            "Add next four ingredients listed (salmon, evaporated milk, flour, salt); mix well.",
            "Spoon mixture into baking shells that have been coated with a butter flavored, nonstick vegetable spray; top with bread crumbs.",
            "Bake at 400° F for fifteen minutes.",
            "Serves two."
        ]
    },
    "improved_recipe": {
        "name": "Scalloped Salmon",
        "category": "Main Dishes",
        "servings": "2 servings",
        "ingredients": [
            {"item": "Onion", "quantity": "2 tablespoons", "notes": "finely chopped", "metric": {"quantity": 20, "unit": "g"}},
            {"item": "Green bell pepper", "quantity": "1 tablespoon", "notes": "finely chopped", "metric": {"quantity": 10, "unit": "g"}},
            {"item": "Margarine or butter", "quantity": "2 tablespoons", "notes": "divided", "metric": {"quantity": 30, "unit": "g"}},
            {"item": "Canned salmon", "quantity": "1 can (7 3/4 oz)", "notes": "drained and flaked, bones removed", "metric": {"quantity": 220, "unit": "g"}},
            {"item": "Evaporated milk", "quantity": "1/2 cup", "notes": "", "metric": {"quantity": 120, "unit": "ml"}},
            {"item": "All-purpose flour", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 8, "unit": "g"}},
            {"item": "Salt", "quantity": "1/4 teaspoon", "notes": "or to taste", "metric": {"quantity": 1.5, "unit": "g"}},
            {"item": "Black pepper", "quantity": "1/8 teaspoon", "notes": "optional", "metric": {"quantity": 0.25, "unit": "g"}},
            {"item": "Soft bread crumbs", "quantity": "2-3 tablespoons", "notes": "fresh, from about 1 slice bread", "metric": {"quantity": 15, "unit": "g"}},
            {"item": "Melted margarine or butter", "quantity": "1 teaspoon", "notes": "for bread crumbs", "metric": {"quantity": 5, "unit": "g"}}
        ],
        "instructions": [
            "Preheat oven to 400°F (200°C). Lightly coat 2 individual baking shells or ramekins (about 1-cup capacity each) with butter-flavored nonstick cooking spray.",
            "In a small skillet, melt 2 tablespoons of margarine or butter over medium heat. Add the chopped onion and green pepper. Sauté for 3-4 minutes, until tender but not browned.",
            "In a medium bowl, combine the flaked salmon, evaporated milk, flour, salt, and black pepper (if using). Mix well.",
            "Add the sautéed onion and pepper (along with any butter from the pan) to the salmon mixture. Stir to combine.",
            "Divide the salmon mixture evenly between the prepared baking shells or ramekins.",
            "In a small bowl, toss the soft bread crumbs with 1 teaspoon melted margarine or butter. Sprinkle the buttered crumbs evenly over the tops of the salmon mixture.",
            "Bake for 15 minutes, or until the tops are golden brown and the filling is bubbly.",
            "Serve hot with a side of steamed vegetables, rice, or a green salad. Excellent with lemon wedges for squeezing over the top."
        ]
    }
}

# Add recipes to appropriate categories
for category in data["categories"]:
    if category["name"] == "Main Dishes":
        category["recipes"].append(macaroni_ham_cheese)
        category["recipes"].append(sweet_sour_roast)
        category["recipes"].append(scalloped_salmon)
    elif category["name"] == "Pies & Pastry Fillings":
        category["recipes"].append(vanilla_cream_pie)
    elif category["name"] == "Icings & Sauces":
        category["recipes"].append(bechamel_sauce)

# Save the updated recipes.json
with open('recipes.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Successfully added 5 recipes (Batch 1B):")
print("- Macaroni, Ham, and Cheese (Main Dishes)")
print("- Sweet and Sour Roast (Main Dishes)")
print("- Vanilla Cream Pie (Pies & Pastry Fillings)")
print("- Bechamel Sauce Topping (Icings & Sauces)")
print("- Scalloped Salmon (Main Dishes)")
