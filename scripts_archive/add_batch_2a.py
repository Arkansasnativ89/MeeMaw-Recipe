import json

# Load the current recipes.json
with open('recipes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Recipe 1: Stöllen (Alma Finken Carle Recipe) (Breads & Breakfast)
stollen_alma = {
    "original_recipe": {
        "name": "Stöllen",
        "subtitle": "Alma Finken Carle Recipe",
        "source": "Alma Finken Carle",
        "category": "Breads & Breakfast",
        "servings": "6 half loaves",
        "ingredients": [
            {"item": "Milk", "quantity": "1 pint", "notes": "2%, 1/2% or skim, scalded", "metric": {"quantity": 480, "unit": "ml"}},
            {"item": "Dry yeast", "quantity": "2 packages", "notes": "", "metric": {"quantity": 14, "unit": "g"}},
            {"item": "All purpose flour, sifted", "quantity": "8 cups", "notes": "", "metric": {"quantity": 960, "unit": "g"}},
            {"item": "Margarine, softened", "quantity": "1 pound (reserve 3 tablespoons)", "notes": "", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Sugar", "quantity": "1 cup", "notes": "", "metric": {"quantity": 200, "unit": "g"}},
            {"item": "Eggs", "quantity": "4", "notes": "or egg substitute", "metric": {"quantity": 200, "unit": "g"}},
            {"item": "Candied fruit and/or seeded Muscat raisins", "quantity": "3/4 to 1 pound", "notes": "", "metric": {"min": 340, "max": 454, "unit": "g"}},
            {"item": "Rum", "quantity": "1/2 cup", "notes": "", "metric": {"quantity": 120, "unit": "ml"}},
            {"item": "Lemon", "quantity": "1", "notes": "grated rind only", "metric": None},
            {"item": "Salt", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 6, "unit": "g"}},
            {"item": "Chopped almonds", "quantity": "1/2 cup", "notes": "", "metric": {"quantity": 60, "unit": "g"}},
            {"item": "Rosewater", "quantity": "3 tablespoons", "notes": "or to taste", "metric": {"quantity": 45, "unit": "ml"}}
        ],
        "instructions": [
            "Set sponge using one cup of flour, milk (cooled to lukewarm) and yeast. Mix well, cover and set in warm place to become light.",
            "Put fruit, raisins and grated lemon rinds in a bowl. Pour rosewater and rum over this. Cover and set aside.",
            "In a large mixing bowl, cream the softened margarine and sugar. Add the eggs, one at a time and mix well.",
            "Put the remaining flour and salt in a large container. Make a 'hollow' in the flour and add the margarine mixture and the sponge and fruit mixtures. Mix well by hand, adding more flour if necessary.",
            "Knead until not too sticky. Let rise in a warm place until light.",
            "Divide into six 'half loaves'. Shape into round lumps and flatten.",
            "Spread with reserved melted margarine, then sugar and nuts. Fold over and place in baking pan.",
            "Pat top with melted margarine and place in a warm place to rise.",
            "Bake in moderate oven at 350° F for forty to sixty minutes."
        ]
    },
    "improved_recipe": {
        "name": "Traditional German Stöllen (Alma's Recipe)",
        "category": "Breads & Breakfast",
        "servings": "6 small loaves",
        "ingredients": [
            {"item": "Milk", "quantity": "2 cups (1 pint)", "notes": "any fat percentage", "metric": {"quantity": 480, "unit": "ml"}},
            {"item": "Active dry yeast", "quantity": "2 packets (4 1/2 tsp)", "notes": "", "metric": {"quantity": 14, "unit": "g"}},
            {"item": "All-purpose flour", "quantity": "8 cups", "notes": "sifted, divided", "metric": {"quantity": 960, "unit": "g"}},
            {"item": "Margarine or butter", "quantity": "1 pound (4 sticks)", "notes": "softened, reserve 3 tbsp", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Granulated sugar", "quantity": "1 cup", "notes": "plus extra for topping", "metric": {"quantity": 200, "unit": "g"}},
            {"item": "Eggs", "quantity": "4 large", "notes": "or 1 cup egg substitute", "metric": {"quantity": 200, "unit": "g"}},
            {"item": "Candied fruit mix and/or Muscat raisins", "quantity": "3/4 to 1 pound", "notes": "seeded raisins", "metric": {"min": 340, "max": 454, "unit": "g"}},
            {"item": "Rum", "quantity": "1/2 cup", "notes": "can substitute rum extract", "metric": {"quantity": 120, "unit": "ml"}},
            {"item": "Fresh lemon zest", "quantity": "from 1 lemon", "notes": "finely grated", "metric": None},
            {"item": "Salt", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 6, "unit": "g"}},
            {"item": "Chopped almonds", "quantity": "1/2 cup", "notes": "", "metric": {"quantity": 60, "unit": "g"}},
            {"item": "Rosewater", "quantity": "3 tablespoons", "notes": "adjust to taste", "metric": {"quantity": 45, "unit": "ml"}}
        ],
        "instructions": [
            "Scald the milk and let it cool to lukewarm (110°F). In a medium bowl, combine 1 cup of the flour, the lukewarm milk, and the yeast. Mix well, cover, and set in a warm place to rise until light and bubbly, about 30-45 minutes.",
            "Meanwhile, combine the candied fruit, raisins, and grated lemon zest in a bowl. Pour the rosewater and rum over the fruit mixture. Cover and set aside to macerate.",
            "In a large mixing bowl, cream together the softened margarine (reserving 3 tablespoons) and 1 cup sugar until light and fluffy. Add the eggs one at a time, beating well after each addition.",
            "In a very large bowl or on a clean work surface, place the remaining 7 cups of flour and the salt. Make a well in the center. Add the creamed margarine mixture, the yeast sponge, and the fruit mixture (including any liquid). Mix well by hand, working the ingredients together and adding a bit more flour if the dough is too sticky.",
            "Knead the dough on a lightly floured surface for about 8-10 minutes, until smooth and not too sticky. Place in a greased bowl, cover, and let rise in a warm place until doubled in size, about 1-2 hours.",
            "Punch down the dough and divide it into 6 equal portions. Shape each portion into a round lump, then flatten slightly into an oval.",
            "Melt the reserved 3 tablespoons of margarine. Brush each oval with melted margarine, then sprinkle with sugar and chopped almonds. Fold each oval in half lengthwise and place in a greased baking pan.",
            "Brush the tops with additional melted margarine. Cover and let rise in a warm place until puffy, about 45-60 minutes.",
            "Preheat oven to 350°F (175°C). Bake for 40-60 minutes, or until golden brown and the bread sounds hollow when tapped. If the tops brown too quickly, tent with foil.",
            "Cool on wire racks. Dust with powdered sugar before serving if desired. Stöllen keeps well and improves with age when wrapped tightly."
        ]
    }
}

# Recipe 2: Stöllen (Kanis Recipe) (Breads & Breakfast)
stollen_kanis = {
    "original_recipe": {
        "name": "Stöllen (Kanis Recipe)",
        "subtitle": None,
        "source": "Kanis",
        "category": "Breads & Breakfast",
        "servings": "Many loaves (large batch)",
        "ingredients": [
            {"item": "Almond extract", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 5, "unit": "ml"}},
            {"item": "Butter or margarine", "quantity": "1 pound", "notes": "", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Cherries", "quantity": "1/2 pound", "notes": "", "metric": {"quantity": 227, "unit": "g"}},
            {"item": "Citron", "quantity": "1/2 pound", "notes": "", "metric": {"quantity": 227, "unit": "g"}},
            {"item": "Eggs", "quantity": "6", "notes": "or egg substitute", "metric": {"quantity": 300, "unit": "g"}},
            {"item": "Flour", "quantity": "7 to 12 pounds", "notes": "", "metric": {"min": 3175, "max": 5440, "unit": "g"}},
            {"item": "Lemon peel", "quantity": "1/4 pound", "notes": "", "metric": {"quantity": 113, "unit": "g"}},
            {"item": "Lemons", "quantity": "2", "notes": "rind only", "metric": None},
            {"item": "Milk", "quantity": "1 quart", "notes": "", "metric": {"quantity": 960, "unit": "ml"}},
            {"item": "Chopped almonds", "quantity": "1/2 pound", "notes": "", "metric": {"quantity": 227, "unit": "g"}},
            {"item": "Chopped pecans", "quantity": "1/2 pound", "notes": "", "metric": {"quantity": 227, "unit": "g"}},
            {"item": "Orange peel", "quantity": "1/4 pound", "notes": "", "metric": {"quantity": 113, "unit": "g"}},
            {"item": "Pineapple", "quantity": "1/2 pound", "notes": "", "metric": {"quantity": 227, "unit": "g"}},
            {"item": "Raisins", "quantity": "1/4 pound", "notes": "may be omitted", "metric": {"quantity": 113, "unit": "g"}},
            {"item": "Rosewater", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 15, "unit": "ml"}},
            {"item": "Salt", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 18, "unit": "g"}},
            {"item": "Sugar", "quantity": "4 pounds (1 1/2 pounds will do)", "notes": "", "metric": {"min": 680, "max": 1800, "unit": "g"}},
            {"item": "Regular commercial yeast", "quantity": "6 packages", "notes": "", "metric": {"quantity": 42, "unit": "g"}},
            {"item": "Whiskey", "quantity": "1/2 cup", "notes": "for soaking fruit", "metric": {"quantity": 120, "unit": "ml"}}
        ],
        "instructions": [
            "Soak fruit and sugar in 1/2 cup whiskey overnight. Add nuts the next morning.",
            "Cream butter, eggs, salt, and sugar together, add rest of the ingredients.",
            "Use enough flour to make a stiff dough.",
            "Let dough rise slowly for a long time (overnight).",
            "Handle dough carefully, roll out lightly, cut into 1 1/2 pound pieces and tuck under.",
            "Let rise again before baking.",
            "Bake at 325° F for one hour.",
            "When baked, brush top with melted butter or margarine. Then rub almond flavored sugar on top."
        ]
    },
    "improved_recipe": {
        "name": "Traditional German Stöllen (Kanis Family Recipe)",
        "category": "Breads & Breakfast",
        "servings": "Multiple loaves (large holiday batch)",
        "ingredients": [
            {"item": "Granulated sugar", "quantity": "1 1/2 to 4 pounds", "notes": "use 1 1/2 lbs for less sweet version", "metric": {"min": 680, "max": 1800, "unit": "g"}},
            {"item": "Mixed candied fruit (cherries, citron, lemon peel, orange peel, pineapple)", "quantity": "about 2 pounds total", "notes": "chopped", "metric": {"quantity": 900, "unit": "g"}},
            {"item": "Raisins", "quantity": "1/4 pound", "notes": "optional", "metric": {"quantity": 113, "unit": "g"}},
            {"item": "Whiskey or brandy", "quantity": "1/2 cup", "notes": "for macerating fruit", "metric": {"quantity": 120, "unit": "ml"}},
            {"item": "Chopped almonds", "quantity": "1/2 pound", "notes": "", "metric": {"quantity": 227, "unit": "g"}},
            {"item": "Chopped pecans", "quantity": "1/2 pound", "notes": "", "metric": {"quantity": 227, "unit": "g"}},
            {"item": "Butter or margarine", "quantity": "1 pound (4 sticks)", "notes": "plus extra for brushing", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Eggs", "quantity": "6 large", "notes": "or 1 1/2 cups egg substitute", "metric": {"quantity": 300, "unit": "g"}},
            {"item": "Salt", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 18, "unit": "g"}},
            {"item": "Milk", "quantity": "1 quart", "notes": "", "metric": {"quantity": 960, "unit": "ml"}},
            {"item": "Active dry yeast", "quantity": "6 packets", "notes": "", "metric": {"quantity": 42, "unit": "g"}},
            {"item": "All-purpose flour", "quantity": "7 to 12 pounds", "notes": "use enough for stiff dough", "metric": {"min": 3175, "max": 5440, "unit": "g"}},
            {"item": "Fresh lemon zest", "quantity": "from 2 lemons", "notes": "finely grated", "metric": None},
            {"item": "Rosewater", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 15, "unit": "ml"}},
            {"item": "Almond extract", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 5, "unit": "ml"}}
        ],
        "instructions": [
            "The night before: In a large bowl, combine all the candied fruit, raisins (if using), and sugar. Pour 1/2 cup whiskey over the mixture, stir well, cover, and let macerate overnight.",
            "The next morning: Add the chopped almonds and pecans to the fruit mixture.",
            "In a very large mixing bowl, cream together the butter, eggs, salt, and remaining sugar until well combined.",
            "Warm the milk to lukewarm (110°F) and dissolve the yeast in it. Let stand for 5 minutes until foamy.",
            "Add the yeast mixture, the fruit-nut mixture, lemon zest, rosewater, and almond extract to the creamed butter mixture. Mix well.",
            "Gradually add flour, starting with about 7 pounds, mixing and kneading until you have a stiff dough that is smooth but not sticky. Add more flour as needed, up to 12 pounds total.",
            "Cover the dough and let it rise slowly in a cool place for a long time—overnight is ideal. The slow rise develops flavor.",
            "The next day, turn the dough out onto a lightly floured surface. Handle gently. Roll or pat out lightly to about 1 inch thickness.",
            "Cut the dough into portions of about 1 1/2 pounds each. Shape each portion into a loaf by folding and tucking the edges under.",
            "Place the loaves on greased baking sheets. Cover and let rise again until puffy, about 1-2 hours.",
            "Preheat oven to 325°F (165°C). Bake for about 1 hour, or until golden brown and the loaves sound hollow when tapped.",
            "While still hot, brush the tops with melted butter or margarine. Mix some powdered sugar with almond extract and rub this almond-flavored sugar on top of each loaf.",
            "Cool completely before slicing. Stöllen improves with age and can be stored for weeks when wrapped tightly."
        ]
    }
}

