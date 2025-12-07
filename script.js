// Global variables
let recipes = [];
let filteredRecipes = [];
let recipeData = null; // Store full recipe data including both versions

// Load recipes from JSON file
async function loadRecipes() {
    try {
        const response = await fetch('recipes.json');
        const data = await response.json();
        recipeData = data; // Store the full data structure
        
        // Handle both flat array and category-based structure
        if (Array.isArray(data)) {
            // Flat array format (legacy)
            recipes = data;
        } else if (data.categories) {
            // Category-based format - simplified structure
            recipes = [];
            data.categories.forEach(category => {
                category.recipes.forEach(recipe => {
                    recipes.push({
                        ...recipe,
                        id: recipes.length + 1
                    });
                });
            });
        }
        
        filteredRecipes = [...recipes];
        
        populateCategoryFilter();
        displayRecipes(filteredRecipes);
    } catch (error) {
        console.error('Error loading recipes:', error);
        document.getElementById('recipeGrid').innerHTML = 
            '<p class="no-results">Error loading recipes. Please make sure recipes.json is in the same directory.</p>';
    }
}

// Populate category filter dropdown
function populateCategoryFilter() {
    const categories = [...new Set(recipes.map(recipe => recipe.category))].sort();
    const filterSelect = document.getElementById('categoryFilter');
    
    categories.forEach(category => {
        const option = document.createElement('option');
        option.value = category;
        option.textContent = category;
        filterSelect.appendChild(option);
    });
}

// Display recipes in grid
function displayRecipes(recipesToDisplay) {
    const recipeGrid = document.getElementById('recipeGrid');
    recipeGrid.innerHTML = '';

    if (recipesToDisplay.length === 0) {
        recipeGrid.innerHTML = '<p class="no-results">No recipes found. Try a different search or filter.</p>';
        return;
    }

    recipesToDisplay.forEach(recipe => {
        const card = createRecipeCard(recipe);
        recipeGrid.appendChild(card);
    });
}

// Create recipe card element
function createRecipeCard(recipe) {
    const card = document.createElement('div');
    card.className = 'recipe-card';
    card.onclick = () => showRecipeDetail(recipe);

    const categoryBadge = `<span class="recipe-category">${recipe.category}</span>`;
    const sourceLine = recipe.source ? `<p class="recipe-source">Recipe from ${recipe.source}</p>` : '';
    const servingsLine = recipe.servings ? `<p class="recipe-servings">📊 ${recipe.servings}</p>` : '';

    card.innerHTML = `
        <h3>${recipe.name}</h3>
        ${categoryBadge}
        ${sourceLine}
        ${servingsLine}
    `;

    return card;
}

