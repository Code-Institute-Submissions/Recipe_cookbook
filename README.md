# CREATE AN ONLINE COOKBOOK

## Brief

Create a web application that allows users to store and easily access cooking recipes.

## Technologies

1. Python 
2. HTML 
3. Materialize CSS - Grid System, Cards, Buttons, Fonts + Icons
4. Javascript - jQuery
3. Flask Framework
4. Pymongo
5. MongoDB

## Features

1. Simple Login feature
2. Users have the ability to view existing recipes by official authors
3. Users can save those recipes to their own collection
4. Users have the ability to create their own recipes, read those recipes, update those recipes and delete those recipes


## Testing
Manual testing was undertaken for this application and satisfactorily passed. Tests were conducted as follows: 
1. Unit testing - Tested small chunks of the code as I progressed to ensure the code is functioning
2. Integration testing - Tested combinations of units to ensure new code doesn't interfere with existing code
3. Acceptance testing — Tested the application in sevreal different browsers and devices to analyze the performance of the entire application.
4. Code which was credited, was tested as the example given, then modified for desired outcome


## Design
Built primarily off the mini project example as basic framework. Website layout was implemented with Flask and custom styled with Materialize. I liked the idea of having official recipes that the user cannot edite but rather can save them as they are. The user still has the ability however to create, read, update and delete their own created recipes.

## Deployment
* Download the project files to your computer
* Connect to the database: user: password:<JoeyDiaz1>
    * export MONGO_URI=mongodb://coderguider:JoeyDiaz1@ds127115.mlab.com:27115/recipe_database  
    * python3 new_mongo.py

You can see the application [here](https://coderguider.github.io/Recipe_cookbook/).

## Credits

**Conor Guider** - This project was completed as part of Code Institute's Full Stack Web Development course.

### Media
* Official recipes were taken from BBC Food website as well as bg img
* Styling was from materialize and Material Design for icons

### Acknowledgments
* Resources - Codedrops, Stackoverflow, Materialize
