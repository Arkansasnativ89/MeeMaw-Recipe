import json

# Load the current recipes.json
with open('recipes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Recipe 1: Dinner Rolls (Breads & Breakfast)
dinner_rolls = {
    "original_recipe": {
        "name": "Dinner Rolls",
        "subtitle": "Alma Finken Carle",
        "source": "Alma Finken Carle",
        "category": "Breads & Breakfast",
        "servings": None,
        "ingredients": [
            {"item": "Sifted bread flour", "quantity": "3 to 3 1/2 cups", "notes": "can use all purpose flour", "metric": {"min": 360, "max": 420, "unit": "g"}},
            {"item": "Dry yeast", "quantity": "1 package", "notes": "", "metric": {"quantity": 7, "unit": "g"}},
            {"item": "Milk", "quantity": "1 cup", "notes": "2%, 1/2%, or skim", "metric": {"quantity": 240, "unit": "ml"}},
            {"item": "Oil", "quantity": "2 tablespoons", "notes": "", "metric": {"quantity": 30, "unit": "ml"}},
            {"item": "Sugar", "quantity": "2 tablespoons", "notes": "", "metric": {"quantity": 25, "unit": "g"}},
            {"item": "Salt", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 6, "unit": "g"}}
        ],
        "instructions": [
            "Sift together about 1/3 of the flour and all of the yeast.",
            "Heat milk, oil, sugar and salt over low heat until hot to the finger, but no more. Stir to dissolve sugar and salt.",
            "Add liquids to the flour-yeast mixture and beat with an electric mixer at medium speed for two minutes, or 300 strokes by hand.",
            "Add another one-half to one cup of flour and beat for another minute with the electric mixer.",
            "Stir in enough more flour to make a soft dough.",
            "Turn onto a floured board and knead until smooth and elastic (eight to ten minutes).",
            "Place in a bowl that has been coated with a nonstick vegetable spray. Spray the top of the mixture with the nonstick vegetable spray. Cover with wax paper and over that place a dry cloth.",
            "Put in a warm place (80° to 85° F), free from drafts, and let rise until doubled (about one hour).",
            "Punch dough down. Turn out onto a floured board again and shape into any desired form.",
            "Place rolls on baking sheets that have been lightly coated with a nonstick vegetable spray, or in muffin cups and let rise again until doubled (takes one to one & one-half hours).",
            "Pre-heat oven to 425° F. Bake for about ten minutes and serve piping hot."
        ]
    },
    "improved_recipe": {
        "name": "Classic Dinner Rolls",
        "category": "Breads & Breakfast",
        "servings": "About 12-15 rolls",
        "ingredients": [
            {"item": "Bread flour or all-purpose flour", "quantity": "3 to 3 1/2 cups", "notes": "sifted, divided", "metric": {"min": 360, "max": 420, "unit": "g"}},
            {"item": "Active dry yeast", "quantity": "1 packet (2 1/4 tsp)", "notes": "", "metric": {"quantity": 7, "unit": "g"}},
            {"item": "Milk", "quantity": "1 cup", "notes": "any fat percentage", "metric": {"quantity": 240, "unit": "ml"}},
            {"item": "Vegetable oil", "quantity": "2 tablespoons", "notes": "", "metric": {"quantity": 30, "unit": "ml"}},
            {"item": "Granulated sugar", "quantity": "2 tablespoons", "notes": "", "metric": {"quantity": 25, "unit": "g"}},
            {"item": "Salt", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 6, "unit": "g"}}
        ],
        "instructions": [
            "In a large bowl, combine about 1 cup of the flour with the yeast. Whisk together to distribute the yeast evenly.",
            "In a small saucepan, combine the milk, oil, sugar, and salt. Heat over low heat, stirring occasionally, until warm to the touch (110-115°F) and the sugar and salt dissolve. The mixture should feel warm but not hot.",
            "Pour the warm liquid into the flour-yeast mixture. Beat with an electric mixer at medium speed for 2 minutes, or beat vigorously by hand for about 300 strokes, until smooth.",
            "Add 1/2 to 1 cup more flour and beat for an additional 1 minute.",
            "Gradually stir in enough of the remaining flour (about 1 1/2 to 2 cups) to form a soft dough that pulls away from the sides of the bowl.",
            "Turn the dough out onto a lightly floured surface. Knead for 8-10 minutes, adding small amounts of flour as needed, until the dough is smooth, elastic, and no longer sticky.",
            "Lightly coat a large bowl with nonstick spray. Place the dough in the bowl and turn once to coat. Cover with plastic wrap or a damp towel.",
            "Let the dough rise in a warm, draft-free place (80-85°F) until doubled in size, about 1 hour. To test, gently press two fingers into the dough; if the indentation remains, it's ready.",
            "Punch down the dough to release the air. Turn out onto a lightly floured surface and shape into desired forms: round rolls, cloverleaf, Parker House, crescents, etc.",
            "Place shaped rolls on lightly greased baking sheets or in muffin tins, spacing them about 2 inches apart. Cover and let rise again until nearly doubled, 1 to 1 1/2 hours.",
            "Preheat the oven to 425°F (220°C).",
            "Bake for 10-12 minutes, or until the rolls are golden brown on top.",
            "Serve piping hot with butter. Store leftovers in an airtight container for up to 3 days, or freeze for up to 1 month."
        ]
    }
}

