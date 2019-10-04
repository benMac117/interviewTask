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
        print('An error occured when committing change to the database')
        print(e)

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
    allRecipes = Recipe.query.all()
    result = recipesSchema.dump(allRecipes)
    return jsonify(result.data)

# Get single recipe
@app.route('/recipes/<id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get(id)
    return recipeSchema.jsonify(recipe)

@app.route('/recipes/<id>', methods=['PUT'])
def update_recipes(id):
    recipe = Recipe.query.get(id)

    recipe.name = request.json['name']
    recipe.instructions = request.json['instructions']
    ingredientIDs = request.json['ingredientIDs']
    #from IPython import embed; embed()
    recipe.ingredients = [Ingredient.query.get(ingID) for ingID in ingredientIDs]

    db.session.commit()

    return recipeSchema.jsonify(recipe)

# Ingredient routing
@app.route('/ingredients', methods=['POST'])
def add_ingredient():
    newIngredient = Ingredient(request.json['name'])
    db.session.add(newIngredient)
    commit_to_db(db)
    print(newIngredient)
    return ingredientSchema.jsonify(newIngredient), 201

# Get all recipes
@app.route('/ingredients', methods=['GET'])
def get_ingredients():
    allIngredients = Ingredient.query.all()
    result = ingredientsSchema.dump(allIngredients)
    return jsonify(result.data)
'''
# Update a product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)

    product.name = request.json['name']
    product.description = request.json['description']
    product.price = request.json['price']
    product.qty = request.json['qty']

    db.session.commit()

    return product_schema.jsonify(product)

# Delete product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product), 202

'''
if __name__ == '__main__':
    # debug=True should only be used during development
    app.run(debug=True)