from flask import Flask
# from replit.web import App

app = Flask(__name__)

# print(__name__)


@app.route('/')
def index():
  return "hi world"


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
