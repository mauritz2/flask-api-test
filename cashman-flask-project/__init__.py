from flask import Flask, jsonify, request

app = Flask(__name__)

incomes = [
    {
        "description": "salary", "amount": 5000
    }
]

@app.route("/index")
def hello_world():
    return "Hello you!!"

@app.route("/incomes")
def get_incomes():
    return jsonify(incomes)


@app.route("/incomes", methods=["POST"])
def add_income():
    incomes.append(request.get_json())
    return "", 204

app.run(debug=True)
