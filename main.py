import os
from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

db_path = os.path.join(app.instance_path, 'recipes.db')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

os.makedirs(app.instance_path, exist_ok=True)

db = SQLAlchemy(app)
@app.route('/')
def home():
    num_recipes = Recipe.query.count()
    return render_template("index.html", num_recipes=num_recipes)

    recipes = Recipe.query.all()
class Recipe(db.Model):
    __tablename__ = "recipes"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

def __repr__(self):
    return "Recipe" + str(self.id)

with app.app_context():
    db.create_all()

@app.route("/recipes/", methods=["GET", "POST"])
def recipes():
    if request.method == "POST":
        recipe_title = request.form["title"]
        recipe_description = request.form["description"]
        new_recipe= recipe(title=recipe_title, description=recipe_description, author="Joey")
        db.session.add(new_recipe)
        db.session.commit()
        return redirect("/recipes")
    else:
        all_recipes = Recipe.query.all()
        return render_template("recipes.html", recipes=all_recipes)

@app.route("/recipes/delete/<int:id>/")
def delete(id):
	recipe = Recipe.query.get_or_404(id)
	db.session.delete(recipe)
	db.session.commit()
	return redirect("/recipes/")

@app.route("/recipes/edit/<int:id>/", methods=["GET", "POST"])
def edit(id):
  recipe = Recipe.query.get_or_404(id)
  if request.method == "POST":
    recipe.title = request.form["title"]
    recipe.description = request.form["description"]

    db.session.commit()
    return redirect("/recipes")

  else:
      all_recipes = Recipe.query.all()
      return render_template("edit.html", recipe=recipe)

@app.route("/recipes/new/", methods=["GET", "POST"])
def new_recipe():
    if request.method == "POST":
        recipe_title = request.form["title"]
        recipe_description = request.form["description"]
        recipe = Recipe(title=recipe_title, description=recipe_description, author="Joey")
        db.session.add(recipe)
        db.session.commit()
        return redirect("/recipes")
    else:
        all_recipes = Recipe.query.all()
        return render_template("new_recipe.html", recipes=all_recipes)

if __name__ == '__main__':
    app.run(debug=True, port=8000)