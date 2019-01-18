from flask import Flask, json, make_response
app = Flask(__name__)
  
@app.route("/")
def hello():
  res = make_response(json.dumps({'ok': True}))
  res.headers['Content-Type'] = 'application/json'
  return res

if __name__ == "__main__":
  app.run('0.0.0.0', port=8080, debug=True)
