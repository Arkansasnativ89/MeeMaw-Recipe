import json

with open('recipes.json', encoding='utf-8') as f:
    data = json.load(f)

total = sum(len(c['recipes']) for c in data['categories'])
print(f'Total recipes: {total}')
print('\nRecipes by category:')
for c in data['categories']:
    print(f"  {c['name']}: {len(c['recipes'])}")
