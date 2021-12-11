import json

from flask import Flask, request, render_template, send_from_directory
from functions import get_data, open_file, kakaya_to_funksia

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    tags = get_data(open_file('posts.json'))
    return render_template("index.html", tags=tags)


@app.route("/tag")
def page_tag():
    tag = request.args.get("tag")
    if tag is None:
        return "Выберите тег"
    data = open_file('posts.json')
    posts = kakaya_to_funksia(data, tag)
    return render_template('post_by_tag.html', posts=posts, tag=tag)

@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    # return send_from_directory("uploads", path)
    pass

app.run(debug=True)

