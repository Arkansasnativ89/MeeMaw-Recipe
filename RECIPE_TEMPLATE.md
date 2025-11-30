# Recipe Batch Update Template

Use this format when providing updated recipes. You can send them in batches of any size.

## Format Example:

```json
[
  {
    "id": 1,
    "name": "Recipe Name",
    "subtitle": "Optional subtitle or variation notes",
    "source": "Person's Name",
    "category": "Appetizers|Desserts|Main Dishes|Salads|Soups|Sauces|Baking|Cookies|Side Dishes|Snacks",
    "yield": "Makes X servings or X items",
    "prep_time": "X minutes",
    "cook_time": "X minutes",
    "total_time": "X minutes to X hours",
    "ingredients": [
      {
        "item": "Ingredient Name",
        "quantity": "1 cup",
        "notes": "optional notes like 'sifted' or 'room temperature'",
        "metric": {
          "quantity": 240,
          "unit": "ml"
        }
      },
      {
        "item": "Another Ingredient",
        "quantity": "2 tablespoons",
        "metric": {
          "min": 25,
          "max": 30,
          "unit": "g"
        }
      },
      {
        "section": "For the Filling",
        "item": "Section ingredients come after this header",
        "quantity": "1/2 cup",
        "metric": {
          "quantity": 120,
          "unit": "ml"
        }
      }
    ],
    "instructions": [
      "First step with temperature 350°F (175°C) and timing.",
      "Second step with detailed instructions.",
      "Continue with numbered steps..."
    ],
    "shaping_methods": [
      {
        "shape": "Method Name",
        "method": "Detailed description of this shaping method"
      }
    ],
    "notes": [
      "Storage tip or variation",
      "Make-ahead instructions",
      "Substitution suggestions"
    ]
  }
]
```

## Metric Conversion Quick Reference:

### Volume:
- 1 teaspoon = 5 ml
- 1 tablespoon = 15 ml
- 1/4 cup = 60 ml
- 1/3 cup = 80 ml
- 1/2 cup = 120 ml
- 1 cup = 240 ml
- 1 pint = 480 ml
- 1 quart = 960 ml

### Weight:
- 1 ounce = 28 g
- 1/4 pound (4 oz) = 113 g
- 1/2 pound (8 oz) = 227 g
- 1 pound = 454 g

### Temperature:
- 250°F = 120°C
- 300°F = 150°C
- 325°F = 165°C
- 350°F = 175°C
- 375°F = 190°C
- 400°F = 205°C
- 425°F = 220°C
- 450°F = 230°C

### Common Ingredients (approximate):
- 1 cup flour = 120 g
- 1 cup sugar = 200 g
- 1 cup brown sugar = 220 g
- 1 cup powdered sugar = 120 g
- 1 cup butter = 227 g
- 1 egg = 50 g
- 1 egg white = 30 g

## Fields Explained:

- **id**: Keep the existing ID number from the current recipes.json
- **name**: Recipe title
- **subtitle**: Optional - use for variations or special notes
- **source**: Person who provided the recipe
- **category**: Must match existing categories
- **yield**: Instead of "servings" - describes output (e.g., "36 rolls", "8-10 servings")
- **prep_time/cook_time/total_time**: All optional, use for timing info
- **ingredients.section**: Optional - creates subheadings for ingredient groups
- **ingredients.metric**: Can be single value or min/max range
- **shaping_methods**: Optional - for recipes with multiple preparation styles
- **notes**: Optional - tips, variations, storage, etc.

## When Sending Batches:

Just provide the JSON array with the recipes you want to update. I'll:
1. Validate the format
2. Merge them into recipes.json
3. Confirm the update

You can update as few or as many recipes at a time as you'd like!