// Fuzzy match recipe name to image filename
function findBestImageMatch(recipeName) {
    // List of all available image files (without .png extension) - exact names from folder
    const availableImages = [
        "APPLE CAKE", "APPLE PIE", "BAKED LASAGNA CASSEROLE", "BAKED RICE CUSTARD", "BAKELESS FRUIT CAKE",
        "BANANA NUT BREAD", "BASIC SWEET DOUGH", "BEAN SALAD", "BECHAMEL SAUCE TOPPING", "BEEF BRISKET (MARINADED)",
        "BLUEBERRY JELLO SALAD", "BLUEBERRY PIE FILLING", "BREAD PUDDING", "BROCCOLI AND RICE", "BROWN SUGAR BROWNIES",
        "CARROT SOUP", "CHEESE DIP (LIKE MEXICO CHIQUITO'S)", "CHERRY PIE FILLING (QUICK)", "CHICKEN BROWN RICE BAKE",
        "CHICKEN CASSEROLE", "CHICKEN RICE CASSEROLE", "CHILI", "CHOCOLATE CREAM PIE", "CHOCOLATE FONDUE",
        "CHOCOLATE OAT-CHIP COOKIES", "CINNAMON ROLLS", "COCKTAIL SAUCE", "COCOANUT CAKE", "CONFECTIONER'S GLAZE",
        "CORNBREAD REVISED 12.24.95", "CORNBREAD SOUTHERN STYLE", "CORNMEAL YEAST ROLLS", "CRAB DIP", "CRANBERRY BREAD",
        "CRANBERRY OR BLUEBERRY CRUNCH", "CRANBERRY ORANGE RELISH", "CRUMBLE CAKE (KRUMELKUCHEN)", "CRUMBLE COFFEE CAKE #2",
        "DELUXE WHITE CAKE", "DINNER ROLL SHAPES", "DINNER ROLLS AND SHAPES", "DINNER ROLLS", "DIVINITY",
        "FETTUCCINE PRIMAVERA", "FLUFFY BUTERMILK BISCUITS", "FLUFFY COCOA FROSTING", "FLUFFY WHITE FROSTING",
        "FROSTED CARROT CAKE", "FROSTED PINEAPPLE SQUARES", "FUDGE (COCOA NUT)", "FUDGE (PLAIN)", "GINGER COOKIES",
        "GINGER SNAPS", "GINGERBREAD MEN COOKIES", "HEARTY CHOWDER", "HOLIDAY JAM CAKE", "HOT WATER GINGERBREAD",
        "HUSH PUPPIES", "ICE BOX PICKLES", "JUMBO SHELLS NO. 1", "JUMBO SHELLS NO. 2", "KARO NUT PIE",
        "KOOL-AID JELLY", "LEMON MERINGUE PIE", "LEMON SNAPS", "LEMON SQUARES", "LIEBKUCHEN",
        "MACARONI, HAM, AND CHEESE", "MARINATED PEPPERS", "Memorandum", "MEMORY BOOK COOKIES", "MERINGUE",
        "MUSHROOM AND NUT PATE", "OATMEAL RAISIN SPICE COOKIES", "OLD FASHIONED JELLY ROLL", "ORANGE-CREAM CHEESE FROSTING",
        "ORIENTAL SALAD", "PEANUT BRITTLE (MUNCHING)", "PEANUT BUTTER PIE", "PFEFFERNUSSE", "PIE CRUST",
        "PIZZA (CARLE VERSION)", "PIZZA DOUGH (CRUSTY)", "PRALINES, OLD FASHIONED", "PUMPKIN BREAD", "PUMPKIN PIE",
        "RASPBERRY JELLO SALAD", "ROASTED NUTS", "ROYAL RICE", "SALMON CROQUETTES", "SCALLOPED SALMON",
        "SPAGHETTI PORTOTINO (SERVES ONE)", "SPAGHETTI PORTOTINO (SERVES SIX)", "SPICE CAKE", "SPRINGERLE NAGEL",
        "SPRINGERLE PG 1", "SPRINGERLE PG 2", "STÖLLEN (KANIS RECIPE)", "STÖLLEN", "STRAWBERRY GLAZE PIE (FRENCH)",
        "SUGAR COOKIES (ALICE CARLE)", "SUGAR COOKIES (PREFERED)", "SUGAR COOKIES (ZUCKERKUCHEN)", "SUGAR COOKIES 50S",
        "SWEET AND SOUR ROAST", "THE LITTLE ENGLISH MUFFIN PIZZA", "TOFU-CHEESE STUFFED SHELLS", "TOMATO SAUCE",
        "TURKEY SAUSAGE", "VANILLA CREAM PIE", "VEGETABLE RELISH SALAD", "WAFFLES"
    ];
    
    const upperRecipeName = recipeName.toUpperCase();
    
    // Try exact match first
    if (availableImages.includes(upperRecipeName)) {
        return `${upperRecipeName}.png`;
    }
    
    // Try to find best partial match
    let bestMatch = null;
    let bestScore = 0;
    
    for (const imageName of availableImages) {
        // Calculate similarity score
        let score = 0;
        
        // Split into words and compare
        const recipeWords = upperRecipeName.split(/[\s'-]+/).filter(w => w.length > 2);
        const imageWords = imageName.split(/[\s'-]+/).filter(w => w.length > 2);
        
        // Count matching words
        for (const word of recipeWords) {
            if (imageWords.some(imgWord => imgWord.includes(word) || word.includes(imgWord))) {
                score++;
            }
        }
        
        // Prefer matches with similar length
        const lengthDiff = Math.abs(recipeWords.length - imageWords.length);
        score -= lengthDiff * 0.3;
        
        if (score > bestScore) {
            bestScore = score;
            bestMatch = imageName;
        }
    }
    
    // Return best match if score is reasonable, otherwise use recipe name
    return bestMatch && bestScore > 1 ? `${bestMatch}.png` : `${upperRecipeName}.png`;
}

// Show recipe detail in modal
function showRecipeDetail(recipe) {
    const modal = document.getElementById('recipeModal');
    const detailDiv = document.getElementById('recipeDetail');

    // Store current recipe globally for batch size adjustments
    window.currentRecipe = recipe;
    window.currentBatchMultiplier = 1;

    // Generate cookbook image filename using fuzzy matching
    const imageName = findBestImageMatch(recipe.name);
    const imagePath = `MeeMaw Recipe Book Image File/${imageName}`;
    
    // Create inline action bar
    const actionBar = `
        <div class="recipe-action-bar">
            <button onclick="showCookbookImage('${imagePath}')" class="view-original-btn">
                📖 View Original Page
            </button>
            <button onclick="showPrintDialog()" class="print-recipe-btn">
                🖨️ Print Recipe
            </button>
            <button onclick="closeRecipeModal()" class="close-recipe-btn">
                ❌ Close
            </button>
        </div>
    `;
    
    detailDiv.innerHTML = `
        ${actionBar}
        ${formatRecipeContent(recipe)}
    `;

    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
}

// Show cookbook image in modal
function showCookbookImage(imagePath) {
    // Create image modal overlay
    const imageModal = document.createElement('div');
    imageModal.className = 'image-modal';
    imageModal.innerHTML = `
        <div class="image-modal-content">
            <span class="image-close">&times;</span>
            <img src="${imagePath}" alt="Original Cookbook Page">
        </div>
    `;
    
    document.body.appendChild(imageModal);
    
    // Show modal
    setTimeout(() => {
        imageModal.classList.add('active');
    }, 10);
    
    // Close handlers
    const closeBtn = imageModal.querySelector('.image-close');
    closeBtn.onclick = () => closeImageModal(imageModal);
    
    imageModal.onclick = (e) => {
        if (e.target === imageModal) {
            closeImageModal(imageModal);
        }
    };
    
    document.addEventListener('keydown', function escHandler(e) {
        if (e.key === 'Escape') {
            closeImageModal(imageModal);
            document.removeEventListener('keydown', escHandler);
        }
    });
}

function closeImageModal(modal) {
    modal.classList.remove('active');
    setTimeout(() => {
        modal.remove();
    }, 300);
}

// Format recipe content
function formatRecipeContent(recipe, versionLabel) {
    if (!recipe) return '<p>Recipe version not available.</p>';
    
    const categoryBadge = `<span class="detail-category">${recipe.category}</span>`;
    
    // Build source line with subtitle if available
    let sourceLine = '';
    if (recipe.subtitle) {
        sourceLine = `<p class="detail-source"><em>${recipe.subtitle}</em></p>`;
    }
    if (recipe.source) {
        sourceLine += `<p class="detail-source">Recipe from: ${recipe.source}</p>`;
    }
    
    // Build servings/timing info
    let metaInfo = '';
    if (recipe.servings || recipe.yield) {
        const servingsText = recipe.yield || recipe.servings;
        metaInfo += `<p class="detail-servings" id="recipeServings" data-original="${servingsText}">📊 ${servingsText}</p>`;
    }
    if (recipe.prep_time) {
        metaInfo += `<p class="detail-servings">⏱️ Prep: ${recipe.prep_time}</p>`;
    }
    if (recipe.cook_time) {
        metaInfo += `<p class="detail-servings">🔥 Cook: ${recipe.cook_time}</p>`;
    }
    if (recipe.total_time) {
        metaInfo += `<p class="detail-servings">⏲️ Total: ${recipe.total_time}</p>`;
    }

    // Format ingredients with batch size selector
    let ingredientsList = '';
    if (recipe.ingredients && recipe.ingredients.length > 0) {
        const batchSelector = `
            <div class="batch-size-selector">
                <label for="batchSize">Batch Size:</label>
                <select id="batchSize" onchange="adjustBatchSize(this.value)">
                    <option value="0.25">¼x (Quarter)</option>
                    <option value="0.5">½x (Half)</option>
                    <option value="1" selected>1x (Original)</option>
                    <option value="2">2x (Double)</option>
                    <option value="3">3x (Triple)</option>
                </select>
            </div>
        `;
        
        const multiplier = window.currentBatchMultiplier || 1;
        const scaledIngredients = recipe.ingredients.map(ing => scaleIngredient(ing, multiplier));
        
        ingredientsList = `
            <h3>Ingredients</h3>
            ${batchSelector}
            <ul id="ingredientsList">${scaledIngredients.map(ing => `<li>${ing}</li>`).join('')}</ul>
        `;
    }

    // Format instructions
    const instructionsList = recipe.instructions && recipe.instructions.length > 0
        ? `<h3>Instructions</h3><ol>${recipe.instructions.map(inst => `<li>${inst}</li>`).join('')}</ol>`
        : '<p><em>Instructions not available for this recipe.</em></p>';

    // Add shaping methods if present (for rolls, etc.)
    let shapingMethods = '';
    if (recipe.shaping_methods && recipe.shaping_methods.length > 0) {
        shapingMethods = '<h3>Shaping Methods</h3>';
        recipe.shaping_methods.forEach(method => {
            shapingMethods += `
                <div style="margin-bottom: 1rem; padding: 1rem; background: rgba(212, 165, 116, 0.1); border-left: 4px solid var(--german-gold); border-radius: 6px;">
                    <h4 style="color: var(--german-red); margin-bottom: 0.5rem;">${method.shape}</h4>
                    <p style="margin: 0; line-height: 1.6;">${method.method}</p>
                </div>
            `;
        });
    }

    // Add notes if present
    let notesSection = '';
    if (recipe.notes && recipe.notes.length > 0) {
        notesSection = `
            <h3>Notes</h3>
            <ul class="recipe-notes">
                ${recipe.notes.map(note => `<li>${note}</li>`).join('')}
            </ul>
        `;
    }

    return `
        <h2>${recipe.name}</h2>
        ${categoryBadge}
        ${sourceLine}
        ${metaInfo}
        ${ingredientsList}
        ${instructionsList}
        ${shapingMethods}
        ${notesSection}
    `;
}

// Close modal
function closeModal() {
    const modal = document.getElementById('recipeModal');
    modal.style.display = 'none';
    document.body.style.overflow = 'auto'; // Restore scrolling
}

// Alias for HTML onclick handlers
function closeRecipeModal() {
    closeModal();
}

// View original image from button click
function viewOriginalImage() {
    if (!window.currentRecipe) return;
    const imageName = findBestImageMatch(window.currentRecipe.name);
    const imagePath = `MeeMaw Recipe Book Image File/${imageName}`;
    showCookbookImage(imagePath);
}

// Search functionality
function searchRecipes(searchTerm) {
    const lowerSearchTerm = searchTerm.toLowerCase();
    
    filteredRecipes = recipes.filter(recipe => {
        // Search in basic fields
        const basicMatch = recipe.name.toLowerCase().includes(lowerSearchTerm) ||
               recipe.category.toLowerCase().includes(lowerSearchTerm) ||
               (recipe.source && recipe.source.toLowerCase().includes(lowerSearchTerm)) ||
               (recipe.subtitle && recipe.subtitle.toLowerCase().includes(lowerSearchTerm));
        
        if (basicMatch) return true;
        
        // Search in ingredients (handle both string and object formats)
        const ingredientMatch = recipe.ingredients && recipe.ingredients.some(ing => {
            if (typeof ing === 'string') {
                return ing.toLowerCase().includes(lowerSearchTerm);
            } else if (typeof ing === 'object') {
                return (ing.item && ing.item.toLowerCase().includes(lowerSearchTerm)) ||
                       (ing.notes && ing.notes.toLowerCase().includes(lowerSearchTerm));
            }
            return false;
        });
        
        if (ingredientMatch) return true;
        
        // Search in instructions
        const instructionMatch = recipe.instructions && recipe.instructions.some(inst => 
            inst.toLowerCase().includes(lowerSearchTerm)
        );
        
        return instructionMatch;
    });

    applyFilters();
}

// Filter by category
function filterByCategory(category) {
    if (category === 'all') {
        applyFilters();
    } else {
        const searchTerm = document.getElementById('searchInput').value.toLowerCase();
        const searchFiltered = searchTerm ? 
            recipes.filter(recipe => {
                return recipe.name.toLowerCase().includes(searchTerm) ||
                       recipe.category.toLowerCase().includes(searchTerm) ||
                       (recipe.source && recipe.source.toLowerCase().includes(searchTerm)) ||
                       recipe.ingredients.some(ing => ing.toLowerCase().includes(searchTerm)) ||
                       recipe.instructions.some(inst => inst.toLowerCase().includes(searchTerm));
            }) : recipes;

        filteredRecipes = searchFiltered.filter(recipe => recipe.category === category);
        displayRecipes(filteredRecipes);
    }
}

// Apply all active filters
function applyFilters() {
    const category = document.getElementById('categoryFilter').value;
    
    if (category === 'all') {
        displayRecipes(filteredRecipes);
    } else {
        const categoryFiltered = filteredRecipes.filter(recipe => recipe.category === category);
        displayRecipes(categoryFiltered);
    }
}

// Scale ingredient quantities based on batch multiplier with metric conversion
function scaleIngredient(ingredient, multiplier) {
    // Extract quantity, unit, and item from string format
    const match = ingredient.match(/^([\d\/.\s-]+)?\s*([a-zA-Z().,\s]*?)\s+(.+)$/);
    
    if (!match) {
        return ingredient; // Return as-is if can't parse
    }
    
    const [, quantityStr, unit, item] = match;
    
    // Skip metric conversion for non-numeric or "to taste" type ingredients
    if (!quantityStr || quantityStr.trim() === '' || 
        ingredient.toLowerCase().includes('to taste') ||
        ingredient.toLowerCase().includes('as needed') ||
        ingredient.toLowerCase().includes('dash') ||
        ingredient.toLowerCase().includes('pinch') ||
        ingredient.toLowerCase().includes('about') ||
        ingredient.toLowerCase().includes('optional')) {
        return ingredient;
    }
    
    // Convert fraction to decimal
    let quantity = 0;
    const parts = quantityStr.trim().split(/\s+/);
    
    for (const part of parts) {
        if (part.includes('/')) {
            const [num, den] = part.split('/').map(Number);
            quantity += num / den;
        } else if (part.includes('-')) {
            // Handle ranges like "2-3" - use average
            const [min, max] = part.split('-').map(Number);
            quantity += (min + max) / 2;
        } else {
            quantity += parseFloat(part) || 0;
        }
    }
    
    // Scale the quantity
    const scaledQuantity = quantity * multiplier;
    
    // Format the scaled quantity
    let formattedQuantity;
    if (scaledQuantity % 1 === 0) {
        formattedQuantity = scaledQuantity.toString();
    } else if (scaledQuantity < 1) {
        // Convert to fraction for small numbers
        const fractions = {
            0.25: '1/4',
            0.33: '1/3',
            0.5: '1/2',
            0.66: '2/3',
            0.75: '3/4'
        };
        const nearest = Object.keys(fractions).reduce((prev, curr) => 
            Math.abs(curr - scaledQuantity) < Math.abs(prev - scaledQuantity) ? curr : prev
        );
        if (Math.abs(nearest - scaledQuantity) < 0.05) {
            formattedQuantity = fractions[nearest];
        } else {
            formattedQuantity = scaledQuantity.toFixed(2).replace(/\.?0+$/, '');
        }
    } else {
        formattedQuantity = scaledQuantity.toFixed(2).replace(/\.?0+$/, '');
    }
    
    // Get metric conversion
    const metricValue = convertToMetric(scaledQuantity, unit, item);
    
    // Show US measurement first, then metric in parentheses
    if (metricValue) {
        return `${formattedQuantity} ${unit.trim()} ${item} <span class="metric-conversion">(${metricValue})</span>`;
    }
    
    return `${formattedQuantity} ${unit.trim()} ${item}`;
}

// Adjust batch size and re-render ingredients
function adjustBatchSize(multiplier) {
    multiplier = parseFloat(multiplier);
    window.currentBatchMultiplier = multiplier;
    
    if (!window.currentRecipe) return;
    
    const recipe = window.currentRecipe;
    const scaledIngredients = recipe.ingredients.map(ing => scaleIngredient(ing, multiplier));
    
    const ingredientsList = document.getElementById('ingredientsList');
    if (ingredientsList) {
        ingredientsList.innerHTML = scaledIngredients.map(ing => `<li>${ing}</li>`).join('');
    }

    // Update servings text
    updateServingsText(multiplier);
}

function updateServingsText(multiplier) {
    const servingsEl = document.getElementById('recipeServings');
    if (!servingsEl) return;
    
    const originalText = servingsEl.getAttribute('data-original');
    if (!originalText) return;
    
    // Regex to find numbers and ranges
    // Matches:
    // 1. Ranges: 20-24, 20–24
    // 2. Simple numbers: 20, 2.5
    const newText = originalText.replace(/(\d+(?:\.\d+)?)(?:\s*([-–])\s*(\d+(?:\.\d+)?))?/g, (match, n1, sep, n2, offset, string) => {
        // Check for dimensions immediately following the match to avoid scaling them
        // e.g. "9-inch", "350 degrees"
        const remainder = string.slice(offset + match.length);
        if (/^[\s-]*(?:inch|in\.|cm|mm|°|"|'|degree)/i.test(remainder)) {
            return match; 
        }
        
        const scale = (n) => {
            const val = parseFloat(n) * multiplier;
            // Format: if integer, show integer. If decimal, max 1 decimal place.
            return Number.isInteger(val) ? val.toString() : val.toFixed(1).replace(/\.0$/, '');
        };
        
        if (n2) {
            // It's a range
            return `${scale(n1)}${sep}${scale(n2)}`;
        } else {
            // Single number
            return scale(n1);
        }
    });
    
    servingsEl.innerHTML = `📊 ${newText}`;
}

// Event listeners
document.addEventListener('DOMContentLoaded', function() {
    loadRecipes();

    // Search input
    const searchInput = document.getElementById('searchInput');
    searchInput.addEventListener('input', (e) => {
        searchRecipes(e.target.value);
    });

    // Category filter
    const categoryFilter = document.getElementById('categoryFilter');
    categoryFilter.addEventListener('change', (e) => {
        filterByCategory(e.target.value);
    });

    // Modal close button
    const closeBtn = document.querySelector('.close');
    closeBtn.addEventListener('click', closeModal);

    // Close modal when clicking outside
    window.addEventListener('click', (e) => {
        const modal = document.getElementById('recipeModal');
        if (e.target === modal) {
            closeModal();
        }
    });

    // Close modal with Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeModal();
        }
    });

    setupMobileNav();
});

// Print recipe function (can be added to modal if needed)
function printRecipe() {
    // Get the active tab content
    const activeTab = document.querySelector('.tab-content.active');
    const recipeContent = activeTab ? activeTab.innerHTML : document.getElementById('recipeDetail').innerHTML;
    
    // Check if user wants to include cookbook image
    const includeImage = document.getElementById('includeCookbookImage').checked;
    
    // Get the cookbook image if it should be included
    let cookbookImageHTML = '';
    if (includeImage) {
        const imageLink = document.querySelector('.cookbook-image-link a');
        if (imageLink) {
            const imagePath = imageLink.href;
            cookbookImageHTML = `
                <div class="print-cookbook-image">
                    <h3 style="page-break-before: always;">Original Cookbook Page</h3>
                    <img src="${imagePath}" alt="Original Cookbook Page" style="max-width: 100%; height: auto; border: 2px solid #d9c9b3; margin: 20px 0;">
                </div>
            `;
        }
    }
    
    // Create a new window for printing
    const printWindow = window.open('', '_blank', 'width=800,height=600');
    printWindow.document.write(`
        <!DOCTYPE html>
        <html>
        <head>
            <title>Print Recipe</title>
            <style>
                body {
                    font-family: Georgia, serif;
                    max-width: 800px;
                    margin: 20px auto;
                    padding: 20px;
                    color: #2c1810;
                }
                h2 { color: #8b2e1f; margin-bottom: 10px; }
                h3 { color: #704214; margin-top: 20px; margin-bottom: 10px; border-bottom: 2px solid #d4a574; padding-bottom: 5px; }
                h4 { color: #8b2e1f; margin-top: 15px; }
                .detail-category { 
                    background: #d4a574; 
                    color: white; 
                    padding: 5px 15px; 
                    border-radius: 20px; 
                    font-size: 0.9em;
                    display: inline-block;
                    margin-bottom: 10px;
                }
                .detail-source { font-style: italic; color: #6b5447; margin: 5px 0; }
                .detail-servings { margin: 5px 0; }
                ul, ol { margin-left: 25px; line-height: 1.8; }
                li { margin-bottom: 8px; }
                .metric-conversion { color: #2d5a7b; font-size: 0.9em; }
                .ingredient-note { color: #6b5447; }
                .ingredient-table { 
                    width: 100%; 
                    border-collapse: collapse; 
                    margin: 15px 0; 
                }
                .ingredient-table th, .ingredient-table td { 
                    border: 1px solid #d9c9b3; 
                    padding: 8px; 
                    text-align: left; 
                }
                .ingredient-table th { background: #f5efe0; font-weight: bold; }
                .recipe-notes { background: #faf7f0; padding: 15px; border-left: 4px solid #d4a574; }
                .cookbook-image-link, .recipe-tabs { display: none; }
                .print-cookbook-image { margin-top: 30px; }
                .print-cookbook-image h3 { margin-top: 40px; }
                @media print {
                    body { margin: 0; padding: 15px; }
                    .cookbook-image-link, .recipe-tabs { display: none; }
                }
            </style>
        </head>
        <body>
            ${recipeContent}
            ${cookbookImageHTML}
        </body>
        </html>
    `);
    printWindow.document.close();
    
    // Wait for content to load, then print
    setTimeout(() => {
        printWindow.print();
    }, 250);
}

// ===== METRIC CONVERSION SYSTEM =====
function convertToMetric(quantity, unit, ingredientName = '') {
    // Skip if quantity is not numeric
    if (!quantity || isNaN(parseFloat(quantity))) {
        return null;
    }
    
    const qty = parseFloat(quantity);
    const lowerUnit = unit.toLowerCase().trim();
    const lowerIngredient = ingredientName.toLowerCase();
    
    // 1. Handle Weight Units (oz, lb) - Always Grams
    // Note: "fl oz" is handled in volume section
    if (lowerUnit === 'oz' || lowerUnit === 'ounce' || lowerUnit === 'ounces') {
        const grams = Math.round(qty * 28.35);
        return grams >= 1000 ? `${(grams / 1000).toFixed(2)} kg` : `${grams} g`;
    }
    if (lowerUnit === 'lb' || lowerUnit === 'lbs' || lowerUnit === 'pound' || lowerUnit === 'pounds') {
        const grams = Math.round(qty * 453.6);
        return grams >= 1000 ? `${(grams / 1000).toFixed(2)} kg` : `${grams} g`;
    }

    // 2. Identify Ingredient Type for Volume-to-Weight Conversion
    
    // Special Case: Powdered Sugar is much lighter (~125g/cup)
    const isPowderedSugar = lowerIngredient.includes('powdered sugar') || 
                           lowerIngredient.includes('confectioners sugar') || 
                           lowerIngredient.includes('icing sugar');

    // Light Solids (~125g/cup): Flour, Oats, Cocoa, Cornmeal, Crumbs, Starch, Powdered Sugar
    const isLightSolid = isPowderedSugar ||
                        lowerIngredient.includes('flour') || 
                        lowerIngredient.includes('oats') || 
                        lowerIngredient.includes('cocoa') || 
                        lowerIngredient.includes('cornmeal') || 
                        lowerIngredient.includes('crumbs') || 
                        lowerIngredient.includes('starch') ||
                        lowerIngredient.includes('baking powder') ||
                        lowerIngredient.includes('baking soda');

    // Medium Solids (~200g/cup): Granulated/Brown Sugar, Rice, Cheese, Chocolate, Nuts, Fruit, Beans
    const isMediumSolid = lowerIngredient.includes('sugar') || // Catches granulated and brown
                         lowerIngredient.includes('rice') || 
                         lowerIngredient.includes('cheese') || 
                         lowerIngredient.includes('chocolate') || 
                         lowerIngredient.includes('chips') || 
                         lowerIngredient.includes('nut') || 
                         lowerIngredient.includes('pecan') || 
                         lowerIngredient.includes('walnut') || 
                         lowerIngredient.includes('almond') || 
                         lowerIngredient.includes('fruit') ||
                         lowerIngredient.includes('raisin') ||
                         lowerIngredient.includes('bean') ||
                         lowerIngredient.includes('salt');

    // Heavy Solids/Fats (~227g/cup): Butter, Margarine, Shortening, Lard
    const isHeavySolid = lowerIngredient.includes('butter') || 
                        lowerIngredient.includes('margarine') || 
                        lowerIngredient.includes('shortening') || 
                        lowerIngredient.includes('lard');

    // 3. Perform Conversion based on Type
    
    // Helper to calculate grams based on density (g/cup)
    const calcGrams = (density) => {
        let grams = 0;
        if (lowerUnit.includes('cup')) grams = qty * density;
        else if (lowerUnit.includes('tablespoon') || lowerUnit.includes('tbsp')) grams = qty * (density / 16);
        else if (lowerUnit.includes('teaspoon') || lowerUnit.includes('tsp')) grams = qty * (density / 48);
        else return null; // Unknown unit for this path
        
        grams = Math.round(grams);
        return grams >= 1000 ? `${(grams / 1000).toFixed(2)} kg` : `${grams} g`;
    };

    if (isLightSolid) return calcGrams(125);
    if (isMediumSolid) return calcGrams(200);
    if (isHeavySolid) return calcGrams(227);

    // 4. Default to Volume (Liquids) - ml
    const volumeConversions = {
        'cup': 240,
        'cups': 240,
        'tablespoon': 15,
        'tablespoons': 15,
        'tbsp': 15,
        'teaspoon': 5,
        'teaspoons': 5,
        'tsp': 5,
        'fluid ounce': 30,
        'fluid ounces': 30,
        'fl oz': 30,
        'pint': 473,
        'pints': 473,
        'quart': 946,
        'quarts': 946,
        'gallon': 3785,
        'gallons': 3785
    };
    
    for (const [key, mlPerUnit] of Object.entries(volumeConversions)) {
        if (lowerUnit.includes(key)) {
            const ml = Math.round(qty * mlPerUnit);
            return ml >= 1000 ? `${(ml / 1000).toFixed(2)} L` : `${ml} ml`;
        }
    }
    
    return null; // No conversion available
}

// ===== PRINT DIALOG =====
function showPrintDialog() {
    // Create custom print dialog
    const dialog = document.createElement('div');
    dialog.className = 'print-dialog-overlay';
    dialog.innerHTML = `
        <div class="print-dialog">
            <h3>Print Recipe</h3>
            <p>Would you like to include the original cookbook page?</p>
            <div class="print-dialog-buttons">
                <button class="btn-secondary" onclick="executePrint(false)">Recipe Only</button>
                <button class="btn-primary" onclick="executePrint(true)">Include Original Page</button>
            </div>
            <button class="print-dialog-close" onclick="closePrintDialog()">&times;</button>
        </div>
    `;
    
    document.body.appendChild(dialog);
    setTimeout(() => dialog.classList.add('active'), 10);
}

function closePrintDialog() {
    const dialog = document.querySelector('.print-dialog-overlay');
    if (dialog) {
        dialog.classList.remove('active');
        setTimeout(() => dialog.remove(), 300);
    }
}

function executePrint(includeImage) {
    closePrintDialog();
    
    const recipeContent = document.getElementById('recipeDetail').innerHTML;
    
    let cookbookImageHTML = '';
    if (includeImage && window.currentRecipe) {
        const imageName = findBestImageMatch(window.currentRecipe.name);
        const imagePath = `MeeMaw Recipe Book Image File/${imageName}`;
        cookbookImageHTML = `
            <div class="print-cookbook-image">
                <h3 style="page-break-before: always;">Original Cookbook Page</h3>
                <img src="${imagePath}" alt="Original Cookbook Page" style="max-width: 100%; height: auto; border: 2px solid #d9c9b3; margin: 20px 0;">
            </div>
        `;
    }
    
    const printWindow = window.open('', '_blank', 'width=800,height=600');
    printWindow.document.write(`
        <!DOCTYPE html>
        <html>
        <head>
            <title>Print Recipe</title>
            <style>
                body {
                    font-family: Georgia, serif;
                    max-width: 800px;
                    margin: 20px auto;
                    padding: 20px;
                    color: #2c1810;
                }
                h2 { color: #8b2e1f; margin-bottom: 10px; }
                h3 { color: #704214; margin-top: 20px; margin-bottom: 10px; border-bottom: 2px solid #d4a574; padding-bottom: 5px; }
                .detail-category { 
                    background: #d4a574; 
                    color: white; 
                    padding: 5px 15px; 
                    border-radius: 20px; 
                    font-size: 0.9em;
                    display: inline-block;
                    margin-bottom: 10px;
                }
                .detail-servings { margin: 5px 0; }
                ul, ol { margin-left: 25px; line-height: 1.8; }
                li { margin-bottom: 8px; }
                .metric-conversion { color: #2d5a7b; font-size: 0.9em; }
                .recipe-action-bar, .cookbook-image-link { display: none; }
                @media print {
                    body { margin: 0; padding: 15px; }
                }
            </style>
        </head>
        <body>
            ${recipeContent}
            ${cookbookImageHTML}
        </body>
        </html>
    `);
    printWindow.document.close();
    setTimeout(() => printWindow.print(), 250);
}



// Mobile Navigation Functions
function toggleMobileNav() {
    const mobileNav = document.getElementById('mobileNav');
    if (mobileNav) mobileNav.classList.toggle('active');
}

function closeMobileNav() {
    const mobileNav = document.getElementById('mobileNav');
    if (mobileNav) mobileNav.classList.remove('active');
}

function setupMobileNav() {
    const hamburgerBtn = document.getElementById('hamburgerBtn');
    const mobileNavClose = document.getElementById('mobileNavClose');
    const mobileNavLinks = document.querySelectorAll('.mobile-nav-links a');
    
    if (hamburgerBtn) {
        hamburgerBtn.addEventListener('click', toggleMobileNav);
    }
    
    if (mobileNavClose) {
        mobileNavClose.addEventListener('click', closeMobileNav);
    }
    
    // Close nav when clicking a link
    mobileNavLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const sectionId = link.getAttribute('data-section');
            scrollToSection(sectionId);
        });
    });
    
    // Close nav when clicking outside
    document.addEventListener('click', (e) => {
        const mobileNav = document.getElementById('mobileNav');
        const hamburgerBtn = document.getElementById('hamburgerBtn');
        
        if (mobileNav && hamburgerBtn && 
            !mobileNav.contains(e.target) && 
            !hamburgerBtn.contains(e.target) &&
            mobileNav.classList.contains('active')) {
            closeMobileNav();
        }
    });
}



// Smooth scroll to section
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        const headerOffset = 100;
        const elementPosition = section.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

        window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
        });
    }
}
