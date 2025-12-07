import json

# Approved list from user
approved = """APPLE CAKE
APPLE PIE
BAKED LASAGNA CASSEROLE
BAKED RICE CUSTARD
BAKELESS FRUIT CAKE
BANANA NUT BREAD
BASIC SWEET DOUGH
BEAN SALAD
BECHAMEL SAUCE TOPPING
BEEF BRISKET (MARINADED)
BLUEBERRY JELLO SALAD
BLUEBERRY PIE FILLING
BREAD PUDDING
BROCCOLI AND RICE
BROWN SUGAR BROWNIES
CARROT SOUP
CHEESE DIP (LIKE MEXICO CHIQUITO'S)
CHERRY PIE FILLING (QUICK)
CHICKEN BROWN RICE BAKE
CHICKEN CASSEROLE
CHICKEN RICE CASSEROLE
CHIL
CHOCOLATE CREAM PIE
CHOCOLATE FONDUE
CHOCOLATE OAT-CHIP COOKIES
CINNAMON ROLLS
COCKTAIL SAUCE
COCOANUT CAKE
CONFECTIONER'S GLAZE
CORNBREAD REVISED 12.24.95
CORNBREAD SOUTHERN STYLE
CORNMEAL YEAST ROLLS
CRAB DIP
CRANBERRY BREAD
CRANBERRY OR BLUEBERRY CRUNCH
CRANBERRY ORANGE RELISH
CRUMBLE CAKE (KRUMELKUCHEN)
CRUMBLE COFFEE CAKE #2
DELUXE WHITE CAKE
DINNER ROLL SHAPES
DINNER ROLLS AND SHAPES
DINNER ROLLS
DIVINITY
FETTUCCINE PRIMAVERA
FLUFFY BUTERMILK BISCUITS
FLUFFY COCOA FROSTING
FLUFFY WHITE FROSTING
FROSTED CARROT CAKE
FROSTED PINEAPPLE SQUARES
FUDGE (COCOA NUT)
FUDGE (PLAIN)
GINGER COOKIES
GINGER SNAPS
GINGERBREAD MEN COOKIES
HEARTY CHOWDER
HOLIDAY JAM CAKE
HOT WATER GINGERBREAD
HUSH PUPPIES
ICE BOX PICKLES
JUMBO SHELLS NO. 1
JUMBO SHELLS NO. 2
KARO NUT PIE
KOOL-AID JELLY
LEMON MERINGUE PIE
LEMON SNAPS
LEMON SQUARES
LIEBKUCHEN
MACARONI, HAM, AND CHEESE
MARINATED PEPPERS
Memorandum
MEMORY BOOK COOKIES
MERINGUE
MUSHROOM AND NUT PATE
OATMEAL RAISIN SPICE COOKIES
OLD FASHIONED JELLY ROLL
ORANGE-CREAM CHEESE FROSTING
ORIENTAL SALAD
PEANUT BRITTLE (MUNCHING)
PEANUT BUTTER PIE
PFEFFERNUSSE
PIE CRUST
PIZZA (CARLE VERSION)
PIZZA DOUGH (CRUSTY)
PRALINES, OLD FASHIONED
PUMPKIN BREAD
PUMPKIN PIE
RASPBERRY JELLO SALAD
ROASTED NUTS
ROYAL RICE
SALMON CROQUETTES
SCALLOPED SALMON
SPAGHETTI PORTOTINO (SERVES ONE)
SPAGHETTI PORTOTINO (SERVES SIX)
SPICE CAKE
SPRINGERLE NAGEL
SPRINGERLE PG 1
SPRINGERLE PG 2
STÖLLEN (KANIS RECIPE)
STÖLLEN
STRAWBERRY GLAZE PIE (FRENCH)
SUGAR COOKIES (ALICE CARLE)
SUGAR COOKIES (PREFERED)
SUGAR COOKIES (ZUCKERKUCHEN)
SUGAR COOKIES 50S
SWEET AND SOUR ROAST
THE LITTLE ENGLISH MUFFIN PIZZA
TOFU-CHEESE STUFFED SHELLS
TOMATO SAUCE
TURKEY SAUSAGE
VANILLA CREAM PIE
VEGETABLE RELISH SALAD
WAFFLES""".split('\n')

# Normalize approved list
approved_normalized = set([name.strip().upper() for name in approved if name.strip()])

# Load current recipes
with open('recipes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract current recipe names with their categories
current_recipes = {}
duplicate_names = []
seen_names = set()

for category in data['categories']:
    for recipe in category['recipes']:
        name = recipe['original_recipe']['name']
        name_upper = name.upper()
        
        if name_upper in seen_names:
            duplicate_names.append(name)
        else:
            seen_names.add(name_upper)
            current_recipes[name] = category['name']

print("=" * 80)
print("DUPLICATE RECIPES IN FILE (need to remove):")
print("=" * 80)
for name in sorted(set(duplicate_names)):
    print(f"  - {name}")

print("\n" + "=" * 80)
print("RECIPES IN FILE BUT NOT ON APPROVED LIST (need to remove):")
print("=" * 80)
not_approved = []
for name in sorted(current_recipes.keys()):
    name_upper = name.upper()
    # Check various normalizations
    if name_upper not in approved_normalized:
        not_approved.append(name)
        print(f"  - {name} (in {current_recipes[name]})")

print("\n" + "=" * 80)
print("RECIPES ON APPROVED LIST BUT MISSING FROM FILE (need to add):")
print("=" * 80)
current_normalized = set([name.upper() for name in current_recipes.keys()])
missing = []
for approved_name in sorted(approved_normalized):
    if approved_name not in current_normalized:
        missing.append(approved_name)
        print(f"  - {approved_name}")

print("\n" + "=" * 80)
print("SUMMARY:")
print("=" * 80)
print(f"Total approved recipes: {len(approved_normalized)}")
print(f"Total current recipes (unique): {len(current_recipes)}")
print(f"Duplicates to remove: {len(set(duplicate_names))}")
print(f"Recipes to remove: {len(not_approved)}")
print(f"Recipes to add: {len(missing)}")
print(f"Net change needed: {len(missing) - len(not_approved) - len(set(duplicate_names))}")
print("=" * 80)
