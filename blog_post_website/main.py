from flask import Flask, render_template
from post import Post
import requests

BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"

posts = requests.get(BLOG_URL).json() 
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

print(post_objects[0].title)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)

@app.route('/post/<int:blog_id>')
def show_post(blog_id):
    post = next((post for post in post_objects if post.id == blog_id), None)
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
