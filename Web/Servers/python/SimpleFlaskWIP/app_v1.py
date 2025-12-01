##Archivo de la clase #6
##6. Consultas HTTP con Postman

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Home App Toys</h1>"


##REST ENDPOINTS
toys = {
    "1": {
        "name": "Figura",
        "brand": "Hasbro",
        "line": "Transformers",
        "material": "Plástico",
        "price": 170,
    },
    "2": {
        "name": "Muñeca",
        "brand": "Mattel",
        "line": "Barbie",
        "material": "Plástico",
        "price": 130,
    },
    "3": {
        "name": "LEGO",
        "brand": "LEGO",
        "line": "Sonic",
        "material": "Plástico",
        "price": 150,
    },
    "4": {
        "name": "Plush",
        "brand": "Pokemon",
        "line": "Pokemon",
        "material": "Algodón",
        "price": 80,
    },
    "5": {
        "name": "Car",
        "brand": "Mattel",
        "line": "Hot Wheels",
        "material": "Metal",
        "price": 50,
    },
}


@app.route("/api/toys/<string:id>/")
def get_toy(id):
    if id in toys:
        return toys[id], 200
    else:
        return {"message": "Toy with id " + id + " not found"}, 404


@app.route("/api/toys/")
def get_toys():
    price = request.args.get("price", 0)
    if price is not None:
        filtered_toys = list(filter(lambda key: toys[key]["price"] >= int(price), toys))
        return list(map(lambda key: toys[key], filtered_toys))


@app.route("/api/toys/", methods=["POST"])
def post_get_toys():
    body = request.json
    toy_id = str(body["id"])
    if toy_id in toys:
        return {"message": "Toy with id " + toy_id + " already exists"}, 409
    else:
        del body["id"]
        toys[toy_id] = body
        return toys[toy_id], 201


@app.route("/api/toys/<string:id>", methods=["DELETE"])
def delete_toys(id):
    if id not in toys:
        return {}, 208
    else:
        del toys[id]
        return {}, 200


if __name__ == "__main__":
    app.run(debug=True, port=8001, host="0.0.0.0")
