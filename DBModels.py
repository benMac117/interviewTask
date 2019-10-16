from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import flask_marshmallow

Base = declarative_base()
# The first time this is run on a machine we need to run db.create_all() to create the tables in the database
# creating a table of links to hold the many-to-many relationship between recipes and ingredients
used = Table('used', Base.metadata,
    Column('recipeID', Integer, ForeignKey('Recipe.id')),
    Column('ingredientID', Integer, ForeignKey('Ingredient.id')),
)

# class for the recipe model
class Recipe(Base):
    __tablename__ = 'Recipe'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    instructions = Column(String(200))
    ingredients = relationship('Ingredient', secondary=used, backref=backref('recipes', lazy='dynamic'))

    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions

    def add_ingredients(ingredientList):
        self.ingredients = ingredientList

# class for the ingredient model
class Ingredient(Base):
    __tablename__ = 'Ingredient'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)

    def __init__(self, name):
        self.name = name

# model schemas - allow easy transport through JSON
class RecipeSchema(flask_marshmallow.Schema):
    # these nested specifications are required to prevent infinite recursion in the many-to-many relationship
    ingredients = flask_marshmallow.fields.fields.Nested('IngredientSchema', many=True, exclude=("recipes",))
    class Meta:
        fields = ('id', 'name', 'instructions', 'ingredients')

class IngredientSchema(flask_marshmallow.Schema):
    recipes = flask_marshmallow.fields.fields.Nested(RecipeSchema, many=True)
    class Meta:
        fields = ('id', 'name', 'recipes')