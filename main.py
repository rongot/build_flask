from flask import Flask, render_template, jsonify
# from replit.web import App

app = Flask(__name__)

# print(__name__)
JOBS = [{
  "id": 1,
  "title": "Qa",
  "location": "new delhk",
  "salary": 12000
}, {
  "id": 2,
  "title": "BD",
  "location": "new pop",
  "salary": 13000
}, {
  "id": 3,
  "title": "DB",
  "location": "sal",
  "salary": 142000
}, {
  "id": 4,
  "title": "CTO",
  "location": "rabak",
}]


@app.route('/')
def index():
  return render_template('home.html', jobs=JOBS, rootname="ronen")


@app.route('/getRoute/')
def getRoute():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
