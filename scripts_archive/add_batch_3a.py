import json

# Load current recipes
with open('recipes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Recipe 1: Chili
chili = {
    "original_recipe": {
        "name": "Chili",
        "subtitle": None,
        "source": None,
        "category": "Main Dishes",
        "servings": None,
        "ingredients": [
            {
                "item": "Chicken breast",
                "quantity": "As needed",
                "notes": "cooked and diced",
                "metric": None
            },
            {
                "item": "Lean chuck",
                "quantity": "As needed",
                "notes": "cooked and diced",
                "metric": None
            },
            {
                "item": "Kidney beans",
                "quantity": "2 cans (15 oz each)",
                "notes": "drained and rinsed",
                "metric": {
                    "quantity": 850,
                    "unit": "g"
                }
            },
            {
                "item": "Diced tomatoes",
                "quantity": "2 cans (14.5 oz each)",
                "notes": "",
                "metric": {
                    "quantity": 820,
                    "unit": "g"
                }
            },
            {
                "item": "Tomato sauce",
                "quantity": "1 can (8 oz)",
                "notes": "",
                "metric": {
                    "quantity": 227,
                    "unit": "g"
                }
            },
            {
                "item": "Onion",
                "quantity": "1 large",
                "notes": "diced",
                "metric": {
                    "quantity": 1,
                    "unit": "large onion"
                }
            },
            {
                "item": "Chili powder",
                "quantity": "2-3 tablespoons",
                "notes": "to taste",
                "metric": {
                    "min": 30,
                    "max": 45,
                    "unit": "ml"
                }
            },
            {
                "item": "Cumin",
                "quantity": "1 tablespoon",
                "notes": "",
                "metric": {
                    "quantity": 15,
                    "unit": "ml"
                }
            },
            {
                "item": "Garlic powder",
                "quantity": "1 teaspoon",
                "notes": "",
                "metric": {
                    "quantity": 5,
                    "unit": "ml"
                }
            },
            {
                "item": "Salt and pepper",
                "quantity": "To taste",
                "notes": "",
                "metric": None
            }
        ],
        "instructions": [
            "In a large pot, combine cooked chicken and beef.",
            "Add kidney beans, diced tomatoes, and tomato sauce.",
            "Stir in diced onion, chili powder, cumin, and garlic powder.",
            "Season with salt and pepper to taste.",
            "Simmer over medium-low heat for 30-45 minutes, stirring occasionally.",
            "Serve hot with cornbread or crackers."
        ]
    },
    "improved_recipe": {
        "name": "MeeMaw's Chili",
        "category": "Main Dishes",
        "servings": "6-8 servings",
        "ingredients": [
            {
                "item": "Boneless chicken breast",
                "quantity": "1 pound",
                "notes": "cooked and diced",
                "metric": {
                    "quantity": 454,
                    "unit": "g"
                }
            },
            {
                "item": "Lean ground chuck",
                "quantity": "1 pound",
                "notes": "browned and drained",
                "metric": {
                    "quantity": 454,
                    "unit": "g"
                }
            },
            {
                "item": "Kidney beans",
                "quantity": "2 cans (15 oz each)",
                "notes": "drained and rinsed",
                "metric": {
                    "quantity": 850,
                    "unit": "g"
                }
            },
            {
                "item": "Diced tomatoes",
                "quantity": "2 cans (14.5 oz each)",
                "notes": "with juices",
                "metric": {
                    "quantity": 820,
                    "unit": "g"
                }
            },
            {
                "item": "Tomato sauce",
                "quantity": "1 can (8 oz)",
                "notes": "",
                "metric": {
                    "quantity": 227,
                    "unit": "g"
                }
            },
            {
                "item": "Large onion",
                "quantity": "1",
                "notes": "diced",
                "metric": {
                    "quantity": 1,
                    "unit": "large onion"
                }
            },
            {
                "item": "Chili powder",
                "quantity": "2-3 tablespoons",
                "notes": "adjust to taste",
                "metric": {
                    "min": 30,
                    "max": 45,
                    "unit": "ml"
                }
            },
            {
                "item": "Ground cumin",
                "quantity": "1 tablespoon",
                "notes": "",
                "metric": {
                    "quantity": 15,
                    "unit": "ml"
                }
            },
            {
                "item": "Garlic powder",
                "quantity": "1 teaspoon",
                "notes": "",
                "metric": {
                    "quantity": 5,
                    "unit": "ml"
                }
            },
            {
                "item": "Salt",
                "quantity": "1 teaspoon",
                "notes": "or to taste",
                "metric": {
                    "quantity": 5,
                    "unit": "ml"
                }
            },
            {
                "item": "Black pepper",
                "quantity": "1/2 teaspoon",
                "notes": "or to taste",
                "metric": {
                    "quantity": 2.5,
                    "unit": "ml"
                }
            }
        ],
        "instructions": [
            "In a large pot or Dutch oven, brown the ground chuck over medium-high heat until fully cooked. Drain excess fat.",
            "Add the diced cooked chicken to the pot.",
            "Stir in the kidney beans, diced tomatoes (with their juices), and tomato sauce.",
            "Add the diced onion, chili powder, cumin, and garlic powder. Stir well to combine.",
            "Season with salt and pepper to taste.",
            "Bring the mixture to a boil, then reduce heat to low.",
            "Cover and simmer for 30-45 minutes, stirring occasionally to prevent sticking.",
            "Taste and adjust seasonings as needed.",
            "Serve hot with cornbread, crackers, or over rice. Top with shredded cheese, sour cream, or chopped green onions if desired.",
            "Note: A favorite of all the grandchildren: Becca, Drew, Alex, Hunter, and Chris."
        ]
    }
}

# Recipe 2: Dinner Roll Shapes
dinner_roll_shapes = {
    "original_recipe": {
        "name": "Dinner Roll Shapes",
        "subtitle": "Cloverleaf, Crescents, Parkerhouse, and Fantans",
        "source": None,
        "category": "Breads & Breakfast",
        "servings": "Variable",
        "ingredients": [
            {
                "item": "Dinner roll dough",
                "quantity": "1 recipe",
                "notes": "such as Basic Sweet Dough or Dinner Rolls",
                "metric": None
            },
            {
                "item": "Margarine or butter",
                "quantity": "As needed",
                "notes": "for brushing",
                "metric": None
            },
            {
                "item": "Nonstick vegetable spray",
                "quantity": "As needed",
                "notes": "",
                "metric": None
            }
        ],
        "instructions": [
            "Cloverleaf Rolls: Form dough into little balls about 1/2\" in diameter. Coat with a nonstick vegetable spray and place three balls in each muffin cup for each cloverleaf.",
            "Crescents: Roll out the dough to a scant 1/4\" thickness. Cut wedges from a six inch circle. Or, roll dough into a rectangle three inches wide, cut into squares, and make triangles by slicing diagonally. Brush with butter flavored oil, or margarine. Roll up the triangles, starting with the wide end, and curve into crescents.",
            "Parkerhouse Rolls: Roll dough out to a thickness of 1/4\". Cut with a three inch biscuit cutter. Make a depression with a spoon just below the center of each circle. Brush with margarine or coat with a butter flavored nonstick vegetable spray, and fold over from the top envelope fashion. The lower part with the depression should be larger than the upper portion.",
            "Fantans: Roll out the dough into an 1/8\" thick rectangle. Cut into one-inch strips. Brush with margarine or coat with butter flavored nonstick vegetable spray. Pile six or seven strips one on top of the other. Cut pieces about 1 & 1/4\" long and place in muffin cups (that have been coated with a nonstick vegetable spray) with the cut sides up. They will open out in a fan shape as they bake."
        ]
    },
    "improved_recipe": {
        "name": "Dinner Roll Shapes (Cloverleaf, Crescents, etc.)",
        "category": "Breads & Breakfast",
        "servings": "Varies by shape",
        "ingredients": [
            {
                "item": "Prepared dinner roll dough",
                "quantity": "1 batch",
                "notes": "from Basic Sweet Dough or Dinner Rolls recipe",
                "metric": None
            },
            {
                "item": "Softened margarine or butter",
                "quantity": "2-4 tablespoons",
                "notes": "for brushing",
                "metric": {
                    "min": 30,
                    "max": 60,
                    "unit": "ml"
                }
            },
            {
                "item": "Nonstick vegetable spray",
                "quantity": "As needed",
                "notes": "",
                "metric": None
            }
        ],
        "instructions": [
            "Prepare your favorite dinner roll dough recipe and let it rise until doubled.",
            "Punch down the dough and divide as needed for the shapes you wish to make.",
            "FOR CLOVERLEAF ROLLS: Pinch off small pieces of dough and roll into balls about 1/2 inch in diameter. Lightly spray muffin cups with nonstick spray. Place 3 balls in each muffin cup to form a cloverleaf shape. Let rise until doubled, then bake at 375°F (190°C) for 12-15 minutes until golden.",
            "FOR CRESCENT ROLLS: Roll dough to 1/4-inch thickness. Cut into 6-inch circles, then cut each circle into 6 wedges (or roll into a 3-inch-wide rectangle and cut into triangles). Brush with melted margarine. Starting at the wide end, roll up each triangle and curve into a crescent shape. Place on greased baking sheet, let rise until doubled, then bake at 375°F (190°C) for 12-15 minutes.",
            "FOR PARKERHOUSE ROLLS: Roll dough to 1/4-inch thickness. Cut with a 3-inch biscuit cutter. Use a spoon handle to make a crease just below center of each circle. Brush with margarine. Fold the top half over the bottom half (bottom should be slightly larger). Place on greased baking sheet, let rise until doubled, then bake at 375°F (190°C) for 12-15 minutes.",
            "FOR FANTAN ROLLS: Roll dough into a rectangle 1/8-inch thick. Cut into 1-inch-wide strips. Brush with melted margarine. Stack 6-7 strips on top of each other. Cut the stack into 1 1/4-inch pieces. Place each piece cut-side up in greased muffin cups. Let rise until doubled, then bake at 375°F (190°C) for 12-15 minutes.",
            "All shapes should be golden brown when done. Brush with additional butter if desired while still warm."
        ]
    }
}

# Recipe 3: Spaghetti Portofino (Serves One)
spaghetti_one = {
    "original_recipe": {
        "name": "Spaghetti Portofino (Serves One)",
        "subtitle": "Original recipe from Cozumel, Mexico",
        "source": "Ed & Mary Carle",
        "category": "Main Dishes",
        "servings": "1 serving",
        "ingredients": [
            {
                "item": "Minced fresh garlic in oil",
                "quantity": "2 tablespoons",
                "notes": "",
                "metric": {
                    "quantity": 30,
                    "unit": "ml"
                }
            },
            {
                "item": "Butter",
                "quantity": "2 pats",
                "notes": "",
                "metric": {
                    "quantity": 10,
                    "unit": "g"
                }
            },
            {
                "item": "Red snapper or halibut filets",
                "quantity": "Small handful",
                "notes": "cut in small strips",
                "metric": None
            },
            {
                "item": "Brandy",
                "quantity": "1/2 oz",
                "notes": "",
                "metric": {
                    "quantity": 15,
                    "unit": "ml"
                }
            },
            {
                "item": "Fresh mussels",
                "quantity": "1/2 cup",
                "notes": "if not available, add same quantity to fish filets",
                "metric": {
                    "quantity": 120,
                    "unit": "ml"
                }
            },
            {
                "item": "Worcestershire sauce",
                "quantity": "1 tablespoon",
                "notes": "",
                "metric": {
                    "quantity": 15,
                    "unit": "ml"
                }
            },
            {
                "item": "Soy sauce",
                "quantity": "1/4 teaspoon",
                "notes": "",
                "metric": {
                    "quantity": 1.25,
                    "unit": "ml"
                }
            },
            {
                "item": "Oregano",
                "quantity": "2 dashes",
                "notes": "",
                "metric": None
            },
            {
                "item": "Tabasco",
                "quantity": "2 dashes",
                "notes": "",
                "metric": None
            },
            {
                "item": "Chunky tomato sauce",
                "quantity": "1/2 cup",
                "notes": "",
                "metric": {
                    "quantity": 120,
                    "unit": "ml"
                }
            },
            {
                "item": "Catsup",
                "quantity": "4 tablespoons",
                "notes": "",
                "metric": {
                    "quantity": 60,
                    "unit": "ml"
                }
            },
            {
                "item": "Parsley",
                "quantity": "2 teaspoons",
                "notes": "",
                "metric": {
                    "quantity": 10,
                    "unit": "ml"
                }
            },
            {
                "item": "White wine",
                "quantity": "2 jiggers",
                "notes": "",
                "metric": {
                    "quantity": 90,
                    "unit": "ml"
                }
            },
            {
                "item": "Spaghetti",
                "quantity": "1 oz",
                "notes": "cooked",
                "metric": {
                    "quantity": 28,
                    "unit": "g"
                }
            }
        ],
        "instructions": [
            "Warm garlic in oil and margarine in skillet over medium flame.",
            "Add fish and saute about one minute.",
            "Add brandy and ignite.",
            "When flame goes out add mussels and rest of the ingredients.",
            "Add spaghetti, simmer one to two minutes.",
            "Serve with salad and French bread."
        ]
    },
    "improved_recipe": {
        "name": "Spaghetti Portofino (Serves One)",
        "category": "Main Dishes",
        "servings": "1 serving",
        "ingredients": [
            {
                "item": "Fresh garlic, minced",
                "quantity": "2 tablespoons",
                "notes": "in oil",
                "metric": {
                    "quantity": 30,
                    "unit": "ml"
                }
            },
            {
                "item": "Butter",
                "quantity": "2 pats (about 1 tablespoon)",
                "notes": "",
                "metric": {
                    "quantity": 10,
                    "unit": "g"
                }
            },
            {
                "item": "Red snapper or halibut filets",
                "quantity": "2-3 ounces",
                "notes": "cut into small strips",
                "metric": {
                    "min": 56,
                    "max": 85,
                    "unit": "g"
                }
            },
            {
                "item": "Brandy",
                "quantity": "1/2 ounce (1 tablespoon)",
                "notes": "",
                "metric": {
                    "quantity": 15,
                    "unit": "ml"
                }
            },
            {
                "item": "Fresh mussels",
                "quantity": "1/2 cup",
                "notes": "cleaned; if not available, increase fish to 4-5 oz",
                "metric": {
                    "quantity": 120,
                    "unit": "ml"
                }
            },
            {
                "item": "Worcestershire sauce",
                "quantity": "1 tablespoon",
                "notes": "",
                "metric": {
                    "quantity": 15,
                    "unit": "ml"
                }
            },
            {
                "item": "Soy sauce",
                "quantity": "1/4 teaspoon",
                "notes": "",
                "metric": {
                    "quantity": 1.25,
                    "unit": "ml"
                }
            },
            {
                "item": "Dried oregano",
                "quantity": "1/4 teaspoon",
                "notes": "",
                "metric": {
                    "quantity": 1.25,
                    "unit": "ml"
                }
            },
            {
                "item": "Tabasco sauce",
                "quantity": "1/4 teaspoon",
                "notes": "or to taste",
                "metric": {
                    "quantity": 1.25,
                    "unit": "ml"
                }
            },
            {
                "item": "Chunky tomato sauce",
                "quantity": "1/2 cup",
                "notes": "",
                "metric": {
                    "quantity": 120,
                    "unit": "ml"
                }
            },
            {
                "item": "Catsup",
                "quantity": "4 tablespoons",
                "notes": "",
                "metric": {
                    "quantity": 60,
                    "unit": "ml"
                }
            },
            {
                "item": "Fresh parsley, chopped",
                "quantity": "2 teaspoons",
                "notes": "",
                "metric": {
                    "quantity": 10,
                    "unit": "ml"
                }
            },
            {
                "item": "White wine",
                "quantity": "3 ounces (6 tablespoons)",
                "notes": "",
                "metric": {
                    "quantity": 90,
                    "unit": "ml"
                }
            },
            {
                "item": "Spaghetti",
                "quantity": "2 ounces dry (1 oz cooked)",
                "notes": "about 1 cup cooked",
                "metric": {
                    "quantity": 56,
                    "unit": "g"
                }
            }
        ],
        "instructions": [
            "Cook spaghetti according to package directions; drain and set aside.",
            "In a medium skillet, warm the minced garlic in oil and butter over medium heat.",
            "Add the fish strips and sauté for about 1 minute until they start to turn opaque.",
            "Carefully add the brandy and ignite with a long match or lighter. Let the flames burn out naturally (about 30 seconds).",
            "Add the mussels, Worcestershire sauce, soy sauce, oregano, and Tabasco. Stir gently.",
            "Stir in the chunky tomato sauce, catsup, parsley, and white wine. Bring to a simmer.",
            "Add the cooked spaghetti to the sauce and toss to combine.",
            "Simmer for 1-2 minutes until everything is heated through.",
            "Serve immediately with a green salad and warm French bread.",
            "Note: Original recipe brought from Cozumel, Mexico by Ed & Mary Carle."
        ]
    }
}

# Recipe 4: Spaghetti Portofino (Serves Six)
spaghetti_six = {
    "original_recipe": {
        "name": "Spaghetti Portofino (Serves Six)",
        "subtitle": "Original recipe from Cozumel, Mexico",
        "source": "Ed & Mary Carle",
        "category": "Main Dishes",
        "servings": "6 servings",
        "ingredients": [
            {
                "item": "Fresh garlic, minced",
                "quantity": "8 large cloves",
                "notes": "in oil",
                "metric": {
                    "quantity": 8,
                    "unit": "cloves"
                }
            },
            {
                "item": "Olive oil",
                "quantity": "3 tablespoons",
                "notes": "",
                "metric": {
                    "quantity": 45,
                    "unit": "ml"
                }
            },
            {
                "item": "Margarine, melted",
                "quantity": "2 tablespoons",
                "notes": "",
                "metric": {
                    "quantity": 30,
                    "unit": "ml"
                }
            },
            {
                "item": "Red snapper or halibut",
                "quantity": "1 & 1/2 pounds",
                "notes": "cut in small strips",
                "metric": {
                    "quantity": 680,
                    "unit": "g"
                }
            },
            {
                "item": "Brandy",
                "quantity": "1/2 cup",
                "notes": "such as Napoleon French brandy",
                "metric": {
                    "quantity": 120,
                    "unit": "ml"
                }
            },
            {
                "item": "Worcestershire sauce",
                "quantity": "3 tablespoons",
                "notes": "",
                "metric": {
                    "quantity": 45,
                    "unit": "ml"
                }
            },
            {
                "item": "Soy sauce",
                "quantity": "2 tablespoons",
                "notes": "",
                "metric": {
                    "quantity": 30,
                    "unit": "ml"
                }
            },
            {
                "item": "Fresh basil",
                "quantity": "2 tablespoons",
                "notes": "",
                "metric": {
                    "quantity": 30,
                    "unit": "ml"
                }
            },
            {
                "item": "Tabasco",
                "quantity": "1 teaspoon",
                "notes": "",
                "metric": {
                    "quantity": 5,
                    "unit": "ml"
                }
            },
            {
                "item": "Chunky tomato sauce",
                "quantity": "2 cups",
                "notes": "",
                "metric": {
                    "quantity": 480,
                    "unit": "ml"
                }
            },
            {
                "item": "Catsup",
                "quantity": "1/2 cup",
                "notes": "",
                "metric": {
                    "quantity": 120,
                    "unit": "ml"
                }
            },
            {
                "item": "Parsley",
                "quantity": "2 tablespoons",
                "notes": "",
                "metric": {
                    "quantity": 30,
                    "unit": "ml"
                }
            },
            {
                "item": "White wine",
                "quantity": "1/2 cup",
                "notes": "",
                "metric": {
                    "quantity": 120,
                    "unit": "ml"
                }
            },
            {
                "item": "Spaghetti",
                "quantity": "17 oz",
                "notes": "cooked",
                "metric": {
                    "quantity": 482,
                    "unit": "g"
                }
            }
        ],
        "instructions": [
            "Combine ingredients in order listed.",
            "Warm garlic in olive oil and margarine in wok (medium heat).",
            "Add fish and saute about three minutes.",
            "Add brandy and rest of ingredients.",
            "Add spaghetti and bring to a simmer.",
            "Serve with salad and French bread."
        ]
    },
    "improved_recipe": {
        "name": "Spaghetti Portofino (Serves Six)",
        "category": "Main Dishes",
        "servings": "6 servings",
        "ingredients": [
            {
                "item": "Fresh garlic, minced",
                "quantity": "8 large cloves",
                "notes": "about 3 tablespoons",
                "metric": {
                    "quantity": 8,
                    "unit": "cloves"
                }
            },
            {
                "item": "Olive oil",
                "quantity": "3 tablespoons",
                "notes": "",
                "metric": {
                    "quantity": 45,
                    "unit": "ml"
                }
            },
            {
                "item": "Margarine or butter, melted",
                "quantity": "2 tablespoons",
                "notes": "",
                "metric": {
                    "quantity": 30,
                    "unit": "ml"
                }
            },
            {
                "item": "Red snapper or halibut filets",
                "quantity": "1 1/2 pounds",
                "notes": "cut into small strips",
                "metric": {
                    "quantity": 680,
                    "unit": "g"
                }
            },
            {
                "item": "Brandy",
                "quantity": "1/2 cup",
                "notes": "such as Napoleon or other quality brandy",
                "metric": {
                    "quantity": 120,
                    "unit": "ml"
                }
            },
            {
                "item": "Worcestershire sauce",
                "quantity": "3 tablespoons",
                "notes": "",
                "metric": {
                    "quantity": 45,
                    "unit": "ml"
                }
            },
            {
                "item": "Soy sauce",
                "quantity": "2 tablespoons",
                "notes": "",
                "metric": {
                    "quantity": 30,
                    "unit": "ml"
                }
            },
            {
                "item": "Fresh basil, chopped",
                "quantity": "2 tablespoons",
                "notes": "or 2 teaspoons dried",
                "metric": {
                    "quantity": 30,
                    "unit": "ml"
                }
            },
            {
                "item": "Tabasco sauce",
                "quantity": "1 teaspoon",
                "notes": "or to taste",
                "metric": {
                    "quantity": 5,
                    "unit": "ml"
                }
            },
            {
                "item": "Chunky tomato sauce",
                "quantity": "2 cups",
                "notes": "",
                "metric": {
                    "quantity": 480,
                    "unit": "ml"
                }
            },
            {
                "item": "Catsup",
                "quantity": "1/2 cup",
                "notes": "",
                "metric": {
                    "quantity": 120,
                    "unit": "ml"
                }
            },
            {
                "item": "Fresh parsley, chopped",
                "quantity": "2 tablespoons",
                "notes": "",
                "metric": {
                    "quantity": 30,
                    "unit": "ml"
                }
            },
            {
                "item": "White wine",
                "quantity": "1/2 cup",
                "notes": "",
                "metric": {
                    "quantity": 120,
                    "unit": "ml"
                }
            },
            {
                "item": "Spaghetti",
                "quantity": "1 pound dry (17 oz cooked)",
                "notes": "",
                "metric": {
                    "quantity": 454,
                    "unit": "g"
                }
            }
        ],
        "instructions": [
            "Cook spaghetti according to package directions; drain and set aside.",
            "In a large wok or deep skillet, warm the minced garlic in olive oil and melted margarine over medium heat.",
            "Add the fish strips and sauté for about 3 minutes until they start to turn opaque and are nearly cooked through.",
            "Carefully add the brandy. If desired, you can ignite it with a long match for dramatic presentation. Let flames burn out naturally.",
            "Add the Worcestershire sauce, soy sauce, fresh basil, and Tabasco. Stir gently to combine.",
            "Stir in the chunky tomato sauce, catsup, parsley, and white wine.",
            "Add the cooked spaghetti to the wok and toss everything together.",
            "Bring to a gentle simmer and cook for 2-3 minutes until everything is heated through and well combined.",
            "Taste and adjust seasonings as needed.",
            "Serve immediately in large pasta bowls with a green salad and warm French bread.",
            "Note: Original recipe brought from Cozumel, Mexico by Ed & Mary Carle."
        ]
    }
}

# Recipe 5: Vegetable Relish Salad
vegetable_relish = {
    "original_recipe": {
        "name": "Vegetable Relish Salad",
        "subtitle": None,
        "source": None,
        "category": "Salads",
        "servings": "6-8 servings",
        "ingredients": [
            {
                "item": "\"Shoe peg\" white sweet corn",
                "quantity": "1 can",
                "notes": "drained",
                "metric": None
            },
            {
                "item": "French style green beans",
                "quantity": "1 can",
                "notes": "save 2 tablespoons juice",
                "metric": None
            },
            {
                "item": "LeSeur early green garden peas",
                "quantity": "1 can",
                "notes": "drained",
                "metric": None
            },
            {
                "item": "White onions, chopped",
                "quantity": "1 cup",
                "notes": "",
                "metric": {
                    "quantity": 240,
                    "unit": "ml"
                }
            },
            {
                "item": "Celery, chopped",
                "quantity": "1 cup",
                "notes": "",
                "metric": {
                    "quantity": 240,
                    "unit": "ml"
                }
            },
            {
                "item": "Green bell peppers, chopped",
                "quantity": "1 cup",
                "notes": "",
                "metric": {
                    "quantity": 240,
                    "unit": "ml"
                }
            },
            {
                "item": "Diced pimento",
                "quantity": "2 ounce jar",
                "notes": "",
                "metric": {
                    "quantity": 56,
                    "unit": "g"
                }
            },
            {
                "item": "Sugar",
                "quantity": "1/2 cup",
                "notes": "for sauce",
                "metric": {
                    "quantity": 100,
                    "unit": "g"
                }
            },
            {
                "item": "Salad oil",
                "quantity": "1/4 cup",
                "notes": "for sauce",
                "metric": {
                    "quantity": 60,
                    "unit": "ml"
                }
            },
            {
                "item": "Vinegar",
                "quantity": "3/4 cup",
                "notes": "for sauce",
                "metric": {
                    "quantity": 180,
                    "unit": "ml"
                }
            },
            {
                "item": "Pepper",
                "quantity": "1/2 teaspoon",
                "notes": "for sauce",
                "metric": {
                    "quantity": 2.5,
                    "unit": "ml"
                }
            },
            {
                "item": "Salt",
                "quantity": "1 teaspoon",
                "notes": "for sauce",
                "metric": {
                    "quantity": 5,
                    "unit": "ml"
                }
            },
            {
                "item": "Green bean juice",
                "quantity": "2 tablespoons",
                "notes": "saved from can",
                "metric": {
                    "quantity": 30,
                    "unit": "ml"
                }
            }
        ],
        "instructions": [
            "Drain all vegetables in colander with exception of two tablespoons of green bean juice (take from can prior to draining). Save vegetable juices for soup.",
            "Mix all sauce ingredients well.",
            "Bring to a boil, pour over vegetables, stir, then refrigerate overnight before serving."
        ]
    },
    "improved_recipe": {
        "name": "Vegetable Relish Salad",
        "category": "Salads",
        "servings": "8-10 servings",
        "ingredients": [
            {
                "item": "White sweet corn (shoe peg style)",
                "quantity": "1 can (15 oz)",
                "notes": "drained",
                "metric": {
                    "quantity": 425,
                    "unit": "g"
                }
            },
            {
                "item": "French style green beans",
                "quantity": "1 can (14.5 oz)",
                "notes": "reserve 2 tablespoons liquid before draining",
                "metric": {
                    "quantity": 410,
                    "unit": "g"
                }
            },
            {
                "item": "Sweet peas",
                "quantity": "1 can (15 oz)",
                "notes": "drained (LeSeur preferred)",
                "metric": {
                    "quantity": 425,
                    "unit": "g"
                }
            },
            {
                "item": "White onion, chopped",
                "quantity": "1 cup",
                "notes": "",
                "metric": {
                    "quantity": 240,
                    "unit": "ml"
                }
            },
            {
                "item": "Celery, chopped",
                "quantity": "1 cup",
                "notes": "",
                "metric": {
                    "quantity": 240,
                    "unit": "ml"
                }
            },
            {
                "item": "Green bell pepper, chopped",
                "quantity": "1 cup",
                "notes": "",
                "metric": {
                    "quantity": 240,
                    "unit": "ml"
                }
            },
            {
                "item": "Diced pimento",
                "quantity": "1 jar (2 oz)",
                "notes": "drained",
                "metric": {
                    "quantity": 56,
                    "unit": "g"
                }
            },
            {
                "item": "Granulated sugar",
                "quantity": "1/2 cup",
                "notes": "for marinade",
                "metric": {
                    "quantity": 100,
                    "unit": "g"
                }
            },
            {
                "item": "Vegetable or salad oil",
                "quantity": "1/4 cup",
                "notes": "for marinade",
                "metric": {
                    "quantity": 60,
                    "unit": "ml"
                }
            },
            {
                "item": "White vinegar",
                "quantity": "3/4 cup",
                "notes": "for marinade",
                "metric": {
                    "quantity": 180,
                    "unit": "ml"
                }
            },
            {
                "item": "Salt",
                "quantity": "1 teaspoon",
                "notes": "for marinade",
                "metric": {
                    "quantity": 5,
                    "unit": "ml"
                }
            },
            {
                "item": "Black pepper",
                "quantity": "1/2 teaspoon",
                "notes": "for marinade",
                "metric": {
                    "quantity": 2.5,
                    "unit": "ml"
                }
            },
            {
                "item": "Reserved green bean juice",
                "quantity": "2 tablespoons",
                "notes": "from canned beans",
                "metric": {
                    "quantity": 30,
                    "unit": "ml"
                }
            }
        ],
        "instructions": [
            "Before draining the green beans, reserve 2 tablespoons of the liquid from the can.",
            "Drain all canned vegetables in a colander. You can save the remaining vegetable juices for soup stock if desired.",
            "In a large bowl, combine the drained corn, green beans, peas, chopped onion, celery, green bell pepper, and pimento.",
            "In a small saucepan, combine the sugar, oil, vinegar, salt, pepper, and reserved green bean juice.",
            "Bring the marinade to a boil over medium-high heat, stirring to dissolve the sugar.",
            "Pour the hot marinade over the vegetables and stir gently to coat everything evenly.",
            "Cover and refrigerate overnight (at least 8 hours) to allow the flavors to blend.",
            "Stir before serving. Serve cold as a side dish or relish.",
            "This salad keeps well in the refrigerator for up to 5 days."
        ]
    }
}

# Find categories and append recipes
for category in data["categories"]:
    if category["name"] == "Main Dishes":
        category["recipes"].extend([chili, spaghetti_one, spaghetti_six])
    elif category["name"] == "Breads & Breakfast":
        category["recipes"].append(dinner_roll_shapes)
    elif category["name"] == "Salads":
        category["recipes"].append(vegetable_relish)

# Save updated recipes
with open('recipes.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Successfully added 5 recipes (Batch 3A):")
print("  - Chili (Main Dishes)")
print("  - Dinner Roll Shapes (Breads & Breakfast)")
print("  - Spaghetti Portofino (Serves One) (Main Dishes)")
print("  - Spaghetti Portofino (Serves Six) (Main Dishes)")
print("  - Vegetable Relish Salad (Salads)")
