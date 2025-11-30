# MeeMaw Recipe Scripts

This folder contains utility scripts for managing the MeeMaw Recipe cookbook.

## Active Scripts

### `compare_recipes.py`
Compares the current `recipes.json` against the approved recipe list to identify:
- Duplicate recipes that need to be removed
- Recipes in the file but not on the approved list
- Recipes on the approved list but missing from the file
- Net changes needed to reach exactly 112 recipes

**Usage:**
```bash
python compare_recipes.py
```

### `count_recipes.py`
Counts and displays the total number of recipes and the breakdown by category.

**Usage:**
```bash
python count_recipes.py
```

**Output:**
- Total recipe count
- Number of recipes in each of the 14 categories

### `list_recipes.py`
Lists all recipe names in the current `recipes.json` file, organized by category.

**Usage:**
```bash
python list_recipes.py
```

## Backup Files

### `recipes_backup_before_cleanup.json`
Backup of the original 109-recipe state before cleanup and systematic batch additions began.

### `recipes_final_112.json`
Final backup of the completed 112-recipe collection (matches current `recipes.json`).

## Archived Scripts

All completed batch processing scripts and temporary utilities have been moved to `scripts_archive/`:
- Batch addition scripts (add_batch_1a.py through add_batch_3a.py)
- Name fixing and cleanup scripts
- Integration and build scripts
- Old backup files

These are preserved for reference but are no longer needed for day-to-day operations.

## Current Recipe Status

✅ **112 recipes** - Complete and verified against approved list
- All recipes have dual-version format (original + improved)
- Full metric conversions included
- 14 categories properly organized
- Zero discrepancies with approved list

---

*Last updated: November 30, 2025*
