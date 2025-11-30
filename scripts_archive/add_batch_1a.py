import json

# Load the current recipes.json
with open('recipes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Recipe 1: Basic Sweet Dough (Breads & Breakfast)
basic_sweet_dough = {
    "original_recipe": {
        "name": "Basic Sweet Dough",
        "subtitle": None,
        "source": None,
        "category": "Breads & Breakfast",
        "servings": None,
        "ingredients": [
            {"item": "All purpose flour", "quantity": "4 1/2 to 5 cups, sifted", "notes": "", "metric": {"min": 540, "max": 600, "unit": "g"}},
            {"item": "Dry yeast", "quantity": "2 packages", "notes": "", "metric": {"quantity": 14, "unit": "g"}},
            {"item": "Milk", "quantity": "1/2 cup", "notes": "2%, 1/2%, or skim", "metric": {"quantity": 120, "unit": "ml"}},
            {"item": "Water", "quantity": "1/2 cup", "notes": "", "metric": {"quantity": 120, "unit": "ml"}},
            {"item": "Sugar", "quantity": "1/2 cup", "notes": "", "metric": {"quantity": 100, "unit": "g"}},
            {"item": "Oil", "quantity": "1/3 cup", "notes": "", "metric": {"quantity": 80, "unit": "ml"}},
            {"item": "Salt", "quantity": "1 1/2 teaspoons", "notes": "", "metric": {"quantity": 9, "unit": "g"}},
            {"item": "Egg whites", "quantity": "4", "notes": "", "metric": {"quantity": 120, "unit": "g"}},
            {"item": "Vegetable oil", "quantity": "for brushing", "notes": "", "metric": None}
        ],
        "instructions": [
            "Sift two cups of the flour and the yeast together into a large bowl. Mix well.",
            "Heat milk, water, sugar, oil and salt over low heat until warm, stirring to dissolve the sugar.",
            "Add liquids to flour-yeast mixture and beat until smooth (two to three minutes with an electric mixer, 300 strokes by hand).",
            "Mix in egg whites. Add one more cup of flour and beat for another minute.",
            "Add more flour and continue to beat until the dough is too stiff to continue.",
            "Turn out onto a floured board and knead for eight to ten minutes, adding remaining flour as needed. Do not stint on the kneading time as it is necessary to develop the gluten.",
            "Form the dough into a ball and place in a bowl coated with a nonstick vegetable spray. Cover, and let rise in a warm place (80° to 85° F), until doubled in bulk (one and one-half to two hours).",
            "Punch down the dough and let it rest for ten minutes.",
            "Shape into rolls, buns, wreaths, etc. Place into pans coated with a nonstick vegetable spray, and brush tops with oil.",
            "Cover and let rise again until doubled (thirty to forty-five minutes).",
            "Bake in a pre-heated 350° F oven for twenty to twenty-five minutes, depending on size."
        ]
    },
    "improved_recipe": {
        "name": "Basic Sweet Dough",
        "category": "Breads & Breakfast",
        "servings": "About 24 rolls or 2 loaves",
        "ingredients": [
            {"item": "All purpose flour", "quantity": "4 1/2 to 5 cups, sifted", "notes": "divided", "metric": {"min": 540, "max": 600, "unit": "g"}},
            {"item": "Active dry yeast", "quantity": "2 packages (4 1/2 teaspoons)", "notes": "", "metric": {"quantity": 14, "unit": "g"}},
            {"item": "Milk", "quantity": "1/2 cup", "notes": "any fat percentage", "metric": {"quantity": 120, "unit": "ml"}},
            {"item": "Water", "quantity": "1/2 cup", "notes": "", "metric": {"quantity": 120, "unit": "ml"}},
            {"item": "Granulated sugar", "quantity": "1/2 cup", "notes": "", "metric": {"quantity": 100, "unit": "g"}},
            {"item": "Vegetable oil", "quantity": "1/3 cup", "notes": "plus extra for brushing", "metric": {"quantity": 80, "unit": "ml"}},
            {"item": "Salt", "quantity": "1 1/2 teaspoons", "notes": "", "metric": {"quantity": 9, "unit": "g"}},
            {"item": "Egg whites", "quantity": "4 large", "notes": "or 1/2 cup liquid egg whites", "metric": {"quantity": 120, "unit": "g"}}
        ],
        "instructions": [
            "In a large mixing bowl, combine 2 cups of the flour with the yeast. Whisk together to distribute the yeast evenly.",
            "In a small saucepan, combine the milk, water, sugar, 1/3 cup oil, and salt. Warm over low heat, stirring occasionally, until the mixture reaches 120–130°F and the sugar dissolves. It should feel warm but not hot to the touch.",
            "Pour the warm liquid into the flour-yeast mixture. Beat with an electric mixer on low speed for 30 seconds, scraping the bowl frequently, then beat on high speed for 2–3 minutes until smooth. (Or beat vigorously by hand for about 300 strokes.)",
            "Add the egg whites and beat until incorporated.",
            "Mix in 1 more cup of flour and beat for 1 minute.",
            "Gradually stir in enough of the remaining flour (about 1 1/2 to 2 cups) to make a dough that is too stiff to stir.",
            "Turn the dough out onto a lightly floured surface. Knead for 8–10 minutes, adding small amounts of flour as needed, until the dough is smooth, elastic, and no longer sticky. Proper kneading develops the gluten and creates a light, airy texture.",
            "Shape the dough into a ball. Place it in a large bowl lightly coated with nonstick spray or oil. Turn the dough once to coat the surface. Cover with a clean kitchen towel or plastic wrap.",
            "Let the dough rise in a warm, draft-free place (80–85°F) until doubled in size, about 1 1/2 to 2 hours. To test, gently press two fingers into the dough; if the indentation remains, the dough is ready.",
            "Punch down the dough to release the air. Let it rest for 10 minutes.",
            "Shape the dough as desired: rolls, buns, cinnamon rolls, coffee cakes, or loaves. Place shaped dough into pans coated with nonstick spray. Lightly brush the tops with oil to prevent drying.",
            "Cover and let rise again in a warm place until nearly doubled in size, 30–45 minutes.",
            "Preheat the oven to 350°F (175°C).",
            "Bake for 20–25 minutes (rolls and buns) or 30–35 minutes (loaves), until golden brown. The bread should sound hollow when tapped on the bottom.",
            "Remove from pans and let cool on a wire rack. Serve warm or at room temperature."
        ]
    }
}

# Recipe 2: Beef Brisket (Marinaded) (Main Dishes)
beef_brisket = {
    "original_recipe": {
        "name": "Beef Brisket (Marinaded)",
        "subtitle": None,
        "source": None,
        "category": "Main Dishes",
        "servings": "8-10 servings",
        "ingredients": [
            {"item": "Beef brisket", "quantity": "5 to 6 pounds", "notes": "", "metric": {"min": 2270, "max": 2720, "unit": "g"}},
            {"item": "Soy sauce", "quantity": "2 ounces", "notes": "", "metric": {"quantity": 60, "unit": "ml"}},
            {"item": "Worcestershire sauce", "quantity": "2 ounces", "notes": "", "metric": {"quantity": 60, "unit": "ml"}},
            {"item": "Liquid smoke", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 15, "unit": "ml"}},
            {"item": "Pickapper hot sauce", "quantity": "1 teaspoon", "notes": "or other Louisiana-style hot sauce", "metric": {"quantity": 5, "unit": "ml"}},
            {"item": "Accent (MSG)", "quantity": "1 teaspoon", "notes": "optional", "metric": {"quantity": 5, "unit": "g"}},
            {"item": "Dried basil", "quantity": "2 teaspoons", "notes": "", "metric": {"quantity": 2, "unit": "g"}},
            {"item": "Sugar", "quantity": "1/2 teaspoon", "notes": "", "metric": {"quantity": 2, "unit": "g"}}
        ],
        "instructions": [
            "Combine soy sauce, Worcestershire sauce, liquid smoke, hot sauce, Accent, basil, and sugar in a small bowl. Stir to dissolve the sugar.",
            "Place the brisket in a large resealable plastic bag or a shallow dish. Pour the marinade over the brisket, turning to coat all sides.",
            "Refrigerate for 24 hours, turning occasionally.",
            "Preheat oven to 250° F.",
            "Place the marinated brisket in a roasting pan and cover tightly with aluminum foil.",
            "Bake for 6 to 7 hours, until the meat is very tender and easily pulls apart with a fork.",
            "Remove from oven and let rest for 10 minutes.",
            "Slice thinly against the grain using an electric knife for best results. Serve with pan juices."
        ]
    },
    "improved_recipe": {
        "name": "Marinated Beef Brisket",
        "category": "Main Dishes",
        "servings": "8-10 servings",
        "ingredients": [
            {"item": "Beef brisket", "quantity": "5 to 6 pounds", "notes": "trimmed", "metric": {"min": 2270, "max": 2720, "unit": "g"}},
            {"item": "Soy sauce", "quantity": "1/4 cup (2 oz)", "notes": "low-sodium if preferred", "metric": {"quantity": 60, "unit": "ml"}},
            {"item": "Worcestershire sauce", "quantity": "1/4 cup (2 oz)", "notes": "", "metric": {"quantity": 60, "unit": "ml"}},
            {"item": "Liquid smoke", "quantity": "1 tablespoon", "notes": "hickory or mesquite", "metric": {"quantity": 15, "unit": "ml"}},
            {"item": "Hot sauce", "quantity": "1 teaspoon", "notes": "Louisiana-style (such as Tabasco or Crystal)", "metric": {"quantity": 5, "unit": "ml"}},
            {"item": "Garlic powder", "quantity": "1 teaspoon", "notes": "optional, for extra flavor", "metric": {"quantity": 3, "unit": "g"}},
            {"item": "Dried basil", "quantity": "2 teaspoons", "notes": "crushed", "metric": {"quantity": 2, "unit": "g"}},
            {"item": "Brown sugar", "quantity": "1/2 teaspoon", "notes": "", "metric": {"quantity": 2, "unit": "g"}},
            {"item": "Black pepper", "quantity": "1/2 teaspoon", "notes": "freshly ground", "metric": {"quantity": 1, "unit": "g"}}
        ],
        "instructions": [
            "In a small bowl, whisk together the soy sauce, Worcestershire sauce, liquid smoke, hot sauce, garlic powder (if using), basil, brown sugar, and black pepper until the sugar dissolves.",
            "Place the brisket in a large resealable plastic bag or a shallow glass or ceramic dish. Pour the marinade over the brisket, turning to coat all sides. Seal the bag or cover the dish tightly with plastic wrap.",
            "Refrigerate for 24 hours, turning the brisket several times to ensure even marination.",
            "When ready to cook, preheat the oven to 250°F (120°C).",
            "Remove the brisket from the marinade and place it fat-side up in a roasting pan or Dutch oven. Pour any remaining marinade over the top. Cover the pan tightly with heavy-duty aluminum foil or a tight-fitting lid to seal in moisture.",
            "Bake for 6 to 7 hours, until the brisket is fork-tender and the internal temperature reaches at least 190–200°F (88–93°C) for best tenderness.",
            "Remove from the oven and let the brisket rest, covered, for 10–15 minutes before slicing.",
            "Transfer the brisket to a cutting board. Slice thinly across the grain using a sharp knife or electric knife. Slicing against the grain ensures tender, easy-to-chew slices.",
            "Serve hot with the pan juices spooned over the slices. Excellent with mashed potatoes, roasted vegetables, or in sandwiches."
        ]
    }
}

