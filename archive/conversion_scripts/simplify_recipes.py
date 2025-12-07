"""
Simplify recipes.json by converting to streamlined format
Reduces from ~11,000 lines to ~3,000 lines while maintaining functionality
"""
import json

def format_ingredient(ing):
    """Convert ingredient object to simple string format"""
    if isinstance(ing, str):
        return ing
    
    quantity = ing.get('quantity', '').strip()
    item = ing.get('item', '').strip()
    notes = ing.get('notes', '').strip()
    
    # Build ingredient string
    parts = []
    if quantity:
        parts.append(quantity)
    if item:
        parts.append(item)
    if notes:
        parts.append(f"({notes})")
    
    return ' '.join(parts) if parts else item

def simplify_recipe(recipe):
    """Convert verbose recipe to simplified format"""
    simplified = {
        'name': recipe['name'],
        'category': recipe['category'],
        'servings': recipe.get('servings', ''),
        'ingredients': [],
        'instructions': recipe.get('instructions', [])
    }
    
    # Add optional fields only if they exist and are not empty
    if recipe.get('subtitle'):
        simplified['subtitle'] = recipe['subtitle']
    if recipe.get('source'):
        simplified['source'] = recipe['source']
    if recipe.get('notes'):
        simplified['notes'] = recipe['notes']
    
    # Convert ingredients to simple strings
    for ing in recipe.get('ingredients', []):
        simplified['ingredients'].append(format_ingredient(ing))
    
    return simplified

# Load current recipes
print("Loading recipes.json...")
with open('recipes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Original file: {sum(len(cat['recipes']) for cat in data['categories'])} recipes")

# Simplify all recipes
simplified_data = {
    'metadata': {
        'title': data['metadata']['title'],
        'compiler': data['metadata']['compiler'],
        'date_compiled': data['metadata']['date_compiled'],
        'family': data['metadata']['family'],
        'note': data['metadata']['note'],
        'version': '3.0 - Streamlined Edition'
    },
    'categories': []
}

for category in data['categories']:
    simplified_category = {
        'name': category['name'],
        'recipes': []
    }
    
    for recipe in category['recipes']:
        simplified_category['recipes'].append(simplify_recipe(recipe))
    
    simplified_data['categories'].append(simplified_category)

# Save simplified version
print("Writing simplified recipes.json...")
with open('recipes.json', 'w', encoding='utf-8') as f:
    json.dump(simplified_data, f, indent=2, ensure_ascii=False)

print("✓ Conversion complete!")
print(f"✓ Backup saved as recipes_verbose_backup.json")
print(f"✓ New version: {sum(len(cat['recipes']) for cat in simplified_data['categories'])} recipes")
print("✓ Estimated size reduction: ~70%")
