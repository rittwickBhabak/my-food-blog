# from myproject import app, db 
from myproject import app
from flask import render_template, redirect, flash 

@app.route('/')
def index():
    return render_template('recipe-list.html')

@app.route('/new-recipe')
def new_recipe():
    return render_template('new-recipe.html')

@app.route('/recipe/<int:id>')
def recipe(id):
    return render_template('recipe-details.html',id=id)


if __name__ == "__main__":
    app.run(debug=True)