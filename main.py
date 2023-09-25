from flask import Flask, request, render_template
from send_mail import Email
import requests


posts = requests.get(url="https://api.npoint.io/e75bd82278527768f3d5").json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", all_post=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html", heading_text='Contact Me')
    else:
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['number']
        message = request.form['message']
        email = Email(name, email, phone_number, message)
        email.send_email()

        return render_template("contact.html", heading_text='Successfully sent your message.')


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for post in posts:
        if post['id'] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