# Recipe 3: Sugar Cookies (Alice Carle) (Cookies & Bars)
sugar_cookies_alice = {
    "original_recipe": {
        "name": "Sugar Cookies (Alice Carle)",
        "subtitle": None,
        "source": "Alice Carle",
        "category": "Cookies & Bars",
        "servings": None,
        "ingredients": [
            {"item": "Powdered sugar", "quantity": "1 1/2 cups", "notes": "", "metric": {"quantity": 180, "unit": "g"}},
            {"item": "Margarine", "quantity": "1 cup", "notes": "", "metric": {"quantity": 227, "unit": "g"}},
            {"item": "Egg", "quantity": "1", "notes": "or egg substitute", "metric": {"quantity": 50, "unit": "g"}},
            {"item": "Vanilla", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 5, "unit": "ml"}},
            {"item": "Almond flavoring", "quantity": "1/2 teaspoon", "notes": "", "metric": {"quantity": 2.5, "unit": "ml"}},
            {"item": "Flour", "quantity": "2 1/2 cups", "notes": "", "metric": {"quantity": 300, "unit": "g"}},
            {"item": "Cream of tartar", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 3, "unit": "g"}},
            {"item": "Salt", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 6, "unit": "g"}}
        ],
        "instructions": [
            "Mix well, then refrigerate two to three hours, or overnight before rolling.",
            "Roll out to desired thickness. Cut into any desirable shape.",
            "Put on a baking sheet that has been coated with a nonstick vegetable spray.",
            "Bake at 350° F for ten to eleven minutes."
        ]
    },
    "improved_recipe": {
        "name": "Alice Carle's Sugar Cookies",
        "category": "Cookies & Bars",
        "servings": "About 3-4 dozen cookies",
        "ingredients": [
            {"item": "Powdered sugar", "quantity": "1 1/2 cups", "notes": "sifted", "metric": {"quantity": 180, "unit": "g"}},
            {"item": "Margarine or butter", "quantity": "1 cup (2 sticks)", "notes": "softened", "metric": {"quantity": 227, "unit": "g"}},
            {"item": "Egg", "quantity": "1 large", "notes": "or 1/4 cup egg substitute", "metric": {"quantity": 50, "unit": "g"}},
            {"item": "Vanilla extract", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 5, "unit": "ml"}},
            {"item": "Almond extract", "quantity": "1/2 teaspoon", "notes": "", "metric": {"quantity": 2.5, "unit": "ml"}},
            {"item": "All-purpose flour", "quantity": "2 1/2 cups", "notes": "", "metric": {"quantity": 300, "unit": "g"}},
            {"item": "Cream of tartar", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 3, "unit": "g"}},
            {"item": "Salt", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 6, "unit": "g"}}
        ],
        "instructions": [
            "In a large bowl, cream together the powdered sugar and softened margarine until light and fluffy.",
            "Beat in the egg, vanilla, and almond extract until well combined.",
            "In a separate bowl, whisk together the flour, cream of tartar, and salt.",
            "Gradually add the dry ingredients to the wet ingredients, mixing until a soft dough forms.",
            "Wrap the dough tightly in plastic wrap and refrigerate for 2-3 hours, or overnight. This makes the dough easier to roll and helps the cookies hold their shape.",
            "When ready to bake, preheat oven to 350°F (175°C). Line baking sheets with parchment paper or coat lightly with nonstick spray.",
            "On a lightly floured surface, roll out the chilled dough to your desired thickness (1/4 inch for crisp cookies, 1/2 inch for softer cookies).",
            "Cut into desired shapes using cookie cutters. Place on prepared baking sheets, spacing about 1 inch apart.",
            "Bake for 10-11 minutes, or until the edges are just barely golden. Do not overbake; the cookies should remain pale.",
            "Cool on the baking sheets for 2 minutes, then transfer to wire racks to cool completely. Decorate with icing or sprinkles if desired."
        ]
    }
}

