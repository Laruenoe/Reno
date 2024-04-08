from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello & Welcome to My AWS Web Server"

@app.route("/about")
def index():
    return "About"

@app.route("/data")
def data():
    sample_data = {"Name" : "Reno", "Age" : 19, "Class" : "LC01"}
    return jsonify(sample_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

