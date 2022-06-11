from flask import Flask, request, jsonify
from dbcreds import *
from helpers.dbhelpers import run_query

app = Flask(__name__)

import sys



@app.post('/api/animals')
def animals_post():
    data = request.json
    animal_name=data.get('animalName')
    image_url=data.get('imageUrl')
    # if animal name == None - this is equivalent to below
    if not animal_name:
        return jsonify("Missing required argument 'animalName'"), 422
    if not image_url:
        return jsonify("Missing required argument 'imageUrl'"), 422
    # TODO: Error checking the actual values for the arguments
    #TODO: DB write
    return jsonify("Animal added"), 201



@app.get('/api/animals')
def animals_get():
    #todo: db select
    animal_list=[]
    return jsonify(animal_list), 200


if (len(sys.argv)>1):
    mode = sys.argv[1]
else:
    print("No mode argument, must pass a mode")
    exit()
    
if mode == "testing":
    from flask_cors import CORS
    CORS(app)
    app.run(debug=True)
elif mode == "production":
    import bjoern
    print("Running in production mode!")
    bjoern.run(app, "0.0.0.0", 5000)
else:
    print("Invalid mode, must be one of: testing|production")
    exit() 

app.run(debug=True)