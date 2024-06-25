from flask import Flask  # flask - module name | Flask - class name

app = Flask(__name__)


# Define route
@app.route("/")  # @ - decoorator
def hello_world():
  return "Hello, World!"


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
