from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/home")
def home():
    return "Hello & Welcome to My AWS Web Service that is connected in {port}"

@app.route("/about-me")
def index():
    return "About-Me"

@app.route("/data")
def data():
    sample_data = {"Name" : "Harry", "Age" : 20, "Class" : "LC01"}
    return jsonify(sample_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

