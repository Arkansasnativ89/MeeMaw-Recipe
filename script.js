// Global variables
let recipes = [];
let filteredRecipes = [];
let useImprovedRecipes = true; // Toggle for original vs improved recipes

// Load recipes from JSON file
async function loadRecipes() {
    try {
        const response = await fetch('recipes.json');
        const data = await response.json();
        
        // Handle both flat array and category-based structure
        if (Array.isArray(data)) {
            // Flat array format (legacy)
            recipes = data;
        } else if (data.categories) {
            // Category-based format with original/improved recipes
            recipes = [];
            data.categories.forEach(category => {
                category.recipes.forEach(recipeGroup => {
                    // Use improved recipe if available and preference is set, otherwise use original
                    const recipe = useImprovedRecipes && recipeGroup.improved_recipe 
                        ? { ...recipeGroup.improved_recipe, id: recipes.length + 1, _hasOriginal: !!recipeGroup.original_recipe }
                        : { ...recipeGroup.original_recipe, id: recipes.length + 1, _hasImproved: !!recipeGroup.improved_recipe };
                    recipes.push(recipe);
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

// Show recipe detail in modal
function showRecipeDetail(recipe) {
    const modal = document.getElementById('recipeModal');
    const detailDiv = document.getElementById('recipeDetail');

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

    detailDiv.innerHTML = `
        <h2>${recipe.name}</h2>
        ${categoryBadge}
        ${sourceLine}
        ${metaInfo}
        ${ingredientsList}
        ${instructionsList}
        ${shapingMethods}
        ${notesSection}
    `;

    modal.style.display = 'block';
    document.body.style.overflow = 'hidden'; // Prevent background scrolling
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
    window.print();
}
