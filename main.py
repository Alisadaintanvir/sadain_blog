from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get(url="https://api.npoint.io/e75bd82278527768f3d5")
    data = response.json()
    return render_template("index.html", blog=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
