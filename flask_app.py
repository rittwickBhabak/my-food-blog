# from myproject import app, db
from myproject import app, filepath, db
from flask import render_template, redirect, flash, request, url_for
from sqlalchemy import desc
from myproject.forms import NewRecipe, EditRecipe
from myproject.models import Recipes
from werkzeug.utils import secure_filename

import os

@app.route('/')
def index():
    recipes = Recipes.query.all()
    list_of_recipes = []
    for recipe in recipes:
        id = recipe.id
        name = recipe.name
        thumb_image = os.path.join('static','recipe_images',recipe.images.split('|')[0])
        list_of_recipes.append([id, name, thumb_image])
    return render_template('recipe-list.html', list_of_recipes=list_of_recipes)


@app.route('/new-recipe', methods=["GET", "POST"])
def new_recipe():
    form = NewRecipe()
    if form.validate_on_submit():
        name = form.name.data
        steps = form.steps.data
        ingredients = form.ingredients.data
        images = []
        if form.image0.data:
            form.image0.data.save(os.path.join(filepath,name.replace(' ','_')+secure_filename(form.image0.data.filename)))
            images.append(name.replace(' ','_')+secure_filename(form.image0.data.filename))
        if form.image1.data:
            form.image1.data.save(os.path.join(filepath,name.replace(' ','_')+secure_filename(form.image1.data.filename)))
            images.append(name.replace(' ','_')+secure_filename(form.image1.data.filename))
        if form.image2.data:
            form.image2.data.save(os.path.join(filepath,name.replace(' ','_')+secure_filename(form.image2.data.filename)))
            images.append(name.replace(' ','_')+secure_filename(form.image2.data.filename))
        if form.image3.data:
            form.image3.data.save(os.path.join(filepath,name.replace(' ','_')+secure_filename(form.image3.data.filename)))
            images.append(name.replace(' ','_')+secure_filename(form.image3.data.filename))
        if form.image4.data:
            form.image4.data.save(os.path.join(filepath,name.replace(' ','_')+secure_filename(form.image4.data.filename)))
            images.append(name.replace(' ','_')+secure_filename(form.image4.data.filename))
        if form.image5.data:
            form.image5.data.save(os.path.join(filepath,name.replace(' ','_')+secure_filename(form.image5.data.filename)))
            images.append(name.replace(' ','_')+secure_filename(form.image5.data.filename))
        if form.image6.data:
            form.image6.data.save(os.path.join(filepath,name.replace(' ','_')+secure_filename(form.image6.data.filename)))
            images.append(name.replace(' ','_')+secure_filename(form.image6.data.filename))
        if form.image7.data:
            form.image7.data.save(os.path.join(filepath,name.replace(' ','_')+secure_filename(form.image7.data.filename)))
            images.append(name.replace(' ','_')+secure_filename(form.image7.data.filename))
        if form.image8.data:
            form.image8.data.save(os.path.join(filepath,name.replace(' ','_')+secure_filename(form.image8.data.filename)))
            images.append(name.replace(' ','_')+secure_filename(form.image8.data.filename))
        if form.image9.data:
            form.image9.data.save(os.path.join(filepath,name.replace(' ','_')+secure_filename(form.image9.data.filename)))
            images.append(name.replace(' ','_')+secure_filename(form.image9.data.filename))
        images = '|'.join(images)
        db.session.add(Recipes(name, ingredients, steps, images))
        db.session.commit()
        flash('Recipe added successfully', 'success')
        id = Recipes.query.order_by(desc(Recipes.id)).first().id
        return redirect(url_for('recipe', id=id))
    return render_template('new-recipe.html', form=form)

@app.route('/recipe/<int:id>')
def recipe(id):
    recipe = Recipes.query.get(id)
    name = recipe.name
    ingredients = recipe.ingredients.split('\n')
    steps = recipe.steps.split('\n')
    images = list(map(lambda x: os.path.join('static','recipe_images',x), recipe.images.split('|')))
    return render_template('recipe-details.html',name=name, ingredients=ingredients, steps=steps, images=images,length=len(images),id=id)

@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    form = EditRecipe()
    # image0, image1, image2, image3, image4, image5, image6, image7, image8, image9 = recipe.images.split('|')
    # images = list(map(lambda x: os.path.join('static','recipe_images',x), recipe.images.split('|')))
    print(form.validate_on_submit())
    if form.validate_on_submit():
        name = form.name.data
        steps = form.steps.data
        ingredients = form.ingredients.data
        recipe = Recipes.query.get(id)
        recipe.name = form.name.data
        recipe.steps = form.steps.data
        recipe.ingredients = form.ingredients.data
        db.session.add(recipe)
        db.session.commit()
        flash('Update successful')
        return redirect(url_for('recipe', id=id))
    recipe = Recipes.query.get(id)
    name = recipe.name
    ingredients = recipe.ingredients
    steps = recipe.steps
    images = list(map(lambda x: os.path.join('static','recipe_images',x), recipe.images.split('|')))
    form.name.data = name
    form.ingredients.data = ingredients
    form.steps.data = steps
    return render_template('edit.html',form=form,id=id,images=images)
# if __name__ == "__main__":
    # app.run(debug=True)