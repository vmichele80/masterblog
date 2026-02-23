# need to resume from - Adding the "Add" Route - chapter of Codio

import os
import json
from flask import Flask, current_app, request, render_template

def load_blog_posts():
    data_path = os.path.join(current_app.instance_path, "blog_posts.json")

    with open(data_path, "r") as f:
        return json.load(f)


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # We will fill this in the next step
        pass
    return render_template('add.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)