# Recipe 2: Crumble Coffee Cake #2 (Breads & Breakfast)
crumble_coffee_cake = {
    "original_recipe": {
        "name": "Crumble Coffee Cake #2",
        "subtitle": None,
        "source": None,
        "category": "Breads & Breakfast",
        "servings": "4-5 cakes",
        "ingredients": [
            {"item": "Basic Sweet Dough", "quantity": "1 batch", "notes": "consistency of thick cake batter", "metric": None},
            {"item": "Flour (for crumbles)", "quantity": "2 1/2 cups", "notes": "", "metric": {"quantity": 300, "unit": "g"}},
            {"item": "Sugar (for crumbles)", "quantity": "2 cups", "notes": "", "metric": {"quantity": 400, "unit": "g"}},
            {"item": "Vanilla (for crumbles)", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 5, "unit": "ml"}},
            {"item": "Eggs (for crumbles)", "quantity": "2", "notes": "or egg substitute", "metric": {"quantity": 100, "unit": "g"}},
            {"item": "Margarine (for crumbles)", "quantity": "1 1/2 sticks", "notes": "", "metric": {"quantity": 170, "unit": "g"}},
            {"item": "Baking powder (for crumbles)", "quantity": "2 teaspoons", "notes": "", "metric": {"quantity": 10, "unit": "g"}}
        ],
        "instructions": [
            "Make up batch of Basic Sweet Dough (see separate recipe). The dough should be the consistency of a thick cake batter.",
            "There should be enough dough to make four or five eight inch square coffee cakes, 3/8\" thick when first put into pan and before rising.",
            "Pans should be coated with a nonstick vegetable spray before they are used.",
            "For crumbles topping: Work flour into mixture of sugar, vanilla, eggs, margarine, and baking powder until crumbles form. They should be random size with largest about the size of a blueberry.",
            "Put crumbles on top of cakes before rising, and let rise for about one hour.",
            "Bake at 375° F for 20 to 25 minutes."
        ]
    },
    "improved_recipe": {
        "name": "Crumble Coffee Cake with Sweet Dough Base",
        "category": "Breads & Breakfast",
        "servings": "4-5 cakes (8-inch square)",
        "ingredients": [
            {"item": "Basic Sweet Dough", "quantity": "1 full batch", "notes": "prepared to thick batter consistency (see Basic Sweet Dough recipe)", "metric": None},
            {"item": "All-purpose flour", "quantity": "2 1/2 cups", "notes": "for crumble topping", "metric": {"quantity": 300, "unit": "g"}},
            {"item": "Granulated sugar", "quantity": "2 cups", "notes": "for crumble topping", "metric": {"quantity": 400, "unit": "g"}},
            {"item": "Vanilla extract", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 5, "unit": "ml"}},
            {"item": "Eggs", "quantity": "2 large", "notes": "or 1/2 cup egg substitute", "metric": {"quantity": 100, "unit": "g"}},
            {"item": "Margarine or butter", "quantity": "12 tablespoons (1 1/2 sticks)", "notes": "softened", "metric": {"quantity": 170, "unit": "g"}},
            {"item": "Baking powder", "quantity": "2 teaspoons", "notes": "", "metric": {"quantity": 10, "unit": "g"}}
        ],
        "instructions": [
            "Prepare one full batch of Basic Sweet Dough according to the recipe, but add a bit more liquid so the dough reaches a thick cake batter consistency rather than a standard bread dough texture.",
            "Coat 4 to 5 eight-inch square baking pans with nonstick cooking spray.",
            "Divide the dough evenly among the pans. Spread to about 3/8-inch thickness (it will rise during proofing). The dough should cover the bottom of each pan.",
            "Prepare the crumble topping: In a medium bowl, combine the sugar, vanilla, eggs (or egg substitute), softened margarine, and baking powder. Mix until well blended.",
            "Gradually work in the flour, mixing and rubbing the mixture between your fingers until crumbles form. The crumbles should vary in size, with the largest about the size of a blueberry.",
            "Sprinkle the crumble topping evenly over each unbaked coffee cake, distributing it as uniformly as possible.",
            "Cover the pans lightly and let the cakes rise in a warm place for about 1 hour, or until noticeably puffy.",
            "Preheat the oven to 375°F (190°C).",
            "Bake for 20-25 minutes, or until the cakes are golden brown and the crumble topping is lightly crisped.",
            "Cool in the pans for 10 minutes, then cut into squares and serve warm or at room temperature. Excellent with coffee or tea!"
        ]
    }
}

