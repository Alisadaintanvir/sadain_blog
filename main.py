from flask import Flask, render_template
import requests

posts = requests.get(url="https://api.npoint.io/e75bd82278527768f3d5").json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", all_post=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for post in posts:
        if post['id'] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
