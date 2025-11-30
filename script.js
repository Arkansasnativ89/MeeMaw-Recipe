// Global variables
let recipes = [];
let filteredRecipes = [];
let recipeData = null; // Store full recipe data including both versions
let viewMode = 'category'; // 'category' or 'index'

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
            // Category-based format with original/improved recipes
            recipes = [];
            data.categories.forEach(category => {
                category.recipes.forEach(recipeGroup => {
                    // Store both versions if available
                    const recipe = {
                        ...(recipeGroup.improved_recipe || recipeGroup.original_recipe),
                        id: recipes.length + 1,
                        _original: recipeGroup.original_recipe,
                        _improved: recipeGroup.improved_recipe,
                        _hasOriginal: !!recipeGroup.original_recipe,
                        _hasImproved: !!recipeGroup.improved_recipe
                    };
                    recipes.push(recipe);
                });
            });
        }
        
        filteredRecipes = [...recipes];
        
        populateCategoryFilter();
        displayCategoryView();
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

// Display recipes in category view
function displayCategoryView() {
    const recipeGrid = document.getElementById('recipeGrid');
    recipeGrid.innerHTML = '';
    recipeGrid.className = 'category-view';
    
    // Group recipes by category
    const categoryGroups = {};
    filteredRecipes.forEach(recipe => {
        if (!categoryGroups[recipe.category]) {
            categoryGroups[recipe.category] = [];
        }
        categoryGroups[recipe.category].push(recipe);
    });
    
    // Sort categories
    const sortedCategories = Object.keys(categoryGroups).sort();
    
    sortedCategories.forEach(categoryName => {
        const categorySection = document.createElement('div');
        categorySection.className = 'category-section';
        
        const categoryHeader = document.createElement('div');
        categoryHeader.className = 'category-header';
        categoryHeader.innerHTML = `
            <h2>${categoryName}</h2>
            <span class="recipe-count">${categoryGroups[categoryName].length} recipes</span>
        `;
        
        const recipeList = document.createElement('div');
        recipeList.className = 'recipe-list';
        
        categoryGroups[categoryName].sort((a, b) => a.name.localeCompare(b.name)).forEach(recipe => {
            const recipeLink = document.createElement('div');
            recipeLink.className = 'recipe-link';
            recipeLink.onclick = () => showRecipeDetail(recipe);
            
            const versionBadge = recipe._hasOriginal && recipe._hasImproved 
                ? '<span class="version-badge">2 versions</span>' 
                : '';
            
            recipeLink.innerHTML = `
                <span class="recipe-name">${recipe.name}</span>
                ${versionBadge}
            `;
            
            recipeList.appendChild(recipeLink);
        });
        
        categorySection.appendChild(categoryHeader);
        categorySection.appendChild(recipeList);
        recipeGrid.appendChild(categorySection);
    });
}

// Display recipes in index (alphabetical) view
function displayIndexView() {
    const recipeGrid = document.getElementById('recipeGrid');
    recipeGrid.innerHTML = '';
    recipeGrid.className = 'index-view';
    
    // Group recipes by first letter
    const letterGroups = {};
    filteredRecipes.forEach(recipe => {
        const firstLetter = recipe.name[0].toUpperCase();
        if (!letterGroups[firstLetter]) {
            letterGroups[firstLetter] = [];
        }
        letterGroups[firstLetter].push(recipe);
    });
    
    // Sort letters
    const sortedLetters = Object.keys(letterGroups).sort();
    
    sortedLetters.forEach(letter => {
        const letterSection = document.createElement('div');
        letterSection.className = 'letter-section';
        
        const letterHeader = document.createElement('div');
        letterHeader.className = 'letter-header';
        letterHeader.innerHTML = `<h2>${letter}</h2>`;
        
        const recipeList = document.createElement('div');
        recipeList.className = 'recipe-list';
        
        letterGroups[letter].sort((a, b) => a.name.localeCompare(b.name)).forEach(recipe => {
            const recipeLink = document.createElement('div');
            recipeLink.className = 'recipe-link';
            recipeLink.onclick = () => showRecipeDetail(recipe);
            
            const categoryTag = `<span class="category-tag">${recipe.category}</span>`;
            const versionBadge = recipe._hasOriginal && recipe._hasImproved 
                ? '<span class="version-badge">2 versions</span>' 
                : '';
            
            recipeLink.innerHTML = `
                <span class="recipe-name">${recipe.name}</span>
                <div class="recipe-meta">
                    ${categoryTag}
                    ${versionBadge}
                </div>
            `;
            
            recipeList.appendChild(recipeLink);
        });
        
        letterSection.appendChild(letterHeader);
        letterSection.appendChild(recipeList);
        recipeGrid.appendChild(letterSection);
    });
}

