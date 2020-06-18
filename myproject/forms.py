from wtforms import StringField, SubmitField, FileField, TextAreaField, FileField
from flask_wtf import FlaskForm

class NewRecipe(FlaskForm):
    name = StringField('Recipe Name')
    ingredients = TextAreaField('Ingredients')
    steps = TextAreaField('Steps')
    image0 = FileField('Thumbnail image')
    image1 = FileField('Slide Show Image')
    image2 = FileField('Slide Show Image')
    image3 = FileField('Slide Show Image')
    image4 = FileField('Slide Show Image')
    image5 = FileField('Slide Show Image')
    image6 = FileField('Slide Show Image')
    image7 = FileField('Slide Show Image')
    image8 = FileField('Slide Show Image')
    image9 = FileField('Slide Show Image')
    submit = SubmitField('Add recipe')


class EditRecipe(FlaskForm):
    name = StringField('Recipe Name')
    ingredients = TextAreaField('Ingredients')
    steps = TextAreaField('Steps')
    image0 = FileField('Thumbnail image')
    image1 = FileField('Slide Show Image')
    image2 = FileField('Slide Show Image')
    image3 = FileField('Slide Show Image')
    image4 = FileField('Slide Show Image')
    image5 = FileField('Slide Show Image')
    image6 = FileField('Slide Show Image')
    image7 = FileField('Slide Show Image')
    image8 = FileField('Slide Show Image')
    image9 = FileField('Slide Show Image')
    submit = SubmitField('Update recipe')
