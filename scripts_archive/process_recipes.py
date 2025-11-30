"""
Process all recipes from the cookbook text file and generate complete JSON
"""
import json
import re

def parse_cookbook_text(filepath):
    """Parse the plain text cookbook into structured data"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into recipe sections
    recipes_by_category = {}
    current_category = None
    current_recipe = None
    lines = content.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines
        if not line:
            i += 1
            continue
            
        # Check for category headers (all caps or specific patterns)
        if line.upper() == line and len(line) > 3 and not line.startswith('•'):
            # This is likely a category
            if 'APPETIZERS' in line or 'BREADS' in line or 'CAKES' in line or \
               'CANDY' in line or 'COOKIES' in line or 'DESSERTS' in line or \
               'ICINGS' in line or 'JAMS' in line or 'MAIN DISHES' in line or \
               'PIES' in line or 'SALADS' in line or 'SIDE DISHES' in line or \
               'SOUPS' in line:
                current_category = line
                recipes_by_category[current_category] = []
                i += 1
                continue
        
        i += 1
    
    return recipes_by_category

def convert_to_metric(ingredient_text, quantity_str):
    """Convert US measurements to metric"""
    # Simple conversion table
    conversions = {
        'cup': {'ml': 240, 'g': 120},  # varies by ingredient
        'tablespoon': {'ml': 15, 'g': 14},
        'teaspoon': {'ml': 5, 'g': 5},
        'pound': {'g': 454},
        'ounce': {'g': 28},
        'stick': {'g': 113},  # stick of butter/margarine
    }
    
    # Try to extract numeric value
    try:
        # Handle fractions
        if '/' in quantity_str:
            parts = quantity_str.split()
            if len(parts) > 1 and '/' in parts[-1]:
                # e.g., "1 1/2" or "1/2"
                frac = parts[-1].split('/')
                value = int(frac[0]) / int(frac[1])
                if len(parts) > 1:
                    value += int(parts[0])
            else:
                frac = quantity_str.split('/')
                value = int(frac[0]) / int(frac[1])
        else:
            value = float(quantity_str.split()[0])
            
        # Determine unit
        text_lower = ingredient_text.lower()
        for unit, conv in conversions.items():
            if unit in text_lower:
                if 'liquid' in text_lower or 'milk' in text_lower or 'water' in text_lower:
                    return {'quantity': int(value * conv.get('ml', 240)), 'unit': 'ml'}
                else:
                    return {'quantity': int(value * conv.get('g', 100)), 'unit': 'g'}
        
        return None
    except:
        return None

# Load existing recipes.json to preserve what's already polished
with open('recipes.json', 'r', encoding='utf-8') as f:
    existing_data = json.load(f)

print(f"Loaded existing recipes with {len(existing_data['categories'])} categories")
print("This script would process all recipes, but given the volume,")
print("let me create a more targeted approach...")