# Recipe 3: Chocolate Cream Pie (Pies & Pastry Fillings)
chocolate_cream_pie = {
    "original_recipe": {
        "name": "Chocolate Cream Pie",
        "subtitle": "Available in 3 sizes: 9-inch, 8-inch, or 6-inch",
        "source": None,
        "category": "Pies & Pastry",
        "servings": "Varies by size",
        "ingredients": [
            {"item": "Sugar (9-inch/8-inch/6-inch)", "quantity": "1 2/3 cups / 1 1/4 cups / 5/8 cup", "notes": "", "metric": {"quantity": 335, "unit": "g"}},
            {"item": "Salt (9-inch/8-inch/6-inch)", "quantity": "2/3 tsp / 1/2 tsp / 1/3 tsp", "notes": "", "metric": {"quantity": 4, "unit": "g"}},
            {"item": "Cornstarch (9-inch/8-inch/6-inch)", "quantity": "2 2/3 tbsp / 2 tbsp / 1 1/3 tbsp", "notes": "", "metric": {"quantity": 40, "unit": "g"}},
            {"item": "Cocoa (9-inch/8-inch/6-inch)", "quantity": "6 tbsp / 4 tbsp / 2 tbsp", "notes": "", "metric": {"quantity": 45, "unit": "g"}},
            {"item": "Flour (9-inch/8-inch/6-inch)", "quantity": "1 1/3 tbsp / 1 tbsp / 1/2 tbsp", "notes": "", "metric": {"quantity": 20, "unit": "g"}},
            {"item": "Milk (9-inch/8-inch/6-inch)", "quantity": "2 2/3 cups / 2 cups / 1 1/3 cups", "notes": "", "metric": {"quantity": 640, "unit": "ml"}},
            {"item": "Egg substitute (9-inch/8-inch/6-inch)", "quantity": "3/4 cup / 1/2 cup / 1/4 cup", "notes": "", "metric": {"quantity": 180, "unit": "ml"}},
            {"item": "Margarine (9-inch/8-inch/6-inch)", "quantity": "2/3 tbsp / 1/2 tbsp / 1/3 tbsp", "notes": "", "metric": {"quantity": 10, "unit": "g"}},
            {"item": "Vanilla extract (9-inch/8-inch/6-inch)", "quantity": "1 1/3 tsp / 1 tsp / 1/2 tsp", "notes": "", "metric": {"quantity": 7, "unit": "ml"}},
            {"item": "Baked pie shell", "quantity": "1 (9-inch, 8-inch, or 6-inch)", "notes": "", "metric": None},
            {"item": "Meringue topping", "quantity": "as needed", "notes": "see Meringue recipe", "metric": None}
        ],
        "instructions": [
            "Mix sugar, salt, cornstarch, cocoa, and flour in top of double boiler.",
            "Stir in milk and place over boiling water.",
            "Boil for 3 minutes, stirring constantly.",
            "Temper the egg substitute by slowly whisking a small amount of the hot mixture into it, then pour the tempered egg back into the double boiler.",
            "Cook over boiling water for 10 minutes, stirring occasionally.",
            "Blend in margarine and cool thoroughly.",
            "Blend in vanilla extract.",
            "Pour into cooled, baked pie shell.",
            "Finish with meringue topping (see Meringue recipe). Bake according to meringue instructions."
        ]
    },
    "improved_recipe": {
        "name": "Chocolate Cream Pie",
        "category": "Pies & Pastry",
        "servings": "8 servings (9-inch pie)",
        "ingredients": [
            {"item": "Granulated sugar", "quantity": "1 2/3 cups (for 9-inch)", "notes": "reduce to 1 1/4 cups for 8-inch, 5/8 cup for 6-inch", "metric": {"quantity": 335, "unit": "g"}},
            {"item": "Salt", "quantity": "2/3 teaspoon (for 9-inch)", "notes": "reduce to 1/2 tsp for 8-inch, 1/3 tsp for 6-inch", "metric": {"quantity": 4, "unit": "g"}},
            {"item": "Cornstarch", "quantity": "2 2/3 tablespoons (for 9-inch)", "notes": "reduce to 2 tbsp for 8-inch, 1 1/3 tbsp for 6-inch", "metric": {"quantity": 40, "unit": "g"}},
            {"item": "Unsweetened cocoa powder", "quantity": "6 tablespoons (for 9-inch)", "notes": "reduce to 4 tbsp for 8-inch, 2 tbsp for 6-inch", "metric": {"quantity": 45, "unit": "g"}},
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
            "In the top of the double boiler (off the heat), whisk together the sugar, salt, cornstarch, cocoa powder, and flour until well combined and lump-free.",
            "Gradually whisk in the milk until the mixture is smooth.",
            "Place the top of the double boiler over the simmering water. Cook, stirring constantly, until the mixture comes to a boil and thickens, about 8–10 minutes. Let it boil gently for 3 minutes, continuing to stir.",
            "In a small bowl, lightly beat the egg substitute (or egg yolks). Slowly whisk about 1/2 cup of the hot chocolate mixture into the egg to temper it, then pour the tempered egg back into the double boiler, whisking constantly.",
            "Cook over the simmering water for an additional 10 minutes, stirring occasionally, until the filling is thick and glossy.",
            "Remove from heat and stir in the margarine or butter until melted and fully incorporated.",
            "Let the filling cool for about 10–15 minutes, stirring occasionally to prevent a skin from forming. When slightly cooled, stir in the vanilla extract.",
            "Pour the chocolate filling into the cooled, baked pie shell. Smooth the top with a spatula.",
            "If topping with meringue: Spread the meringue over the filling while the filling is still warm, sealing the edges to the crust. Bake at 300°F (150°C) for 15–20 minutes until the meringue is lightly golden. Let cool completely before slicing.",
            "If topping with whipped cream: Refrigerate the pie until fully set (at least 3 hours or overnight), then top with whipped cream just before serving.",
            "Store leftovers covered in the refrigerator for up to 3 days."
        ]
    }
}

