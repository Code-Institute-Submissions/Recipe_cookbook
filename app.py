import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_database'
app.config["MONGO_URI"] = 'mongodb://coderguider:JoeyDiaz1@ds127115.mlab.com:27115/recipe_database'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", 
        recipes=mongo.db.recipes.find())
        
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', courses=mongo.db.courses.find())

@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_courses = mongo.db.courses.find()
    return render_template('editrecipe.html', recipe=the_recipe, courses=all_courses)
    
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id' : ObjectId(recipe_id)},
    {
        'recipe_name' : request.form.get('recipe_name'),
        'course_name' : request.form.get('course_name'),
        'recipe_description' : request.form.get('recipe_description'),
        'recipe_ingredients' : request.form.get('recipe_ingredients'),
        'recipe_instructions' : request.form.get('recipe_instructions'),
        'cooking_time' : request.form.get('cooking_time')
    })
    return redirect(url_for('get_recipes'))
    



"""LOGIN/LOGOUT FUNCTIONS"""
# @app.route('/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('lobby'))
#     return "<h1>You are not logged in<h1><h2>Login below to join lobby!</h2>" '''
#         <form method="post">
#             <p><input type=text name=username>
#             <p><input type=submit value=Login>
#         </form>
#     '''

# @app.route('/lobby')
# def lobby():
#     if 'username' in session:
#         return render_template('index.html')
    
    
# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('login'))
    

if __name__=='__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
