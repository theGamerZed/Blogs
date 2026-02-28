from flask import Flask,render_template
import requests

blog_data = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
posts = blog_data.json()
app = Flask(__name__)
print(posts[0]['title'])

@app.route("/")
def say_hello():
    return render_template("index.html",blogs = posts)
@app.route("/about")
def goto_about():
    return render_template("about.html")
@app.route("/contact")
def goto_contact():
    return render_template("contact.html")

@app.route("/post/<int:number>")
def show_blog(number):
    selected_post = None
    for post in posts:
        if post["id"] == number:
            selected_post = post
            break

    return render_template("post.html", post=selected_post)
if __name__ == "__main__":
    app.run(debug = True)