# Recipe 3: Fudge (Plain) (Candy)
fudge_plain = {
    "original_recipe": {
        "name": "Fudge (Plain)",
        "subtitle": None,
        "source": None,
        "category": "Candy",
        "servings": None,
        "ingredients": [
            {"item": "Granulated sugar", "quantity": "2 cups", "notes": "", "metric": {"quantity": 400, "unit": "g"}},
            {"item": "Cocoa powder", "quantity": "3 tablespoons", "notes": "", "metric": {"quantity": 20, "unit": "g"}},
            {"item": "Salt", "quantity": "1/8 teaspoon", "notes": "", "metric": {"quantity": 0.75, "unit": "g"}},
            {"item": "Milk", "quantity": "3/4 cup", "notes": "1/2% milk", "metric": {"quantity": 180, "unit": "ml"}},
            {"item": "Margarine", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 15, "unit": "g"}},
            {"item": "Vegetable oil", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 15, "unit": "ml"}},
            {"item": "Vanilla extract", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 5, "unit": "ml"}}
        ],
        "instructions": [
            "Combine sugar, cocoa powder, salt and milk in a saucepan.",
            "Heat slowly, stirring constantly, until sugar is dissolved.",
            "Cook to the soft-ball stage, 234° F to 238° F. DO NOT STIR WHILE COOKING!",
            "Stir in margarine and oil and cool to lukewarm.",
            "Add vanilla and beat with a spoon until the mixture is almost stiff.",
            "Pour onto a pan that has been coated with a nonstick vegetable spray.",
            "Cool, and cut into squares."
        ]
    },
    "improved_recipe": {
        "name": "Classic Chocolate Fudge",
        "category": "Candy",
        "servings": "About 36 pieces",
        "ingredients": [
            {"item": "Granulated sugar", "quantity": "2 cups", "notes": "", "metric": {"quantity": 400, "unit": "g"}},
            {"item": "Unsweetened cocoa powder", "quantity": "3 tablespoons", "notes": "", "metric": {"quantity": 20, "unit": "g"}},
            {"item": "Salt", "quantity": "1/8 teaspoon", "notes": "", "metric": {"quantity": 0.75, "unit": "g"}},
            {"item": "Milk", "quantity": "3/4 cup", "notes": "low-fat or whole", "metric": {"quantity": 180, "unit": "ml"}},
            {"item": "Margarine or butter", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 15, "unit": "g"}},
            {"item": "Vegetable oil", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 15, "unit": "ml"}},
            {"item": "Vanilla extract", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 5, "unit": "ml"}}
        ],
        "instructions": [
            "Lightly coat an 8x8-inch baking pan with nonstick cooking spray or line with parchment paper.",
            "In a heavy-bottomed saucepan, combine the sugar, cocoa powder, salt, and milk. Stir well to mix.",
            "Place the saucepan over medium-low heat. Stir constantly until the sugar is completely dissolved and the mixture is smooth.",
            "Once the sugar dissolves, stop stirring. Attach a candy thermometer to the side of the pan. Continue cooking without stirring until the mixture reaches the soft-ball stage (234-238°F). This may take 15-20 minutes. Be patient and do not stir during this time, or the fudge may crystallize.",
            "When the mixture reaches the soft-ball stage, remove from heat immediately. Stir in the margarine and oil.",
            "Let the mixture cool, undisturbed, to lukewarm (about 110°F). This may take 30-45 minutes. Do not stir during cooling, or the fudge may become grainy.",
            "Once lukewarm, add the vanilla extract. Beat vigorously with a wooden spoon until the mixture thickens and loses its glossy appearance. This can take 5-10 minutes of beating.",
            "Quickly pour the fudge into the prepared pan and spread evenly with a spatula.",
            "Let the fudge cool completely at room temperature until firm, about 2 hours.",
            "Cut into 1-inch squares. Store in an airtight container at room temperature for up to 2 weeks."
        ]
    }
}

