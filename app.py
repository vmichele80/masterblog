# need to resume from - Adding the "Add" Route - chapter of Codio

import os
import json
from flask import Flask, request, render_template, redirect, url_for

def get_data_path():
    # instance_path is a good place to store writable data files
    return os.path.join(app.instance_path, "blog_posts.json")


def save_posts(posts):
    data_path = get_data_path()

    # here I make sure the folder already exists in order to avoid crashes
    # if the folder does exist, it will just overwrite the file, otherwise
    # create a new one
    os.makedirs(app.instance_path, exist_ok=True)

    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

def load_blog_posts():
    data_path = get_data_path()

    # If file doesn't exist yet, return empty list
    if not os.path.exists(data_path):
        return []


    with open(data_path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []




app = Flask(__name__)


@app.route('/')
def index():
    blog_posts = load_blog_posts()
    return render_template('index.html', posts=blog_posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Add the code that handles adding a new blog
        author = request.form.get("author", "").strip()
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()

        # Think about validation of the entries

        blog_posts = load_blog_posts()

        # I generate the id. checking all the IDs in the json and looking
        # for the Max value. in case no ID is present, setting it to zero
        # does not affect the result and avoids the code from breaking
        next_id = (max((p.get("id", 0) for p in blog_posts), default=0) + 1)

        # I generate the new post entry to add to the json
        new_post = {
            "id": next_id,
            "author": author,
            "title": title,
            "content": content
        }

        # I now add the new post entry to  the list of posts
        # (generated from the json)
        blog_posts.append(new_post)

        # and now I save it in the original json
        save_posts(blog_posts)
        ...
        return redirect(url_for('index'))

    # this is what you get if the request is a GET
    return render_template('add.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)