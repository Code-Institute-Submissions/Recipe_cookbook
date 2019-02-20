import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipe_database'
app.config["MONGO_URI"] = 'mongodb://coderguider:JoeyDiaz1@ds127115.mlab.com:27115/recipe_database'

mongo = PyMongo(app)



################ RECIPE DATABASE #############
@app.route('/')
@app.route('/all_recipes')
def all_recipes():
    return render_template("allrecipes.html", 
        recipes=mongo.db.recipes.find())
        
        
################## MY RECIPES #################

@app.route('/myrecipes')
def myrecipes():
    if 'username' in session:
        return render_template("myrecipes.html", 
        myrecipes=mongo.db.myrecipes.find())
    return redirect(url_for('login'))
        
@app.route('/add_recipe')
def add_recipe():
    if 'username' in session:
        return render_template('addrecipe.html', courses=mongo.db.courses.find())
    return redirect(url_for('login'))

@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipes = mongo.db.myrecipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('myrecipes'))
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    if 'username' in session:
        the_recipe = mongo.db.myrecipes.find_one({"_id": ObjectId(recipe_id)})
        all_courses = mongo.db.courses.find()
        return render_template('editrecipe.html', recipe=the_recipe, courses=all_courses)
    return redirect(url_for('login'))    
    
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.myrecipes
    recipes.update( {'_id' : ObjectId(recipe_id)},
    {
        'recipe_name' : request.form.get('recipe_name'),
        'course_name' : request.form.get('course_name'),
        'recipe_description' : request.form.get('recipe_description'),
        'recipe_ingredients' : request.form.get('recipe_ingredients'),
        'recipe_instructions' : request.form.get('recipe_instructions'),
        'cooking_time' : request.form.get('cooking_time'),
        'preparation_time' : request.form.get('preparation_time'),
        'serves' : request.form.get('serves')
    })
    return redirect(url_for('myrecipes'))
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.myrecipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('myrecipes'))
    
    
########### RECIPE DETAIL ##########

@app.route('/recipe_detail/<recipe_id>', methods=['GET', 'POST'])
def recipe_detail(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipedetail.html', recipe=the_recipe)




######### SAVED RECIPES ###########


@app.route('/saved_recipes')
def saved_recipes():
    if 'username' in session:
        return render_template("savedrecipes.html", 
        saved_recipes=mongo.db.saved_recipes.find())
    return redirect(url_for('login'))

@app.route('/add_saved_recipe/<recipe_id>', methods=["GET"])
def add_saved_recipe(recipe_id):
    recipes = mongo.db.recipes
    savedrecipe = mongo.db.saved_recipes
    recipe_id = recipes.find_one({"_id": ObjectId(recipe_id)})
    savedrecipe.insert_one(recipe_id)
    if 'username' in session:
        return redirect(url_for('saved_recipes'))
    return redirect(url_for('login'))


############ Courses ##########    
    
@app.route('/get_courses')
def get_courses():
    return render_template('courses.html',
        courses=mongo.db.courses.find())    
        

########## login #########

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('myrecipes'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('all_recipes'))
    
######### runpage #########

if __name__=='__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