# Recipe 4: Cocoanut Cake (Cakes)
cocoanut_cake = {
    "original_recipe": {
        "name": "Cocoanut Cake",
        "subtitle": None,
        "source": None,
        "category": "Cakes",
        "servings": None,
        "ingredients": [
            {"item": "Deluxe White Cake", "quantity": "1 recipe", "notes": "baked in two 9-inch layers", "metric": None},
            {"item": "Confectioners' sugar", "quantity": "1 pound", "notes": "", "metric": {"quantity": 450, "unit": "g"}},
            {"item": "Butter or margarine", "quantity": "1/2 cup", "notes": "softened", "metric": {"quantity": 113, "unit": "g"}},
            {"item": "Milk", "quantity": "1/4 cup", "notes": "", "metric": {"quantity": 60, "unit": "ml"}},
            {"item": "Vanilla extract", "quantity": "1/2 teaspoon", "notes": "", "metric": {"quantity": 2.5, "unit": "ml"}},
            {"item": "Shredded coconut", "quantity": "2 cups", "notes": "sweetened or unsweetened", "metric": {"quantity": 160, "unit": "g"}}
        ],
        "instructions": [
            "Bake Deluxe White Cake according to recipe directions in two 9-inch round pans. Cool completely.",
            "In a mixing bowl, cream together confectioners' sugar and softened butter or margarine until light and fluffy.",
            "Gradually add milk and vanilla extract, beating until smooth and spreadable. Add more milk if needed for desired consistency.",
            "Place one cake layer on a serving plate. Spread with a layer of icing.",
            "Sprinkle coconut generously over the icing on the first layer.",
            "Place the second cake layer on top. Frost the top and sides of the cake with the remaining icing.",
            "Press shredded coconut onto the top and sides of the cake, covering completely.",
            "Refrigerate until serving time."
        ]
    },
    "improved_recipe": {
        "name": "Coconut Layer Cake",
        "category": "Cakes",
        "servings": "12 servings",
        "ingredients": [
            {"item": "Deluxe White Cake", "quantity": "1 recipe", "notes": "or your favorite white cake, baked in two 9-inch round pans and cooled", "metric": None},
            {"item": "Confectioners' sugar", "quantity": "4 cups (1 pound)", "notes": "sifted", "metric": {"quantity": 450, "unit": "g"}},
            {"item": "Butter or margarine", "quantity": "1/2 cup (1 stick)", "notes": "softened to room temperature", "metric": {"quantity": 113, "unit": "g"}},
            {"item": "Milk", "quantity": "1/4 cup", "notes": "plus more as needed", "metric": {"quantity": 60, "unit": "ml"}},
            {"item": "Vanilla extract", "quantity": "1/2 teaspoon", "notes": "", "metric": {"quantity": 2.5, "unit": "ml"}},
            {"item": "Sweetened shredded coconut", "quantity": "2 to 2 1/2 cups", "notes": "or unsweetened if preferred", "metric": {"quantity": 180, "unit": "g"}}
        ],
        "instructions": [
            "Bake the Deluxe White Cake (or your favorite white cake recipe) in two greased and floured 9-inch round cake pans according to the recipe directions. Let cool in the pans for 10 minutes, then turn out onto wire racks to cool completely.",
            "While the cakes cool, prepare the buttercream icing: In a large bowl, beat the softened butter or margarine with an electric mixer until creamy.",
            "Gradually add the sifted confectioners' sugar, about 1 cup at a time, beating on low speed after each addition.",
            "Add the milk and vanilla extract. Beat on medium-high speed for 2–3 minutes until the icing is light, fluffy, and spreadable. If the icing is too thick, add a little more milk, 1 teaspoon at a time.",
            "Place one cake layer on a serving plate or cake stand. Spread about 1/2 cup of the icing evenly over the top.",
            "Sprinkle about 1/2 to 3/4 cup of the shredded coconut over the icing on the first layer.",
            "Carefully place the second cake layer on top, pressing gently to adhere.",
            "Frost the top of the cake with a generous layer of icing, then frost the sides, using an offset spatula or butter knife for a smooth finish.",
            "While the icing is still soft, gently press the remaining shredded coconut onto the top and sides of the cake, covering it completely. You may need to work in sections and press the coconut gently with your hands.",
            "Refrigerate the cake for at least 1 hour before serving to let the icing set.",
            "Store leftover cake covered in the refrigerator for up to 4 days. Bring to room temperature before serving for best flavor and texture."
        ]
    }
}

