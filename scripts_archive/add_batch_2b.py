import json

# Load the current recipes.json
with open('recipes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Recipe 1: Liebkuchen (Cookies & Bars)
liebkuchen = {
    "original_recipe": {
        "name": "Liebkuchen",
        "subtitle": "German Spiced Honey Cookies",
        "source": "Grandmother Caroline Nagel Carle",
        "category": "Cookies & Bars",
        "servings": None,
        "ingredients": [
            {"item": "Honey", "quantity": "2 pounds", "notes": "", "metric": {"quantity": 900, "unit": "g"}},
            {"item": "Pecans or any nut", "quantity": "1 pound", "notes": "", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Cloves", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 2, "unit": "g"}},
            {"item": "Sherry or red wine", "quantity": "4 ounces", "notes": "", "metric": {"quantity": 120, "unit": "ml"}},
            {"item": "Harzhorne", "quantity": "2 teaspoons", "notes": "", "metric": {"quantity": 10, "unit": "g"}},
            {"item": "Citron", "quantity": "1/4 pound", "notes": "", "metric": {"quantity": 113, "unit": "g"}},
            {"item": "Sugar", "quantity": "1 pound", "notes": "", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Cinnamon", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 3, "unit": "g"}},
            {"item": "Allspice", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 2, "unit": "g"}},
            {"item": "Flour", "quantity": "2 pounds", "notes": "", "metric": {"quantity": 900, "unit": "g"}},
            {"item": "Orange", "quantity": "1/2", "notes": "grated rind only", "metric": None},
            {"item": "Lemons", "quantity": "2", "notes": "grated rind only", "metric": None}
        ],
        "instructions": [
            "Get a large container and put in all of the dry ingredients. Make a 'well' in the center, and add the honey, wine, orange and lemon rind. Set aside.",
            "Mix nuts and citron in a separate bowl. Put through a food grinder. Add this to the first mixture.",
            "Mix by hand until well blended. Cover, and let stand overnight.",
            "Roll out on breadboard to 1/4\" thickness. Cut in diamond shapes.",
            "Bake on a pan that has been lightly coated with a nonstick vegetable spray at 325° F until light brown (12 to 15 minutes).",
            "Use powdered sugar glaze or leave plain."
        ]
    },
    "improved_recipe": {
        "name": "German Spiced Honey Cookies (Liebkuchen)",
        "category": "Cookies & Bars",
        "servings": "About 6-7 dozen cookies",
        "ingredients": [
            {"item": "All-purpose flour", "quantity": "2 pounds (about 7-8 cups)", "notes": "", "metric": {"quantity": 900, "unit": "g"}},
            {"item": "Granulated sugar", "quantity": "1 pound (2 1/4 cups)", "notes": "", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Ground cinnamon", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 3, "unit": "g"}},
            {"item": "Ground cloves", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 2, "unit": "g"}},
            {"item": "Ground allspice", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 2, "unit": "g"}},
            {"item": "Hartshorn (baker's ammonia) or baking powder", "quantity": "2 teaspoons", "notes": "hartshorn for traditional flavor", "metric": {"quantity": 10, "unit": "g"}},
            {"item": "Honey", "quantity": "2 pounds (about 2 2/3 cups)", "notes": "", "metric": {"quantity": 900, "unit": "g"}},
            {"item": "Sherry or red wine", "quantity": "1/2 cup (4 oz)", "notes": "", "metric": {"quantity": 120, "unit": "ml"}},
            {"item": "Orange zest", "quantity": "from 1/2 orange", "notes": "finely grated", "metric": None},
            {"item": "Lemon zest", "quantity": "from 2 lemons", "notes": "finely grated", "metric": None},
            {"item": "Pecans or mixed nuts", "quantity": "1 pound (about 4 cups)", "notes": "chopped", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Citron", "quantity": "1/4 pound (about 1/2 cup)", "notes": "finely chopped candied citron", "metric": {"quantity": 113, "unit": "g"}}
        ],
        "instructions": [
            "In a very large bowl, combine the flour, sugar, cinnamon, cloves, allspice, and hartshorn (or baking powder). Mix well and make a well in the center.",
            "Pour the honey, sherry (or wine), orange zest, and lemon zest into the well. Stir to begin combining.",
            "In a food processor or grinder, finely grind the nuts and citron together. Add this mixture to the honey-flour mixture.",
            "Mix by hand, kneading until all ingredients are well blended into a stiff dough. This may take some time and effort.",
            "Cover the dough tightly and let it stand at room temperature overnight. This resting period allows the flavors to meld.",
            "The next day, preheat oven to 325°F (165°C). Line baking sheets with parchment paper or coat lightly with nonstick spray.",
            "On a lightly floured surface, roll out the dough to 1/4-inch thickness. Cut into diamond shapes (traditional) or use cookie cutters.",
            "Place the cookies on prepared baking sheets, spacing about 1 inch apart.",
            "Bake for 12-15 minutes, or until lightly browned. Do not overbake; the cookies should remain soft initially and will firm up as they cool.",
            "Cool on wire racks. If desired, glaze with a simple powdered sugar icing while still slightly warm, or leave plain.",
            "Store in an airtight container. These cookies improve with age and can be stored for several weeks."
        ]
    }
}

# Recipe 2: Pfeffernusse (Cookies & Bars)
pfeffernusse = {
    "original_recipe": {
        "name": "Pfeffernusse",
        "subtitle": "Pepper Nuts",
        "source": "Grandmother Caroline Nagel Carle",
        "category": "Cookies & Bars",
        "servings": None,
        "ingredients": [
            {"item": "Flour", "quantity": "4 cups", "notes": "", "metric": {"quantity": 480, "unit": "g"}},
            {"item": "Powdered sugar", "quantity": "1 pound", "notes": "", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Eggs", "quantity": "4", "notes": "or egg substitute", "metric": {"quantity": 200, "unit": "g"}},
            {"item": "Cinnamon", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 3, "unit": "g"}},
            {"item": "Cloves", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 2, "unit": "g"}},
            {"item": "Black pepper", "quantity": "1 teaspoon", "notes": "for extra hot, use 2 teaspoons", "metric": {"quantity": 2, "unit": "g"}},
            {"item": "Melted margarine", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 15, "unit": "g"}},
            {"item": "Soda", "quantity": "1 level teaspoon", "notes": "", "metric": {"quantity": 5, "unit": "g"}}
        ],
        "instructions": [
            "Beat eggs slightly. Add powdered sugar and melted margarine.",
            "Mix in electric mixer for 15 minutes (30 minutes if mixed by hand).",
            "Add dry ingredients and spices a tablespoon at a time and mix well.",
            "Roll out to 1/4\" thickness and cut into small cookies (about 1 1/4\" diameter).",
            "Bake on a cookie sheet lightly coated with nonstick vegetable spray at 300° F until slightly brown (about 20 minutes).",
            "Glaze with powdered sugar mixed with boiling water and vanilla."
        ]
    },
    "improved_recipe": {
        "name": "German Pepper Nuts (Pfeffernüsse)",
        "category": "Cookies & Bars",
        "servings": "About 8-10 dozen small cookies",
        "ingredients": [
            {"item": "Eggs", "quantity": "4 large", "notes": "or 1 cup egg substitute", "metric": {"quantity": 200, "unit": "g"}},
            {"item": "Powdered sugar", "quantity": "1 pound (about 4 cups)", "notes": "sifted", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Margarine or butter", "quantity": "1 tablespoon", "notes": "melted", "metric": {"quantity": 15, "unit": "g"}},
            {"item": "All-purpose flour", "quantity": "4 cups", "notes": "", "metric": {"quantity": 480, "unit": "g"}},
            {"item": "Baking soda", "quantity": "1 teaspoon, level", "notes": "", "metric": {"quantity": 5, "unit": "g"}},
            {"item": "Ground cinnamon", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 3, "unit": "g"}},
            {"item": "Ground cloves", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 2, "unit": "g"}},
            {"item": "Black pepper", "quantity": "1 to 2 teaspoons", "notes": "use 2 tsp for extra spicy", "metric": {"min": 2, "max": 4, "unit": "g"}},
            {"item": "Powdered sugar", "quantity": "2 cups", "notes": "for glaze", "metric": {"quantity": 240, "unit": "g"}},
            {"item": "Boiling water", "quantity": "3-4 tablespoons", "notes": "for glaze", "metric": {"quantity": 50, "unit": "ml"}},
            {"item": "Vanilla extract", "quantity": "1/2 teaspoon", "notes": "for glaze", "metric": {"quantity": 2.5, "unit": "ml"}}
        ],
        "instructions": [
            "In a large bowl, beat the eggs slightly. Add 1 pound powdered sugar and the melted margarine.",
            "Mix with an electric mixer for 15 minutes, or beat by hand for 30 minutes. The mixture should be very light and fluffy.",
            "In a separate bowl, combine the flour, baking soda, cinnamon, cloves, and black pepper.",
            "Add the dry ingredients to the egg mixture one tablespoon at a time, mixing well after each addition. This gradual incorporation ensures a smooth dough.",
            "Once all dry ingredients are incorporated, the dough should be stiff but pliable.",
            "On a lightly floured surface, roll out the dough to 1/4-inch thickness.",
            "Cut into small rounds, about 1 1/4 inches in diameter. These are traditional \"pepper nuts\" - small and round.",
            "Preheat oven to 300°F (150°C). Line baking sheets with parchment paper or coat lightly with nonstick spray.",
            "Place the cookies on prepared baking sheets and bake for about 20 minutes, or until slightly browned.",
            "While the cookies are still warm, prepare the glaze: Mix 2 cups powdered sugar with 3-4 tablespoons boiling water and 1/2 teaspoon vanilla until smooth.",
            "Brush or drizzle the glaze over the warm cookies, or dip each cookie into the glaze.",
            "Let the glaze set completely before storing. These cookies keep well and are traditional German Christmas treats."
        ]
    }
}

