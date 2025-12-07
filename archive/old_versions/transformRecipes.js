const fs = require('fs');

// Read the current recipes
const recipes = JSON.parse(fs.readFileSync('recipes.json', 'utf8'));

// Metric conversion utilities
function convertToMetric(quantity, unit) {
    const conversions = {
        // Volume
        'cup': { factor: 240, metricUnit: 'ml' },
        'cups': { factor: 240, metricUnit: 'ml' },
        'tablespoon': { factor: 15, metricUnit: 'ml' },
        'tablespoons': { factor: 15, metricUnit: 'ml' },
        'tbsp': { factor: 15, metricUnit: 'ml' },
        'teaspoon': { factor: 5, metricUnit: 'ml' },
        'teaspoons': { factor: 5, metricUnit: 'ml' },
        'tsp': { factor: 5, metricUnit: 'ml' },
        'pint': { factor: 480, metricUnit: 'ml' },
        'quart': { factor: 960, metricUnit: 'ml' },
        'fluid ounce': { factor: 30, metricUnit: 'ml' },
        'fluid ounces': { factor: 30, metricUnit: 'ml' },
        'oz': { factor: 30, metricUnit: 'ml' },
        
        // Weight
        'pound': { factor: 454, metricUnit: 'g' },
        'pounds': { factor: 454, metricUnit: 'g' },
        'lb': { factor: 454, metricUnit: 'g' },
        'lbs': { factor: 454, metricUnit: 'g' },
        'ounce': { factor: 28, metricUnit: 'g' },
        'ounces': { factor: 28, metricUnit: 'g' },
    };
    
    const conv = conversions[unit.toLowerCase()];
    if (!conv) return null;
    
    return {
        quantity: Math.round(quantity * conv.factor),
        unit: conv.metricUnit
    };
}

// Parse fractions
function parseFraction(str) {
    if (str.includes('/')) {
        const [num, den] = str.split('/').map(Number);
        return num / den;
    }
    if (str.includes(' ')) {
        const parts = str.split(' ');
        const whole = parseFloat(parts[0]);
        if (parts[1] && parts[1].includes('/')) {
            const [num, den] = parts[1].split('/').map(Number);
            return whole + (num / den);
        }
        return whole;
    }
    return parseFloat(str);
}

// Parse ingredient string
function parseIngredient(ingredientStr) {
    // Match pattern: [quantity] [unit] [of] item
    const patterns = [
        /^([\d\s\/\-]+)\s+(cup|cups|tablespoon|tablespoons|tbsp|teaspoon|teaspoons|tsp|pound|pounds|lb|lbs|ounce|ounces|oz|pint|quart|can|package|pkg)\s+(?:of\s+)?(.+)$/i,
        /^([\d\s\/\-]+)\s+(.+)$/,
        /^(.+)$/
    ];
    
    for (const pattern of patterns) {
        const match = ingredientStr.match(pattern);
        if (match) {
            if (pattern.source.includes('cup|cups')) {
                // Has quantity and unit
                const quantity = match[1].trim();
                const unit = match[2].toLowerCase();
                const item = match[3];
                const numericQty = parseFraction(quantity);
                const metric = convertToMetric(numericQty, unit);
                
                return {
                    item: item.charAt(0).toUpperCase() + item.slice(1),
                    quantity: quantity,
                    notes: "",
                    metric: metric || undefined
                };
            } else if (match.length === 3 && /[\d\/]/.test(match[1])) {
                // Has quantity but no recognized unit
                return {
                    item: match[2].charAt(0).toUpperCase() + match[2].slice(1),
                    quantity: match[1].trim(),
                    notes: ""
                };
            } else {
                // Just the item
                return {
                    item: match[1].charAt(0).toUpperCase() + match[1].slice(1),
                    quantity: "As needed",
                    notes: ""
                };
            }
        }
    }
    
    return {
        item: ingredientStr,
        quantity: "",
        notes: ""
    };
}

// Transform recipes
const polishedRecipes = recipes.map(recipe => {
    const polished = {
        id: recipe.id,
        name: recipe.name,
        source: recipe.source,
        category: recipe.category,
        servings: recipe.servings || "Not specified",
        prep_time: null,
        cook_time: null,
        ingredients: [],
        instructions: recipe.instructions || [],
        notes: []
    };
    
    // Parse ingredients
    if (Array.isArray(recipe.ingredients)) {
        polished.ingredients = recipe.ingredients.map(ing => {
            if (typeof ing === 'string') {
                return parseIngredient(ing);
            }
            return ing; // Already structured
        });
    }
    
    // Keep table format if exists
    if (recipe.hasTable) {
        polished.hasTable = true;
        polished.ingredientTable = recipe.ingredientTable;
        polished.tableNote = recipe.tableNote;
    }
    
    return polished;
});

// Write polished recipes
fs.writeFileSync('recipes_polished_auto.json', JSON.stringify(polishedRecipes, null, 2));
console.log(`Transformed ${polishedRecipes.length} recipes successfully!`);
console.log('Output written to: recipes_polished_auto.json');