# Recipe 5: Salmon Croquettes (Main Dishes)
salmon_croquettes = {
    "original_recipe": {
        "name": "Salmon Croquettes",
        "subtitle": None,
        "source": None,
        "category": "Main Dishes",
        "servings": None,
        "ingredients": [
            {"item": "Canned salmon", "quantity": "15 ounces", "notes": "bones and skin removed", "metric": {"quantity": 425, "unit": "g"}},
            {"item": "Onion", "quantity": "1 tablespoon", "notes": "minced", "metric": {"quantity": 10, "unit": "g"}},
            {"item": "Egg", "quantity": "1", "notes": "", "metric": {"quantity": 50, "unit": "g"}},
            {"item": "Soda crackers", "quantity": "as needed", "notes": "crushed", "metric": None},
            {"item": "Tabasco sauce", "quantity": "to taste", "notes": "", "metric": None},
            {"item": "Vegetable oil", "quantity": "for frying", "notes": "", "metric": None}
        ],
        "instructions": [
            "Drain the canned salmon and remove all bones and skin. Flake the salmon with a fork.",
            "In a mixing bowl, combine the flaked salmon, minced onion, egg, and a few dashes of Tabasco sauce.",
            "Add crushed soda crackers until the mixture holds together and can be shaped into patties.",
            "Shape the mixture into patties about 3 inches in diameter and 1/2 inch thick.",
            "Heat vegetable oil in a frying pan over medium heat.",
            "Fry the croquettes until browned on both sides, turning once.",
            "Drain on paper towels to remove excess oil. Serve hot."
        ]
    },
    "improved_recipe": {
        "name": "Classic Salmon Croquettes",
        "category": "Main Dishes",
        "servings": "4 servings (8 small croquettes)",
        "ingredients": [
            {"item": "Canned salmon", "quantity": "15 ounces (1 can)", "notes": "drained, bones and skin removed", "metric": {"quantity": 425, "unit": "g"}},
            {"item": "Onion", "quantity": "2 tablespoons", "notes": "finely minced", "metric": {"quantity": 20, "unit": "g"}},
            {"item": "Egg", "quantity": "1 large", "notes": "lightly beaten", "metric": {"quantity": 50, "unit": "g"}},
            {"item": "Soda crackers or saltines", "quantity": "1/2 to 3/4 cup", "notes": "finely crushed (about 12–15 crackers)", "metric": {"quantity": 60, "unit": "g"}},
            {"item": "Tabasco or hot sauce", "quantity": "1/4 to 1/2 teaspoon", "notes": "or to taste", "metric": {"quantity": 1.5, "unit": "ml"}},
            {"item": "Black pepper", "quantity": "1/4 teaspoon", "notes": "freshly ground", "metric": {"quantity": 0.5, "unit": "g"}},
            {"item": "Lemon juice", "quantity": "1 teaspoon", "notes": "optional, for brightness", "metric": {"quantity": 5, "unit": "ml"}},
            {"item": "Vegetable oil or butter", "quantity": "2 to 3 tablespoons", "notes": "for pan-frying", "metric": {"quantity": 40, "unit": "ml"}}
        ],
        "instructions": [
            "Drain the canned salmon thoroughly. Place it in a mixing bowl and use a fork to flake it, removing any large bones and skin (though small soft bones are safe and add calcium).",
            "Add the minced onion, beaten egg, Tabasco or hot sauce, black pepper, and lemon juice (if using). Mix gently to combine.",
            "Stir in the crushed crackers, a little at a time, until the mixture holds together when pressed into a patty. It should be moist but not wet. If too dry, add a teaspoon of water or milk; if too wet, add more cracker crumbs.",
            "Shape the mixture into 8 small patties, about 2 1/2 to 3 inches in diameter and about 1/2 inch thick. Place on a plate.",
            "Heat 2 tablespoons of vegetable oil or butter in a large skillet over medium heat until shimmering.",
            "Carefully place the croquettes in the skillet, working in batches if necessary to avoid crowding. Cook for 3–4 minutes per side, until golden brown and crispy. Handle gently when flipping to keep them intact.",
            "Transfer the cooked croquettes to a plate lined with paper towels to drain excess oil.",
            "Serve hot with lemon wedges, tartar sauce, or a side of coleslaw and cornbread. Enjoy!"
        ]
    }
}

# Add recipes to appropriate categories
for category in data["categories"]:
    if category["name"] == "Main Dishes":
        category["recipes"].append(beef_brisket)
        category["recipes"].append(salmon_croquettes)
    elif category["name"] == "Breads & Breakfast":
        category["recipes"].append(basic_sweet_dough)
    elif category["name"] == "Cakes":
        category["recipes"].append(cocoanut_cake)
    elif category["name"] == "Pies & Pastry Fillings":
        category["recipes"].append(chocolate_cream_pie)

# Save the updated recipes.json
with open('recipes.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Successfully added 5 recipes:")
print("- Basic Sweet Dough (Breads & Breakfast)")
print("- Beef Brisket (Marinaded) (Main Dishes)")
print("- Chocolate Cream Pie (Pies & Pastry Fillings)")
print("- Cocoanut Cake (Cakes)")
print("- Salmon Croquettes (Main Dishes)")
