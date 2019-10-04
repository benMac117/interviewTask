from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import cPickle as cP
import DBModels

from sqlalchemy import Table, Column, Integer, ForeignKey, String

app = Flask(__name__)

# trying to avoid saving the password in plain text
with open('config') as f:
   passw = cP.load(f)

# I think ideally this should have a different user
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ben:{}@localhost/recipeBook'.format(passw)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)


# The first time this is run on a machine we need to run db.create_all() to create the tables in the database
# Create a table of links to hold the mabny-to-many relationship between recipes and ingredients
used = db.Table('used',
    db.Column('recipeID', Integer, db.ForeignKey('Recipe.id')),
    db.Column('ingredientID', Integer, db.ForeignKey('Ingredient.id')),
)

class Recipe(db.Model):
    __tablename__ = 'Recipe'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    instructions = Column(String(200))
    ingredients = db.relationship('Ingredient', secondary=used, backref=db.backref('recipes', lazy='dynamic'))

    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions

    def add_ingredients(ingredientList):
        self.ingredients = ingredientList

class Ingredient(db.Model):
    __tablename__ = 'Ingredient'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)

    def __init__(self, name):
        self.name = name

# model schemas
class RecipeSchema(ma.Schema):
    ingredients = ma.Nested('IngredientSchema', many=True, exclude=("recipes",))
    class Meta:
        fields = ('id', 'name', 'instructions', 'ingredients')

class IngredientSchema(ma.Schema):
    recipes = ma.Nested(RecipeSchema, many=True)
    class Meta:
        fields = ('id', 'name', 'recipes')

# Init schemas, to represent the single and plural of each data model
recipeSchema = RecipeSchema(strict=True)
recipesSchema = RecipeSchema(strict=True, many=True)
ingredientSchema = IngredientSchema(strict=True)
ingredientsSchema = IngredientSchema(strict=True, many=True)

def commit_to_db(db):
    try:
        db.session.commit()
    except Exception as e:
        print('An error occured when committing a change to the database')
        raise e

# generic CRUD operations
def handleGetAll(modelClass, schema):
    result = recipesSchema.dump(modelClass.query.all())
    return jsonify(result.data)

# Recipe routing
# Create a recipe
@app.route('/recipes', methods=['POST'])
def add_recipe():
    newRecipe = Recipe(request.json['name'], request.json['instructions'])
    db.session.add(newRecipe)
    commit_to_db(db)
    return recipeSchema.jsonify(newRecipe), 201

# Get all recipes
@app.route('/recipes', methods=['GET'])
def get_recipes():
    return handleGetAll(Recipe, recipesSchema)

# Get single recipe
@app.route('/recipes/<id>', methods=['GET'])
def get_recipe(id):
    return recipeSchema.jsonify(Recipe.query.get(id))

@app.route('/recipes/<id>', methods=['PUT'])
def update_recipes(id):
    recipe = Recipe.query.get(id)
    recipe.name = request.json['name']
    recipe.instructions = request.json['instructions']
    ingredientIDs = request.json['ingredientIDs']
    recipe.ingredients = [Ingredient.query.get(ingID) for ingID in ingredientIDs]

    db.session.commit()
    return recipeSchema.jsonify(recipe)

@app.route('/recipe/<id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()

    return product_schema.jsonify(product), 202

# Ingredient routing
@app.route('/ingredients', methods=['POST'])
def add_ingredient():
    newIngredient = Ingredient(request.json['name'])
    db.session.add(newIngredient)
    commit_to_db(db)
    return ingredientSchema.jsonify(newIngredient), 201

# Get all ingredient
@app.route('/ingredients', methods=['GET'])
def get_ingredients():
    return handleGetAll(Ingredient, ingredientsSchema)

# Get single ingredient
@app.route('/ingredients/<id>', methods=['GET'])
def get_ingredient(id):
    return ingredientsSchema.jsonify(Ingredient.query.get(id))

@app.route('/ingredients/<id>', methods=['PUT'])
def update_product(id):
    ingredient = Ingredient.query.get(id)
    ingredient.name = request.json['name']
    
    db.session.commit()
    return recipeSchema.jsonify(ingredient)

@app.route('/ingredients/<id>', methods=['DELETE'])
def delete_recipe(id):
    ingredient = Ingredient.query.get(id)
    db.session.delete(ingredient)
    db.session.commit()

    return product_schema.jsonify(product), 202

if __name__ == '__main__':
    # debug=True should only be used during development
    app.run(debug=True)
