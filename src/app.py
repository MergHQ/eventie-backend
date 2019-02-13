from flask import Flask, json, Response, request
from services import event_service
from flask_cors import CORS, cross_origin
import os
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def create_response(data, status = 200):
  return Response(json.dumps(data), status=200, mimetype='application/json')

@app.route('/api/events/upcoming')
def getUpcomingEvents():
  events = event_service.getUpcomingEvents()
  return create_response(events)

@app.route('/api/events/past')
def getPastEvents():
  events = event_service.getPastEvents()
  return create_response(events)

@app.route('/api/events', methods=['POST'])
def createNewEvent():
  data = event_service.createEvent(request.json)
  return create_response(data)

if __name__ == "__main__":
  app.run('0.0.0.0', port=int(os.environ['PORT']) if os.environ['ENV'] == 'production' else 8080, debug=os.environ['ENV'] != 'production')