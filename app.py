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
def get_tasks():
    return render_template("recipes.html", 
        recipes=mongo.db.recipes.find())


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
