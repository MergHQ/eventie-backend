from flask import Flask, json, Response
from services import event_service
import os
app = Flask(__name__)

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

if __name__ == "__main__":
  app.run('0.0.0.0', port=int(os.environ['PORT']) if os.environ['ENV'] == 'production' else 8080, debug=os.environ['ENV'] != 'production')