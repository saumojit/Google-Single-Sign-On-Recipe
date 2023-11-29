import flask
from flask_cors import CORS
from flask import request , jsonify
import requests


app = flask.Flask(__name__)
cors = CORS(app)
app.config['SECRET_KEY'] = '777'
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/jwttoken' , methods=['POST'])
def test_api_request():
    print("Backend :  test_api_request () ")
    endpoint = "https://www.googleapis.com/oauth2/v1/userinfo"
    requested_data_from_react=request.json.get('google_access_token', None)
    google_access_token=requested_data_from_react["access_token"]
    params = {"access_token": google_access_token }
    response = requests.get(endpoint, params=params, headers={'Content-type': 'application/json'})
    print("test_api_request() => Response.Json() : " , response.json())
    return jsonify(response.json())



if(__name__ == "__main__"):
    app.run('localhost', 8080, debug=True)
