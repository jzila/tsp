from flask import (
    Flask,
    request,
)
import json
from graph.Point2D import Point2D

app = Flask(__name__)

def as_point(dct):
    if 'x' in dct and 'y' in dct:
        return Point2D(dct['x'], dct['y'])
    return None

@app.route('/hull/', methods=['POST'])
def hull(points):
    return "hull"

@app.route('/tsp/', methods=['POST'])
def tsp():
    points_array = request.get_json()
    points = [Point2D(p['x'], p['y']) for p in points_array]
    return "TSP"


if __name__ == '__main__':
    app.run()
