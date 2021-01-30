# import necessary libraries
from flask import (
    Flask,
    jsonify,
    request)

# instantiate Flask
app = Flask(__name__)

@app.route("/api/data")
def list_results():
    return 'taco cat'


# run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