# Recipe 3: Gingerbread Men Cookies (Cookies & Bars)
gingerbread_men = {
    "original_recipe": {
        "name": "Gingerbread Men Cookies",
        "subtitle": "Old Fashioned Spicy",
        "source": None,
        "category": "Cookies & Bars",
        "servings": None,
        "ingredients": [
            {"item": "Brown sugar, packed", "quantity": "1 cup", "notes": "", "metric": {"quantity": 220, "unit": "g"}},
            {"item": "Eggs", "quantity": "3", "notes": "or egg substitute", "metric": {"quantity": 150, "unit": "g"}},
            {"item": "Margarine, softened", "quantity": "1 cup", "notes": "", "metric": {"quantity": 227, "unit": "g"}},
            {"item": "Molasses", "quantity": "1 1/4 cups", "notes": "", "metric": {"quantity": 300, "unit": "ml"}},
            {"item": "Salt", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 6, "unit": "g"}},
            {"item": "All purpose flour", "quantity": "3 cups", "notes": "for initial mix", "metric": {"quantity": 360, "unit": "g"}},
            {"item": "Baking soda", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 15, "unit": "g"}},
            {"item": "Ground cinnamon", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 3, "unit": "g"}},
            {"item": "Ground allspice", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 2, "unit": "g"}},
            {"item": "Ground clove", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 2, "unit": "g"}},
            {"item": "Ground ginger", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 2, "unit": "g"}},
            {"item": "All purpose flour", "quantity": "5 to 6 cups", "notes": "to be used later", "metric": {"min": 600, "max": 720, "unit": "g"}}
        ],
        "instructions": [
            "Early in the day: In a large bowl beat first 11 ingredients (all but the 5-6 cups flour) until just mixed. Increasing speed to medium, beat 2 more minutes.",
            "Using a wooden spoon, stir additional 5 to 6 cups of flour into dough to make it stiff.",
            "Divide dough in half and wrap in plastic wrap. Refrigerate for up to two days.",
            "Preheat oven to 350° F. Roll half the dough until 1/8\" thick.",
            "Cut with gingerbread man cookie cutter.",
            "Bake 12 minutes until cookie edges are firm. Cool. Decorate."
        ]
    },
    "improved_recipe": {
        "name": "Old-Fashioned Spicy Gingerbread Men",
        "category": "Cookies & Bars",
        "servings": "About 3-4 dozen cookies",
        "ingredients": [
            {"item": "Brown sugar", "quantity": "1 cup, packed", "notes": "", "metric": {"quantity": 220, "unit": "g"}},
            {"item": "Margarine or butter", "quantity": "1 cup (2 sticks)", "notes": "softened", "metric": {"quantity": 227, "unit": "g"}},
            {"item": "Eggs", "quantity": "3 large", "notes": "or 3/4 cup egg substitute", "metric": {"quantity": 150, "unit": "g"}},
            {"item": "Molasses", "quantity": "1 1/4 cups", "notes": "dark or light", "metric": {"quantity": 300, "unit": "ml"}},
            {"item": "All-purpose flour", "quantity": "3 cups", "notes": "for initial mix", "metric": {"quantity": 360, "unit": "g"}},
            {"item": "Baking soda", "quantity": "1 tablespoon", "notes": "", "metric": {"quantity": 15, "unit": "g"}},
            {"item": "Salt", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 6, "unit": "g"}},
            {"item": "Ground cinnamon", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 3, "unit": "g"}},
            {"item": "Ground ginger", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 2, "unit": "g"}},
            {"item": "Ground allspice", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 2, "unit": "g"}},
            {"item": "Ground cloves", "quantity": "1 teaspoon", "notes": "", "metric": {"quantity": 2, "unit": "g"}},
            {"item": "All-purpose flour", "quantity": "5 to 6 cups", "notes": "additional, for stiff dough", "metric": {"min": 600, "max": 720, "unit": "g"}}
        ],
        "instructions": [
            "Early in the day (or up to 2 days ahead): In a large bowl, combine the brown sugar, softened margarine, eggs, molasses, 3 cups flour, baking soda, salt, and all the spices (cinnamon, ginger, allspice, cloves).",
            "Beat with an electric mixer on low speed until just mixed, then increase to medium speed and beat for 2 more minutes.",
            "Using a wooden spoon, gradually stir in 5 to 6 additional cups of flour until the dough is very stiff and no longer sticky. You may need the full 6 cups.",
            "Divide the dough in half and wrap each half tightly in plastic wrap. Refrigerate for at least 2 hours, or up to 2 days.",
            "When ready to bake, preheat oven to 350°F (175°C). Line baking sheets with parchment paper.",
            "Working with one half of the dough at a time (keep the other half refrigerated), roll out on a lightly floured surface to 1/8-inch thickness.",
            "Cut out gingerbread men shapes using a cookie cutter. Use a spatula to carefully transfer to prepared baking sheets.",
            "Bake for 12 minutes, or until the edges are firm and the cookies are set. Do not overbake.",
            "Cool on the baking sheets for 2 minutes, then transfer to wire racks to cool completely.",
            "Decorate with royal icing, raisins, candies, or leave plain. Store in an airtight container."
        ]
    }
}