// Toggle view mode
function toggleViewMode(mode) {
    viewMode = mode;
    const categoryBtn = document.getElementById('categoryViewBtn');
    const indexBtn = document.getElementById('indexViewBtn');
    
    if (mode === 'category') {
        categoryBtn.classList.add('active');
        indexBtn.classList.remove('active');
        displayCategoryView();
    } else {
        indexBtn.classList.add('active');
        categoryBtn.classList.remove('active');
        displayIndexView();
    }
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

    // Generate cookbook image filename using fuzzy matching
    const imageName = findBestImageMatch(recipe.name);
    const imagePath = `MeeMaw Recipe Book Image File/${imageName}`;
    
    // Check if we have both versions
    const hasOriginal = recipe._hasOriginal;
    const hasImproved = recipe._hasImproved;
    const hasBothVersions = hasOriginal && hasImproved;
    
    // Create tabs if both versions exist
    let tabsHTML = '';
    if (hasBothVersions) {
        tabsHTML = `
            <div class="recipe-tabs">
                <button class="tab-button active" onclick="switchTab(event, 'original')">Original Recipe</button>
                <button class="tab-button" onclick="switchTab(event, 'improved')">Alternate Recipe</button>
            </div>
        `;
    }
    
    // Create image link and hidden print image
    const imageLink = `
        <div class="cookbook-image-link">
            <button onclick="showCookbookImage('${imagePath}')" class="view-original-btn">
                📖 View Original Cookbook Page
            </button>
        </div>
        <div class="cookbook-image-print" data-image-path="${imagePath}">
            <h3>Original Cookbook Page</h3>
            <img src="${imagePath}" alt="Original Cookbook Page">
        </div>
    `;
    
    detailDiv.innerHTML = `
        ${tabsHTML}
        ${imageLink}
        <div id="original-tab" class="tab-content ${hasBothVersions ? 'active' : ''}">
            ${formatRecipeContent(recipe._original || recipe, 'Original')}
        </div>
        ${hasBothVersions ? `
        <div id="improved-tab" class="tab-content">
            ${formatRecipeContent(recipe._improved, 'Alternate')}
        </div>
        ` : ''}
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

// Switch between tabs
function switchTab(event, tabName) {
    // Remove active class from all tabs and content
    const tabs = document.querySelectorAll('.tab-button');
    const contents = document.querySelectorAll('.tab-content');
    
    tabs.forEach(tab => tab.classList.remove('active'));
    contents.forEach(content => content.classList.remove('active'));
    
    // Add active class to clicked tab and corresponding content
    event.currentTarget.classList.add('active');
    document.getElementById(`${tabName}-tab`).classList.add('active');
}

// Format recipe content (extracted from showRecipeDetail for reusability)
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
        metaInfo += `<p class="detail-servings">📊 ${recipe.yield || recipe.servings}</p>`;
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

    // Format ingredients - handle both simple strings and structured objects
    let ingredientsList = '';
    if (recipe.hasTable && recipe.ingredientTable) {
        // Table format (for variable measurements)
        const table = recipe.ingredientTable;
        const tableHTML = `
            <table class="ingredient-table">
                <thead>
                    <tr>${table.headers.map(header => `<th>${header}</th>`).join('')}</tr>
                </thead>
                <tbody>
                    ${table.rows.map(row => `<tr>${row.map(cell => `<td>${cell}</td>`).join('')}</tr>`).join('')}
                </tbody>
            </table>
        `;
        const tableNote = recipe.tableNote ? `<p class="table-note"><em>${recipe.tableNote}</em></p>` : '';
        ingredientsList = `<h3>Ingredients</h3>${tableHTML}${tableNote}`;
    } else if (recipe.ingredients && recipe.ingredients.length > 0) {
        // Check if ingredients are structured objects or simple strings
        const firstIng = recipe.ingredients[0];
        const isStructured = typeof firstIng === 'object' && firstIng.item;
        
        if (isStructured) {
            // Structured format with metric conversions
            let currentSection = null;
            let ingredientsHTML = '';
            
            recipe.ingredients.forEach(ing => {
                // Handle section headers
                if (ing.section && ing.section !== currentSection) {
                    if (currentSection !== null) ingredientsHTML += '</ul>';
                    ingredientsHTML += `<h4 style="margin-top: 1.5rem; margin-bottom: 0.5rem; color: var(--warm-brown); font-size: 1.1rem;">${ing.section}</h4><ul>`;
                    currentSection = ing.section;
                } else if (currentSection === null) {
                    ingredientsHTML += '<ul>';
                    currentSection = '';
                }
                
                // Build ingredient line
                let ingLine = '';
                if (ing.quantity) ingLine += `<strong>${ing.quantity}</strong> `;
                ingLine += ing.item;
                
                // Add notes if available
                if (ing.notes) {
                    ingLine += ` <em class="ingredient-note">(${ing.notes})</em>`;
                }
                
                // Add metric conversion if available
                if (ing.metric) {
                    const metricQty = ing.metric.min 
                        ? `${ing.metric.min}–${ing.metric.max}` 
                        : ing.metric.quantity;
                    ingLine += ` <span class="metric-conversion">[${metricQty} ${ing.metric.unit}]</span>`;
                }
                
                ingredientsHTML += `<li>${ingLine}</li>`;
            });
            
            ingredientsHTML += '</ul>';
            ingredientsList = `<h3>Ingredients</h3>${ingredientsHTML}`;
        } else {
            // Simple string format (backward compatible)
            ingredientsList = `<h3>Ingredients</h3><ul>${recipe.ingredients.map(ing => `<li>${ing}</li>`).join('')}</ul>`;
        }
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

    if (viewMode === 'category') {
        displayCategoryView();
    } else {
        displayIndexView();
    }
}

// Filter by category
function filterByCategory(category) {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();
    
    if (category === 'all') {
        if (searchTerm) {
            searchRecipes(searchTerm);
        } else {
            filteredRecipes = [...recipes];
            if (viewMode === 'category') {
                displayCategoryView();
            } else {
                displayIndexView();
            }
        }
    } else {
        const searchFiltered = searchTerm ?  
            recipes.filter(recipe => {
                return recipe.name.toLowerCase().includes(searchTerm) ||
                       recipe.category.toLowerCase().includes(searchTerm) ||
                       (recipe.source && recipe.source.toLowerCase().includes(searchTerm));
            }) : recipes;

        filteredRecipes = searchFiltered.filter(recipe => recipe.category === category);
        if (viewMode === 'category') {
            displayCategoryView();
        } else {
            displayIndexView();
        }
    }
}

// Apply all active filters (deprecated - kept for compatibility)
function applyFilters() {
    if (viewMode === 'category') {
        displayCategoryView();
    } else {
        displayIndexView();
    }
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

// Mobile Navigation Functions
function toggleMobileNav() {
    const mobileNav = document.getElementById('mobileNav');
    mobileNav.classList.toggle('active');
}

function closeMobileNav() {
    const mobileNav = document.getElementById('mobileNav');
    mobileNav.classList.remove('active');
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
    closeMobileNav();
}

// Header search functionality with live results dropdown
function setupHeaderSearch() {
    const headerSearchInput = document.getElementById('headerSearchInput');
    const headerSearchResults = document.getElementById('headerSearchResults');
    
    if (headerSearchInput && headerSearchResults) {
        headerSearchInput.addEventListener('input', (e) => {
            const searchTerm = e.target.value.toLowerCase().trim();
            
            if (!searchTerm) {
                headerSearchResults.classList.remove('active');
                headerSearchResults.innerHTML = '';
                return;
            }
            
            // Filter recipes based on search term
            const matchingRecipes = recipes.filter(recipe => 
                recipe.name.toLowerCase().includes(searchTerm) ||
                (recipe.category && recipe.category.toLowerCase().includes(searchTerm))
            );
            
            if (matchingRecipes.length > 0) {
                headerSearchResults.innerHTML = matchingRecipes
                    .slice(0, 8) // Limit to 8 results
                    .map(recipe => `
                        <div class="header-search-result-item" onclick="openRecipeFromHeaderSearch(${recipe.id})">
                            <div class="header-search-result-name">${recipe.name}</div>
                            <div class="header-search-result-category">${recipe.category || 'Recipe'}</div>
                        </div>
                    `).join('');
                headerSearchResults.classList.add('active');
            } else {
                headerSearchResults.innerHTML = '<div class="header-search-no-results">No recipes found</div>';
                headerSearchResults.classList.add('active');
            }
        });
        
        // Close dropdown when clicking outside
        document.addEventListener('click', (e) => {
            if (!headerSearchInput.contains(e.target) && !headerSearchResults.contains(e.target)) {
                headerSearchResults.classList.remove('active');
            }
        });
        
        // Clear on escape key
        headerSearchInput.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                headerSearchInput.value = '';
                headerSearchResults.classList.remove('active');
                headerSearchResults.innerHTML = '';
            }
        });
    }
}

// Open recipe from header search dropdown
function openRecipeFromHeaderSearch(recipeId) {
    const recipe = recipes.find(r => r.id === recipeId);
    if (recipe) {
        showRecipeDetail(recipe);
        
        // Clear and hide search results
        const headerSearchInput = document.getElementById('headerSearchInput');
        const headerSearchResults = document.getElementById('headerSearchResults');
        if (headerSearchInput) headerSearchInput.value = '';
        if (headerSearchResults) {
            headerSearchResults.classList.remove('active');
            headerSearchResults.innerHTML = '';
        }
    }
}

// Initialize mobile navigation
document.addEventListener('DOMContentLoaded', () => {
    // Existing initialization
    loadRecipes();
    
    // Mobile nav event listeners
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
    
    // Setup header search
    setupHeaderSearch();
    
    // Setup quick jump navigation
    setupQuickJump();
    
    // Handle cookbook image print checkbox
    const checkbox = document.getElementById('includeCookbookImage');
    const modal = document.getElementById('recipeModal');
    if (checkbox && modal) {
        // Set initial state
        if (checkbox.checked) {
            modal.classList.add('print-include-image');
        }
        // Listen for changes
        checkbox.addEventListener('change', function() {
            if (this.checked) {
                modal.classList.add('print-include-image');
            } else {
                modal.classList.remove('print-include-image');
            }
        });
    }
});

// Quick Jump Navigation
function setupQuickJump() {
    const quickJumpBtn = document.getElementById('quickJumpBtn');
    const quickJumpMenu = document.getElementById('quickJumpMenu');
    const quickJumpClose = document.getElementById('quickJumpClose');
    const quickJumpLinks = document.querySelectorAll('.quick-jump-link');
    
    if (quickJumpBtn && quickJumpMenu) {
        quickJumpBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            quickJumpMenu.classList.toggle('active');
        });
        
        if (quickJumpClose) {
            quickJumpClose.addEventListener('click', () => {
                quickJumpMenu.classList.remove('active');
            });
        }
        
        quickJumpLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = link.getAttribute('data-target');
                
                if (targetId === 'top') {
                    window.scrollTo({
                        top: 0,
                        behavior: 'smooth'
                    });
                } else {
                    scrollToSection(targetId);
                }
                
                quickJumpMenu.classList.remove('active');
            });
        });
        
        // Close when clicking outside
        document.addEventListener('click', (e) => {
            if (!quickJumpMenu.contains(e.target) && 
                !quickJumpBtn.contains(e.target) &&
                quickJumpMenu.classList.contains('active')) {
                quickJumpMenu.classList.remove('active');
            }
        });
    }
}
