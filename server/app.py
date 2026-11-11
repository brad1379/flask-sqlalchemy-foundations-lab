# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

@app.route('/earthquakes/<int:id>')
def get_earthquake(id):
    # Query specific earthquake based on id
    earthquake = Earthquake.query.filter(Earthquake.id == id).first()

    # Ensure it's a valid query and return the body else return no earthquake found
    if earthquake:
        body = {
            'id': earthquake.id,
            'magnitude': earthquake.magnitude,
            'location': earthquake.location,
            'year': earthquake.year
        }
        status = 200
    else:
        body = {
            'message': f'Earthquake {id} not found.'
        }
        status = 404

    return make_response(body, status)


@app.route('/earthquakes/magnitude/<magnitude>')
def get_earthquakes(magnitude):
    magnitude = float(magnitude) # converts the magnitude number into a float incase an integer is used
    earthquakes = [] 

    # Get all earthquakes above specified magnitude
    earthquakes_query = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    # Loop through all the earthquakes in the query and add them to a dictionary that then appends to a list
    for eq in earthquakes_query:
        earthquake_dict = {
            'id': eq.id, 
            'magnitude': eq.magnitude, 
            'location': eq.location, 
            'year': eq.year
            }
        earthquakes.append(earthquake_dict)

    # Return the count and the earthquakes within the list
    body = {'count': len(earthquakes), 'quakes': earthquakes}
    return make_response(body,200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
