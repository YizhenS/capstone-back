import flask
from flask import request, jsonify
import json
import time
from flask import Response
from flask_cors import CORS


app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True



# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/', methods=['GET'])
def api_all():
	# f = open("data.txt", "r")
	# raw = f.read()
	# data = {
 #        'hello'  : 'world',
 #        'number' : 3
 #    }
	# js = json.dumps(data)
	# resp = Response(response = js, status=200, mimetype='application/json')
	# resp.headers['Link'] = 'http://luisrei.com'

	
		while True:
			f = open("data.txt", "r")
			raw = f.read()
			time.sleep(0.1) 
			temp = list(raw)
			js = json.dumps(temp)
			resp = Response(js, status=200, mimetype='application/json')
			return resp
    
app.run()