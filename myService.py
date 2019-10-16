from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import flask_marshmallow
import cPickle as cP
import DBModels

# trying to avoid saving the password in plain text
with open('config') as f:
   passw = cP.load(f)

# initialise flask and database libraries
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ben:{}@localhost/recipeBook'.format(passw)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#ma = flask_marshmallow.Marshmallow(app)

# Init schemas, to represent the single and plural of each data model
recipeSchema = DBModels.RecipeSchema(strict=True)
recipesSchema = DBModels.RecipeSchema(strict=True, many=True)
ingredientSchema = DBModels.IngredientSchema(strict=True)
ingredientsSchema = DBModels.IngredientSchema(strict=True, many=True)

# abstracting the database commit and exception handling
def commit_to_db(db):
    try:
        db.session.commit()
    except Exception as e:
        print('An error occured when committing a change to the database')
        raise e

# generic get all function
def handleGetAll(modelClass, schema):
    result = recipesSchema.dump(db.session.query(modelClass).all())
    return jsonify(result.data)

# Recipe routing
# Create a recipe
@app.route('/recipes', methods=['POST'])
def add_recipe():
    newRecipe = DBModels.Recipe(request.json['name'], request.json['instructions'])
    db.session.add(newRecipe)
    commit_to_db(db)
    return recipeSchema.jsonify(newRecipe), 201

# Get all recipes
@app.route('/recipes', methods=['GET'])
def get_recipes():
    return handleGetAll(DBModels.Recipe, recipesSchema)

# Get single recipe
@app.route('/recipes/<id>', methods=['GET'])
def get_recipe(id):
    return recipeSchema.jsonify(db.session.query(DBModels.Recipe).get(id))

# Edit a recipe. This is also where ingredients can be added to recipes via their ID
@app.route('/recipes/<id>', methods=['PUT'])
def update_recipes(id):
    recipe = db.session.query(DBModels.Recipe).get(id)
    recipe.name = request.json['name']
    recipe.instructions = request.json['instructions']
    ingredientIDs = request.json['ingredientIDs']
    recipe.ingredients = [db.session.query(DBModels.Ingredient).get(ingID) for ingID in ingredientIDs]

    commit_to_db(db)
    return recipeSchema.jsonify(recipe)

# Delete a recipe
# This will also remove the recipe from the 'recipes' list of ingredients which are included in it
@app.route('/recipes/<id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = db.session.query(DBModels.Recipe).get(id)
    db.session.delete(recipe)
    commit_to_db(db)
    return recipeSchema.jsonify(recipe), 202

# Ingredient routing
# Creating an ingredient
@app.route('/ingredients', methods=['POST'])
def add_ingredient():
    newIngredient = DBModels.Ingredient(request.json['name'])
    db.session.add(newIngredient)
    commit_to_db(db)
    return ingredientSchema.jsonify(newIngredient), 201

# Get all ingredients
@app.route('/ingredients', methods=['GET'])
def get_ingredients():
    return handleGetAll(DBModels.Ingredient, ingredientsSchema)

# Get single ingredient
@app.route('/ingredients/<id>', methods=['GET'])
def get_ingredient(id):
    return ingredientSchema.jsonify(db.session.query(DBModels.Ingredient).get(id))

# Editing an ingredient
@app.route('/ingredients/<id>', methods=['PUT'])
def update_ingredient(id):
    ingredient = db.session.query(DBModels.Ingredient).get(id)
    ingredient.name = request.json['name']
    commit_to_db(db)
    return ingredientSchema.jsonify(ingredient)

# Deleting an ingredient
# This will also remove the ingredient from the 'ingredients' list of the receipes which include it
@app.route('/ingredients/<id>', methods=['DELETE'])
def delete_ingredient(id):
    ingredient = db.session.query(DBModels.Ingredient).get(id)
    db.session.delete(ingredient)
    commit_to_db(db)
    return ingredientSchema.jsonify(ingredient), 202

if __name__ == '__main__':
    # debug=True should only be used during development
    app.run(debug=True)
