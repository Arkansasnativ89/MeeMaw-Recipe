// Global variables
let recipes = [];
let filteredRecipes = [];

// Load recipes from JSON file
async function loadRecipes() {
    try {
        const response = await fetch('recipes.json');
        recipes = await response.json();
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
    const sourceLine = recipe.source ? `<p class="detail-source">Recipe from: ${recipe.source}</p>` : '';
    const servingsLine = recipe.servings ? `<p class="detail-servings">Servings: ${recipe.servings}</p>` : '';

    // Check if recipe has a table format for ingredients
    let ingredientsList = '';
    if (recipe.hasTable && recipe.ingredientTable) {
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
    } else if (recipe.ingredients.length > 0) {
        ingredientsList = `<h3>Ingredients</h3><ul>${recipe.ingredients.map(ing => `<li>${ing}</li>`).join('')}</ul>`;
    }

    const instructionsList = recipe.instructions.length > 0
        ? `<h3>Instructions</h3><ol>${recipe.instructions.map(inst => `<li>${inst}</li>`).join('')}</ol>`
        : '<p><em>Instructions not available for this recipe.</em></p>';

    detailDiv.innerHTML = `
        <h2>${recipe.name}</h2>
        ${categoryBadge}
        ${sourceLine}
        ${servingsLine}
        ${ingredientsList}
        ${instructionsList}
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
        return recipe.name.toLowerCase().includes(lowerSearchTerm) ||
               recipe.category.toLowerCase().includes(lowerSearchTerm) ||
               (recipe.source && recipe.source.toLowerCase().includes(lowerSearchTerm)) ||
               recipe.ingredients.some(ing => ing.toLowerCase().includes(lowerSearchTerm)) ||
               recipe.instructions.some(inst => inst.toLowerCase().includes(lowerSearchTerm));
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
