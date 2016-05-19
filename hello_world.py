from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Billy's Ranch"
    return "Our environmentally friendly production and packaging is very smart and clean!"
    return "Buy now for $10.99 at the nearest black market near you!"
    return ""
    return ""
    return "Served best with Mommy's Salad"

if __name__ == "__main__":
    port = os.environ.get("PORT")
    app.run(
        "0.0.0.0"
    , port    
    )
