from flask import  Flask, request, make_response, Response, send_from_directory
from graph.algorithms import hull_from_points, tsp_from_points
from graph.structs import Point, StructEncoder, GraphError

import json

app = Flask(__name__)

def graphCallWrapper(f):
    try:
        points = [Point(p[0], p[1]) for p in request.get_json()]
        js = json.dumps(f(points), cls=StructEncoder)
    except Exception as e:
        js = json.dumps({
            'error': {
                'type': type(e).__name__,
                'message': str(e)
            }
        })
    return Response(js, mimetype="application/json")


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/hull/', methods=['POST'])
def hull():
    return graphCallWrapper(hull_from_points)


@app.route('/tsp/', methods=['POST'])
def tsp():
    return graphCallWrapper(tsp_from_points)


if __name__ == '__main__':
    app.run(debug=True)
