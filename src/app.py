from flask import Flask, json, Response, request
from services import event_service, user_service, auth_service
from flask_cors import CORS, cross_origin
import jwt
import os
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def create_response(data, status=200):
  return Response(json.dumps(data), status, mimetype='application/json')

@app.route('/api/events/upcoming')
def getUpcomingEvents():
  events = event_service.getUpcomingEvents()
  return create_response(events)

@app.route('/api/events/past')
def getPastEvents():
  events = event_service.getPastEvents()
  return create_response(events)

@app.route('/api/events', methods=['POST'])
@cross_origin()
def createNewEvent():
  data = event_service.createEvent(request.json)
  return create_response(data)

@app.route('/api/users/me')
@cross_origin()
def getUser():
  token = request.headers.get('Authorization')

  if token is None:
    return create_response({'error': 'Unauthorized'}, 401)

  decoded_token = jwt.decode(token, os.environ['JWT_SECRET'], algorithms=['HS256'])

  if decoded_token is None:
    return create_response({'error': 'Unauthorized'}, 401)

  data = user_service.getUser(decoded_token['user_id'])
  return create_response(data)

@app.route('/api/users', methods=['POST'])
@cross_origin()
def createUser():
  if request.json is None or 'username' not in request.json or 'password' not in request.json or 'email' not in request.json or 'name' not in request.json:
    return create_response({'error': 'Invalid post body'}, 400)
  data = user_service.createUser(request.json)
  return create_response(data)

@app.route('/api/auth/login', methods=['POST'])
@cross_origin()
def authUser():
  json = request.json

  if 'username' not in json or 'password' not in json:
    return create_response({'error': 'Invalid post body'}, 400)

  username = json['username']
  password = json['password']
  
  token = auth_service.loginUser(username, password)
  if token is None:
    return create_response({'error': 'Wrong username or password'}, 400)
  
  return create_response(token)


if __name__ == "__main__":
  app.run('0.0.0.0', port=int(os.environ['PORT']) if os.environ['ENV'] == 'production' else 8080, debug=os.environ['ENV'] != 'production')