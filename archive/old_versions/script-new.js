// Global variables
let recipes = [];
let filteredRecipes = [];
let recipeData = null;
let viewMode = 'category'; // 'category' or 'index'

// Load recipes from JSON file
async function loadRecipes() {
    try {
        const response = await fetch('recipes.json');
        const data = await response.json();
        recipeData = data;
        
        // Flatten recipes into array with metadata
        recipes = [];
        let id = 0;
        
        if (Array.isArray(data)) {
            // Handle flat array format
            recipes = data.map(recipe => ({ ...recipe, id: id++ }));
        } else if (data.categories) {
            // Handle category-based format
            data.categories.forEach(category => {
                category.recipes.forEach(recipeObj => {
                    const original = recipeObj.original_recipe;
                    const improved = recipeObj.improved_recipe;
                    
                    // Use improved as main recipe if available, otherwise original
                    const recipe = improved || original;
                    recipe.id = id++;
                    recipe._original = original;
                    recipe._improved = improved;
                    recipe._hasOriginal = !!original;
                    recipe._hasImproved = !!improved;
                    
                    recipes.push(recipe);
                });
            });
        }
        
        filteredRecipes = [...recipes];
        displayCategoryView();
        populateCategoryFilter();
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
