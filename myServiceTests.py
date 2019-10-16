import requests

# delete all recipes and ingredients
recipes = requests.get('http://localhost:5000/recipes')
recipeIDs = [recipe['id'] for recipe in recipes.json()]
for recipeID in recipeIDs:
    requests.delete('http://localhost:5000/recipes/{}'.format(recipeID))

ingredients = requests.get('http://localhost:5000/ingredients')
ingredientIDs = [ingredient['id'] for ingredient in ingredients.json()]
for ingredientID in ingredientIDs:
    requests.delete('http://localhost:5000/ingredients/{}'.format(ingredientID))


# create ham and cheese sandwich recipe
hamRecipe = {
    'name': 'Ham and cheese sandwich',
    'instructions': 'Put a slice of ham and a slice of cheese between two slices of bread'
}
requests.post('http://localhost:5000/recipes', json=hamRecipe)

# create bacon sandwich recipe
baconSandRecipe = {
    'name': 'Bacon sandwich',
    'instructions': 'Put some bacon and a slice of cheese on a slice of bread, then grill and top with more bread'
}
requests.post('http://localhost:5000/recipes', json=baconSandRecipe)

# create bacon mac recipe
baconMacRecipe = {
    'name': 'Bacon mac and cheese',
    'instructions': 'Cook some pasta, then mix it with cheese and bacon'
}
requests.post('http://localhost:5000/recipes', json=baconMacRecipe)

# create chicken parma ham recipe
baconMacRecipe = {
    'name': 'Bacon mac and cheese',
    'instructions': 'Cook some pasta, then mix it with cheese and bacon'
}

# create chicken parma ham recipe
chickenRecipe = {
    'name': 'Chicken Parma ham',
    'instructions': 'Cut a slit in chicken, stuff with half of the blue cheese. Wrap chicken in parma ham, lay on spinach in casserole dish. Pour over creme fraiche, add nugmeg and remaining blue cheese. Place in preheated oven, 180c for 40 minutes'
}

requests.post('http://localhost:5000/recipes', json=baconMacRecipe)

# create ingredients
requests.post('http://localhost:5000/ingredients', json={'name': 'Ham'})
requests.post('http://localhost:5000/ingredients', json={'name': 'Cheese'})
requests.post('http://localhost:5000/ingredients', json={'name': 'Bread'})
requests.post('http://localhost:5000/ingredients', json={'name': 'Bacon'})
requests.post('http://localhost:5000/ingredients', json={'name': 'Pasta'})
requests.post('http://localhost:5000/ingredients', json={'name': 'Chicken'})
requests.post('http://localhost:5000/ingredients', json={'name': 'Parma ham'})
requests.post('http://localhost:5000/ingredients', json={'name': 'Blue cheese'})
requests.post('http://localhost:5000/ingredients', json={'name': 'Creme fraiche'})
requests.post('http://localhost:5000/ingredients', json={'name': 'Nutmeg'})
requests.post('http://localhost:5000/ingredients', json={'name': 'Spinach'})
requests.post('http://localhost:5000/ingredients', json={'name': 'Potatoes'})

# get IDs for current recipes and ingredients
recipes = requests.get('http://localhost:5000/recipes')
recipeIDMapper = {ingredient['name']: ingredient['id'] for ingredient in recipes.json()}
ingredients = requests.get('http://localhost:5000/ingredients')
ingredientIDMapper = {ingredient['name']: ingredient['id'] for ingredient in ingredients.json()}

# add ingredients to ham and cheese sandwich
hamRecipe['ingredientIDs'] = [ingredientIDMapper[ingName] for ingName in ['Ham', 'Cheese', 'Bread']]
hamID = recipeIDMapper[hamRecipe['name']]
requests.put('http://localhost:5000/recipes/{}'.format(hamID), json=hamRecipe)

# add ingredients to bacon sandwich
baconSandRecipe['ingredientIDs'] = [ingredientIDMapper[ingName] for ingName in ['Bacon', 'Cheese', 'Bread']]
baconSandID = recipeIDMapper[baconSandRecipe['name']]
requests.put('http://localhost:5000/recipes/{}'.format(baconSandID), json=baconSandRecipe)

# add ingredients to bacon mac
baconMacRecipe['ingredientIDs'] = [ingredientIDMapper[ingName] for ingName in ['Bacon', 'Cheese', 'Pasta']]
baconMacID = recipeIDMapper[baconMacRecipe['name']]
requests.put('http://localhost:5000/recipes/{}'.format(baconMacID), json=baconMacRecipe)

# add ingredients to bacon mac
baconMacRecipe['ingredientIDs'] = [ingredientIDMapper[ingName] for ingName in ['Bacon', 'Cheese', 'Pasta']]
baconMacID = recipeIDMapper[baconMacRecipe['name']]
requests.put('http://localhost:5000/recipes/{}'.format(baconMacID), json=baconMacRecipe)


print('===Getting all recipes===')
allRecipes = requests.get('http://localhost:5000/recipes').json()
for recipe in allRecipes:
    print(recipe)

print('===Getting bacon sandwich recipe===')
print(requests.get('http://localhost:5000/recipes/{}'.format(baconSandID)).json())

print('===Deleting bacon sandwich recipe===')
print(requests.delete('http://localhost:5000/recipes/{}'.format(baconSandID)).json())

print('===Getting all recipes===')
allRecipes = requests.get('http://localhost:5000/recipes').json()
for recipe in allRecipes:
    print(recipe)

print('===Getting all ingredients===')
allIngredients = requests.get('http://localhost:5000/ingredients').json()
for ingredient in allIngredients:
    print(ingredient)

print('===Getting cheese===')
print(requests.get('http://localhost:5000/ingredients/{}'.format(ingredientIDMapper['Cheese'])).json())

print('===Deleting cheese===')
print(requests.delete('http://localhost:5000/ingredients/{}'.format(ingredientIDMapper['Cheese'])).json())

print('===Getting all ingredients===')
allIngredients = requests.get('http://localhost:5000/ingredients').json()
for ingredient in allIngredients:
    print(ingredient)

print('===Getting ham and cheese sandwich recipe===')
print(requests.get('http://localhost:5000/recipes/{}'.format(hamID)).json())
