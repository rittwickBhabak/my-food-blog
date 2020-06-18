from myproject import db   
class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    steps = db.Column(db.String)
    images = db.Column(db.String)
    def __init__(self,name,ingredients,steps,images):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.images = images