# Recipe 4: Sugar Cookies (Preferred) (Cookies & Bars)
sugar_cookies_preferred = {
    "original_recipe": {
        "name": "Sugar Cookies (Prefered)",
        "subtitle": None,
        "source": None,
        "category": "Cookies & Bars",
        "servings": None,
        "ingredients": [
            {"item": "Flour", "quantity": "2 1/4 cups", "notes": "", "metric": {"quantity": 270, "unit": "g"}},
            {"item": "Salt", "quantity": "1/2 teaspoon", "notes": "", "metric": {"quantity": 3, "unit": "g"}},
            {"item": "Baking powder", "quantity": "2 teaspoons", "notes": "", "metric": {"quantity": 10, "unit": "g"}},
            {"item": "Eggs", "quantity": "2", "notes": "or egg substitute", "metric": {"quantity": 100, "unit": "g"}},
            {"item": "Sugar", "quantity": "1 cup", "notes": "", "metric": {"quantity": 200, "unit": "g"}},
            {"item": "Vanilla", "quantity": "1/2 teaspoon", "notes": "", "metric": {"quantity": 2.5, "unit": "ml"}},
            {"item": "Milk", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 15, "unit": "ml"}},
            {"item": "Margarine", "quantity": "1/2 cup", "notes": "", "metric": {"quantity": 113, "unit": "g"}}
        ],
        "instructions": [
            "Sift flour, salt, and baking powder together.",
            "Cream margarine and sugar together, add egg and vanilla; then add sifted ingredients and milk.",
            "Roll out to desired thickness. Cut into various shapes and place a baking sheet that has been lightly coated with a nonstick vegetable spray.",
            "Sprinkle with sugar and bake at 375° F for twelve minutes."
        ]
    },
    "improved_recipe": {
        "name": "Preferred Sugar Cookies",
        "category": "Cookies & Bars",
        "servings": "About 2-3 dozen cookies",
        "ingredients": [
            {"item": "All-purpose flour", "quantity": "2 1/4 cups", "notes": "", "metric": {"quantity": 270, "unit": "g"}},
            {"item": "Baking powder", "quantity": "2 teaspoons", "notes": "", "metric": {"quantity": 10, "unit": "g"}},
            {"item": "Salt", "quantity": "1/2 teaspoon", "notes": "", "metric": {"quantity": 3, "unit": "g"}},
            {"item": "Margarine or butter", "quantity": "1/2 cup (1 stick)", "notes": "softened", "metric": {"quantity": 113, "unit": "g"}},
            {"item": "Granulated sugar", "quantity": "1 cup", "notes": "plus extra for sprinkling", "metric": {"quantity": 200, "unit": "g"}},
            {"item": "Eggs", "quantity": "2 large", "notes": "or 1/2 cup egg substitute", "metric": {"quantity": 100, "unit": "g"}},
            {"item": "Vanilla extract", "quantity": "1/2 teaspoon", "notes": "", "metric": {"quantity": 2.5, "unit": "ml"}},
            {"item": "Milk", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 15, "unit": "ml"}}
        ],
        "instructions": [
            "In a medium bowl, sift together the flour, baking powder, and salt. Set aside.",
            "In a large bowl, cream the margarine and 1 cup sugar together until light and fluffy.",
            "Beat in the eggs and vanilla until well combined.",
            "Gradually add the sifted dry ingredients to the creamed mixture, alternating with the milk, mixing until a dough forms.",
            "If the dough is too soft to roll, wrap it in plastic and refrigerate for 30 minutes to 1 hour.",
            "Preheat oven to 375°F (190°C). Line baking sheets with parchment paper or coat lightly with nonstick spray.",
            "On a lightly floured surface, roll out the dough to your desired thickness (about 1/4 inch for crisp cookies).",
            "Cut into various shapes using cookie cutters and place on prepared baking sheets, spacing about 1 inch apart.",
            "Sprinkle the tops of the cookies lightly with granulated sugar.",
            "Bake for 12 minutes, or until the edges are lightly golden.",
            "Cool on the baking sheets for 2 minutes, then transfer to wire racks to cool completely."
        ]
    }
}