# Recipe 4: Springerle Nagel (Cookies & Bars)
springerle_nagel = {
    "original_recipe": {
        "name": "Springerle Nagel",
        "subtitle": "Original Carle Recipe",
        "source": "Grandmother Caroline Nagel Carle",
        "category": "Cookies & Bars",
        "servings": None,
        "ingredients": [
            {"item": "Eggs", "quantity": "4", "notes": "or egg substitute", "metric": {"quantity": 200, "unit": "g"}},
            {"item": "Powdered sugar", "quantity": "1 pound", "notes": "", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Flour", "quantity": "1 pound", "notes": "", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Baking powder", "quantity": "2 teaspoons", "notes": "", "metric": {"quantity": 10, "unit": "g"}},
            {"item": "Melted margarine, cooled", "quantity": "2 tablespoons", "notes": "", "metric": {"quantity": 30, "unit": "g"}},
            {"item": "Lemon", "quantity": "1", "notes": "grated rind only", "metric": None},
            {"item": "Anise oil", "quantity": "10 drops", "notes": "", "metric": None}
        ],
        "instructions": [
            "Beat eggs and powdered sugar together at least 15 minutes in an electric mixer.",
            "Then add melted margarine, anise oil, and grated lemon rind. Mix well.",
            "Next, add flour and again mix well.",
            "Roll on breadboard to 3/8\" thickness. Use springerle roller or board for the cookie 'patterns'.",
            "Cut cookies and place on a baking sheet that has been lightly coated with a nonstick vegetable spray.",
            "Let stand overnight.",
            "Bake at 325° F until slightly browned. Do not 'ice'."
        ]
    },
    "improved_recipe": {
        "name": "Traditional Springerle (Nagel Family Recipe)",
        "category": "Cookies & Bars",
        "servings": "About 4-5 dozen cookies",
        "ingredients": [
            {"item": "Eggs", "quantity": "4 large", "notes": "or 1 cup egg substitute", "metric": {"quantity": 200, "unit": "g"}},
            {"item": "Powdered sugar", "quantity": "1 pound (about 4 cups)", "notes": "sifted", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "All-purpose flour", "quantity": "1 pound (about 3 2/3 cups)", "notes": "sifted", "metric": {"quantity": 454, "unit": "g"}},
            {"item": "Baking powder", "quantity": "2 teaspoons", "notes": "", "metric": {"quantity": 10, "unit": "g"}},
            {"item": "Margarine or butter", "quantity": "2 tablespoons", "notes": "melted and cooled", "metric": {"quantity": 30, "unit": "g"}},
            {"item": "Fresh lemon zest", "quantity": "from 1 lemon", "notes": "finely grated", "metric": None},
            {"item": "Anise oil", "quantity": "10 drops", "notes": "or 1 tsp anise extract", "metric": None}
        ],
        "instructions": [
            "In a large bowl with an electric mixer, beat the eggs and powdered sugar together for at least 15 minutes. The mixture should be very thick, pale, and fluffy, resembling a soft meringue.",
            "Add the cooled melted margarine, anise oil, and grated lemon zest. Mix well until fully incorporated.",
            "Sift together the flour and baking powder. Add to the egg mixture and mix well until a smooth, firm dough forms.",
            "Cover the dough and let it rest for 15-20 minutes to make it easier to roll.",
            "On a lightly floured surface, roll out the dough to 3/8-inch thickness (slightly thicker than most cookies).",
            "Press a floured springerle rolling pin or mold firmly into the dough to create the traditional embossed designs.",
            "Cut the cookies apart along the design lines using a sharp knife or pastry wheel.",
            "Place the cookies on lightly greased baking sheets or parchment paper. Leave space between them.",
            "Cover with a clean kitchen towel and let the cookies stand at room temperature overnight (12-24 hours). This drying step creates the characteristic hard texture.",
            "The next day, preheat oven to 325°F (165°C).",
            "Bake for 15-20 minutes, or until the cookies are slightly browned on the bottom but still pale on top. Do not overbake.",
            "Cool completely on wire racks. Do not ice these cookies; the anise flavor and embossed design are meant to shine on their own.",
            "Store in airtight containers. Springerle improve with age and can be kept for several weeks. They will soften slightly over time."
        ]
    }
}