# Recipe 4: Waffles (Breads & Breakfast)
waffles = {
    "original_recipe": {
        "name": "Waffles",
        "subtitle": None,
        "source": None,
        "category": "Breads & Breakfast",
        "servings": None,
        "ingredients": [
            {"item": "All purpose flour", "quantity": "2 cups", "notes": "", "metric": {"quantity": 240, "unit": "g"}},
            {"item": "Baking powder", "quantity": "2 teaspoons", "notes": "", "metric": {"quantity": 10, "unit": "g"}},
            {"item": "Baking soda", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 5, "unit": "g"}},
            {"item": "Salt", "quantity": "1/2 teaspoon", "notes": "", "metric": {"quantity": 3, "unit": "g"}},
            {"item": "Sugar", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 15, "unit": "g"}},
            {"item": "Vegetable oil", "quantity": "6 tablespoons", "notes": "", "metric": {"quantity": 90, "unit": "ml"}},
            {"item": "Low fat buttermilk", "quantity": "2 cups", "notes": "", "metric": {"quantity": 480, "unit": "ml"}},
            {"item": "Yellow food coloring", "quantity": "4 drops", "notes": "", "metric": None},
            {"item": "Egg whites", "quantity": "4", "notes": "beaten stiff", "metric": {"quantity": 120, "unit": "g"}}
        ],
        "instructions": [
            "Sift the dry ingredients together.",
            "Combine oil, buttermilk, and food coloring. Add all at once to dry ingredients and mix with a few quick strokes.",
            "Fold in the egg whites.",
            "Coat the waffle iron with nonstick vegetable spray.",
            "Pour just enough batter on the waffle iron to make a thin layer.",
            "Bake until golden brown and crisp."
        ]
    },
    "improved_recipe": {
        "name": "Fluffy Buttermilk Waffles",
        "category": "Breads & Breakfast",
        "servings": "About 6-8 waffles",
        "ingredients": [
            {"item": "All-purpose flour", "quantity": "2 cups", "notes": "", "metric": {"quantity": 240, "unit": "g"}},
            {"item": "Baking powder", "quantity": "2 teaspoons", "notes": "", "metric": {"quantity": 10, "unit": "g"}},
            {"item": "Baking soda", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 5, "unit": "g"}},
            {"item": "Salt", "quantity": "1/2 teaspoon", "notes": "", "metric": {"quantity": 3, "unit": "g"}},
            {"item": "Granulated sugar", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 15, "unit": "g"}},
            {"item": "Vegetable oil", "quantity": "6 tablespoons", "notes": "", "metric": {"quantity": 90, "unit": "ml"}},
            {"item": "Low-fat buttermilk", "quantity": "2 cups", "notes": "", "metric": {"quantity": 480, "unit": "ml"}},
            {"item": "Yellow food coloring", "quantity": "4 drops", "notes": "optional, for color", "metric": None},
            {"item": "Egg whites", "quantity": "4 large", "notes": "", "metric": {"quantity": 120, "unit": "g"}}
        ],
        "instructions": [
            "Preheat your waffle iron according to the manufacturer's instructions.",
            "In a large bowl, sift together the flour, baking powder, baking soda, salt, and sugar.",
            "In a separate bowl or large measuring cup, whisk together the vegetable oil, buttermilk, and food coloring (if using).",
            "In a clean, dry mixing bowl, beat the egg whites with an electric mixer on high speed until stiff peaks form. This should take about 3-4 minutes.",
            "Pour the buttermilk mixture into the dry ingredients and stir with a few quick strokes just until combined. The batter should be slightly lumpy; do not overmix.",
            "Gently fold the beaten egg whites into the batter using a rubber spatula, taking care not to deflate them. Fold just until no large streaks of egg white remain.",
            "Lightly coat the preheated waffle iron with nonstick cooking spray.",
            "Pour enough batter onto the waffle iron to cover about two-thirds of the surface (the exact amount will depend on your waffle iron size).",
            "Close the lid and cook until the waffle is golden brown and crisp, usually 3-5 minutes. Most waffle irons will signal when the waffle is done.",
            "Carefully remove the waffle and keep warm in a low oven (200°F) while you cook the remaining batter.",
            "Serve hot with butter, maple syrup, fresh fruit, or whipped cream. Enjoy immediately for best texture!"
        ]
    }
}

