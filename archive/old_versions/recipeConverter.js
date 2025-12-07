// Conversion utilities for recipe polishing
const conversionFactors = {
    // Volume conversions (to ml)
    'cup': 240,
    'cups': 240,
    'tablespoon': 15,
    'tablespoons': 15,
    'tbsp': 15,
    'teaspoon': 5,
    'teaspoons': 5,
    'tsp': 5,
    'pint': 480,
    'quart': 960,
    'gallon': 3840,
    'ounce': 30,
    'ounces': 30,
    'oz': 30,
    
    // Weight conversions (to g)
    'pound': 454,
    'pounds': 454,
    'lb': 454,
    'lbs': 454,
    
    // Temperature conversion
    fahrenheitToCelsius: (f) => Math.round((f - 32) * 5/9)
};

// Parse ingredient string and extract quantity, unit, item
function parseIngredient(ingredientString) {
    // This is a simplified parser - you'd need more sophisticated parsing for all cases
    const match = ingredientString.match(/^([\d\/\s\-]+)?\s*(\w+)?\s+(.+)/);
    if (match) {
        return {
            quantity: match[1]?.trim(),
            unit: match[2]?.toLowerCase(),
            item: match[3]
        };
    }
    return { item: ingredientString };
}

console.log('Recipe conversion utilities loaded');