# Recipe 5: Lemon Meringue Pie (Pies & Pastry Fillings)
lemon_meringue_pie = {
    "original_recipe": {
        "name": "Lemon Meringue Pie",
        "subtitle": "9-inch",
        "source": None,
        "category": "Pies & Pastry Fillings",
        "servings": "8 servings",
        "ingredients": [
            {"item": "Sugar (filling)", "quantity": "1 1/2 cups", "notes": "", "metric": {"quantity": 300, "unit": "g"}},
            {"item": "Cornstarch (filling)", "quantity": "6 tablespoons", "notes": "", "metric": {"quantity": 55, "unit": "g"}},
            {"item": "Boiling water (filling)", "quantity": "1 1/2 cups", "notes": "", "metric": {"quantity": 360, "unit": "ml"}},
            {"item": "Egg substitute (filling)", "quantity": "3/4 cup", "notes": "", "metric": {"quantity": 180, "unit": "ml"}},
            {"item": "Margarine (filling)", "quantity": "3 tablespoons", "notes": "", "metric": {"quantity": 45, "unit": "g"}},
            {"item": "Lemon juice (filling)", "quantity": "4 tablespoons", "notes": "", "metric": {"quantity": 60, "unit": "ml"}},
            {"item": "Grated lemon rind (filling)", "quantity": "1 1/2 tablespoons", "notes": "", "metric": None},
            {"item": "Egg whites (meringue)", "quantity": "3", "notes": "", "metric": {"quantity": 90, "unit": "g"}},
            {"item": "Cream of tartar (meringue)", "quantity": "1/4 teaspoon", "notes": "", "metric": {"quantity": 0.5, "unit": "g"}},
            {"item": "Sugar (meringue)", "quantity": "6 tablespoons", "notes": "", "metric": {"quantity": 75, "unit": "g"}},
            {"item": "Baked pie shell", "quantity": "1", "notes": "9-inch, cooled", "metric": None}
        ],
        "instructions": [
            "Mix sugar and cornstarch. Stir in boiling water, cook over direct heat, stirring constantly, until mixture thickens and boils.",
            "Set over boiling water and cook 10 minutes longer.",
            "Beat a little of the hot mixture into the egg substitute. Then beat into hot mixture in double-boiler. Cook 5 minutes, stirring constantly.",
            "Remove from over hot water. Blend in margarine, lemon juice, rind. Cool. Pour into cooled baked pie shell.",
            "Cover with meringue. Bake. Serve cool.",
            "For meringue: Beat egg whites until frothy, add cream of tartar, and continue beating until stiff enough to hold a point. Gradually beat in sugar...continuing beating until mixture is stiff and glossy.",
            "Pile meringue lightly on cooled pie filling...seal it onto edge of crust to prevent shrinking. Swirl or pull up points to make it look decorative.",
            "Bake 15 to 20 minutes at 350° F until meringue is golden brown."
        ]
    },
    "improved_recipe": {
        "name": "Classic Lemon Meringue Pie",
        "category": "Pies & Pastry Fillings",
        "servings": "8 servings (9-inch pie)",
        "ingredients": [
            {"item": "Granulated sugar", "quantity": "1 1/2 cups", "notes": "for filling", "metric": {"quantity": 300, "unit": "g"}},
            {"item": "Cornstarch", "quantity": "6 tablespoons", "notes": "for filling", "metric": {"quantity": 55, "unit": "g"}},
            {"item": "Water", "quantity": "1 1/2 cups", "notes": "boiling", "metric": {"quantity": 360, "unit": "ml"}},
            {"item": "Egg yolks or egg substitute", "quantity": "3/4 cup", "notes": "about 4 egg yolks", "metric": {"quantity": 180, "unit": "ml"}},
            {"item": "Margarine or butter", "quantity": "3 tablespoons", "notes": "", "metric": {"quantity": 45, "unit": "g"}},
            {"item": "Fresh lemon juice", "quantity": "1/4 cup", "notes": "from about 2 lemons", "metric": {"quantity": 60, "unit": "ml"}},
            {"item": "Fresh lemon zest", "quantity": "1 1/2 tablespoons", "notes": "finely grated", "metric": None},
            {"item": "Pre-baked pie crust", "quantity": "1 (9-inch)", "notes": "cooled completely", "metric": None},
            {"item": "Egg whites", "quantity": "3 large", "notes": "for meringue", "metric": {"quantity": 90, "unit": "g"}},
            {"item": "Cream of tartar", "quantity": "1/4 teaspoon", "notes": "for meringue", "metric": {"quantity": 0.5, "unit": "g"}},
            {"item": "Granulated sugar", "quantity": "6 tablespoons", "notes": "for meringue", "metric": {"quantity": 75, "unit": "g"}}
        ],
        "instructions": [
            "Prepare the lemon filling: In a medium saucepan, whisk together the 1 1/2 cups sugar and cornstarch.",
            "Gradually stir in the 1 1/2 cups boiling water. Cook over medium heat, stirring constantly, until the mixture thickens and comes to a boil.",
            "Transfer the mixture to the top of a double boiler set over simmering water. Cook for 10 minutes, stirring occasionally.",
            "In a small bowl, lightly beat the egg yolks or egg substitute. Slowly whisk about 1/2 cup of the hot sugar mixture into the eggs to temper them.",
            "Pour the tempered egg mixture back into the double boiler, whisking constantly. Cook for 5 more minutes, stirring constantly, until thick.",
            "Remove from heat. Stir in the margarine, lemon juice, and lemon zest until the margarine is melted and everything is well combined.",
            "Let the filling cool for about 10 minutes, stirring occasionally. Pour into the cooled, pre-baked pie shell. Set aside while you make the meringue.",
            "Preheat oven to 350°F (175°C).",
            "Make the meringue: In a clean, dry bowl, beat the egg whites with an electric mixer until foamy. Add the cream of tartar.",
            "Continue beating on high speed until soft peaks form. Gradually add the 6 tablespoons sugar, one tablespoon at a time, beating constantly until stiff, glossy peaks form. The meringue should stand up straight when the beaters are lifted.",
            "Spread the meringue over the warm (not hot) lemon filling, making sure to seal the meringue all the way to the edge of the crust. This prevents shrinking. Swirl or create peaks for a decorative look.",
            "Bake for 15-20 minutes, or until the meringue is golden brown on the peaks.",
            "Cool the pie at room temperature for 1 hour, then refrigerate for at least 3 hours before serving. The filling needs to set completely.",
            "Serve chilled. Store any leftovers covered in the refrigerator for up to 3 days."
        ]
    }
}

# Add recipes to appropriate categories
for category in data["categories"]:
    if category["name"] == "Cookies & Bars":
        category["recipes"].append(liebkuchen)
        category["recipes"].append(pfeffernusse)
        category["recipes"].append(gingerbread_men)
        category["recipes"].append(springerle_nagel)
    elif category["name"] == "Pies & Pastry Fillings":
        category["recipes"].append(lemon_meringue_pie)

# Save the updated recipes.json
with open('recipes.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Successfully added 5 recipes (Batch 2B):")
print("- Liebkuchen (Cookies & Bars)")
print("- Pfeffernusse (Cookies & Bars)")
print("- Gingerbread Men Cookies (Cookies & Bars)")
print("- Springerle Nagel (Cookies & Bars)")
print("- Lemon Meringue Pie (Pies & Pastry Fillings)")
