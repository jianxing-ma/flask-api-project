#!/usr/bin/env python3
"""
Flask application that explores using sessions and json. This 
   application has the following endpoints: 
   
   /
   /index        - main page, check if username stored in session; 
                   if not, redirect to login

   /login        - login page
   
   /inventory    - POST returns JSON
                 
"""

# pip install flask
from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    session,
    make_response,
    redirect,
    url_for,
)
import json


app = Flask(__name__)


app.secret_key = "any random string"


## If the user hits the root of our API
@app.route("/")
def index():
    ## if the key "username" has a value in session
    if "username" in session:
        username = session["username"]
        return (
            "Logged in as "
            + username
            + "<br>"
            + "<button><a href = '/inventory'>click here to check inventory</a></button>"
            + "<br>"
            + "<b><a href = '/logout'>click here to log out</a></b>"
        )

    ## if the key "username" does not have a value in session
    return "Sign in to see inventory <br><a href = '/login'></b>" + "Login</b></a>"


## If the user hits /login with a GET or POST
@app.route("/login", methods=["GET", "POST"])
def login():
    ## if you sent us a POST because you clicked the login button
    if request.method == "POST":
        ## request.form["xyzkey"]: use indexing if you know the key exists
        ## request.form.get("xyzkey"): use get if the key might not exist
        session["username"] = request.form.get("username")
        return redirect(url_for("index"))

    ## return this HTML data if you send us a GET
    return """
   <form action = "" method = "post">
      <p><input type = text name = username></p>
      <p><input type = submit value = Login></p>
   </form>
  """


@app.route("/logout")
def logout():
    # remove the username from the session if it is there
    session.pop("username", None)
    return redirect(url_for("index"))


### Endpoints to show inventory that returns JSON
inventory_data = [
    {
        "brand": "Honda",
        "model": "CBR600RR",
        "year": 2022,
        "engine_capacity": 599,
        "color": "Red",
        "price": 12000.00,
        "features": ["ABS", "LED headlights", "Quickshifter"],
    },
    {
        "brand": "Yamaha",
        "model": "YZF-R6",
        "year": 2023,
        "engine_capacity": 599,
        "color": "Blue",
        "price": 11500.00,
        "features": ["Traction control", "Riding modes"],
    },
    {
        "brand": "Kawasaki",
        "model": "Ninja ZX-6R",
        "year": 2022,
        "engine_capacity": 636,
        "color": "Green",
        "price": 13000.00,
        "features": ["Power modes", "Slipper clutch"],
    },
    {
        "brand": "Suzuki",
        "model": "GSX-R750",
        "year": 2021,
        "engine_capacity": 750,
        "color": "Black",
        "price": 12500.00,
        "features": ["Brembo brakes", "Stainless steel exhaust"],
    },
    {
        "brand": "Ducati",
        "model": "Panigale V4",
        "year": 2022,
        "engine_capacity": 1103,
        "color": "Red",
        "price": 25000.00,
        "features": ["Cornering ABS", "Electronically adjustable suspension"],
    },
]


@app.route("/inventory", methods=["GET", "POST"])
def post_inventory():
    if request.method == "POST":
        data = request.json
        if data:
            data = json.loads(data)
            brand = data["brand"]
            model = data["model"]
            year = data["year"]
            engine_capacity = data["engine_capacity"]
            color = data["color"]
            price = data["price"]
            features = data["features"]
            inventory_data.append(
                {
                    "brand": brand,
                    "model": model,
                    "year": year,
                    "engine_capacity": engine_capacity,
                    "color": color,
                    "price": price,
                    "features": features,
                }
            )

    return jsonify(inventory_data)


#######################################################################


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
