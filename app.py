from flask import Flask, request, jsonify
from dbcreds import *
from helpers.dbhelpers import run_query

app = Flask(__name__)

import sys


@app.get('/api/animals')
def animals_get():
    #todo: db select
    animal_list= run_query("SELECT * FROM animal")
    resp = []
    for animal in animal_list:
        an_obj = {}
        an_obj['animalId'] = animal[0]
        an_obj['animalName'] = animal[1]
        an_obj['imageURL'] = animal[2]
        resp.append(an_obj)
    return jsonify(animal_list), 200

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
    run_query("INSERT INTO animal (name, image_url) VALUES(?,?)", [animal_name, image_url])
    return jsonify("Animal added"), 201



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