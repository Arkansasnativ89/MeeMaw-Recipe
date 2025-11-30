import json

# Load the current recipes.json
with open('recipes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Recipe 1: Chicken Brown Rice Bake (Main Dishes)
chicken_brown_rice = {
    "original_recipe": {
        "name": "Chicken Brown Rice Bake",
        "subtitle": None,
        "source": None,
        "category": "Main Dishes",
        "servings": "6-8 servings",
        "ingredients": [
            {"item": "Chopped onion", "quantity": "1/2 cup", "notes": "", "metric": {"quantity": 80, "unit": "g"}},
            {"item": "Vegetable oil", "quantity": "2 tablespoons", "notes": "", "metric": {"quantity": 30, "unit": "ml"}},
            {"item": "Curry powder", "quantity": "2 teaspoons", "notes": "", "metric": {"quantity": 4, "unit": "g"}},
            {"item": "Chicken broth, de-fatted", "quantity": "3 cups", "notes": "", "metric": {"quantity": 720, "unit": "ml"}},
            {"item": "Uncooked brown rice", "quantity": "1 cup", "notes": "", "metric": {"quantity": 195, "unit": "g"}},
            {"item": "Frozen mixed vegetables", "quantity": "1 package (16 oz)", "notes": "", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Chopped cooked chicken and/or turkey", "quantity": "2 cups", "notes": "", "metric": {"quantity": 280, "unit": "g"}},
            {"item": "Water or chicken broth", "quantity": "1 cup", "notes": "recommended addition", "metric": {"quantity": 240, "unit": "ml"}}
        ],
        "instructions": [
            "Saute onion in oil until crisp-tender. Add curry powder, and cook one minute, stirring constantly.",
            "Add chicken broth; bring mixture to a boil. Cover, reduce heat, and simmer fifteen minutes.",
            "Stir in rice; cover and cook over heat fifty minutes or more until liquid is absorbed.",
            "Stir in vegetables and chicken. (Note: while original recipe does not call for it, at this point it is recommended that a cup of water or chicken broth be added. Otherwise, the rice will be a little too firm).",
            "Spoon into a 12\"x8\"x2\" baking dish that has been coated with a nonstick vegetable spray.",
            "Cover and bake at 350° F for 30 to 35 minutes."
        ]
    },
    "improved_recipe": {
        "name": "Curried Chicken and Brown Rice Bake",
        "category": "Main Dishes",
        "servings": "6-8 servings",
        "ingredients": [
            {"item": "Yellow onion", "quantity": "1/2 cup, chopped", "notes": "", "metric": {"quantity": 80, "unit": "g"}},
            {"item": "Vegetable oil", "quantity": "2 tablespoons", "notes": "", "metric": {"quantity": 30, "unit": "ml"}},
            {"item": "Curry powder", "quantity": "2 teaspoons", "notes": "adjust to taste", "metric": {"quantity": 4, "unit": "g"}},
            {"item": "Low-sodium chicken broth", "quantity": "3 cups", "notes": "fat skimmed off", "metric": {"quantity": 720, "unit": "ml"}},
            {"item": "Brown rice", "quantity": "1 cup, uncooked", "notes": "", "metric": {"quantity": 195, "unit": "g"}},
            {"item": "Frozen mixed vegetables", "quantity": "16 ounces (1 bag)", "notes": "carrots, peas, corn, green beans", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Cooked chicken or turkey", "quantity": "2 cups, chopped", "notes": "about 1 lb", "metric": {"quantity": 280, "unit": "g"}},
            {"item": "Additional chicken broth or water", "quantity": "1 cup", "notes": "recommended for better texture", "metric": {"quantity": 240, "unit": "ml"}}
        ],
        "instructions": [
            "Preheat oven to 350°F (175°C). Coat a 12x8x2-inch baking dish with nonstick cooking spray.",
            "In a large skillet or saucepan, heat the vegetable oil over medium heat. Add the chopped onion and sauté for 3-4 minutes, until crisp-tender.",
            "Stir in the curry powder and cook for 1 minute, stirring constantly. This blooms the curry spices and enhances their flavor.",
            "Add the 3 cups of chicken broth and bring to a boil. Cover, reduce heat to low, and simmer for 15 minutes.",
            "Stir in the uncooked brown rice. Cover and continue to cook over low heat for 50-60 minutes, or until the liquid is mostly absorbed and the rice is tender. Check occasionally and add a bit more liquid if needed.",
            "Once the rice is cooked, stir in the frozen mixed vegetables, chopped chicken (or turkey), and the additional 1 cup of broth or water. Mix well.",
            "Transfer the mixture to the prepared baking dish and spread evenly.",
            "Cover tightly with foil and bake for 30-35 minutes, or until heated through and the vegetables are tender.",
            "Let stand for 5 minutes before serving. This dish pairs well with a crisp salad and crusty bread."
        ]
    }
}

# Recipe 2: Chicken Casserole (Main Dishes)
chicken_casserole = {
    "original_recipe": {
        "name": "Chicken Casserole",
        "subtitle": "Vocla Poulet Denomandine",
        "source": None,
        "category": "Main Dishes",
        "servings": "8-10 servings",
        "ingredients": [
            {"item": "Seasoned bread stuffing", "quantity": "1 package (14 oz)", "notes": "", "metric": {"quantity": 396, "unit": "g"}},
            {"item": "Margarine", "quantity": "1 stick", "notes": "", "metric": {"quantity": 113, "unit": "g"}},
            {"item": "Water", "quantity": "1/4 cup", "notes": "", "metric": {"quantity": 60, "unit": "ml"}},
            {"item": "Cooked chicken, diced", "quantity": "2 1/2 cups", "notes": "", "metric": {"quantity": 350, "unit": "g"}},
            {"item": "Chopped onion", "quantity": "1/2 cup", "notes": "", "metric": {"quantity": 80, "unit": "g"}},
            {"item": "Chopped green onion or chives", "quantity": "1/4 cup", "notes": "", "metric": {"quantity": 25, "unit": "g"}},
            {"item": "Chopped celery", "quantity": "1/2 cup", "notes": "", "metric": {"quantity": 60, "unit": "g"}},
            {"item": "Mayonnaise", "quantity": "1/2 cup", "notes": "", "metric": {"quantity": 120, "unit": "ml"}},
            {"item": "Salt", "quantity": "3/4 teaspoon", "notes": "", "metric": {"quantity": 4.5, "unit": "g"}},
            {"item": "Eggs", "quantity": "2", "notes": "or egg substitute", "metric": {"quantity": 100, "unit": "g"}},
            {"item": "Milk", "quantity": "1 1/2 cups", "notes": "", "metric": {"quantity": 360, "unit": "ml"}},
            {"item": "Condensed cream of mushroom soup", "quantity": "2 cans", "notes": "", "metric": {"quantity": 640, "unit": "g"}}
        ],
        "instructions": [
            "Mix together bread stuffing, margarine and water. Put one-half of the mixture in a 9\" x 13\" casserole that has been coated with a nonstick vegetable spray.",
            "Mix together chicken, onion, chives, celery, mayonnaise and salt. Put in casserole over bread mixture, then top with remaining bread mixture.",
            "Beat eggs slightly, and add milk. Stir. Pour this mixture evenly over bread mixture.",
            "Cover with foil and refrigerate overnight.",
            "Take out one hour before baking. Spread the cream of mushroom soup over the top.",
            "Bake uncovered in oven at 325° F for one hour."
        ]
    },
    "improved_recipe": {
        "name": "Classic Chicken Casserole (Make-Ahead)",
        "category": "Main Dishes",
        "servings": "8-10 servings",
        "ingredients": [
            {"item": "Seasoned bread stuffing mix", "quantity": "14 ounces (1 package)", "notes": "", "metric": {"quantity": 396, "unit": "g"}},
            {"item": "Margarine or butter", "quantity": "1/2 cup (1 stick)", "notes": "melted", "metric": {"quantity": 113, "unit": "g"}},
            {"item": "Water", "quantity": "1/4 cup", "notes": "", "metric": {"quantity": 60, "unit": "ml"}},
            {"item": "Cooked chicken", "quantity": "2 1/2 cups, diced", "notes": "about 1 lb cooked", "metric": {"quantity": 350, "unit": "g"}},
            {"item": "Yellow onion", "quantity": "1/2 cup, chopped", "notes": "", "metric": {"quantity": 80, "unit": "g"}},
            {"item": "Green onions or fresh chives", "quantity": "1/4 cup, chopped", "notes": "", "metric": {"quantity": 25, "unit": "g"}},
            {"item": "Celery", "quantity": "1/2 cup, chopped", "notes": "", "metric": {"quantity": 60, "unit": "g"}},
            {"item": "Mayonnaise", "quantity": "1/2 cup", "notes": "can use light mayo", "metric": {"quantity": 120, "unit": "ml"}},
            {"item": "Salt", "quantity": "3/4 teaspoon", "notes": "", "metric": {"quantity": 4.5, "unit": "g"}},
            {"item": "Eggs", "quantity": "2 large", "notes": "or 1/2 cup egg substitute", "metric": {"quantity": 100, "unit": "g"}},
            {"item": "Milk", "quantity": "1 1/2 cups", "notes": "", "metric": {"quantity": 360, "unit": "ml"}},
            {"item": "Condensed cream of mushroom soup", "quantity": "2 cans (10.5 oz each)", "notes": "can use reduced-fat", "metric": {"quantity": 640, "unit": "g"}}
        ],
        "instructions": [
            "Coat a 9x13-inch baking dish with nonstick cooking spray.",
            "In a large bowl, combine the bread stuffing mix, melted margarine, and 1/4 cup water. Toss until the stuffing is moistened.",
            "Spread half of the stuffing mixture evenly in the bottom of the prepared baking dish.",
            "In another bowl, combine the diced chicken, chopped onion, green onions (or chives), celery, mayonnaise, and salt. Mix well.",
            "Spread the chicken mixture evenly over the stuffing layer in the casserole dish.",
            "Top with the remaining stuffing mixture, spreading it evenly.",
            "In a medium bowl, lightly beat the eggs. Whisk in the milk until well combined.",
            "Pour the egg-milk mixture evenly over the entire casserole, trying to moisten all areas.",
            "Cover the dish tightly with aluminum foil and refrigerate overnight (or for at least 4 hours).",
            "When ready to bake, remove the casserole from the refrigerator and let it sit at room temperature for 1 hour.",
            "Preheat oven to 325°F (165°C).",
            "Spread the 2 cans of cream of mushroom soup evenly over the top of the casserole.",
            "Bake uncovered for 1 hour, or until the casserole is hot and bubbly and the top is lightly browned.",
            "Let stand for 10 minutes before serving. This is a perfect make-ahead dish for entertaining!"
        ]
    }
}

# Recipe 3: Chicken Rice Casserole (Main Dishes)
chicken_rice_casserole = {
    "original_recipe": {
        "name": "Chicken Rice Casserole",
        "subtitle": None,
        "source": None,
        "category": "Main Dishes",
        "servings": "8 servings",
        "ingredients": [
            {"item": "Chicken breasts", "quantity": "8", "notes": "or whole fryer", "metric": None},
            {"item": "Cream of mushroom soup", "quantity": "1 can", "notes": "", "metric": {"quantity": 320, "unit": "g"}},
            {"item": "Cream of chicken or celery soup", "quantity": "1 can", "notes": "", "metric": {"quantity": 320, "unit": "g"}},
            {"item": "Water", "quantity": "2 soup cans", "notes": "", "metric": {"quantity": 640, "unit": "ml"}},
            {"item": "Margarine, melted", "quantity": "1 stick", "notes": "", "metric": {"quantity": 113, "unit": "g"}},
            {"item": "Uncooked rice", "quantity": "1 1/2 cups", "notes": "", "metric": {"quantity": 300, "unit": "g"}}
        ],
        "instructions": [
            "Mix soups and water, stir in rice in large casserole dish or baking pan that has been coated with a nonstick vegetable oil.",
            "Place chicken, dipped in melted margarine, on top, and cover.",
            "Cook at 300° F about 2 hours.",
            "Uncover and brown."
        ]
    },
    "improved_recipe": {
        "name": "Easy Chicken and Rice Casserole",
        "category": "Main Dishes",
        "servings": "8 servings",
        "ingredients": [
            {"item": "Chicken breasts", "quantity": "8 pieces", "notes": "bone-in or boneless, or 1 whole fryer cut up", "metric": None},
            {"item": "Condensed cream of mushroom soup", "quantity": "1 can (10.5 oz)", "notes": "", "metric": {"quantity": 320, "unit": "g"}},
            {"item": "Condensed cream of chicken or celery soup", "quantity": "1 can (10.5 oz)", "notes": "", "metric": {"quantity": 320, "unit": "g"}},
            {"item": "Water", "quantity": "2 2/3 cups (2 soup cans)", "notes": "", "metric": {"quantity": 640, "unit": "ml"}},
            {"item": "Long-grain white rice", "quantity": "1 1/2 cups, uncooked", "notes": "", "metric": {"quantity": 300, "unit": "g"}},
            {"item": "Margarine or butter", "quantity": "1/2 cup (1 stick)", "notes": "melted", "metric": {"quantity": 113, "unit": "g"}},
            {"item": "Salt and pepper", "quantity": "to taste", "notes": "", "metric": None}
        ],
        "instructions": [
            "Preheat oven to 300°F (150°C). Coat a large 9x13-inch casserole dish or baking pan with nonstick cooking spray.",
            "In a large bowl, whisk together the cream of mushroom soup, cream of chicken (or celery) soup, and 2 soup cans of water until smooth.",
            "Stir the uncooked rice into the soup mixture until well combined.",
            "Pour the rice and soup mixture into the prepared casserole dish and spread evenly.",
            "Dip each piece of chicken in the melted margarine, coating both sides. Season the chicken with salt and pepper to taste.",
            "Arrange the chicken pieces on top of the rice mixture in a single layer.",
            "Cover the dish tightly with aluminum foil.",
            "Bake for about 2 hours, or until the chicken is cooked through (internal temperature of 165°F) and the rice is tender.",
            "Remove the foil during the last 15-20 minutes of baking to allow the chicken to brown on top.",
            "Let stand for 5-10 minutes before serving. The rice will absorb the flavorful juices from the chicken and soup."
        ]
    }
}

# Recipe 4: Jumbo Shells No. 1 (Main Dishes)
jumbo_shells_1 = {
    "original_recipe": {
        "name": "Jumbo Shells No. 1",
        "subtitle": "Spinach-Ricotta",
        "source": None,
        "category": "Main Dishes",
        "servings": "20 shells",
        "ingredients": [
            {"item": "Fresh spinach", "quantity": "1 lb", "notes": "", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Chopped onion", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 10, "unit": "g"}},
            {"item": "Margarine", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 15, "unit": "g"}},
            {"item": "Egg", "quantity": "1, beaten", "notes": "or egg substitute", "metric": {"quantity": 50, "unit": "g"}},
            {"item": "Ricotta cheese", "quantity": "2/3 cup", "notes": "", "metric": {"quantity": 165, "unit": "g"}},
            {"item": "Grated Parmesan cheese", "quantity": "1/2 cup", "notes": "", "metric": {"quantity": 50, "unit": "g"}},
            {"item": "Ground nutmeg", "quantity": "1/8 teaspoon", "notes": "", "metric": {"quantity": 0.25, "unit": "g"}},
            {"item": "Tomato sauce", "quantity": "1 recipe", "notes": "", "metric": None},
            {"item": "Jumbo pasta shells", "quantity": "20", "notes": "cooked", "metric": None}
        ],
        "instructions": [
            "In a large saucepan combine the fresh spinach with a small amount of water. Simmer, covered for 3 to 5 minutes. Drain well. Squeeze the spinach to remove excess moisture. Chop spinach.",
            "In a skillet cook onion in margarine till tender but not brown. Add spinach; heat through.",
            "Combine egg, ricotta, Parmesan, nutmeg and spinach mixture.",
            "Pour half of the sauce in a baking dish. Stuff (20) shells with filling, arrange in dish and top with remaining sauce.",
            "Bake in 350° oven 30 minutes."
        ]
    },
    "improved_recipe": {
        "name": "Spinach and Ricotta Stuffed Shells",
        "category": "Main Dishes",
        "servings": "20 stuffed shells (6-8 servings)",
        "ingredients": [
            {"item": "Fresh spinach", "quantity": "1 pound", "notes": "or 10 oz frozen chopped spinach, thawed", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Yellow onion", "quantity": "1 tablespoon, chopped", "notes": "", "metric": {"quantity": 10, "unit": "g"}},
            {"item": "Margarine or butter", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 15, "unit": "g"}},
            {"item": "Egg", "quantity": "1 large, beaten", "notes": "or 1/4 cup egg substitute", "metric": {"quantity": 50, "unit": "g"}},
            {"item": "Ricotta cheese", "quantity": "2/3 cup", "notes": "part-skim or whole milk", "metric": {"quantity": 165, "unit": "g"}},
            {"item": "Grated Parmesan cheese", "quantity": "1/2 cup", "notes": "", "metric": {"quantity": 50, "unit": "g"}},
            {"item": "Ground nutmeg", "quantity": "1/8 teaspoon", "notes": "", "metric": {"quantity": 0.25, "unit": "g"}},
            {"item": "Jumbo pasta shells", "quantity": "20", "notes": "cooked according to package directions", "metric": None},
            {"item": "Marinara or tomato sauce", "quantity": "3-4 cups", "notes": "homemade or jarred", "metric": {"quantity": 750, "unit": "ml"}}
        ],
        "instructions": [
            "Cook the jumbo pasta shells according to package directions until al dente. Drain and set aside.",
            "If using fresh spinach: In a large saucepan, combine the spinach with 2-3 tablespoons of water. Cover and simmer for 3-5 minutes until wilted. Drain well and squeeze out as much excess moisture as possible. Chop finely.",
            "If using frozen spinach: Thaw completely and squeeze out all excess moisture. Chop if pieces are large.",
            "In a small skillet, melt the margarine over medium heat. Add the chopped onion and cook for 3-4 minutes, until tender but not browned.",
            "Add the chopped spinach to the skillet and stir to combine. Heat through for 1-2 minutes. Remove from heat.",
            "In a medium bowl, combine the beaten egg, ricotta cheese, Parmesan cheese, nutmeg, and the spinach-onion mixture. Mix well.",
            "Preheat oven to 350°F (175°C).",
            "Spread half of the tomato sauce in the bottom of a 9x13-inch baking dish.",
            "Carefully stuff each cooked shell with about 2 tablespoons of the spinach-ricotta filling. Arrange the stuffed shells in the baking dish in a single layer.",
            "Pour the remaining tomato sauce over the top of the shells, covering them evenly.",
            "Cover the dish with aluminum foil and bake for 30 minutes, or until hot and bubbly.",
            "Let stand for 5 minutes before serving. Garnish with additional Parmesan cheese if desired."
        ]
    }
}

# Recipe 5: Jumbo Shells No. 2 (Main Dishes)
jumbo_shells_2 = {
    "original_recipe": {
        "name": "Jumbo Shells No. 2",
        "subtitle": "Meat Filling",
        "source": None,
        "category": "Main Dishes",
        "servings": "20 shells",
        "ingredients": [
            {"item": "Ground beef or chicken", "quantity": "1 lb", "notes": "", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Egg", "quantity": "1, beaten", "notes": "or egg substitute", "metric": {"quantity": 50, "unit": "g"}},
            {"item": "Grated Parmesan cheese", "quantity": "1/4 cup", "notes": "", "metric": {"quantity": 25, "unit": "g"}},
            {"item": "Chopped parsley", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 4, "unit": "g"}},
            {"item": "Salt and pepper", "quantity": "to taste", "notes": "", "metric": None},
            {"item": "Tomato sauce", "quantity": "1 recipe", "notes": "", "metric": None},
            {"item": "DaVinci Seasoned Bread Crumbs", "quantity": "1/4 cup", "notes": "", "metric": {"quantity": 30, "unit": "g"}},
            {"item": "Jumbo pasta shells", "quantity": "20", "notes": "cooked", "metric": None}
        ],
        "instructions": [
            "Saute chopped meat in olive oil until brown.",
            "Mix with egg, or egg substitute, cheese, bread crumbs, parsley, salt and pepper.",
            "Pour half of the sauce in a baking dish. Stuff (20) shells with filling, arrange in dish and top with remaining sauce.",
            "Bake in 350° oven 30 minutes."
        ]
    },
    "improved_recipe": {
        "name": "Meat-Stuffed Jumbo Shells",
        "category": "Main Dishes",
        "servings": "20 stuffed shells (6-8 servings)",
        "ingredients": [
            {"item": "Ground beef or ground chicken", "quantity": "1 pound", "notes": "lean", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Olive oil", "quantity": "1 tablespoon", "notes": "for sautéing", "metric": {"quantity": 15, "unit": "ml"}},
            {"item": "Egg", "quantity": "1 large, beaten", "notes": "or 1/4 cup egg substitute", "metric": {"quantity": 50, "unit": "g"}},
            {"item": "Grated Parmesan cheese", "quantity": "1/4 cup", "notes": "", "metric": {"quantity": 25, "unit": "g"}},
            {"item": "Italian seasoned bread crumbs", "quantity": "1/4 cup", "notes": "", "metric": {"quantity": 30, "unit": "g"}},
            {"item": "Fresh parsley", "quantity": "1 tablespoon, chopped", "notes": "", "metric": {"quantity": 4, "unit": "g"}},
            {"item": "Salt", "quantity": "1/2 teaspoon", "notes": "or to taste", "metric": {"quantity": 3, "unit": "g"}},
            {"item": "Black pepper", "quantity": "1/4 teaspoon", "notes": "or to taste", "metric": {"quantity": 0.5, "unit": "g"}},
            {"item": "Jumbo pasta shells", "quantity": "20", "notes": "cooked according to package directions", "metric": None},
            {"item": "Marinara or tomato sauce", "quantity": "3-4 cups", "notes": "homemade or jarred", "metric": {"quantity": 750, "unit": "ml"}}
        ],
        "instructions": [
            "Cook the jumbo pasta shells according to package directions until al dente. Drain and set aside.",
            "In a large skillet, heat the olive oil over medium-high heat. Add the ground beef (or chicken) and sauté, breaking it up with a spoon, until fully browned and cooked through, about 8-10 minutes.",
            "Drain any excess fat from the cooked meat and transfer it to a mixing bowl. Let cool slightly.",
            "To the cooled meat, add the beaten egg, Parmesan cheese, bread crumbs, chopped parsley, salt, and pepper. Mix well until all ingredients are thoroughly combined.",
            "Preheat oven to 350°F (175°C).",
            "Spread half of the tomato sauce in the bottom of a 9x13-inch baking dish.",
            "Carefully stuff each cooked shell with about 2 tablespoons of the meat filling. Arrange the stuffed shells in the baking dish in a single layer.",
            "Pour the remaining tomato sauce over the top of the shells, covering them evenly.",
            "Cover the dish with aluminum foil and bake for 30 minutes, or until hot and bubbly.",
            "Let stand for 5 minutes before serving. These can be served with a side salad and garlic bread for a complete meal."
        ]
    }
}

# Add recipes to appropriate categories
for category in data["categories"]:
    if category["name"] == "Main Dishes":
        category["recipes"].append(chicken_brown_rice)
        category["recipes"].append(chicken_casserole)
        category["recipes"].append(chicken_rice_casserole)
        category["recipes"].append(jumbo_shells_1)
        category["recipes"].append(jumbo_shells_2)

# Save the updated recipes.json
with open('recipes.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Successfully added 5 recipes (Batch 2C):")
print("- Chicken Brown Rice Bake (Main Dishes)")
print("- Chicken Casserole (Main Dishes)")
print("- Chicken Rice Casserole (Main Dishes)")
print("- Jumbo Shells No. 1 (Main Dishes)")
print("- Jumbo Shells No. 2 (Main Dishes)")
