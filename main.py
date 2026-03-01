from flask import Flask,render_template,request
import requests
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage
import os

load_dotenv()


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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        print(data)

        EMAIL_ADDRESS = os.getenv("EMAIL")
        EMAIL_PASSWORD = os.getenv("PASSWORD")
        RECIEVER = os.getenv("RECIEVER")

        # Create email
        msg = EmailMessage()
        msg["Subject"] = f"Email from {data['name']}"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = RECIEVER
        msg.set_content(f"{data['message']} ... from {data['email']}, at {data['telephone']}")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print("Email sent successfully!")
    return render_template('login.html' )

if __name__ == "__main__":
    app.run(debug = True)