# Recipe 5: Crumble Cake (Krumelkuchen) (Cakes)
crumble_cake = {
    "original_recipe": {
        "name": "Crumble Cake (Krumelkuchen)",
        "subtitle": None,
        "source": None,
        "category": "Cakes",
        "servings": "6 cakes",
        "ingredients": [
            {"item": "All purpose flour (crust)", "quantity": "2 cups, sifted", "notes": "", "metric": {"quantity": 240, "unit": "g"}},
            {"item": "Baking powder (crust)", "quantity": "2 teaspoons", "notes": "", "metric": {"quantity": 10, "unit": "g"}},
            {"item": "Salt (crust)", "quantity": "1/4 teaspoon", "notes": "", "metric": {"quantity": 1.5, "unit": "g"}},
            {"item": "Margarine (crust)", "quantity": "1 stick, melted", "notes": "", "metric": {"quantity": 113, "unit": "g"}},
            {"item": "Sugar (crust)", "quantity": "2/3 cup", "notes": "", "metric": {"quantity": 135, "unit": "g"}},
            {"item": "Eggs (crust)", "quantity": "2", "notes": "or egg substitute", "metric": {"quantity": 100, "unit": "g"}},
            {"item": "Milk (crust)", "quantity": "1/4 cup", "notes": "2%, 1/2% or skim", "metric": {"quantity": 60, "unit": "ml"}},
            {"item": "Flour (crumbles)", "quantity": "2 1/2 cups", "notes": "", "metric": {"quantity": 300, "unit": "g"}},
            {"item": "Sugar (crumbles)", "quantity": "2 cups", "notes": "", "metric": {"quantity": 400, "unit": "g"}},
            {"item": "Vanilla (crumbles)", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 5, "unit": "ml"}},
            {"item": "Eggs (crumbles)", "quantity": "2", "notes": "or egg substitute", "metric": {"quantity": 100, "unit": "g"}},
            {"item": "Margarine (crumbles)", "quantity": "1 1/2 sticks", "notes": "", "metric": {"quantity": 170, "unit": "g"}},
            {"item": "Baking powder (crumbles)", "quantity": "2 teaspoons", "notes": "", "metric": {"quantity": 10, "unit": "g"}},
            {"item": "Eggs (binder)", "quantity": "2", "notes": "or egg substitute", "metric": {"quantity": 100, "unit": "g"}},
            {"item": "Milk (binder)", "quantity": "1/4 cup", "notes": "", "metric": {"quantity": 60, "unit": "ml"}},
            {"item": "Vanilla (binder)", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 5, "unit": "ml"}},
            {"item": "Sugar (binder)", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 5, "unit": "g"}}
        ],
        "instructions": [
            "Step 1 (Crust): Blend dry ingredients. Add margarine, eggs, and milk. Mix well. Divide into six portions. Roll each portion out to a size to fit an eight-inch pie plate; about 3/4\" up the side.",
            "Step 2 (Crumbles): Blend and mix sugar, vanilla, eggs, margarine, and baking powder well. Work enough flour into mixture until crumbles form. They should be random size with largest about the size of a blueberry.",
            "Step 3 (Binder): Mix eggs, milk, vanilla, and sugar well, then spread four teaspoonfuls of binder evenly on top of each crust before adding crumbles.",
            "Add crumbles to each shell as evenly as possible.",
            "Bake at 350° F for twenty to thirty minutes until nicely browned."
        ]
    },
    "improved_recipe": {
        "name": "German Crumble Cake (Krümelkuchen)",
        "category": "Cakes",
        "servings": "6 cakes (8-inch)",
        "ingredients": [
            {"item": "All-purpose flour", "quantity": "2 cups", "notes": "for crust, sifted", "metric": {"quantity": 240, "unit": "g"}},
            {"item": "Baking powder", "quantity": "2 teaspoons", "notes": "for crust", "metric": {"quantity": 10, "unit": "g"}},
            {"item": "Salt", "quantity": "1/4 teaspoon", "notes": "", "metric": {"quantity": 1.5, "unit": "g"}},
            {"item": "Margarine or butter", "quantity": "1/2 cup (1 stick)", "notes": "for crust, melted", "metric": {"quantity": 113, "unit": "g"}},
            {"item": "Granulated sugar", "quantity": "2/3 cup", "notes": "for crust", "metric": {"quantity": 135, "unit": "g"}},
            {"item": "Eggs", "quantity": "2 large", "notes": "for crust, or 1/2 cup egg substitute", "metric": {"quantity": 100, "unit": "g"}},
            {"item": "Milk", "quantity": "1/4 cup", "notes": "for crust", "metric": {"quantity": 60, "unit": "ml"}},
            {"item": "All-purpose flour", "quantity": "2 1/2 cups", "notes": "for crumble topping", "metric": {"quantity": 300, "unit": "g"}},
            {"item": "Granulated sugar", "quantity": "2 cups", "notes": "for crumble topping", "metric": {"quantity": 400, "unit": "g"}},
            {"item": "Vanilla extract", "quantity": "1 teaspoon", "notes": "for crumble topping", "metric": {"quantity": 5, "unit": "ml"}},
            {"item": "Eggs", "quantity": "2 large", "notes": "for crumble topping, or 1/2 cup egg substitute", "metric": {"quantity": 100, "unit": "g"}},
            {"item": "Margarine or butter", "quantity": "12 tablespoons (1 1/2 sticks)", "notes": "for crumble topping, softened", "metric": {"quantity": 170, "unit": "g"}},
            {"item": "Baking powder", "quantity": "2 teaspoons", "notes": "for crumble topping", "metric": {"quantity": 10, "unit": "g"}},
            {"item": "Eggs", "quantity": "2 large", "notes": "for binder, or 1/2 cup egg substitute", "metric": {"quantity": 100, "unit": "g"}},
            {"item": "Milk", "quantity": "1/4 cup", "notes": "for binder", "metric": {"quantity": 60, "unit": "ml"}},
            {"item": "Vanilla extract", "quantity": "1 teaspoon", "notes": "for binder", "metric": {"quantity": 5, "unit": "ml"}},
            {"item": "Granulated sugar", "quantity": "1 teaspoon", "notes": "for binder", "metric": {"quantity": 5, "unit": "g"}}
        ],
        "instructions": [
            "Preheat oven to 350°F (175°C). Lightly grease six 8-inch pie plates or cake pans.",
            "Prepare the crust: In a large bowl, whisk together 2 cups flour, 2 tsp baking powder, and 1/4 tsp salt. Add the melted margarine, 2/3 cup sugar, 2 eggs (or substitute), and 1/4 cup milk. Mix well until a soft dough forms.",
            "Divide the dough into 6 equal portions. Roll out each portion on a lightly floured surface to fit an 8-inch pie plate, bringing the dough about 3/4 inch up the sides. Press into the prepared pans.",
            "Prepare the crumble topping: In a medium bowl, combine 2 cups sugar, 1 tsp vanilla, 2 eggs (or substitute), 12 tbsp softened margarine, and 2 tsp baking powder. Mix well.",
            "Gradually work in 2 1/2 cups flour, mixing and rubbing with your fingers until crumbles form. The crumbles should be random in size, with the largest about the size of a blueberry.",
            "Prepare the binder: In a small bowl, whisk together 2 eggs (or substitute), 1/4 cup milk, 1 tsp vanilla, and 1 tsp sugar until well combined.",
            "Brush or spoon about 4 teaspoons of the binder mixture evenly over each crust.",
            "Distribute the crumbles evenly over the 6 crusts, dividing them as equally as possible.",
            "Bake for 20-30 minutes, or until the cakes are nicely browned and the crumbles are golden and crisp.",
            "Cool in the pans for 10 minutes, then carefully transfer to a wire rack. Serve warm or at room temperature. These cakes are wonderful with coffee or tea!"
        ]
    }
}

# Add recipes to appropriate categories
for category in data["categories"]:
    if category["name"] == "Breads & Breakfast":
        category["recipes"].append(dinner_rolls)
        category["recipes"].append(crumble_coffee_cake)
        category["recipes"].append(waffles)
    elif category["name"] == "Candy":
        category["recipes"].append(fudge_plain)
    elif category["name"] == "Cakes":
        category["recipes"].append(crumble_cake)

# Save the updated recipes.json
with open('recipes.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Successfully added 5 recipes (Batch 1C):")
print("- Dinner Rolls (Breads & Breakfast)")
print("- Crumble Coffee Cake #2 (Breads & Breakfast)")
print("- Fudge (Plain) (Candy)")
print("- Waffles (Breads & Breakfast)")
print("- Crumble Cake (Krumelkuchen) (Cakes)")
