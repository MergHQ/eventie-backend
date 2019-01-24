from flask import Flask, json, make_response
from services import event_service
import os
app = Flask(__name__)

def create_response(data):
  res = make_response(json.dumps(data))
  res.headers['Content-Type'] = 'application/json'
  return res

  
@app.route("/")
def hello():
  return create_response({'ok': True})

@app.route('/api/events')
def getEvents():
  return create_response(event_service.getAllEvents())

if __name__ == "__main__":
  app.run('0.0.0.0', port=int(os.environ['PORT']) if os.environ['ENV'] == 'production' else 8080, debug=True)