# Recipe 5: Sugar Cookies (Zuckerkuchen) (Cookies & Bars)
sugar_cookies_zuckerkuchen = {
    "original_recipe": {
        "name": "Sugar Cookies (Zuckerkuchen)",
        "subtitle": None,
        "source": None,
        "category": "Cookies & Bars",
        "servings": None,
        "ingredients": [
            {"item": "Flour", "quantity": "4 cups", "notes": "", "metric": {"quantity": 480, "unit": "g"}},
            {"item": "Soda", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 5, "unit": "g"}},
            {"item": "Salt", "quantity": "1/2 teaspoon", "notes": "", "metric": {"quantity": 3, "unit": "g"}},
            {"item": "Sugar", "quantity": "1 1/2 cups", "notes": "", "metric": {"quantity": 300, "unit": "g"}},
            {"item": "Margarine", "quantity": "1 1/2 cups", "notes": "Grandmother used Lard", "metric": {"quantity": 340, "unit": "g"}},
            {"item": "Low fat buttermilk or sour milk", "quantity": "1/2 cup", "notes": "", "metric": {"quantity": 120, "unit": "ml"}},
            {"item": "Eggs", "quantity": "2", "notes": "or egg substitute", "metric": {"quantity": 100, "unit": "g"}},
            {"item": "Vanilla", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 5, "unit": "ml"}},
            {"item": "Lemon extract", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 5, "unit": "ml"}}
        ],
        "instructions": [
            "Cream sugar and margarine, add eggs and mix well.",
            "Combine dry ingredients. Add flavorings to milk.",
            "Add dry ingredients and flavorings to items in first step in stages, about 1/3 of each quantity at a time. After each addition, mix well.",
            "Roll out to 1/4\" (or to desired thickness). Cut into various shapes and place on a baking sheet that has been coated with a nonstick vegetable spray.",
            "Bake at 350° F for ten to eleven minutes."
        ]
    },
    "improved_recipe": {
        "name": "German Sugar Cookies (Zuckerkuchen)",
        "category": "Cookies & Bars",
        "servings": "About 5-6 dozen cookies",
        "ingredients": [
            {"item": "All-purpose flour", "quantity": "4 cups", "notes": "", "metric": {"quantity": 480, "unit": "g"}},
            {"item": "Baking soda", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 5, "unit": "g"}},
            {"item": "Salt", "quantity": "1/2 teaspoon", "notes": "", "metric": {"quantity": 3, "unit": "g"}},
            {"item": "Granulated sugar", "quantity": "1 1/2 cups", "notes": "", "metric": {"quantity": 300, "unit": "g"}},
            {"item": "Margarine or butter", "quantity": "1 1/2 cups (3 sticks)", "notes": "softened (traditional used lard)", "metric": {"quantity": 340, "unit": "g"}},
            {"item": "Eggs", "quantity": "2 large", "notes": "or 1/2 cup egg substitute", "metric": {"quantity": 100, "unit": "g"}},
            {"item": "Low-fat buttermilk or sour milk", "quantity": "1/2 cup", "notes": "", "metric": {"quantity": 120, "unit": "ml"}},
            {"item": "Vanilla extract", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 5, "unit": "ml"}},
            {"item": "Lemon extract", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 5, "unit": "ml"}}
        ],
        "instructions": [
            "In a large bowl, cream together the sugar and margarine until light and fluffy.",
            "Beat in the eggs and mix well.",
            "In a separate bowl, combine the flour, baking soda, and salt.",
            "In a small bowl or measuring cup, combine the buttermilk, vanilla extract, and lemon extract.",
            "Add the dry ingredients and the flavored milk to the creamed mixture in stages: add about 1/3 of the dry ingredients, mix well, then add about 1/3 of the milk mixture, and mix well. Repeat until all ingredients are incorporated. The dough should be smooth and pliable.",
            "If the dough is too soft, wrap in plastic and refrigerate for 30 minutes to 1 hour.",
            "Preheat oven to 350°F (175°C). Line baking sheets with parchment paper or coat lightly with nonstick spray.",
            "On a lightly floured surface, roll out the dough to 1/4-inch thickness (or thicker if you prefer softer cookies).",
            "Cut into various shapes using cookie cutters. Place on prepared baking sheets, spacing about 1 inch apart.",
            "Bake for 10-11 minutes, or until the edges are just barely golden. Do not overbake.",
            "Cool on the baking sheets for 2 minutes, then transfer to wire racks to cool completely. These cookies are perfect for decorating with icing!"
        ]
    }
}

# Add recipes to appropriate categories
for category in data["categories"]:
    if category["name"] == "Breads & Breakfast":
        category["recipes"].append(stollen_alma)
        category["recipes"].append(stollen_kanis)
    elif category["name"] == "Cookies & Bars":
        category["recipes"].append(sugar_cookies_alice)
        category["recipes"].append(sugar_cookies_preferred)
        category["recipes"].append(sugar_cookies_zuckerkuchen)

# Save the updated recipes.json
with open('recipes.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Successfully added 5 recipes (Batch 2A):")
print("- Stöllen (Alma Finken Carle Recipe) (Breads & Breakfast)")
print("- Stöllen (Kanis Recipe) (Breads & Breakfast)")
print("- Sugar Cookies (Alice Carle) (Cookies & Bars)")
print("- Sugar Cookies (Prefered) (Cookies & Bars)")
print("- Sugar Cookies (Zuckerkuchen) (Cookies & Bars)")
